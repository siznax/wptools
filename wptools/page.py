# -*- coding:utf-8 -*-

"""
WPTools Page module
~~~~~~~~~~~~~~~~~~~

Support for getting Mediawiki/Wikidata/RESTBase page info.

* https://www.mediawiki.org/wiki/Manual:Page_table
"""

import html2text

from . import core
from . import utils

from .wikidata import WPToolsWikidata


class WPToolsPage(core.WPTools):
    """
    WPtools core class
    """

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsPage object.

        Optional positional arguments:
        - [title]: <str> Mediawiki page title, file, category, etc.

        Optional keyword arguments:
        - [lang]: <str> Mediawiki language code (default='en')
        - [pageid]: <int> Mediawiki pageid
        - [variant]: <str> Mediawiki langauge variant
        - [wiki]: <str> alternative wiki site (default='wikipedia.org')
        - [wikibase]: <str> Wikidata database ID (e.g. 'Q1')

        Keyword flags:
        - [silent]: <bool> do not echo page data if True
        - [skip]: <list> skip actions in this list
        - [verbose]: <bool> verbose output to stderr if True
        """
        super(WPToolsPage, self).__init__(**kwargs)

        title = None
        if len(args) > 0:  # first positional arg is title
            title = args[0].replace(' ', '_')

        pageid = kwargs.get('pageid')
        wikibase = kwargs.get('wikibase')

        self.params.update({
            'pageid': pageid,
            'title': title,
            'wikibase': wikibase})

        if not title and not pageid and not wikibase:
            self.get_random()
        else:
            self.show()

    def __get_image_files(self):
        """
        returns normalized list of image filenames
        """
        files = []
        image = self.data['image']

        for item in (x['file'] for x in image if x.get('file')):
            fname = item.replace('_', ' ')
            if (not fname.startswith('File')
                    and not fname.startswith('Image')):
                fname = 'File:' + fname
            if fname not in files:
                files.append(fname)
        return files

    def __update_imageinfo(self, title, info):
        """
        update page imageinfos with get_imageinfo data
        """
        for i, image in enumerate(self.data['image']):
            if image.get('file'):
                fname = image.get('file').replace('_', ' ')
                if fname.lower() in title.lower():
                    if image.get('kind') != 'query-thumbnail':
                        self.data['image'][i].update(info)

    def _missing_imageinfo(self):
        """
        returns page images missing info
        """
        if 'image' in self.data:
            return [x for x in self.data['image'] if not x.get('url')]

    def _query(self, action, qobj):
        """
        returns WPToolsQuery string
        """
        title = self.params['title']
        pageid = self.params['pageid']

        if action == 'random':
            return qobj.random()
        elif action == 'query':
            return qobj.query(title, pageid)
        elif action == 'parse':
            return qobj.parse(title, pageid)
        elif action == 'imageinfo':
            return qobj.imageinfo(self.__get_image_files())

    def _set_data(self, action):
        """
        Marshals response data into page data
        """
        if action == 'imageinfo':
            self._set_imageinfo_data()
        elif action == 'parse':
            self._set_parse_data()
        elif action == 'query':
            self._set_query_data()
        elif action == 'random':
            self._set_random_data()

        if self._missing_imageinfo() and not self.flags.get('defer_imageinfo'):
            self.get_imageinfo(show=False)

    def _set_imageinfo_data(self):
        """
        set image attributes from MediaWiki API:Imageinfo response
        """
        data = self._load_response('imageinfo')
        pages = data['query'].get('pages')
        for page in pages:
            title = page.get('title')
            if page.get('imageinfo'):
                for info in page['imageinfo']:
                    info.update({'file': title})
                    self.__update_imageinfo(title, info)

    def _set_parse_data(self):
        """
        set attributes derived from MediaWiki (action=parse)
        """
        pdata = self._load_response('parse')['parse']

        parsetree = pdata.get('parsetree')
        wikibase = pdata.get('properties').get('wikibase_item')
        self.data['pageid'] = pdata.get('pageid')
        self.data['parsetree'] = parsetree
        self.data['wikibase'] = wikibase
        self.data['wikitext'] = pdata.get('wikitext')

        infobox = utils.get_infobox(parsetree)
        self.data['infobox'] = infobox
        self.data['links'] = utils.get_links(pdata.get('iwlinks'))
        self.data['wikidata_url'] = utils.wikidata_url(wikibase)

        title = pdata.get('title')
        if title:
            self.data['title'] = title.replace(' ', '_')

        if self.data['infobox']:
            self._unpack_images(self.data['infobox'], 'parse')

    def _set_query_data(self):
        """
        set attributes derived from MediaWiki (action=query)
        """
        data = self._load_response('query')
        page = data['query']['pages'][0]

        self._set_query_data_fast(data, page)
        self._set_query_data_slow(page)

    def _set_query_data_fast(self, data, page):
        """
        Set less expensive action=query response data
        """
        self.data['languages'] = page.get('langlinks')
        self.data['length'] = page.get('length')
        self.data['pageid'] = page.get('pageid')
        self.data['random'] = data['query']['random'][0]["title"]
        self.data['title'] = page.get('title').replace(' ', '_')
        self.data['watchers'] = page.get('watchers')

        fullurl = page.get('fullurl')
        if fullurl:
            self.data['url'] = fullurl
            self.data['url_raw'] = fullurl + '?action=raw'

        modified = page.get('touched')
        if 'modified' in self.data:
            self.data['modified'].update({'page': modified})
        else:
            self.data['modified'] = {'page': modified}

        pageprops = page.get('pageprops')
        if pageprops:
            wikibase = pageprops.get('wikibase_item')
            if wikibase:
                self.data['wikibase'] = wikibase
                self.data['wikidata_url'] = utils.wikidata_url(wikibase)

        terms = page.get('terms')
        if terms:
            if terms.get('description'):
                self.data['description'] = next(iter(terms['description']),
                                                None)
            if terms.get('label'):
                self.data['label'] = next(iter(terms['label']), None)

        self._unpack_images(page, 'query')

    def _set_query_data_slow(self, page):
        """
        Set more expensive action=query response data
        """
        categories = page.get('categories')
        if categories:
            self.data['categories'] = [x['title'] for x in categories]

        contributors = page.get("contributors") or 0
        anoncontributors = page.get("anoncontributors") or 0
        if isinstance(contributors, list):
            contributors = len(contributors)
        self.data['contributors'] = contributors + anoncontributors

        extract = page.get('extract')
        if extract:
            self.data['extract'] = extract
            extext = html2text.html2text(extract)
            if extext:
                self.data['extext'] = extext.strip()

        files = page.get('images')  # really, these are FILES
        if files:
            self.data['files'] = [x['title'] for x in files]

        pageviews = page.get('pageviews')
        if pageviews:
            values = [x for x in pageviews.values() if x]
            self.data['views'] = int(sum(values) / len(values))

    def _set_random_data(self):
        """
        Sets random page data
        """
        rdata = self._load_response('random')
        rdata = rdata['query']['random'][0]

        pageid = rdata.get('id')
        title = rdata.get('title')

        self.data.update({'pageid': pageid,
                          'title': title})

        self.params['title'] = title.replace(' ', '_')
        self.params['pageid'] = pageid

    def _unpack_images(self, source, action):
        """
        Set image data from Mediawiki response data
        """
        if 'image' not in self.data:
            self.data['image'] = []

        if action == 'parse':

            image = source.get('image')
            cover = source.get('Cover')

            if image:
                self.data['image'].append({
                    'kind': 'parse-image',
                    'file': source['image']})

            if cover:
                self.data['image'].append({
                    'kind': 'parse-cover',
                    'file': source['Cover']})

        if action == 'query':

            pageimage = source.get('pageimage')
            thumbnail = source.get('thumbnail')

            if pageimage:
                self.data['image'].append({
                    'kind': 'query-pageimage',
                    'file': pageimage})

            if thumbnail:
                qthumb = {'kind': 'query-thumbnail'}
                qthumb.update(thumbnail)
                qthumb['url'] = thumbnail.get('source')
                del qthumb['source']
                qthumb['file'] = qthumb['url'].split('/')[-2]
                self.data['image'].append(qthumb)

    def get(self, show=True, proxy=None, timeout=0):
        """
        Make Mediawiki, RESTBase, and Wikidata requests for page data
        some sequence of:
        - get_parse()
        - get_query()
        - get_rest()
        - get_wikidata()
        """
        title = self.params['title']
        wikibase = self.params['wikibase']

        if wikibase and not title:
            self.flags['defer_imageinfo'] = True
            # self.get_wikidata(False, proxy, timeout)
            self.get_query(False, proxy, timeout)
            self.flags['defer_imageinfo'] = False
            self.get_parse(show, proxy, timeout)
        else:
            self.flags['defer_imageinfo'] = True
            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)
            self.flags['defer_imageinfo'] = False
            # self.get_wikidata(show, proxy, timeout)

        return self

    def get_imageinfo(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki request for API:Imageinfo
        - image: <dict> updates image URLs, sizes, etc.
        https://www.mediawiki.org/wiki/API:Imageinfo
        """
        if not self.data['image']:
            raise LookupError("get_imageinfo needs image")

        if not self._missing_imageinfo() and 'imageinfo' in self.cache:
            utils.stderr("complete imageinfo in cache", self.flags['silent'])
            return

        self._get('imageinfo', show, proxy, timeout)

        return self

    def get_parse(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API action=parse request for:
        - image: <dict> {parse-image, parse-cover}
        - infobox: <dict> Infobox data as python dictionary
        - links: <list> interwiki links (iwlinks)
        - pageid: <int> Wikipedia database ID
        - parsetree: <str> XML parse tree
        - wikibase: <str> Wikidata entity ID or wikidata URL
        - wikitext: <str> raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=parse
        """
        if not self.params['title'] and not self.params['pageid']:
            raise LookupError("get_parse needs title or pageid")

        self._get('parse', show, proxy, timeout)

        return self

    def get_query(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API action=query request for:
        - description: <str> Wikidata description (via pageterms)
        - extext: <str> plain text (Markdown) extract
        - extract: <str> HTML extract from Extension:TextExtract
        - files: <list> list of files contained in the page
        - image: <dict> {query-pageimage, query-thumbnail}
        - label: <str> Wikidata label (via pageterms)
        - modified (page): <str> ISO8601 date and time
        - pageid: <int> Wikipedia database ID
        - random: <str> a random article title with every request!
        - url: <str> the canonical wiki URL
        - url_raw: <str> ostensible raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=query
        """
        if not self.params['title'] and not self.params['pageid']:
            raise LookupError("get_query needs title or pageid")

        self._get('query', show, proxy, timeout)

        return self

    def get_random(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API (action=query) list=random

        Arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - pageid: <int> Wikipedia database ID
        - title: <str> article title

        See:
        https://www.mediawiki.org/wiki/API:Random
        """
        self._get('random', show, proxy, timeout)

        # flush cache to allow repeated random requests
        del self.cache['random']

        return self

    def get_wikidata(self, show=True, proxy=None, timeout=0):
        """
        Envoke wptools.wikidata.WPToolsWikidata()
        """
        wdobj = WPToolsWikidata(self.params.get('title'), **self.params)

        wdobj.get_wikidata(show, proxy, timeout)

        self.data.update(wdobj.data)

    def pageimage(self, token=None):
        """
        returns first pageimage info with kind containing token
        or list of pageimage kinds
        """
        if 'image' not in self.data:
            return

        if not token:
            return [x['kind'] for x in self.data['image']]

        for img in self.data['image']:
            if token in img.get('kind'):
                return img

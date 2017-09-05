# -*- coding:utf-8 -*-

"""
WPTools Page module
~~~~~~~~~~~~~~~~~~~

Support for getting Wikimedia page info.

Access to Wikimedia APIs:

- Mediawiki: https://www.mediawiki.org/wiki/API:Main_page
- RESTBase: https://www.mediawiki.org/wiki/RESTBase
- Wikidata: https://www.wikidata.org/wiki/Wikidata:Data_access

See also:

- https://www.mediawiki.org/wiki/Manual:Page_table
"""

import html2text

from . import core
from . import utils

from .restbase import WPToolsRESTBase
from .wikidata import WPToolsWikidata


class WPToolsPage(core.WPTools):
    """
    WPtools core class
    """

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsPage object

        Gets a random title without arguments

        Optional positional {params}:
        - [title]: <str> Mediawiki page title, file, category, etc.

        Optional keyword {params}:
        - [endpoint]: <str> RESTBase entry point (default=summary)
        - [lang]: <str> Mediawiki language code (default=en)
        - [pageid]: <int> Mediawiki pageid
        - [variant]: <str> Mediawiki language variant
        - [wiki]: <str> alternative wiki site (default=wikipedia.org)
        - [wikibase]: <str> Wikidata database ID (e.g. 'Q1')

        Optional keyword {flags}:
        - [silent]: <bool> do not echo page data if True
        - [skip]: <list> skip actions in this list
        - [verbose]: <bool> verbose output to stderr if True
        """
        super(WPToolsPage, self).__init__(**kwargs)

        title = None
        if len(args) > 0 and args[0]:  # first positional arg is title
            title = args[0]

        endpoint = kwargs.get('endpoint')
        pageid = kwargs.get('pageid')
        wikibase = kwargs.get('wikibase')

        self.params.update({
            'endpoint': endpoint,
            'pageid': pageid,
            'title': title,
            'wikibase': wikibase})

        if not title and not endpoint and not pageid and not wikibase:
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
        marshals response data into page data
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

        self._update_params()

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

        self.data['pageid'] = pdata.get('pageid')
        self.data['parsetree'] = parsetree
        self.data['wikitext'] = pdata.get('wikitext')

        infobox = utils.get_infobox(parsetree)
        self.data['infobox'] = infobox
        self.data['links'] = utils.get_links(pdata.get('iwlinks'))

        title = pdata.get('title')
        if title:
            self.data['title'] = title
            if not self.params.get('title'):
                self.params['title'] = title

        wikibase = pdata.get('properties').get('wikibase_item')
        if wikibase:
            self.data['wikibase'] = wikibase
            self.data['wikidata_url'] = utils.wikidata_url(wikibase)

        if self.data['infobox']:
            self._set_parse_image(self.data['infobox'])

    def _set_parse_image(self, infobox):
        """
        set image data from action=parse response
        """
        if 'image' not in self.data:
            self.data['image'] = []

        image = infobox.get('image')
        cover = infobox.get('Cover')

        if image:
            self.data['image'].append({
                'kind': 'parse-image',
                'file': infobox['image']})

        if cover:
            self.data['image'].append({
                'kind': 'parse-cover',
                'file': infobox['Cover']})

    def _set_query_data(self):
        """
        set attributes derived from MediaWiki (action=query)
        """
        data = self._load_response('query')
        page = data['query']['pages'][0]

        self.data['random'] = data['query']['random'][0]["title"]

        self._set_query_data_fast(page)
        self._set_query_data_slow(page)

    def _set_query_data_fast(self, page):
        """
        set less expensive action=query response data
        """
        self.data['languages'] = page.get('langlinks')
        self.data['length'] = page.get('length')
        self.data['pageid'] = page.get('pageid')
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

        title = page.get('title')
        self.data['title'] = title
        if not self.params.get('title'):
            self.params['title'] = title

        self._set_query_image(page)

    def _set_query_data_slow(self, page):
        """
        set more expensive action=query response data
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
            if values:
                self.data['views'] = int(sum(values) / len(values))
            else:
                self.data['views'] = 0

    def _set_query_image(self, page):
        """
        set image data from action=query response
        """
        if 'image' not in self.data:
            self.data['image'] = []

        pageimage = page.get('pageimage')
        thumbnail = page.get('thumbnail')

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

    def _set_random_data(self):
        """
        sets page data from random request
        """
        rdata = self._load_response('random')
        rdata = rdata['query']['random'][0]

        pageid = rdata.get('id')
        title = rdata.get('title')

        self.data.update({'pageid': pageid,
                          'title': title})

    def _update_params(self):
        """
        update params from response data
        """
        self.params['title'] = self.data.get('title')
        self.params['pageid'] = self.data.get('pageid')
        self.params['wikibase'] = self.data.get('wikibase')

    def get(self, show=True, proxy=None, timeout=0):
        """
        Make Mediawiki, RESTBase, and Wikidata requests for page data
        some sequence of:
        - get_parse()
        - get_query()
        - get_restbase()
        - get_wikidata()
        """
        title = self.params.get('title')
        wikibase = self.params.get('wikibase')

        if not self.params.get('endpoint'):
            self.params['endpoint'] = 'summary'

        if wikibase and not title:

            self.flags['defer_imageinfo'] = True

            self.get_wikidata(False, proxy, timeout)
            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)

            self.flags['defer_imageinfo'] = False

            self.get_restbase(False, proxy, timeout)

            if show:
                self.show()
        else:

            self.flags['defer_imageinfo'] = True

            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)

            if not self.data.get('wikibase'):
                self.flags['skip'].append('wikidata')

            self.get_wikidata(False, proxy, timeout)

            self.flags['defer_imageinfo'] = False

            self.get_restbase(False, proxy, timeout)

            if show:
                self.show()

        return self

    def get_imageinfo(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki request for API:Imageinfo

        https://www.mediawiki.org/wiki/API:Imageinfo

        Required {data}:
        - image: <list> member (<dict>) with 'file' and not 'url'

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - image: <list> member (<dict>) image URLs, sizes, etc.
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
        GET MediaWiki:API action=parse request

        https://en.wikipedia.org/w/api.php?action=help&modules=parse

        Required {params}: title OR pageid
        - title: <str> article title
        - pageid: <int> Wikipedia database ID

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - image: <dict> {parse-image, parse-cover}
        - infobox: <dict> Infobox data as python dictionary
        - links: <list> interwiki links (iwlinks)
        - pageid: <int> Wikipedia database ID
        - parsetree: <str> XML parse tree
        - wikibase: <str> Wikidata entity ID or wikidata URL
        - wikitext: <str> raw wikitext URL
        """
        if not self.params['title'] and not self.params['pageid']:
            raise LookupError("get_parse needs title or pageid")

        self._get('parse', show, proxy, timeout)

        return self

    def get_query(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API action=query selected data

        https://en.wikipedia.org/w/api.php?action=help&modules=query

        Required {params}: title OR pageid
        - title: <str> article title
        - pageid: <int> Wikipedia database ID

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
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
        """
        if not self.params['title'] and not self.params['pageid']:
            raise LookupError("get_query needs title or pageid")

        self._get('query', show, proxy, timeout)

        return self

    def get_random(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API (action=query) list=random

        https://www.mediawiki.org/wiki/API:Random

        Required {params}: None

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - pageid: <int> Wikipedia database ID
        - title: <str> article title
        """
        self._get('random', show, proxy, timeout)

        # flush cache to allow repeated random requests
        del self.cache['random']

        return self

    def get_restbase(self, show=True, proxy=None, timeout=0):
        """
        Envoke wptools.restbase.get_restbase()
        """
        kwargs = {}
        kwargs.update(self.params)
        kwargs.update(self.flags)

        rbobj = WPToolsRESTBase(self.params.get('title'), **kwargs)
        rbobj.cache.update(self.cache)
        rbobj.get_restbase(False, proxy, timeout)

        self.cache.update(rbobj.cache)
        self.data.update(rbobj.data)
        self.flags.update(rbobj.flags)
        self.params.update(rbobj.params)

        if show:
            self.show()

        return self

    def get_wikidata(self, show=True, proxy=None, timeout=0):
        """
        Envoke wptools.wikidata.get_wikidata()
        """
        kwargs = {}
        kwargs.update(self.params)
        kwargs.update(self.flags)

        wdobj = WPToolsWikidata(self.params.get('title'), **kwargs)
        wdobj.cache.update(self.cache)
        wdobj.get_wikidata(False, proxy, timeout)

        self.cache.update(wdobj.cache)
        self.data.update(wdobj.data)
        self.flags.update(wdobj.flags)
        self.params.update(wdobj.params)

        if show:
            self.show()

        return self

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

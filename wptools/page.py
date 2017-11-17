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


class WPToolsPage(WPToolsRESTBase,
                  WPToolsWikidata,
                  core.WPTools):
    """
    WPtools Page class, derived from wptools.core
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
        super(WPToolsPage, self).__init__(*args, **kwargs)

        title = self.params.get('title')

        endpoint = kwargs.get('endpoint')
        if endpoint:
            endpoint = self._parse_endpoint(endpoint, title)
            self.params.update({'endpoint': endpoint})

        pageid = kwargs.get('pageid')
        if pageid:
            self.params.update({'pageid': pageid})

        wikibase = kwargs.get('wikibase')
        if wikibase:
            self.params.update({'wikibase': wikibase})

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
        title = self.params.get('title')
        pageid = self.params.get('pageid')
        wikibase = self.params.get('wikibase')
        endpoint = self.params.get('endpoint')

        qstr = None

        if action == 'random':
            qstr = qobj.random()
        elif action == 'query':
            qstr = qobj.query(title, pageid)
        elif action == 'querymore':
            qstr = qobj.querymore(title, pageid)
        elif action == 'parse':
            qstr = qobj.parse(title, pageid)
        elif action == 'imageinfo':
            qstr = qobj.imageinfo(self.__get_image_files())
        elif action == 'claims':
            qstr = qobj.claims(self.data['claims'].keys())
        elif action == 'wikidata':
            qstr = qobj.wikidata(title, wikibase)
        elif action == 'restbase':
            qstr = qobj.restbase(endpoint)

        if qstr is None:
            raise ValueError("Unknown action: %s" % action)

        return qstr

    def _set_data(self, action):
        """
        marshals response data into page data
        """
        if 'query' in action:
            self._set_query_data(action)
        elif action == 'imageinfo':
            self._set_imageinfo_data()
        elif action == 'parse':
            self._set_parse_data()
        elif action == 'random':
            self._set_random_data()
        elif action == 'claims':
            self._set_claims_data()
        elif action == 'wikidata':
            self._set_wikidata()
            if self.data.get('claims'):
                self.get_claims(show=False)
        elif action == 'restbase':
            self._set_restbase_data()

        self._update_imageinfo()
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
        self.data['iwlinks'] = utils.get_links(pdata.get('iwlinks'))

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
        image = infobox.get('image')
        cover = infobox.get('Cover')

        if image or cover:
            if 'image' not in self.data:
                self.data['image'] = []

        if image and utils.isfilename(image):
            self.data['image'].append({'kind': 'parse-image', 'file': image})

        if cover and utils.isfilename(cover):
            self.data['image'].append({'kind': 'parse-cover', 'file': cover})

    def _set_query_data(self, action='query'):
        """
        set attributes derived from MediaWiki (action=query)
        """
        data = self._load_response(action)
        page = data['query']['pages'][0]

        if action == 'query':
            self.data['random'] = data['query']['random'][0]["title"]

        if 'redirects' in data['query']:
            self.data['redirected'] = data['query']['redirects']

        self._set_query_data_fast_1(page)  # avoid pylint too-many-branches
        self._set_query_data_fast_2(page)
        self._set_query_data_slow(page)

    def _set_query_data_fast_1(self, page):
        """
        set less expensive action=query response data PART 1
        """
        self.data['pageid'] = page.get('pageid')

        extract = page.get('extract')
        if extract:
            self.data['extract'] = extract
            extext = html2text.html2text(extract)
            if extext:
                self.data['extext'] = extext.strip()

        fullurl = page.get('fullurl')
        if fullurl:
            self.data['url'] = fullurl
            self.data['url_raw'] = fullurl + '?action=raw'

        length = page.get('length')
        if length:
            self.data['length'] = length

        self.data['links'] = utils.get_links(page.get('links'))

        modified = page.get('touched')
        if modified:
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

            if 'disambiguation' in pageprops:
                self.data['disambiguation'] = len(self.data['links'])

    def _set_query_data_fast_2(self, page):
        """
        set less expensive action=query response data PART 2
        """
        self.data['pageid'] = page.get('pageid')

        redirects = page.get('redirects')
        if redirects:
            self.data['redirects'] = redirects

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

        watchers = page.get('watchers')
        if watchers:
            self.data['watchers'] = watchers

        self._set_query_image(page)

    def _set_query_data_slow(self, page):
        """
        set more expensive action=query response data
        """
        categories = page.get('categories')
        if categories:
            self.data['categories'] = [x['title'] for x in categories]

        if page.get('contributors'):
            contributors = page.get('contributors') or 0
            anoncontributors = page.get('anoncontributors') or 0
            if isinstance(contributors, list):
                contributors = len(contributors)
            self.data['contributors'] = contributors + anoncontributors

        files = page.get('images')  # really, these are FILES
        if files:
            self.data['files'] = [x['title'] for x in files]

        languages = page.get('langlinks')
        if languages:
            self.data['languages'] = languages

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
        pageimage = page.get('pageimage')
        thumbnail = page.get('thumbnail')

        if pageimage or thumbnail:
            if 'image' not in self.data:
                self.data['image'] = []

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

    def _update_imageinfo(self):
        """
        calls get_imageinfo() if data image missing info
        """
        if self._missing_imageinfo() and not self.flags.get('defer_imageinfo'):
            self.get_imageinfo(show=False)

    def _update_params(self):
        """
        update params from response data
        """
        if self.data.get('title'):
            self.params['title'] = self.data.get('title')
        if self.data.get('pageid'):
            self.params['pageid'] = self.data.get('pageid')
        if self.data.get('wikibase'):
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
        wikibase = self.params.get('wikibase')

        if wikibase:

            self.flags['defer_imageinfo'] = True

            self.get_wikidata(False, proxy, timeout)
            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)

            self.flags['defer_imageinfo'] = False

            self.get_restbase('summary', False, proxy, timeout)

            if show:
                self.show()

        else:

            self.flags['defer_imageinfo'] = True

            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)

            if not self.data.get('wikibase'):
                self.flags['skip'] = ['wikidata']

            self.get_wikidata(False, proxy, timeout)

            self.flags['defer_imageinfo'] = False

            self.get_restbase('summary', False, proxy, timeout)

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
        if not self.data.get('image'):
            raise ValueError("get_imageinfo needs a page image")

        if not self._missing_imageinfo() and 'imageinfo' in self.cache:
            utils.stderr("complete imageinfo in cache", self.flags['silent'])
            return

        self._get('imageinfo', show, proxy, timeout)

        return self

    def get_more(self, show=True, proxy=None, timeout=0):
        """
        Calls get_querymore() Is for convenience. You like.
        """
        return self.get_querymore(show, proxy, timeout)

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
        - iwlinks: <list> interwiki links
        - pageid: <int> Wikipedia database ID
        - parsetree: <str> XML parse tree
        - wikibase: <str> Wikidata entity ID or wikidata URL
        - wikitext: <str> raw wikitext URL
        """
        if not self.params.get('title') and not self.params.get('pageid'):
            raise ValueError("get_parse needs title or pageid")

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
        - image: <dict> {query-pageimage, query-thumbnail}
        - label: <str> Wikidata label (via pageterms)
        - modified (page): <str> ISO8601 date and time
        - pageid: <int> Wikipedia database ID
        - random: <str> a random article title with every request!
        - url: <str> the canonical wiki URL
        - url_raw: <str> ostensible raw wikitext URL
        - watchers: <int> number of people watching this page
        """
        if not self.params.get('title') and not self.params.get('pageid'):
            raise ValueError("get_query needs title or pageid")

        self._get('query', show, proxy, timeout)

        return self

    def get_querymore(self, show=True, proxy=None, timeout=0):
        """
        GET MediaWiki:API action=query for MORE data
        A much more expensive (slower!) query for popular pages
        https://en.wikipedia.org/w/api.php?action=help&modules=query

        Required {params}: title OR pageid
        - title: <str> article title
        - pageid: <int> Wikipedia database ID

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - categories: <list> list of categories used on the page
        - contributors: <int> total number of contributors
        - files: <list> list of files contained in the page
        - languages: <int> number of wiki languages having this page
        - views: <int> average daily page views over past 60 days
        """
        if not self.params['title'] and not self.params['pageid']:
            raise ValueError("get_query needs title or pageid")

        self._get('querymore', show, proxy, timeout)

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

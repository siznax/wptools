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
        - [boxterm]: <str> Infobox title name or substring
        - [endpoint]: <str> alternative API endpoint (default=/w/api.php)
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

        boxterm = kwargs.get('boxterm')
        if boxterm:
            self.params.update({'boxterm': boxterm})

        endpoint = kwargs.get('endpoint')
        if endpoint:
            self.params.update({'endpoint': endpoint})

        pageid = kwargs.get('pageid')
        if pageid:
            self.params.update({'pageid': pageid})

        wikibase = kwargs.get('wikibase')
        if wikibase:
            self.params.update({'wikibase': wikibase})

        if not title and not pageid and not wikibase:
            self.get_random()
        else:
            self.show()

    def __insert_image_info(self, title, _from, info):
        """
        Insert API image INFO into matching image dict

        We make one imageinfo request containing only unique image
        filenames. We reduce duplication by asking for image data per
        file, instead of per "kind" or source (Wikipedia, Wikidata,
        etc.), because some sources reference the same image file. We
        match API imageinfo response data to existing image filenames
        by API title or normalized "from" title. So, some imageinfo
        data will be applied to more than one image "kind" (source) if
        they share the same filename.
        """
        for img in self.data['image']:
            if 'url' not in img:
                if title == img['file']:  # matching title/file
                    img.update(info)
                elif _from == img['file']:  # matching from/file
                    img.update(info)

    def __pull_image_info(self, title, imageinfo, normalized):
        """
        Pull image INFO from API response and insert
        """
        for info in imageinfo:
            info.update({'title': title})

            # get API normalized "from" filename for matching
            _from = None
            for norm in normalized:
                if title == norm['to']:
                    _from = norm['from']

            # let's put all "metadata" in one member
            info['metadata'] = {}
            extmetadata = info.get('extmetadata')
            if extmetadata:
                info['metadata'].update(extmetadata)
                del info['extmetadata']

            self.__insert_image_info(title, _from, info)

    def _extend_data(self, datapoint, new_data):
        """
        extend or assign new data to datapoint
        """
        if new_data:
            try:
                self.data[datapoint].extend(new_data)
            except KeyError:
                self.data[datapoint] = new_data

    def _missing_imageinfo(self):
        """
        returns list of image filenames that are missing info
        """
        if 'image' not in self.data:
            return
        missing = []
        for img in self.data['image']:
            if 'url' not in img:
                missing.append(img['file'])
        return list(set(missing))

    def _normalize_images(self):
        """
        normalizes image filenames by prepending 'File:' if needed
        """
        if 'image' not in self.data:
            return
        for img in self.data['image']:
            fname = img['file'].replace('_', ' ')
            fstart = fname.startswith('File:')
            istart = fname.startswith('Image:')
            if not fstart and not istart:
                fname = 'File:' + fname
                img['orig'] = img['file']
                img['file'] = fname

    def _query(self, action, qobj):
        """
        returns WPToolsQuery string
        """
        title = self.params.get('title')
        pageid = self.params.get('pageid')
        wikibase = self.params.get('wikibase')

        qstr = None

        if action == 'random':
            qstr = qobj.random()
        elif action == 'query':
            qstr = qobj.query(title, pageid, self._continue_params())
        elif action == 'querymore':
            qstr = qobj.querymore(title, pageid, self._continue_params())
        elif action == 'parse':
            qstr = qobj.parse(title, pageid)
        elif action == 'imageinfo':
            qstr = qobj.imageinfo(self._missing_imageinfo())
        elif action == 'labels':
            qstr = qobj.labels(self._pop_entities())
        elif action == 'wikidata':
            qstr = qobj.wikidata(title, wikibase)
        elif action == 'restbase':
            qstr = qobj.restbase(self.params.get('rest_endpoint'), title)

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
        elif action == 'labels':
            self._set_labels()
        elif action == 'wikidata':
            self._set_wikidata()
            self.get_labels()
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

        normalized = []
        if 'normalized' in data['query']:
            normalized = data['query']['normalized']

        for page in pages:
            title = page.get('title')
            imageinfo = page.get('imageinfo')
            if imageinfo:
                self.__pull_image_info(title, imageinfo, normalized)

        # Mark missing imageinfo to prevent duplicate requests
        for img in self.data['image']:
            if 'url' not in img:
                img['url'] = 'MISSED'

    def _set_parse_data(self):
        """
        set attributes derived from MediaWiki (action=parse)
        """
        pdata = self._load_response('parse')['parse']

        self.data['iwlinks'] = utils.get_links(pdata.get('iwlinks'))
        self.data['pageid'] = pdata.get('pageid')
        self.data['wikitext'] = pdata.get('wikitext')

        parsetree = pdata.get('parsetree')
        self.data['parsetree'] = parsetree

        boxterm = self.params.get('boxterm')
        if boxterm:
            infobox = utils.get_infobox(parsetree, boxterm)
        else:
            infobox = utils.get_infobox(parsetree)
        self.data['infobox'] = infobox

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
        cover = infobox.get('Cover') or infobox.get('cover')

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

        self._handle_continuations(data, action)

        if action == 'query':
            self.data['random'] = data['query']['random'][0]["title"]

        self._extend_data('backlinks', data['query'].get('backlinks'))

        self.data['redirected'] = data['query'].get('redirects')

        self._set_query_data_fast_1(page)  # avoid pylint too-many-branches
        self._set_query_data_fast_2(page)
        self._set_query_data_slow(page)

    def _set_query_data_fast_1(self, page):
        """
        set less expensive action=query response data PART 1
        """
        self.data['pageid'] = page.get('pageid')

        assessments = page.get('pageassessments')
        if assessments:
            self.data['assessments'] = assessments

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

        self._extend_data('links', utils.get_links(page.get('links')))

        self._update_data('modified', 'page', page.get('touched'))

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
            if terms.get('alias'):
                self.data['aliases'] = terms['alias']

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

    def _update_data(self, datapoint, key, new_data):
        """
        update or assign new data to datapoint
        """
        if new_data:
            try:
                self.data[datapoint].update({key: new_data})
            except KeyError:
                self.data[datapoint] = {key: new_data}

    def _update_imageinfo(self):
        """
        calls get_imageinfo() if data image missing info
        """
        missing = self._missing_imageinfo()
        deferred = self.flags.get('defer_imageinfo')
        continuing = self.data.get('continue')

        if missing and not deferred and not continuing:
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

    def skip_action(self, action):
        """
        append action to skip flag
        """
        if 'skip' not in self.flags:
            self.flags['skip'] = []
        self.flags['skip'].append(action)

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

            self.get_restbase('/page/summary/', False, proxy, timeout)

            if show and not self.flags.get('silent'):
                self.show()

        else:

            self.flags['defer_imageinfo'] = True

            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)

            if not self.data.get('wikibase'):
                self.skip_action('wikidata')

            self.get_wikidata(False, proxy, timeout)

            self.flags['defer_imageinfo'] = False

            wiki = self.params.get('wiki')
            if wiki and 'wikipedia.org' not in wiki:
                self.skip_action('restbase')

            self.get_restbase('/page/summary/', False, proxy, timeout)

            if show and not self.flags.get('silent'):
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

        self._normalize_images()
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
        - requests: list of request actions made
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
        - requests: list of request actions made
        - url: <str> the canonical wiki URL
        - url_raw: <str> ostensible raw wikitext URL
        - watchers: <int> number of people watching this page
        """
        if not self.params.get('title') and not self.params.get('pageid'):
            raise ValueError("get_query needs title or pageid")

        self._get('query', show, proxy, timeout)

        while self.data.get('continue'):
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

        while self.data.get('continue'):
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

    def images(self, fields=None, token=None):
        """
        Returns image info keys for kind containing token

        Args:
        - fields: <list> image info values wanted
        - token: <str> substring to match image kind

        EXAMPLES

        Get all available image info:
        >>> page.images()

        Get all image kinds:
        >>> page.images('kind')

        Get only "query" (kind) image info
        >>> page.images(token='query')

        Get only file, url fields from "wikidata" images
        >>> page.images(['file', 'url'], token='wikidata')
        """

        if 'image' not in self.data:
            return

        out = []
        for img in self.data['image']:
            if token and token not in img['kind']:
                continue
            info = {}
            for key in img:
                if fields and key not in fields:
                    continue
                info.update({key: img[key]})
            if info:
                out.append(info)

        return out

    def pageimage(self, token=None):
        """
        DEPRECATED see page.images()
        """
        return self.images(token=token)

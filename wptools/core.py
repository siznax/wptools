# -*- coding:utf-8 -*-

"""
WPTools core module.
~~~~~~~~~~~~~~~~~~~~
"""

from __future__ import print_function
try:  # python2
    from urllib import quote
    from urlparse import urlparse
except ImportError:  # python3
    from urllib.parse import quote, urlparse

import collections
import re

import html2text

from . import fetch
from . import utils


class WPTools(object):
    """
    A user-created :class:WPTools object.
    """

    _WIKIPROPS = {'P17': 'country',
                  'P18': 'image',
                  'P27': 'citizenship',
                  'P30': 'continent',
                  'P31': 'instance',
                  'P50': 'author',
                  'P57': 'director',
                  'P86': 'composer',
                  'P105': 'taxon rank',
                  'P110': 'illustrator',
                  'P123': 'publisher',
                  'P135': 'movement',
                  'P136': 'genre',
                  'P144': 'based on',
                  'P161': 'cast',
                  'P170': 'creator',
                  'P171': 'parent taxon',
                  'P175': 'performer',
                  'P186': 'material',
                  'P195': 'collection',
                  'P212': 'ISBN',
                  'P225': 'taxon name',
                  'P301': 'topic',
                  'P345': 'IMDB',
                  'P217': 'inventory',
                  'P276': 'location',
                  'P279': 'subclass',
                  'P569': 'birth',
                  'P570': 'death',
                  'P577': 'pubdate',
                  'P585': 'datetime',
                  'P625': 'coordinates',
                  'P655': 'translator',
                  'P658': 'tracklist',
                  'P800': 'work',
                  'P856': 'website',
                  'P910': 'category',
                  'P1773': 'attribution',
                  'P1779': 'creator'}

    _defer_imageinfo = False

    description = None
    extext = None
    extract = None
    fatal = False
    infobox = None
    label = None
    lead = None
    links = None
    pageid = None
    parsetree = None
    random = None
    title = None
    url = None
    url_raw = None
    what = None
    wikibase = None
    wikidata_url = None
    wikitext = None

    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            if args[0]:
                self.title = args[0].replace(' ', '_')

        self.lang = kwargs.get('lang') or 'en'
        self.pageid = kwargs.get('pageid')
        self.silent = kwargs.get('silent') or False
        self.variant = kwargs.get('variant')
        self.verbose = kwargs.get('verbose') or False
        self.wiki = kwargs.get('wiki')
        self.wikibase = kwargs.get('wikibase')

        self.cache = {}
        self.claims = {}
        self.images = []
        self.modified = {}
        self.props = {}
        self.wikidata = {}

        if not self.pageid and not self.title and not self.wikibase:
            self.get_random()
        else:
            self.show()

    def __get_entity_prop(self, entity, prop):
        """
        returns Wikidata entity property value
        """
        if entity.get(prop):
            try:
                return entity.get(prop).get(self.lang).get('value')
            except AttributeError:
                return entity.get(prop).get('value')

    def __get_image_files(self):
        """
        returns normalized list of image filenames
        """
        files = []
        for item in [x['file'] for x in self.images if x.get('file')]:
            fname = item.replace('_', ' ')
            if (not fname.startswith('File')
                    and not fname.startswith('Image')):
                fname = 'File:' + fname
            if fname not in files:
                files.append(fname)
        return files

    def __get_lead(self, data):
        """
        returns lead HTML with heading and image and refs removed
        """
        lead = []
        lead.append(self.__get_lead_image())
        lead.append(self.__get_lead_heading())
        lead.append(self.__get_lead_rest(data))
        lead.append(self.__get_lead_metadata())
        return "\n".join([x for x in lead if x])

    def __get_lead_heading(self):
        """
        returns lead section HTML heading
        """
        if not hasattr(self, 'url') or not hasattr(self, 'title'):
            return

        heading = "<a href=\"%s\">%s</a>" % (self.url, self.title)
        if hasattr(self, 'description') and self.description:
            heading += "&mdash;<i>%s</i>. " % self.description
        else:
            heading += ':'

        return "<span heading>%s</span>" % heading

    def __get_lead_image(self):
        """
        returns <img> HTML from image attributes
        """
        src = None
        for kind in ['cover', 'wikidata', 'thumbnail', 'thumb', 'page']:
            if self.image(kind):
                src = self.image(kind)['url']
                cls = kind
                break

        if src:
            alt = self.title or self.label
            img = "<img %s" % (cls)
            img += " src=\"%s\"" % (src)
            img += " alt=\"%s\" title=\"%s\">" % (alt, alt)
            return img

    def __get_lead_metadata(self):
        """
        returns lead HTML metadata from attributes
        """
        meta = []
        if hasattr(self, 'modified'):
            meta.append("Modified: %s" % self.modified['page'])
        return "<span metadata>%s</span>" % "\n".join([x for x in meta if x])

    def __get_lead_rest(self, data):
        """
        returns lead section HTML from RESTBase:/page/mobile-text/
        """
        pars = []
        for section in data['sections']:
            for item in section['items']:
                _type = item.get('type')
                if _type == 'hatnote' or _type == 'image':
                    continue
                if item.get('text'):
                    pars.append(item['text'])
                else:
                    pars.append(", ".join(item.keys()))
            break

        if pars:
            html = "\n".join(pars)
            self.cache['rest']['html'] = html
            return self.__postprocess_lead(html)

    def __postprocess_lead(self, html):
        """
        snip and base href lead HTML
        """
        snip = utils.snip_html(html, verbose=1 if self.verbose else 0)
        snip = "<span snipped>%s</span>" % snip
        url = urlparse(self.cache['rest']['query'])
        base = "%s://%s" % (url.scheme, url.netloc)
        snip = snip.replace('href="/', "href=\"%s/" % base)
        return snip

    def __update_imageinfo(self, title, info):
        """
        update images with get_imageinfo data
        """
        for i, image in enumerate(self.images):
            if image.get('file'):
                fname = image.get('file').replace('_', ' ')
                if fname.lower() in title.lower():
                    if image['kind'] != 'query-thumbnail':
                        self.images[i].update(info)

    def __set_title_wikidata(self, item):
        """
        attempt to set title from wikidata
        """
        if not self.title and item.get('sitelinks'):
            for link in item['sitelinks']:
                if link == "%swiki" % self.lang:
                    title = item['sitelinks'][link]['title']
                    self.title = title.replace(' ', '_')

        if not self.title and hasattr(self, 'label') and self.label:
            self.title = self.label.replace(' ', '_')

    def __setattr(self, attr, value, suffix):
        """
        set attribute, append suffix if clobber
        """
        if hasattr(self, attr) and getattr(self, attr):
            extant = getattr(self, attr)
            if extant != value:
                attr = "%s_%s" % (attr, suffix)
                setattr(self, attr, value)

    def _fetch(self, proxy, timeout):
        """
        returns wptools.fetch object for making HTTP requests
        """
        return fetch.WPToolsFetch(
            lang=self.lang,
            silent=self.silent,
            variant=self.variant,
            verbose=self.verbose,
            wiki=self.wiki,
            proxy=proxy,
            timeout=timeout)

    def _load_response(self, action):
        """
        returns API reponse from cache or raises ValueError
        """
        try:
            query = self.cache[action]['query'].replace('&format=json', '')
            data = utils.json_loads(self.cache[action]['response'])

            if action == 'parse' and not data.get('parse'):
                raise LookupError

            if action == 'query':
                if [x for x in data['query']['pages'] if x.get('missing')]:
                    raise LookupError

            if action == 'wikidata' and '-1' in data.get('entities'):
                raise LookupError

            return data

        except LookupError:
            raise LookupError(query)

    def _missing_imageinfo(self):
        """
        returns images missing info
        """
        return [x for x in self.images if not x.get('url')]

    def _marshal_claims(self, query_claims):
        """
        set Wikidata properties and entities from query claims
        """
        self.props = self._wikidata_props(query_claims)

        for propid in self.props:
            label = self._WIKIPROPS[propid]
            for val in self.props[propid]:
                if utils.is_text(val) and re.match(r'^Q\d+', val):
                    self.claims[val] = label
                else:
                    self._update_wikidata(label, val)

    def _query(self, action, _fetch):
        if action == 'query' or action == 'parse':
            if self.pageid:
                return _fetch.query(action, self.pageid, pageid=True)
            return _fetch.query(action, self.title)

        elif action == 'wikidata':
            thing = {'id': '', 'site': '', 'title': ''}
            if self.wikibase:
                thing['id'] = self.wikibase
            elif self.lang and self.title:
                thing['site'] = "%swiki" % self.lang
                thing['title'] = self.title
            return _fetch.query(action, thing)

        elif action == 'rest':
            try:
                title = quote(self.title)
            except KeyError:
                title = quote(self.title.encode('utf-8'))
            return _fetch.query('/page/mobile-text/', title)

        elif action == 'claims':
            thing = {'id': "|".join(self.claims.keys()), 'props': 'labels'}
            return _fetch.query('claims', thing)

        elif action == 'imageinfo':
            files = self.__get_image_files()
            try:
                files = [quote(x) for x in files]
            except KeyError:
                files = [quote(x.encode('utf-8')) for x in files]
            return _fetch.query('imageinfo', '|'.join(files))

    def _request(self, action, show, proxy, timeout):
        """
        make HTTP request and cache response
        """
        if action in self.cache:
            if action != 'imageinfo':
                utils.stderr("%s results in cache" % action)
                return

        _fetch = self._fetch(proxy, timeout)
        query = self._query(action, _fetch)

        req = {}
        req['query'] = query
        req['response'] = _fetch.curl(query)
        req['info'] = _fetch.info

        self.cache[action] = req

        if action == 'claims':
            self._set_claims_data()
        elif action == 'imageinfo':
            self._set_imageinfo_data()
        elif action == 'parse':
            self._set_parse_data()
        elif action == 'query':
            self._set_query_data()
        elif action == 'rest':
            self._set_rest_data()
        elif action == 'wikidata':
            self._set_wikidata()
            if self.claims:
                self.get_claims(False)

        if action in ['parse', 'query', 'rest', 'wikidata']:
            if self._missing_imageinfo() and not self._defer_imageinfo:
                self.get_imageinfo(False)

        if show:
            self.show()

    def _set_claims_data(self):
        """
        set property claim labels from get_claims()
        """
        data = self._load_response('claims')
        entities = data.get('entities')
        for item in entities:
            attr = self.claims[item]
            value = self.__get_entity_prop(entities[item], 'labels')
            self._update_wikidata(attr, value)

        self.what = self.wikidata.get('instance')

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

        self.pageid = pdata.get('pageid')
        self.parsetree = pdata.get('parsetree')
        self.wikibase = pdata.get('properties').get('wikibase_item')
        self.wikitext = pdata.get('wikitext')

        self.infobox = utils.get_infobox(self.parsetree)
        self.links = utils.get_links(pdata.get('iwlinks'))
        self.wikidata_url = utils.wikidata_url(self.wikibase)

        if not self.title:
            self.title = pdata.get('title').replace(' ', '_')

        if self.infobox:
            if self.infobox.get('image'):
                self.images.append({'kind': 'parse-image',
                                    'file': self.infobox['image']})
            if self.infobox.get('Cover'):
                self.images.append({'kind': 'parse-cover',
                                    'file': self.infobox['Cover']})

    def _set_query_data(self):
        """
        set attributes derived from MediaWiki (action=query)
        """
        data = self._load_response('query')
        page = data['query']['pages'][0]

        self.modified['page'] = page.get('touched')
        self.pageid = page.get('pageid')
        self.random = data['query']['random'][0]["title"]
        self.title = page.get('title').replace(' ', '_')

        if page.get('extract'):
            self.extract = page['extract']
            extext = html2text.html2text(self.extract)
            if extext:
                self.extext = extext.strip()

        if page.get('fullurl'):
            self.url = page['fullurl']
            self.url_raw = self.url + '?action=raw'

        if page.get('pageimage'):
            self.images.append({'kind': 'query-pageimage',
                                'file': page['pageimage']})

        if page.get('pageprops'):
            wikibase = page['pageprops'].get('wikibase_item')
            if wikibase:
                self.wikibase = wikibase
                self.wikidata_url = utils.wikidata_url(self.wikibase)

        if page.get('terms'):
            if page['terms'].get('description'):
                self.description = ''.join(page['terms']['description'])
            if page['terms'].get('label'):
                self.label = ''.join(page['terms']['label'])

        if page.get('thumbnail'):
            qthumb = {'kind': 'query-thumbnail'}
            qthumb.update(page['thumbnail'])
            qthumb['url'] = page['thumbnail']['source']
            del qthumb['source']
            qthumb['file'] = qthumb['url'].split('/')[-2]
            self.images.append(qthumb)

    def _set_rest_data(self):
        """
        set attributes derived from RESTBase
        """
        data = self._load_response('rest')

        self.description = data.get('description')
        self.modified['page'] = data.get('lastmodified')
        self.pageid = data.get('id')

        if data.get('detail'):
            error = data.get('detail').get('error')
            if error:
                utils.stderr("RESTBase error: %s" % error)
                return

        if data.get('image'):
            rimg = {'kind': 'rest-image'}
            rimg.update(data.get('image'))
            self.images.append(rimg)

        title = (data.get('redirected')
                 or data.get('normalizedtitle')
                 or data.get('displaytitle'))
        if title:
            self.title = title.replace(' ', '_')

        if data.get('sections'):
            self.lead = self.__get_lead(data)

        if data.get('thumb'):
            rthumb = {'kind': 'rest-thumb'}
            rthumb.update(data.get('thumb'))
            self.images.append(rthumb)

        url = urlparse(self.cache['rest']['query'])
        self.url = "%s://%s/wiki/%s" % (url.scheme, url.netloc, self.title)
        self.url_raw = self.url + '?action=raw'

    def _set_wikidata(self):
        """
        set attributes derived from Wikidata (action=wbentities)
        """
        data = self._load_response('wikidata')
        entities = data.get('entities')
        item = entities.get(next(iter(entities)))

        self.modified['wikidata'] = item.get('modified')
        self.wikibase = item.get('id')
        self.wikidata_url = utils.wikidata_url(self.wikibase)

        self.description = self.__get_entity_prop(item, 'descriptions')
        self.label = self.__get_entity_prop(item, 'labels')

        self._marshal_claims(item.get('claims'))
        self.__set_title_wikidata(item)

        if self.wikidata.get('image'):
            self.images.append({'kind': 'wikidata-image',
                                'file': self.wikidata['image']})

    def _update_wikidata(self, label, value):
        """
        add or update Wikidata
        """
        if self.wikidata.get(label):
            try:
                self.wikidata[label].append(value)
            except AttributeError:
                first = self.wikidata.get(label)
                self.wikidata[label] = [first]
                self.wikidata[label].append(value)
        else:
            self.wikidata[label] = value

    def _wikidata_props(self, query_claims):
        """
        returns dict containing selected properties from Wikidata query claims
        """
        props = collections.defaultdict(list)
        for claim in query_claims:
            for prop in query_claims.get(claim):
                try:
                    snak = prop.get('mainsnak').get('datavalue').get('value')
                except AttributeError:
                    if self._WIKIPROPS.get(claim):
                        props[claim] = None
                        continue
                try:
                    if snak.get('id'):
                        val = snak.get('id')
                    elif snak.get('text'):
                        val = snak.get('text')
                    elif snak.get('time'):
                        val = snak.get('time')
                    else:
                        val = snak
                except AttributeError:
                    val = snak

                if not val or not [x for x in val if x]:
                    raise ValueError("%s %s" % (claim, prop))

                if self._WIKIPROPS.get(claim):
                    props[claim].append(val)

        return dict(props)

    def get(self, show=True, proxy=None, timeout=0):
        """
        make requests needed to populate most the things.
        some sequence of:
        - get_query()
        - get_parse()
        - get_wikidata()
        """
        if self.wikibase and not self.title:
            self._defer_imageinfo = True
            self.get_wikidata(False, proxy, timeout)
            self.get_query(False, proxy, timeout)
            self._defer_imageinfo = False
            self.get_parse(show, proxy, timeout)
        else:
            self._defer_imageinfo = True
            self.get_query(False, proxy, timeout)
            self.get_parse(False, proxy, timeout)
            self._defer_imageinfo = False
            self.get_wikidata(show, proxy, timeout)
        return self

    def get_claims(self, show=True, proxy=None, timeout=0):
        """
        Wikidata:API (action=wbgetentities) for labels of claims
        - e.g. {'Q298': 'country'} resolves to {'country': 'Chile'}
        - use get_wikidata() to populate claims
        """
        if not self.claims:
            raise LookupError("get_claims needs claims")

        self._request('claims', show, proxy, timeout)

        return self

    def get_imageinfo(self, show=False, proxy=None, timeout=0):
        """
        MediaWiki request for API:Imageinfo
        - images: <dict> updates image URLs, sizes, etc.
        https://www.mediawiki.org/wiki/API:Imageinfo
        """
        if not self.images:
            raise LookupError("get_images needs images")

        if not self._missing_imageinfo() and 'imageinfo' in self.cache:
            utils.stderr("complete imageinfo in cache")
            return

        self._request('imageinfo', show, proxy, timeout)

        return self

    def get_parse(self, show=True, proxy=None, timeout=0):
        """
        MediaWiki:API action=parse request for:
        - images: <dict> {parse-image, parse-cover}
        - infobox: <dict> Infobox data as python dictionary
        - links: <list> interwiki links (iwlinks)
        - pageid: <int> Wikipedia database ID
        - parsetree: <str> XML parse tree
        - wikibase: <str> Wikidata entity ID or wikidata URL
        - wikitext: <str> raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=parse
        """
        if not self.title and not self.pageid:
            raise LookupError("get_parse needs title or pageid")

        self._request('parse', show, proxy, timeout)

        return self

    def get_query(self, show=True, proxy=None, timeout=0):
        """
        MediaWiki:API action=query request for:
        - description: <str> Wikidata description (via pageterms)
        - extext: <str> plain text (Markdown) extract
        - extract: <str> HTML extract via Extension:TextExtract
        - images: <dict> {query-pageimage, query-thumbnail}
        - label: <str> Wikidata label (via pageterms)
        - modified (page): <str> ISO8601 date and time
        - pageid: <int> Wikipedia database ID
        - random: <str> a random article title with every request!
        - url: <str> the canonical wiki URL
        - url_raw: <str> ostensible raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=query
        """
        if not self.title and not self.pageid:
            raise LookupError("get_query needs title or pageid")

        self._request('query', show, proxy, timeout)

        return self

    def get_random(self, show=True, proxy=None, timeout=0):
        """
        MediaWiki:API (action=query) request for:
        - pageid: <int> Wikipedia database ID
        - title: <str> article title
        https://www.mediawiki.org/wiki/API:Random
        """
        _fetch = self._fetch(proxy, timeout)
        query = _fetch.query('random', None)
        response = _fetch.curl(query)

        try:
            data = utils.json_loads(response)
        except ValueError:
            raise LookupError(query.replace('&format=json', ''))

        rand = data.get('query').get('random')[0]
        self.pageid = rand.get('id')

        if not self.title:
            self.title = rand.get('title').replace(' ', '_')

        if show:
            self.show()

        return self

    def get_rest(self, show=True, proxy=None, timeout=0):
        """
        RESTBase (/page/mobile-text/)
        - description: <str> apparently, Wikidata description
        - images: <dict> {rest-image, rest-thumb}
        - lead: <str> encyclopedia-like lead section
        - modified (page): <str> ISO8601 date and time
        - url: <str> the canonical wiki URL
        - url_raw: <str> ostensible raw wikitext URL
        https://en.wikipedia.org/api/rest_v1/
        """
        if not self.title:
            raise LookupError("get_rest needs a title")

        self._request('rest', show, proxy, timeout)

        return self

    def get_wikidata(self, show=True, proxy=None, timeout=0):
        """
        Wikidata:API (action=wbgetentities) for:
        - claims: <dict> Wikidata claims (to be resolved)
        - description: <str> Wikidata description
        - images: <dict> {wikidata-image} Wikidata Property:P18
        - label: <str> Wikidata label
        - modified (wikidata): <str> ISO8601 date and time
        - props: <dict> Wikidata properties
        - what: <str> Wikidata Property:P31 "instance of"
        - wikibase: <str> Wikidata item ID
        - wikidata: <dict> resolved Wikidata properties
        - wikidata_url: <str> Wikidata URL
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if not self.wikibase and (not self.lang and not self.title):
            raise LookupError("get_wikidata needs wikibase or lang and title")

        self._request('wikidata', show, proxy, timeout)

        return self

    def image(self, token):
        """
        returns first image info with kind containing token
        """
        for img in self.images:
            if token in img.get('kind'):
                return img

    def show(self):
        """
        pretty-print instance attributes
        """
        maxlen = 72

        def ptrunc(prefix, tail):
            """pretty truncate text"""
            pad = 8
            text = tail[:maxlen - (len(prefix) + pad)]
            if len(prefix) + len(tail) + pad >= maxlen:
                text += '...'
            return text

        data = {}
        for item in dir(self):
            prop = getattr(self, item)
            if not prop or callable(prop) or item.startswith('_'):
                continue
            if isinstance(prop, dict):
                keys = sorted(prop.keys())
                klen = len(keys)
                kstr = ', '.join(keys)
                data[item] = ptrunc(item, "<dict(%d)> {%s}" % (klen, kstr))
            elif isinstance(prop, list):
                data[item] = "<list(%d)>" % len(prop)
            elif utils.is_text(prop):
                prop = prop.strip().replace("\n", '')
                prop = re.sub(' +', ' ', prop)
                if len(prop) > maxlen and not prop.startswith('http'):
                    prop = ptrunc(item, "<str(%d)> %s" % (len(prop), prop))
                data[item] = prop
            else:
                data[item] = prop

        lang = self.lang
        if self.variant:
            lang = "%s/%s" % (self.lang, self.variant)

        thing = self.title
        if self.wikibase and not self.title:
            thing = self.wikibase
            if thing.startswith('http'):
                thing = thing.split('/')[-1]

        header = "%s (%s)" % (thing, lang)

        # NOTE: json.dumps and pprint show unicode literals
        utils.stderr(header, self.silent)
        utils.stderr("{", self.silent)
        for item in sorted(data):
            utils.stderr("  %s: %s" % (item, data[item]), self.silent)
        utils.stderr("}", self.silent)

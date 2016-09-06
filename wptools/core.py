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

import json
import re
import sys

import lxml
import html2text

from . import fetch
from . import utils


class WPTools(object):
    """
    A user-created :class:WPTools object.
    """

    _skipmap = {
        'get_parse': {'parsetree', 'wikibase', 'wikitext'},
        'get_query': {'extract', 'pageid', 'random'},
        'get_wikidata': {'label'}
    }

    coordinates = None
    description = None
    image = None
    label = None

    claims = {}
    extext = None
    extract = None
    fatal = False
    g_claims = None
    g_parse = None
    g_query = None
    g_rest = None
    g_wikidata = None
    images = {}
    infobox = None
    lastmodified = None
    lead = None
    links = None
    pageid = None
    pageimage = None
    parsetree = None
    random = None
    thumbnail = None
    title = None
    url = None
    urlraw = None
    wikibase = None
    wikitext = None

    def __init__(self, title='', lang='en', wikibase=None,
                 silent=False, verbose=False, wiki=None):
        self.silent = silent
        self.lang = lang
        self.__fetch = fetch.WPToolsFetch(self.lang, silent, verbose, wiki)
        if wikibase:
            self.wikibase = wikibase
        if title:
            self.title = title.replace(' ', '_')
        if not wikibase and not title:
            self.get_random()
        else:
            self.show()
        self.verbose = verbose

    def __getattrs(self):
        """
        returns list of "public" attributes
        """
        return [x for x in self.__dict__
                if getattr(self, x)
                and not x.startswith("__")]

    def __get_claim_label(self, item):
        """
        returns label value from Wikidata claim item
        """
        labels = item.get('labels')
        if labels:
            try:
                return labels.get(self.lang).get('value')
            except AttributeError:
                return labels.get('value')

    def __get_lead(self, data):
        """
        returns lead HTML with heading and image and refs removed
        """
        lead = []
        lead.append(self.__get_lead_heading())
        lead.append(self.__get_lead_image())
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
            heading += "&mdash;<i>%s</i>" % self.description
        return "<p heading>%s</p>" % heading

    def __get_lead_image(self):
        """
        returns <img> HTML from image attributes
        """
        alt = self.title
        if hasattr(self, 'label') and self.label:
            alt = self.label

        src = None
        cls = None
        if hasattr(self, 'image') and self.image:
            src = self.image
            cls = 'image'
        elif hasattr(self, 'pageimage') and self.pageimage:
            src = self.pageimage
            cls = 'pageimage'
        elif hasattr(self, 'thumbnail') and self.thumbnail:
            src = self.thumbnail
            cls = 'thumbnail'
        if src:
            img = ("<img %s src=\"%s\" alt=\"%s\" title=\"%s\" "
                   % (cls, src, alt, alt))
            img += "align=right width=240>"
            return img

    def __get_lead_metadata(self):
        """
        returns lead HTML metadata from attributes
        """
        meta = []
        if hasattr(self, 'lastmodified'):
            meta.append("Last modified: %s" % self.lastmodified)
        if hasattr(self, 'geo'):
            meta.append("coordinates: %s" % self.coordinates)
        return "<p metadata>%s</p>" % "\n".join([x for x in meta if x])

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
                if 'text' in item:
                    ids = utils.span_ids(item['text'])
                    if ids and ids == ['coordinates']:
                        continue
                    pars.append(item['text'])
                else:
                    pars.append(", ".join(item.keys()))
            break

        if pars:
            html = "\n".join(pars)
            self.g_rest['html'] = html
            return self.__postprocess_lead(html)

    def __postprocess_lead(self, html):
        """
        snip and base href lead HTML
        """
        snip = utils.snip_html(html, verbose=1 if self.verbose else 0)
        snip = "<p snipped>%s</p>" % snip
        url = urlparse(self.g_rest['query'])
        base = "%s://%s" % (url.scheme, url.netloc)
        snip = snip.replace('href="/', "href=\"%s/" % base)
        return snip

    def __setattr(self, attr, value, suffix):
        """
        set attribute, append suffix if clobber
        """
        if hasattr(self, attr):
            extant = getattr(self, attr)
            if extant != value:
                attr = "%s_%s" % (attr, suffix)
                setattr(self, attr, value)

    def _set_parse_data(self):
        """
        set attributes derived from MediaWiki (action=parse)
        """
        try:
            data = json_loads(self.g_parse['response'])
        except ValueError:
            self.fatal = True
            stderr("Could not load query response: %s"
                   % self.g_parse['query'])
            return

        pdata = data.get('parse')
        if not pdata:
            error = data.get('error')
            if error:
                stderr("MediaWiki:API error: %s" % error)
            return

        parsetree = pdata.get('parsetree')
        self.infobox = get_infobox(parsetree)
        self.links = get_links(pdata.get('iwlinks'))
        self.pageid = pdata.get('pageid')
        self.parsetree = parsetree
        self.title = pdata.get('title').replace(' ', '_')
        self.wikibase = pdata.get('properties').get('wikibase_item')
        self.wikitext = pdata.get('wikitext')

    def _set_query_data(self):
        """
        set attributes derived from MediaWiki (action=query)
        """
        try:
            data = json_loads(self.g_query['response'])
        except ValueError:
            self.fatal = True
            stderr("Could not load query response: %s"
                   % self.g_query['query'])
            return

        qdata = data.get('query')
        page = qdata.get('pages')[0]

        if page.get('missing'):
            stderr("MediaWiki:API missing title: %s" % page.get('title'))
            return

        extext = None
        extract = page.get('extract')
        if extract:
            self.extract = extract
            extext = html2text.html2text(self.extract)
            if extext:
                self.extext = extext.strip()

        images = {}
        pageimage = page.get('pageimage')
        if pageimage:
            images['qimage'] = pageimage
            self.pageimage = utils.media_url(pageimage)

        thumbnail = page.get('thumbnail')
        if thumbnail:
            images['qthumb'] = thumbnail
            self.thumbnail = thumbnail

        self.images = images

        self.pageid = page.get('pageid')

        props = page.get('pageprops')
        if props:
            wikibase = props.get('wikibase_item')
            if wikibase:
                self.wikibase = wikibase

        self.random = qdata.get('random')[0]["title"]
        self.title = page.get('title').replace(' ', '_')

        url = page.get('fullurl')
        if url:
            self.url = url
            self.urlraw = url + '?action=raw'

    def _set_rest_data(self):
        """
        set attributes derived from RESTBase
        """
        try:
            data = json_loads(self.g_rest['response'])
            url = urlparse(self.g_rest['query'])
        except ValueError:
            self.fatal = True
            stderr("Could not load query response: %s"
                   % self.g_rest['query'])
            return

        if data.get('detail'):
            error = data.get('detail').get('error')
            if error:
                stderr("RESTBase error: %s" % error)
                return

        self.__setattr('description', data.get('description'), 'rest')

        image = data.get('image')
        if image:
            self.images['rimage'] = image
            image_file = utils.media_url(image.get('file'))
            # apparently get_query pageimage or get_wikidata image
            # self.__setattr('pageimage', image_file, 'rest')
            self.pageimage = image_file

        thumb = data.get('thumb')
        if thumb:
            self.images['rthumb'] = thumb
            thumbnail = "%s:%s" % (url.scheme, thumb.get('url'))
            # apparently scaled (larger) get_query thumbnail
            # self.__setattr('thumbnail', thumbnail, 'rest')
            self.thumbnail = thumbnail

        title = data.get('displaytitle')
        if 'redirected' in data:
            title = data['redirected']
        self.title = title.replace(' ', '_')

        self.lastmodified = data.get('lastmodified')
        self.pageid = data.get('id')

        self.url = "%s://%s/wiki/%s" % (url.scheme, url.netloc, self.title)
        self.urlraw = self.url + '?action=raw'

        if 'sections' in data:
            lead = self.__get_lead(data)
            if lead:
                self.lead = lead

    def _set_wikidata_claims(self, claims):
        """
        set selected Wikidata claims attributes
        """
        if not claims:
            return

        claimattr = {}

        p17 = claims.get('P17')  # P17 country
        if p17:
            country = p17[0].get('mainsnak').get('datavalue').get('value')
            if country:
                claimattr[country.get('id')] = 'country'

        p18 = claims.get('P18')  # P18 image
        if p18:
            image = p18[0].get('mainsnak').get('datavalue').get('value')
            if image:
                self.image = utils.media_url(image)
            if self.images:
                self.images['wimage'] = image

        p30 = claims.get('P30')  # P30 continent
        if p30:
            cont = p30[0].get('mainsnak').get('datavalue').get('value')
            if cont:
                claimattr[cont.get('id')] = 'continent'

        p625 = claims.get('P625')  # P625 coordinate location
        if p625:
            geo = p625[0].get('mainsnak').get('datavalue').get('value')
            if geo:
                self.coordinates = "%s,%s" % (geo.get('latitude'),
                                              geo.get('longitude'))

        if claimattr:
            self.claims = claimattr

    def _set_wikidata(self):
        """
        set attributes derived from Wikidata (action=wbentities)
        """
        try:
            data = json_loads(self.g_wikidata['response'])
            entities = data.get('entities')
        except ValueError:
            self.fatal = True
            stderr("Could not load query response: %s"
                   % self.g_wikidata['query'])
            return

        item = entities.get(next(iter(entities)))

        if 'id' not in item:
            if 'title' in item:
                stderr("Wikidata missing title: %s" % item['title'])
            return

        self.wikibase = "https://www.wikidata.org/wiki/%s" % item.get('id')

        self._set_wikidata_claims(item.get('claims'))

        descriptions = item.get('descriptions')
        if descriptions:
            try:
                self.description = descriptions.get(self.lang).get('value')
            except AttributeError:
                self.description = descriptions.get('value')

        labels = item.get('labels')
        if labels:
            try:
                self.label = labels.get(self.lang).get('value')
            except AttributeError:
                self.label = labels.get('value')

        if hasattr(self, 'label') and not self.title:
            self.title = self.label.replace(' ', '_')

    def _skip_get(self, action):
        """
        returns true if additional request is likely not needed
        """
        if self.fatal:
            return True
        for attr in self._skipmap[action]:
            has_attr = hasattr(self, attr)
            if not has_attr:
                return False
            if has_attr and not getattr(self, attr):
                return False
        stderr("skipping %s" % action, self.silent)
        return True

    def get(self):
        """
        make all requests necessary to populate all the things:
        - get_query()
        - get_parse()
        - get_wikidata()
        """
        if self.wikibase and not self.title:
            self.get_wikidata(show=False)
            self.get_query(show=False)
            self.get_parse()
        else:
            self.get_query(show=False)
            self.get_parse(show=False)
            self.get_wikidata()
        return self

    def get_claims(self, show=True):
        """
        Wikidata:API (action=wbgetentities) for labels of claims
        - e.g. turns claim {'Q298': 'country'} into country: Chile
        - use get_wikidata() to populate selected claims
        """
        if not self.claims:
            return

        thing = {'id': "|".join(self.claims.keys()), 'props': 'labels'}
        query = self.__fetch.query('wikidata', thing)

        g_claims = {}
        g_claims['query'] = query
        g_claims['response'] = self.__fetch.curl(query)
        g_claims['info'] = self.__fetch.info
        self.g_claims = g_claims

        data = json_loads(self.g_claims['response'])
        entities = data.get('entities')
        for item in entities:
            attr = self.claims[item]
            value = self.__get_claim_label(entities[item])
            if value:
                setattr(self, attr, value)

        if show:
            self.show()
        return self

    def get_parse(self, show=True):
        """
        MediaWiki:API action=parse request for:
        - infobox: <dict> Infobox data as python dictionary
        - links: <list> interwiki links (iwlinks)
        - pageid: <int> Wikipedia database ID
        - parsetree: <unicode> XML parse tree
        - wikibase: <unicode> Wikidata entity ID or wikidata URL
        - wikitext: <unicode> raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=parse
        """
        if self._skip_get('get_parse'):
            return
        query = self.__fetch.query('parse', self.title)
        parse = {}
        parse['query'] = query
        parse['response'] = self.__fetch.curl(query)
        parse['info'] = self.__fetch.info
        self.g_parse = parse
        self._set_parse_data()
        if show:
            self.show()
        return self

    def get_query(self, show=True):
        """
        MediaWiki:API action=query request for:
        - extext: <unicode> plain text (Markdown) extract
        - extract: <unicode> HTML extract via Extension:TextExtract
        - images: <dict> {qimage, qthumb}
        - pageid: <int> Wikipedia database ID
        - pageimage: <unicode> pageimage URL via Extension:PageImages
        - random: <unicode> a random article title with every request!
        - thumbnail: <unicode> thumbnail URL via Extension:PageImages
        - url: <unicode> the canonical wiki URL
        - urlraw: <unicode> ostensible raw wikitext URL
        https://en.wikipedia.org/w/api.php?action=help&modules=query
        """
        if self._skip_get('get_query'):
            return
        qry = self.__fetch.query('query', self.title)
        if self.pageid:
            qry = self.__fetch.query('query', self.pageid, pageid=True)
        query = {}
        query['query'] = qry
        query['response'] = self.__fetch.curl(qry)
        query['info'] = self.__fetch.info
        self.g_query = query
        self._set_query_data()
        if show:
            self.show()
        return self

    def get_random(self, show=True):
        """
        MediaWiki:API (action=query) request for:
        - pageid: <int> Wikipedia database ID
        - title: <unicode> article title
        https://www.mediawiki.org/wiki/API:Random
        """
        query = self.__fetch.query('random', None)
        response = self.__fetch.curl(query)

        try:
            data = json_loads(response)
            rdata = data.get('query').get('random')[0]
        except ValueError:
            self.fatal = True
            stderr("Could not load query response: %s" % query)
            return

        self.pageid = rdata.get('id')
        self.title = rdata.get('title').replace(' ', '_')

        if show:
            self.show()
        return self

    def get_rest(self, show=True):
        """
        RESTBase (/page/mobile-text/)
        - description: <unicode> apparently, Wikidata description
        - images: <dict> {rimage, rthumb}
        - lastmodified: <str> ISO8601 date and time
        - lead: <str> encyclopedia-like lead section
        - pageimage: <unicode> apparently, action=query pageimage
        - thumbnail: <unicode> larger action=query thumbnail
        - url: <unicode> the canonical wiki URL
        - urlraw: <unicode> ostensible raw wikitext URL
        https://en.wikipedia.org/api/rest_v1/
        """
        try:
            title = quote(self.title)
        except KeyError:
            title = quote(self.title.encode('utf-8'))
        query = self.__fetch.query('/page/mobile-text/', title)
        rest = {}
        rest['query'] = query
        rest['response'] = self.__fetch.curl(query)
        rest['info'] = self.__fetch.info
        self.g_rest = rest
        self._set_rest_data()
        if show:
            self.show()
        return self

    def get_wikidata(self, show=True):
        """
        Wikidata:API (action=wbgetentities) for:
        - claims: <dict> Wikidata claims (see get_claims)
        - coordinates: <str> Wikidata Property:P625 coordinates (lat,lon)
        - description: <unicode> Wikidata description
        - image: <unicode> Wikidata Property:P18 image URL
        - images: <dict> {wimage}
        - label: <unicode> Wikidata label
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if self._skip_get('get_wikidata'):
            return

        thing = {'id': '', 'site': '', 'title': ''}
        if self.wikibase:
            thing['id'] = self.wikibase
        elif self.lang and self.title:
            thing['site'] = "%swiki" % self.lang
            thing['title'] = self.title
        else:
            stderr("%s: need wikibase or lang and title"
                   % self.get_wikidata.__name__,
                   self.silent)
            return

        query = self.__fetch.query('wikidata', thing)
        wdata = {}
        wdata['query'] = query
        wdata['response'] = self.__fetch.curl(query)
        wdata['info'] = self.__fetch.info
        self.g_wikidata = wdata
        self._set_wikidata()
        if show:
            self.show()
        return self

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
        for item in self.__getattrs():
            if item.startswith("_WPTools"):
                continue

            if item is None:
                continue

            prop = self.__dict__[item]

            if isinstance(prop, dict):
                keys = sorted(prop.keys())
                klen = len(keys)
                kstr = ', '.join(keys)
                data[item] = ptrunc(item, "<dict(%d)> {%s}" % (klen, kstr))
            elif isinstance(prop, list):
                data[item] = "<list(%d)>" % len(prop)
            elif is_text(prop):
                prop = prop.strip().replace("\n", '')
                prop = re.sub(' +', ' ', prop)
                if len(prop) > maxlen and not prop.startswith('http'):
                    prop = ptrunc(item, "<str(%d)> %s" % (len(prop), prop))
                data[item] = prop
            else:
                data[item] = prop

        header = None
        if hasattr(self, 'title') and self.title:
            header = "%s (%s)" % (self.title, self.lang)
        elif hasattr(self, 'wikibase') and self.wikibase:
            header = "%s (%s)" % (self.wikibase, self.lang)

        # NOTE: json.dumps and pprint show unicode literals
        stderr(header, self.silent)
        stderr("{", self.silent)
        for item in sorted(data):
            stderr("  %s: %s" % (item, data[item]), self.silent)
        stderr("}", self.silent)


def get_infobox(ptree):
    """
    returns infobox <type 'dict'> from parse/parsetreee
    """
    for item in lxml.etree.fromstring(ptree).xpath("//template"):
        if "box" in item.find('title').text:
            return utils.template_to_dict(item)


def get_links(iwlinks):
    """
    returns list of interwiki links from parse/iwlinks
    """
    links = []
    for item in iwlinks:
        links.append(item['url'])
    if len(links) == 1:
        return links[0]
    return sorted(links) if links else None


def is_text(obj, name=None):
    """
    returns True if object is text-like
    """
    try:  # python2
        ans = isinstance(obj, basestring)
    except NameError:  # python3
        ans = isinstance(obj, str)
    if name:
        stderr("is_text: (%s) %s = %s" % (ans, name, obj.__class__))
    return ans


def json_loads(data):
    """
    python-version safe json.loads
    """
    try:  # python2
        return json.loads(data)
    except TypeError:  # python3
        return json.loads(data.decode('utf-8'))


def stderr(msg, silent=False):
    """write msg to stderr if not silent"""
    if not silent:
        print(msg, file=sys.stderr)

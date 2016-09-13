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

    WIKIPROPS = {'P17': 'country',
                 'P18': 'image',
                 'P27': 'citizenship',
                 'P30': 'continent',
                 'P31': 'class',
                 'P50': 'author',
                 'P57': 'director',
                 'P86': 'composer',
                 'P110': 'illustrator',
                 'P123': 'publisher',
                 'P170': 'creator',
                 'P175': 'performer',
                 'P176': 'material',
                 'P212': 'ISBN',
                 'P301': 'topic',
                 'P345': 'IMDB',
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

    claims = {}
    description = None
    extext = None
    extract = None
    fatal = False
    g_claims = None
    g_parse = None
    g_query = None
    g_rest = None
    g_wikidata = None
    image = None
    images = {}
    infobox = None
    label = None
    lastmodified = None
    lead = None
    links = None
    pageid = None
    pageimage = None
    parsetree = None
    props = {}
    random = None
    thumbnail = None
    title = None
    url = None
    urlraw = None
    wikibase = None
    wikitext = None
    wikidata = {}

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

    def __get_entity_prop(self, entity, prop):
        """
        returns Wikidata entity property value
        """
        if entity.get(prop):
            try:
                return entity.get(prop).get(self.lang).get('value')
            except AttributeError:
                return entity.get(prop).get('value')

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

    def __postprocess_wikidata(self):
        """
        transform selected wikidata items
        """
        if 'coordinates' in self.wikidata:
            data = self.wikidata['coordinates']
            if 'latitude' in data:
                geo = "%s,%s" % (data['latitude'], data['longitude'])
                self.wikidata['coordinates'] = geo

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
            source = thumbnail.get('source')
            if source:
                self.thumbnail = source

        self.images = images

        self.pageid = page.get('pageid')

        pageprops = page.get('pageprops')
        if pageprops:
            wikibase = pageprops.get('wikibase_item')
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

    def _process_claims(self, item_claims):
        """
        set Wikidata properties and Q claims from claims
        """
        clams = {}
        props = {}
        wdata = {}

        for pid in item_claims:
            if pid in self.WIKIPROPS:
                props[pid] = wikidata_property(item_claims, pid)

        for item in props:
            label = self.WIKIPROPS[item]
            if is_text(props[item]) and re.match(r'^Q\d+', props[item]):
                clams[props[item]] = label
            else:
                wdata[label] = props[item]

        if clams:
            self.claims = clams
        if props:
            self.props = props
        if wdata:
            self.wikidata = wdata
            self.__postprocess_wikidata()

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

        self._process_claims(item.get('claims'))

        descriptions = self.__get_entity_prop(item, 'descriptions')
        if descriptions:
            self.description = descriptions

        if 'image' in self.wikidata:
            self.image = utils.media_url(self.wikidata['image'])

        labels = self.__get_entity_prop(item, 'labels')
        if labels:
            self.label = labels

        if hasattr(self, 'label') and not self.title:
            self.title = self.label.replace(' ', '_')

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
        - e.g. {'Q298': 'country'} resolves to {'country': 'Chile'}
        - use get_wikidata() to populate claims
        """
        if not self.claims:
            return
        if self.g_claims:
            stderr("Request cached in g_claims.")
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
            value = self.__get_entity_prop(entities[item], 'labels')
            if value:
                self.wikidata[attr] = value

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
        if self.g_parse:
            stderr("Request cached in g_parse.")
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
        if self.g_query:
            stderr("Request cached in g_query.")
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
        if self.g_rest:
            stderr("Request cached in g_rest.")
            return
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

    def get_wikidata(self, show=True, get_claims=True):
        """
        Wikidata:API (action=wbgetentities) for:
        - claims: <dict> Wikidata claims (to be resolved)
        - description: <unicode> Wikidata description
        - image: <unicode> Wikidata Property:P18 image URL
        - images: <dict> {wimage}
        - label: <unicode> Wikidata label
        - props: <dict> Wikidata properties
        - wikibase: <str> Wikidata URL
        - wikidata: <dict> resolved Wikidata properties and claims
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if self.g_wikidata:
            stderr("Request cached in g_wikidata.")
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
        if self.claims and get_claims:
            self.get_claims(False)
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
    returns infobox <type 'dict'> from get_parse:parsetreee
    """
    for item in lxml.etree.fromstring(ptree).xpath("//template"):
        if "box" in item.find('title').text:
            return utils.template_to_dict(item)


def get_links(iwlinks):
    """
    returns list of interwiki links get_parse/iwlinks
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


def wikidata_property(claims, pid):
    """
    returns Wikidata property value from claims
    """
    prop = claims.get(pid)[0]
    if prop:
        val = prop.get('mainsnak').get('datavalue').get('value')
        if isinstance(val, dict):
            if 'id' in val:
                return val['id']
            if 'time' in val:
                return val['time']
        return val

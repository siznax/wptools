# -*- coding:utf-8 -*-

"""
WPTools core module.
~~~~~~~~~~~~~~~~~~~~
"""

from __future__ import print_function

import html2text
import json
import lxml
import re
import sys
import urlparse

from . import fetch
from . import utils


class WPTools:
    """
    A user-created :class:WPTools object.
    """

    _skipmap = {
        'get_parse': {'parsetree', 'wikibase', 'wikitext'},
        'get_query': {'extract', 'pageid', 'random'},
        'get_wikidata': {'Label'}
    }

    fatal = False
    images = dict()
    pageid = None
    title = None
    wikibase = None

    def __init__(self, title='',  lang='en', wikibase=None,
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

    def __get_links(self, iwlinks):
        """
        returns list of interwiki links from parse/iwlinks
        """
        links = []
        for item in iwlinks:
            links.append(item['url'])
        if len(links) == 1:
            return links[0]
        return sorted(links) if links else None

    def __get_infobox(self, ptree):
        """
        returns infobox <type 'dict'> from parse/parsetreee
        """
        for item in lxml.etree.fromstring(ptree).xpath("//template"):
            if "box" in item.find('title').text:
                return utils.template_to_dict(item)

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

    def __get_lead_geo(self, data):
        """
        returns span.geo text from RESTBase sections
        """
        for section in data['sections']:
            for item in section.get('items'):
                if item.get('text') is None:
                    continue
                text = item['text']
                if 'geo' in utils.span_classes(text):
                    doc = lxml.html.fromstring(text)
                    for geo in doc.xpath('//span[@class="geo"]'):
                        return geo.text

    def __get_lead_heading(self):
        """
        returns lead section HTML heading
        """
        if not hasattr(self, 'url') or not hasattr(self, 'title'):
            return
        heading = "<a href=\"%s\">%s</a>" % (self.url, self.title)
        if hasattr(self, 'Description') and self.Description:
            heading += "&mdash;<i>%s</i>" % self.Description
        return "<p heading>%s</p>" % heading

    def __get_lead_image(self):
        """
        returns <img> HTML from image attributes
        """
        alt = self.title
        if hasattr(self, 'Label') and self.Label:
            alt = self.Label

        src = None
        cls = None
        if hasattr(self, 'Image') and self.Image:
            src = self.Image
            cls = 'Image'
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
            meta.append("Coordinates: %s" % self.geo)
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
            pars = "\n".join(pars)
            self.g_rest['html'] = pars
            return self.__postprocess_lead(pars)

    def __postprocess_lead(self, html):
        """
        snip and base href lead HTML
        """
        snip = utils.snip_html(html, verbose=1 if self.verbose else 0)
        snip = "<p snipped>%s</p>" % snip
        url = urlparse.urlparse(self.g_rest['query'])
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
            data = json.loads(self.g_parse['response'])
        except:
            self.fatal = True
            stderr("Could not load JSON response for query: %s"
                   % self.g_parse['query'])
            return

        pdata = data.get('parse')
        if not pdata:
            error = data.get('error')
            if error:
                stderr("MediaWiki:API error: %s" % error)
            return

        parsetree = pdata.get('parsetree')
        self.infobox = self.__get_infobox(parsetree)
        self.links = self.__get_links(pdata.get('iwlinks'))
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
            data = json.loads(self.g_query['response'])
        except:
            self.fatal = True
            stderr("Could not load JSON response for query: %s"
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
            try:
                extext = html2text.html2text(self.extract)
                if extext.strip():
                    self.extext = extext
            except:
                pass

        images = dict()
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
        self.url = url
        self.urlraw = url + '?action=raw'

    def _set_rest_data(self):
        """
        set attributes derived from RESTBase
        """
        try:
            data = json.loads(self.g_rest['response'])
            url = urlparse.urlparse(self.g_rest['query'])
        except:
            self.fatal = True
            stderr("Could not load JSON response for query: %s"
                   % self.g_rest['query'])
            return

        if data.get('detail'):
            error = data.get('detail').get('error')
            if error:
                stderr("RESTBase error: %s" % error)
                return

        self.__setattr('Description', data.get('description'), 'rest')

        image = data.get('image')
        if image:
            self.images['rimage'] = image
            image_file = utils.media_url(image.get('file'))
            # apparently get_query pageimage or get_wikidata Image
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
        if 'normalizedtitle' in data:
            title = data['normalizedtitle']
        self.title = title.replace(' ', '_')

        self.lastmodified = data.get('lastmodified')
        self.pageid = data.get('id')

        self.url = "%s://%s/wiki/%s" % (url.scheme, url.netloc, self.title)
        self.urlraw = self.url + '?action=raw'

        if 'sections' in data:
            geo = self.__get_lead_geo(data)
            if geo:
                self.geo = geo

        if 'sections' in data:
            lead = self.__get_lead(data)
            if lead:
                self.lead = lead

    def _set_wikibase_claims(self, claims):
        """
        set selected Wikidata claims attributes
        """
        if not claims:
            return

        # P17  country
        P18 = claims.get('P18')  # image
        if P18:
            image = P18[0].get('mainsnak').get('datavalue').get('value')
            self.Image = utils.media_url(image)
            if self.images:
                self.images['wimage'] = image
        # P585 point in time
        # P625 coordinate location

    def _set_wikibase_data(self):
        """
        set attributes derived from Wikidata (action=wbentities)
        """
        try:
            data = json.loads(self.g_wikidata['response'])
        except:
            self.fatal = True
            stderr("Could not load JSON response for query: %s"
                   % self.g_wikidata['query'])
            return
        entities = data.get('entities')
        item = None
        if entities:
            item = entities.get(self.wikibase.upper())
        if not item:
            return
        self.wikibase = "https://www.wikidata.org/wiki/%s" % item.get('id')

        self._set_wikibase_claims(item.get('claims'))

        descriptions = item.get('descriptions')
        if descriptions:
            try:
                self.Description = descriptions.get(self.lang).get('value')
            except:
                self.Description = descriptions.get('value')

        labels = item.get('labels')
        if labels:
            try:
                self.Label = labels.get(self.lang).get('value')
            except:
                self.Label = labels.get('value')
        if self.Label and not self.title:
            self.title = self.Label.replace(' ', '_')

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
        - images: <dict> {image, pageimages, thumbnail}
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
            rdata = json.loads(response).get('query').get('random')[0]
        except:
            self.fatal = True
            stderr("Could not load JSON response for query: %s" % query)
            return
        self.pageid = rdata.get('id')
        self.title = rdata.get('title').replace(' ', '_')
        if show:
            self.show()
        return self

    def get_rest(self, show=True):
        """
        MediaWiki:RESTBase (/page/mobile-text/)
        """
        query = self.__fetch.query('/page/mobile-text/', self.title)
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
        - Description: <unicode> Wikidata description
        - Image: <unicode> Wikidata Property:P18 image URL
        - Label: <unicode> Wikidata label
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if not self.wikibase:
            stderr("%s: need wikibase" % self.get_wikidata.__name__,
                   self.silent)
            return
        if self._skip_get('get_wikidata'):
            return
        query = self.__fetch.query('wikidata', self.wikibase)
        wdata = {}
        wdata['query'] = query
        wdata['response'] = self.__fetch.curl(query)
        wdata['info'] = self.__fetch.info
        self.g_wikidata = wdata
        self._set_wikibase_data()
        if show:
            self.show()
        return self

    def show(self):
        """
        pretty-print instance attributes
        """
        maxlen = 72

        def ptrunc(prefix, tail):  # pretty truncate
            pad = 8
            _str = tail[:maxlen - (len(prefix) + pad)]
            if len(prefix) + len(tail) + pad >= maxlen:
                _str += '...'
            try:
                return str(_str)
            except:
                return _str

        data = {}
        attrs = [x for x in self.__dict__ if getattr(self, x)
                 and not x.startswith("__")]
        for item in attrs:
            if item.startswith("_WPTools"):
                continue
            prop = self.__dict__[item]
            data[item] = prop
            if item is None:
                continue
            if type(prop) is dict:
                keys = sorted(prop.keys())
                klen = len(keys)
                kstr = ', '.join(keys)
                data[item] = ptrunc(item, "<dict(%d)> {%s}" % (klen, kstr))
            if type(prop) is list:
                data[item] = "<list(%d)>" % len(prop)
            if type(prop) is str or type(prop) is unicode:
                prop = prop.strip().replace("\n", '')
                prop = re.sub(' +', ' ', prop)
                try:
                    prop = str(prop.encode('utf-8'))
                except:
                    prop = str(prop)
                if len(prop) > maxlen and not prop.startswith('http'):
                    prop = ptrunc(item, "<str(%d)> %s" % (len(prop), prop))
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


def stderr(msg, silent=False):
    if not silent:
        print(msg, file=sys.stderr)

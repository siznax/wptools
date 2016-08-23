# -*- coding:utf-8 -*-

"""
WPTools core module.
~~~~~~~~~~~~~~~~~~~~
"""

from __future__ import print_function

import html2text
import json
import lxml.etree
import re
import sys

from . import fetch
from . import utils


class WPTools:

    _skipmap = {
        'get_parse': {'parsetree', 'wikibase', 'wikitext'},
        'get_query': {'extract', 'pageid', 'random'},
        'get_wikidata': {'Label'}
    }

    Description = None
    Image = None
    Label = None
    g_parse = {}
    g_query = {}
    g_wikidata = {}
    images = {}
    pageid = None
    title = None
    wikibase = None

    def __init__(self, title='', lang='en', verbose=False,
                 wikibase=None, wiki=None):
        self.lang = lang
        self.__fetch = fetch.WPToolsFetch(self.lang, verbose, wiki)
        if wikibase:
            self.wikibase = wikibase
        if title:
            self.title = title.replace(' ', '_')
        if not wikibase and not title:
            self.get_random()
        else:
            self.show()

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

    def __get_images(self, page):
        """
        returns image dict from query/page
        """
        image = {}
        if page.get('pageimage'):
            image['pageimage'] = {
                "file": page.get('pageimage'),
                "source": page.get('pageimage')}
        if page.get('thumbnail'):
            thumb = page.get('thumbnail')
            image["thumbnail"] = thumb
            self.thumbnail = thumb.get('source')
        return image if image else None

    def __get_infobox(self, ptree):
        """
        returns infobox <type 'dict'> from parse/parsetreee
        """
        for item in lxml.etree.fromstring(ptree).xpath("//template"):
            if "box" in item.find('title').text:
                return utils.template_to_dict(item)

    def _set_parse_data(self):
        """
        set attributes derived from action=parse
        """
        data = json.loads(self.g_parse['response'])
        pdata = data.get('parse')
        if not pdata:
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
        set attributes derived from action=query
        """
        data = json.loads(self.g_query['response'])
        qdata = data.get('query')
        page = qdata.get('pages')[0]
        self.extract = page.get('extract')
        try:
            self.extext = html2text.html2text(self.extract)
        except:
            pass
        self.images = self.__get_images(page)
        self.pageid = page.get('pageid')
        if self.images and 'pageimage' in self.images:
            pageimage = self.images.get('pageimage').get('source')
            self.pageimage = utils.media_url(pageimage)
        self.random = qdata.get('random')[0]["title"]
        self.title = page.get('title').replace(' ', '_')
        self.url = page.get('fullurl')
        self.urlraw = self._wiki_url(raw=True)

    def _set_wikibase_claims(self, claims):
        if not claims:
            return
        # P17 = claims.get('P17')  # country
        # P585 = claims.get('P569')  # point in time
        P18 = claims.get('P18')  # image
        if P18:
            image = P18[0].get('mainsnak').get('datavalue').get('value')
            self.Image = utils.media_url(image)
            if self.images:
                self.images['Image'] = image

    def _set_wikibase_data(self):
        """
        set attributes derived from action=wbentities
        """
        data = json.loads(self.g_wikidata['response'])
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

    def _skip_get(self, action):
        """
        returns true if additional request is likely not needed
        """
        for attr in self._skipmap[action]:
            has_attr = hasattr(self, attr)
            if not has_attr:
                return False
            if has_attr and not getattr(self, attr):
                return False
        print("skipping %s" % action, file=sys.stderr)
        return True

    def _wiki_url(self, raw=False):
        url = "https://%s.wikipedia.org/wiki/%s" % (self.lang, self.title)
        if raw:
            return url + '?action=raw'
        return url

    def get(self):
        """
        make all available API requests and fully hydrate instance
        """
        self.get_query(show=False)
        self.get_parse(show=False)
        self.get_wikidata()

    def get_parse(self, show=True):
        """
        request MediaWiki:API action=parse
        see https://en.wikipedia.org/w/api.php?action=help&modules=parse
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
        request MediaWiki:API action=query
        see https://en.wikipedia.org/w/api.php?action=help&modules=query
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
        request MediaWiki API:Random
        see https://www.mediawiki.org/wiki/API:Random
        """
        query = self.__fetch.query('random', None)
        response = self.__fetch.curl(query)
        rdata = json.loads(response).get('query').get('random')[0]
        self.pageid = rdata.get('id')
        self.title = rdata.get('title').replace(' ', '_')
        if show:
            self.show()
        return self

    def get_wikidata(self, show=True):
        """
        request Wikidata:API action=wbgetentities
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if not self.wikibase:
            print("instance needs a wikibase")
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
        prettyprint instance attributes
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
        print(header, file=sys.stderr)
        print("{")
        for item in sorted(data):
            print("  %s: %s" % (item, data[item]))
        print("}")

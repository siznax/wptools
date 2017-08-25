# -*- coding:utf-8 -*-

"""
WPTools Query module
~~~~~~~~~~~~~~~~~~~~

Support for forming WMF API query strings.

* Mediawiki: https://www.mediawiki.org/wiki/API:Main_page
* Wikidata: https://www.wikidata.org/wiki/Wikidata:Data_access
* RESTBase: https://www.mediawiki.org/wiki/RESTBase

See also:

* WMF: https://wikimediafoundation.org/wiki/Our_projects
"""

from __future__ import print_function

try:  # python2
    from urllib import quote, unquote
except ImportError:  # python3
    from urllib.parse import quote, unquote

from string import Template

import random


class WPToolsQuery(object):
    """
    WPToolsQuery class
    """

    IMAGEINFO = Template((
        "${WIKI}/w/api.php?action=query"
        "&format=json"
        "&formatversion=2"
        "&iiprop=size|url|timestamp"
        "&prop=imageinfo"
        "&titles=${FILES}"))

    LIST = Template((
        "${WIKI}/w/api.php?action=query"
        "&format=json"
        "&formatversion=2"
        "&list=${LIST}"))

    PARSE = Template((
        "${WIKI}/w/api.php?action=parse"
        "&contentmodel=text"
        "&disableeditsection="
        "&disablelimitreport="
        "&disabletoc="
        "&format=json"
        "&formatversion=2"
        "&prop=text|iwlinks|parsetree|wikitext|displaytitle|properties"
        "&redirects"
        "&page=${PAGE}"))

    QUERY = Template((
        "${WIKI}/w/api.php?action=query"
        "&cllimit=500"
        "&clshow=!hidden"
        "&exintro"
        "&format=json"
        "&formatversion=2"
        "&imlimit=500"
        "&inprop=url|watchers"
        "&list=random"
        "&lllimit=500"
        "&pithumbsize=240"
        "&ppprop=wikibase_item"
        "&prop=categories|contributors|extracts|images|info|langlinks"
        "|pageimages|pageprops|pageterms|pageviews"
        "&redirects"
        "&rnlimit=1"
        "&rnnamespace=0"
        "&titles=${TITLES}"))

    WIKIDATA = Template((
        "${WIKI}/w/api.php?action=wbgetentities"
        "&format=json"
        "&formatversion=2"
        "&languages=${LANG}"
        "&props=${PROPS}"
        "&redirects=yes"))

    lang = None
    status = None
    variant = None
    wiki = None

    def __init__(self, lang='en', variant=None, wiki=None):
        """
        Returns a WPToolsQuery object

        Arguments:
        - [lang=en]: <str> Mediawiki language code
        - [variant=None]: <str> language variant
        - [wiki=None]: <str> alternative wiki site
        """
        self.lang = lang
        self.variant = variant
        self.wiki = wiki or "%s.wikipedia.org" % self.lang
        self.domain = domain_name(self.wiki)
        self.uri = self.wiki_uri(self.wiki)

    def category(self, title, pageid=None, limit=500, namespace=None):
        """
        Returns category query string
        """
        query = self.LIST.substitute(WIKI=self.uri, LIST='categorymembers')

        if limit:
            query += "&cmlimit=%d" % limit

        if namespace is not None:
            query += "&cmnamespace=%d" % namespace

        if title:
            query += "&cmtitle=" + safequote(title)

        if pageid:
            query += "&cmpageid=%d" % pageid

        self.set_status('categorymembers', pageid or title)

        return query

    def claims(self, qids):
        """
        Returns Wikidata claims query string
        """
        self.domain = 'www.wikidata.org'
        self.uri = self.wiki_uri(self.domain)

        query = self.WIKIDATA.substitute(
            WIKI=self.uri,
            LANG=self.variant or self.lang,
            PROPS='labels')

        qids = '|'.join(qids)
        query += "&ids=%s" % qids

        self.set_status('claims', qids)

        return query

    def imageinfo(self, files):
        """
        Returns imageinfo query string
        """
        files = '|'.join([safequote(x) for x in files])

        self.set_status('imageinfo', files)

        return self.IMAGEINFO.substitute(WIKI=self.uri, FILES=files)

    def parse(self, title, pageid=None):
        """
        Returns Mediawiki action=parse query string
        """
        qry = self.PARSE.substitute(WIKI=self.uri, PAGE=title or pageid)

        if pageid and not title:
            qry = qry.replace('&page=', '&pageid=').replace('&redirects', '')

        if self.variant:
            qry += '&variant=' + self.variant

        self.set_status('parse', pageid or title)

        return qry

    def query(self, titles, pageids=None):
        """
        Returns MediaWiki action=query query string
        """
        query = self.QUERY.substitute(WIKI=self.uri, TITLES=titles or pageids)

        if pageids and not titles:
            query = query.replace('&titles=', '&pageids=')

        if self.variant:
            query += '&variant=' + self.variant

        self.set_status('query', pageids or titles)

        return query

    def random(self, namespace=0):
        """
        Returns query string for random page
        """
        query = self.LIST.substitute(WIKI=self.uri, LIST='random')
        query += "&rnlimit=1&rnnamespace=%d" % namespace

        emoji = [
            u'\U0001f32f',  # burrito or wrap
            u'\U0001f355',  # slice of pizza
            u'\U0001f35c',  # steaming bowl of ramen
            u'\U0001f363',  # sushi
            u'\U0001f369',  # doughnut
            u'\U0001f36a',  # cookie
            u'\U0001f36d',  # lollipop
            u'\U0001f370',  # strawberry shortcake
        ]

        self.set_status('random:%d' % namespace, random.choice(emoji))

        return query

    def rest(self, endpoint):
        """
        Returns RESTBase query string
        """
        self.set_status('rest', safequote(endpoint))

        return "%s/api/rest_v1%s" % (self.uri, endpoint)

    def set_status(self, action, target):
        """
        Sets query status with format: "{domain} ({action}) {target}"
        """
        try:
            target = unquote(target)
        except (AttributeError, TypeError):
            pass

        status = "%s (%s) %s" % (self.domain, action, target)

        if len(status) >= 80:
            self.status = status[:77] + '...'
        else:
            self.status = status

    def wiki_uri(self, wiki):
        """
        Returns scheme://domain from wiki name
        """
        if wiki.startswith('http'):
            return wiki
        return "https://" + self.domain

    def wikidata(self, title, wikibase=None):
        """
        Returns Wikidata query string
        """
        self.domain = 'www.wikidata.org'
        self.uri = self.wiki_uri(self.domain)

        query = self.WIKIDATA.substitute(
            WIKI=self.uri,
            LANG=self.variant or self.lang,
            PROPS="info|claims|descriptions|labels|sitelinks")

        if title:
            query += "&sites=%swiki" % self.lang
            query += "&titles=%s" % title
        elif wikibase:
            query += "&ids=%s" % wikibase

        self.set_status('wikidata', wikibase or title)

        return query


def domain_name(wiki):
    """
    Returns domain name from wiki name
    """
    if '//' in wiki:
        wiki = wiki.split('//')[1]
    return wiki.split('/')[0]


def safequote(string):
    """
    UTF-8 encode string if quote() throws KeyError
    """
    try:
        return quote(string)
    except KeyError:
        return quote(string.encode('utf-8'))

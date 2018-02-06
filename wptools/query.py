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

    MAXWIDTH = 72
    RPAD = 4

    IMAGEINFO = Template((
        "${WIKI}/w/api.php?action=query"
        "&format=json"
        "&formatversion=2"
        "&iiprop=size|url|timestamp|extmetadata"
        "&prop=imageinfo"
        "&titles=${FILES}"))

    LIST = Template((
        "${WIKI}/w/api.php?action=query"
        "&format=json"
        "&formatversion=2"
        "&list=${LIST}"))

    PARSE = Template((
        "${WIKI}/w/api.php?action=parse"
        "&format=json"
        "&formatversion=2"
        "&contentmodel=text"
        "&disableeditsection="
        "&disablelimitreport="
        "&disabletoc="
        "&prop=text|iwlinks|parsetree|wikitext|displaytitle|properties"
        "&redirects"
        "&page=${PAGE}"))

    QUERY = Template((
        "${WIKI}/w/api.php?action=query"
        "&exintro"
        "&format=json"
        "&formatversion=2"
        "&inprop=url|watchers"
        "&list=random"
        "&pithumbsize=240"
        "&pllimit=500"
        "&ppprop=disambiguation|wikibase_item"
        "&prop=extracts|info|links|pageassessments|pageimages|pageprops"
        "|pageterms|redirects"
        "&redirects"
        "&rdlimit=500"
        "&rnlimit=1"
        "&rnnamespace=0"
        "&titles=${TITLES}"))

    QUERYMORE = Template((
        "${WIKI}/w/api.php?action=query"
        "&cllimit=500"
        "&clshow=!hidden"
        "&format=json"
        "&formatversion=2"
        "&imlimit=500"
        "&lllimit=500"
        "&pclimit=500"
        "&prop=categories|contributors|images|langlinks|pageviews"
        "&redirects"
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

        if title and pageid:
            title = None

        if title:
            query += "&cmtitle=" + safequote(title)

        if pageid:
            query += "&cmpageid=%d" % pageid

        self.set_status('categorymembers', pageid or title)

        return query

    def labels(self, qids):
        """
        Returns Wikidata labels query string
        """
        if len(qids) > 50:
            raise ValueError("The limit is 50.")

        self.domain = 'www.wikidata.org'
        self.uri = self.wiki_uri(self.domain)

        query = self.WIKIDATA.substitute(
            WIKI=self.uri,
            LANG=self.variant or self.lang,
            PROPS='labels')

        qids = '|'.join(qids)
        query += "&ids=%s" % qids

        self.set_status('labels', qids)

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
        qry = self.PARSE.substitute(WIKI=self.uri,
                                    PAGE=safequote(title) or pageid)

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
        query = self.QUERY.substitute(WIKI=self.uri,
                                      TITLES=safequote(titles) or pageids)

        if pageids and not titles:
            query = query.replace('&titles=', '&pageids=')

        if self.variant:
            query += '&variant=' + self.variant

        self.set_status('query', titles or pageids)

        return query

    def querymore(self, titles, pageids=None):
        """
        Returns MediaWiki action=query query string (for MORE)
        A much more expensive query for popular pages
        """
        query = self.QUERYMORE.substitute(
            WIKI=self.uri,
            TITLES=safequote(titles) or pageids)

        if pageids and not titles:
            query = query.replace('&titles=', '&pageids=')

        if self.variant:
            query += '&variant=' + self.variant

        self.set_status('querymore', pageids or titles)

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

        action = 'random'
        if namespace:
            action = 'random:%d' % namespace

        self.set_status(action, random.choice(emoji))

        return query

    def restbase(self, endpoint, title):
        """
        Returns RESTBase query string
        """
        if not endpoint:
            raise ValueError("invalid endpoint: %s" % endpoint)

        route = endpoint
        if title and endpoint != '/page/':
            route = endpoint + safequote_restbase(title)

        self.set_status('restbase', route)

        return "%s/api/rest_v1/%s" % (self.uri, route[1:])

    def set_status(self, action, target):
        """
        Sets query status with format: "{domain} ({action}) {target}"
        """
        try:
            target = unquote(target)
        except (AttributeError, TypeError):
            pass

        status = "%s (%s) %s" % (self.domain, action, target)
        status = status.strip().replace('\n', '')

        if len(status) >= self.MAXWIDTH:
            tail = '...'
            extent = self.MAXWIDTH - (len(tail) + self.RPAD)
            self.status = status[:extent] + tail
        else:
            self.status = status

    def site(self, action):
        """
        Returns site query
        """
        query = None
        viewdays = 7

        if action == 'siteinfo':
            query = self.uri + ('/w/api.php?action=query'
                                '&meta=siteinfo|siteviews'
                                '&siprop=general|statistics'
                                '&list=mostviewed&pvimlimit=max')
            query += '&pvisdays=%d' % viewdays  # meta=siteviews
            self.set_status('query', 'siteinfo|siteviews|mostviewed')
        elif action == 'sitematrix':
            query = self.uri + '/w/api.php?action=sitematrix'
            self.set_status('sitematrix', 'all')
        elif action == 'sitevisitors':
            query = self.uri + ('/w/api.php?action=query'
                                '&meta=siteviews&pvismetric=uniques')
            query += '&pvisdays=%d' % viewdays  # meta=siteviews
            self.set_status('query', 'siteviews:uniques')

        query += '&format=json&formatversion=2'

        if not query:
            raise ValueError("Could not form query")

        return query

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
            PROPS="aliases|info|claims|descriptions|labels|sitelinks")

        if wikibase:
            query += "&ids=%s" % wikibase
        elif title:
            title = safequote(title)
            query += "&sites=%swiki" % self.lang
            query += "&titles=%s" % title

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
    Try to UTF-8 encode and percent-quote string
    """
    if string is None:
        return
    try:
        return quote(string.encode('utf-8'))
    except UnicodeDecodeError:
        return quote(string)


def safequote_restbase(title):
    """
    Safequote restbase title possibly having slash in title
    """
    try:
        return quote(title.encode('utf-8'), safe='')
    except UnicodeDecodeError:
        return quote(title, safe='')

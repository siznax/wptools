# -*- coding:utf-8 -*-

"""
WPTools Fetch module.
"""

from __future__ import print_function
try:  # python2
    from urllib import unquote
except ImportError:  # python3
    from urllib.parse import unquote

from io import BytesIO
from string import Template

import sys

import certifi
import pycurl

from . import __title__, __contact__, __version__


class WPToolsFetch(object):
    """
    Supports MediaWiki:API, RESTBase, Wikidata API HTTP requests
    """

    QUERY = {
        "imageinfo": Template((
            "${WIKI}/w/api.php?action=query"
            "&format=json"
            "&formatversion=2"
            "&iiprop=size|url|timestamp"
            "&prop=imageinfo"
            "&titles=${thing}")),
        "parse": Template((
            "${WIKI}/w/api.php?action=parse"
            "&contentmodel=text"
            "&disableeditsection="
            "&disablelimitreport="
            "&disabletoc="
            "&format=json"
            "&formatversion=2"
            "&prop="
            "text|iwlinks|parsetree|wikitext|displaytitle|properties"
            "&redirects"
            "&page=${thing}")),
        "query": Template((
            "${WIKI}/w/api.php?action=query"
            "&exintro"
            "&format=json"
            "&formatversion=2"
            "&inprop=displaytitle|url"
            "&list=random"
            "&pithumbsize=240"
            "&ppprop=wikibase_item"
            "&prop=extracts|images|info|pageimages|pageprops|pageterms"
            "&redirects"
            "&rnlimit=1"
            "&rnnamespace=0"
            "&titles=${thing}")),
        "random": Template((
            "${WIKI}/w/api.php?action=query"
            "&format=json"
            "&formatversion=2"
            "&list=random"
            "&rnlimit=1"
            "&rnnamespace=0")),
        "rest": Template((
            "${WIKI}/api/rest_v1${entrypoint}${title}")),
        "wikidata": Template((
            "${WIKI}/w/api.php?action=wbgetentities"
            "&format=json"
            "&formatversion=2"
            "&ids=${ids}"
            "&languages=${lang}"
            "&props=${props}"
            "&redirects=yes"
            "&sites=${site}"
            "&titles=${title}"))
    }

    action = None
    info = None
    silent = False
    thing = None
    title = None

    def __init__(self, **kwargs):
        self.lang = kwargs.get('lang')
        self.silent = kwargs.get('silent') or False
        self.variant = kwargs.get('variant')
        self.verbose = kwargs.get('verbose') or False
        self.wiki = kwargs.get('wiki')

        self.curl_setup(kwargs.get('proxy'), kwargs.get('timeout'))

    def __del__(self):
        self.cobj.close()

    def curl(self, url):
        """
        in favor of python-requests for speed
        """

        # consistently faster than requests by 3x
        #
        # r = requests.get(url,
        #                  headers={'User-Agent': self.user_agent})
        # return r.text

        crl = self.cobj
        try:
            crl.setopt(pycurl.URL, url)
        except UnicodeEncodeError:
            crl.setopt(pycurl.URL, url.encode('utf-8'))

        if not self.silent:
            print(self.status_line(), file=sys.stderr)

        return self.curl_perform(crl)

    def curl_perform(self, crl):
        """
        performs HTTP GET and returns body of response
        """
        bfr = BytesIO()
        crl.setopt(crl.WRITEFUNCTION, bfr.write)
        crl.perform()
        info = curl_info(crl)
        if info:
            if self.verbose and not self.silent:
                for item in sorted(info):
                    print("  %s: %s" % (item, info[item]), file=sys.stderr)
            self.info = info
        body = bfr.getvalue()
        bfr.close()
        return body

    def curl_setup(self, proxy=None, timeout=0):
        """
        set curl options
        """

        crl = pycurl.Curl()
        crl.setopt(pycurl.USERAGENT, user_agent())
        crl.setopt(pycurl.FOLLOWLOCATION, True)
        crl.setopt(pycurl.CAINFO, certifi.where())

        if proxy:
            crl.setopt(pycurl.PROXY, proxy)
        if timeout:  # 0 = wait forever
            crl.setopt(pycurl.TIMEOUT, timeout)

        self.cobj = crl

    def query(self, action, thing, pageid=False):
        """
        returns API query string
        """
        if not self.wiki or self.wiki == 'www.wikidata.org':
            self.wiki = "%s.wikipedia.org" % self.lang

        tmpl_wiki = self.wiki
        if not tmpl_wiki.startswith('http'):
            tmpl_wiki = 'https://' + self.wiki

        if action.startswith('/'):
            qry = self.QUERY['rest'].substitute(
                WIKI=tmpl_wiki,
                entrypoint=action,
                title=thing)
        elif action == 'wikidata' or action == 'claims':
            ids = ''
            site = ''
            title = ''
            props = "info|claims|descriptions|labels|sitelinks"
            self.wiki = 'www.wikidata.org'
            tmpl_wiki = 'https://' + self.wiki

            if thing.get('props'):
                props = thing['props']
            if thing.get('id'):
                ids = thing.get('id')
                thing = ids
            else:
                site = thing.get('site')
                title = thing.get('title')
                thing = title

            qry = self.QUERY['wikidata'].substitute(
                WIKI=tmpl_wiki,
                ids=ids,
                lang=self.variant or self.lang,
                props=props,
                site=site,
                title=title)
        else:
            qry = self.QUERY[action].substitute(
                WIKI=tmpl_wiki,
                thing=thing)

        if action == 'parse' and pageid:
            qry = qry.replace('&page=', '&pageid=').replace('&redirects', '')

        if action == 'query' and pageid:
            qry = qry.replace('&titles=', '&pageids=')

        if self.variant:
            qry += '&variant=' + self.variant

        self.action = action
        self.thing = thing
        return qry

    def status_line(self):
        """
        returns request status line
        """
        try:
            thing = unquote(self.thing)
        except (AttributeError, TypeError):
            thing = self.thing

        status = "%s (%s) %s" % (self.wiki, self.action, thing)

        if len(status) > 80:
            status = status[:72] + '...'

        return status


def curl_info(crl):
    """
    returns curl (response) info from Pycurl object
    """
    kbps = crl.getinfo(crl.SPEED_DOWNLOAD) / 1000.0
    url = crl.getinfo(crl.EFFECTIVE_URL)
    url = url.replace("&format=json", '').replace("&formatversion=2", '')
    return {"url": url,
            "user-agent": user_agent(),
            "content": crl.getinfo(crl.CONTENT_TYPE),
            "status": crl.getinfo(crl.RESPONSE_CODE),
            "bytes": crl.getinfo(crl.SIZE_DOWNLOAD),
            "seconds": "%5.3f" % crl.getinfo(crl.TOTAL_TIME),
            "kB/s": "%3.1f" % kbps}


def get(action, title):
    """
    returns GET result from API
    """
    obj = WPToolsFetch()
    return obj.curl(obj.query(action, title))


def user_agent():
    """
    returns the wptools user-agent string
    """
    return "%s/%s (%s) %s" % (__title__,
                              __version__,
                              __contact__,
                              pycurl.version)

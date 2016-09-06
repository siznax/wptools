# -*- coding:utf-8 -*-

"""
WPTools Fetch module.
"""

from __future__ import print_function

from io import BytesIO
from string import Template

import sys
import pycurl

from . import __title__, __contact__, __version__


class WPToolsFetch(object):
    """
    Supports MediaWiki:API, RESTBase, Wikidata API HTTP requests
    """

    QUERY = {
        "parse": Template((
            "https://${WIKI}/w/api.php?action=parse"
            "&contentmodel=text"
            "&disableeditsection="
            "&disablelimitreport="
            "&disabletoc="
            "&format=json"
            "&formatversion=2"
            "&page=${thing}"
            "&prop="
            "text|iwlinks|parsetree|wikitext|displaytitle|properties"
            "&redirects")),
        "query": Template((
            "https://${WIKI}/w/api.php?action=query"
            "&exintro"
            "&format=json"
            "&formatversion=2"
            "&inprop=displaytitle|url|watchers"
            "&list=random"
            "&pithumbsize=240"
            "&ppprop=wikibase_item"
            "&prop=extracts|images|info|pageimages|pageprops"
            "&redirects"
            "&rnlimit=1"
            "&rnnamespace=0"
            "&titles=${thing}")),
        "random": Template((
            "https://${WIKI}/w/api.php?action=query"
            "&format=json"
            "&formatversion=2"
            "&list=random"
            "&rnlimit=1"
            "&rnnamespace=0")),
        "rest": Template((
            "https://${WIKI}/api/rest_v1${entrypoint}${title}")),
        "wikidata": Template((
            "https://${WIKI}/w/api.php?action=wbgetentities"
            "&format=json"
            "&formatversion=2"
            "&ids=${ids}"
            "&languages=${lang}"
            "&props=${props}"
            "&sites=${site}"
            "&titles=${title}"))
    }

    action = None
    info = None
    silent = False
    thing = None
    timeout = 15
    title = None

    def __init__(self, lang='en', silent=False, verbose=False, wiki=None):
        self.lang = lang
        self.wiki = "%s.wikipedia.org" % lang
        if wiki:
            self.wiki = wiki
        self.silent = silent
        self.verbose = verbose
        self.curl_setup()

    def __del__(self):
        self.cobj.close()

    def curl(self, url):
        """
        in favor of python-requests for speed
        """

        # consistently faster than requests by 3x
        #
        # r = requests.get(url,
        #                  timeout=self.TIMEOUT,
        #                  headers={'User-Agent': self.user_agent})
        # return r.text

        crl = self.cobj
        try:
            crl.setopt(pycurl.URL, url)
        except UnicodeEncodeError:
            crl.setopt(pycurl.URL, url.encode('utf-8'))
        if not self.silent:
            print("%s (action=%s) %s" % (self.wiki, self.action,
                                         self.thing), file=sys.stderr)
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

    def curl_setup(self):
        """
        set curl options
        """
        crl = pycurl.Curl()
        crl.setopt(pycurl.USERAGENT, user_agent())
        crl.setopt(pycurl.FOLLOWLOCATION, True)
        crl.setopt(pycurl.CONNECTTIMEOUT, self.timeout)
        self.cobj = crl

    def query(self, action, thing, pageid=False):
        """
        returns API query string
        """
        if action.startswith('/'):
            qry = self.QUERY['rest'].substitute(
                WIKI=self.wiki,
                entrypoint=action,
                title=thing)
        elif action == 'wikidata':
            ids = ''
            site = ''
            title = ''
            props = "info|claims|descriptions|labels|sitelinks"
            if thing.get('props'):
                props = thing['props']
            if thing.get('id'):
                ids = thing.get('id')
                thing = ids
            else:
                site = thing.get('site')
                title = thing.get('title')
                thing = title
            qry = self.QUERY[action].substitute(
                WIKI="www.wikidata.org",
                ids=ids,
                lang=self.lang,
                props=props,
                site=site,
                title=title)
        else:
            qry = self.QUERY[action].substitute(
                WIKI=self.wiki,
                thing=thing)

        if action == 'query' and pageid:
            qry = qry.replace('&titles=', '&pageids=')

        self.action = action
        self.thing = thing
        return qry


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

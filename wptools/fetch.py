# -*- coding:utf-8 -*-

"""
WPTools Fetch module.
"""

from __future__ import print_function

import pycurl
import sys
import time

from . import __title__, __contact__, __version__
from io import BytesIO
from string import Template


class WPToolsFetch:

    ENDPOINT = "http://en.wikipedia.org"
    QUERY = {"html": Template(("${WIKI}/w/api.php?action=parse"
                               "&format=json"
                               "&page=${page}"
                               "&prop=text"
                               "&contentmodel=text"
                               "&disablelimitreport="
                               "&disableeditsection="
                               "&disabletoc=")),
             "images": Template(("${WIKI}/w/api.php?action=query"
                                 "&titles=${page}"
                                 "&format=json"
                                 "&formatversion=2"
                                 "&prop=images")),
             "pageimages": Template(("${WIKI}/w/api.php?action=query"
                                     "&titles=${page}"
                                     "&format=json"
                                     "&formatversion=2"
                                     "&prop=pageimages"
                                     "&pithumbsize=320"
                                     "&pilimit=1")),
             "parsetree": Template(("${WIKI}/w/api.php?action=parse"
                                    "&format=json"
                                    "&page=${page}"
                                    "&prop=parsetree"
                                    "&disablelimitreport="
                                    "&disableeditsection="
                                    "&disabletoc="
                                    "&contentmodel=text")),
             "wikitext": Template(("${WIKI}/w/api.php?action=parse"
                                   "&format=json"
                                   "&page=${page}"
                                   "&prop=wikitext"
                                   "&contentmodel=wikitext"
                                   "&disablelimitreport="
                                   "&disableeditsection="
                                   "&disabletoc="))}
    RETRY_SLEEP = 2
    RETRY_MAX = 3
    TIMEOUT = 5

    def __init__(self, wiki=ENDPOINT, lead=False, verbose=False):
        self.wiki = wiki or self.ENDPOINT
        self.lead = lead
        self.verbose = verbose
        self.curl_setup()
        self.title = None
        self.retries = 0

    def __del__(self):
        self.cobj.close()
        if self.verbose:
            print("connection closed.", file=sys.stderr)

    def curl(self, url):
        """speed"""

        # consistently faster than requests by 3x
        #
        # r = requests.get(url,
        #                  timeout=self.TIMEOUT,
        #                  headers={'User-Agent': self.user_agent})
        # return r.text

        crl = self.cobj
        try:
            crl.setopt(crl.URL, url)
        except UnicodeEncodeError:
            crl.setopt(crl.URL, url.encode('utf-8'))
        return self.curl_perform(crl)

    def curl_perform(self, crl):
        """try curl, retry after sleep up to max retries"""
        if self.retries >= self.RETRY_MAX:
            return "RETRY_MAX (%d) exceeded!" % self.RETRY_MAX
        try:
            bfr = BytesIO()
            crl.setopt(crl.WRITEFUNCTION, bfr.write)
            crl.perform()
            if self.verbose:
                self.curl_report(crl)
            body = bfr.getvalue()
            bfr.close()
            self.retries = 0
            return body
        except Exception as detail:
            print("RETRY Caught exception: %s" % detail)
            self.retries += 1
            time.sleep(self.RETRY_SLEEP)
            self.curl_perform(crl)

    def curl_report(self, crl):
        kbps = crl.getinfo(crl.SPEED_DOWNLOAD) / 1000.0
        out = {"url": crl.getinfo(crl.EFFECTIVE_URL),
               "user-agent": self.user_agent(),
               "content": crl.getinfo(crl.CONTENT_TYPE),
               "status": crl.getinfo(crl.RESPONSE_CODE),
               "bytes": crl.getinfo(crl.SIZE_DOWNLOAD),
               "seconds": "%5.3f" % crl.getinfo(crl.TOTAL_TIME),
               "kB/s": "%3.1f" % kbps}
        print("WPToolsFetch HTTP", file=sys.stderr)
        for key in out:
            print("    %s: %s" % (key, out[key]), file=sys.stderr)
        print(file=sys.stderr)

    def curl_setup(self):
        crl = pycurl.Curl()
        # crl.setopt(crl.URL, wiki)
        crl.setopt(crl.USERAGENT, self.user_agent())
        crl.setopt(crl.FOLLOWLOCATION, True)
        crl.setopt(crl.CONNECTTIMEOUT, self.TIMEOUT)
        self.cobj = crl

    def html(self, title):
        """get HTML keeping connection open"""
        return self.curl(self.query('html', title))

    def query(self, content, page):
        self.title = page
        page = page.replace(" ", "+")
        page = page[0].upper() + page[1:]
        qry = self.QUERY[content].substitute(WIKI=self.wiki, page=page)
        if self.lead:
            return qry + "&section=0"
        return qry

    def user_agent(self):
        return "%s/%s (+%s)" % (__title__, __version__, __contact__)


def get_html(title,
             lead=False,
             test=False,
             wiki=WPToolsFetch.ENDPOINT,
             verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    qry = obj.query('html', title)
    if test:
        return qry
    return obj.curl(qry)


def get_infobox():
    """currently, no way to query Infobox directly"""
    pass


def get_images(title, source,
               lead=False,
               test=False,
               wiki=WPToolsFetch.ENDPOINT,
               verbose=False):
    if source == "infobox":
        return get_parsetree(title, lead, test, wiki, verbose)
    obj = WPToolsFetch(wiki, lead, verbose)
    qry = obj.query(source, title)
    if test:
        return qry
    return obj.curl(qry)


def get_parsetree(title,
                  lead=False,
                  test=False,
                  wiki=WPToolsFetch.ENDPOINT,
                  verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    qry = obj.query('parsetree', title)
    if test:
        return qry
    return obj.curl(qry)


def get_wikitext(title,
                 lead=False,
                 test=False,
                 wiki=WPToolsFetch.ENDPOINT,
                 verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    url = obj.query('wikitext', title)
    if test:
        return url
    return obj.curl(url)

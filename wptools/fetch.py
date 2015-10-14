# -*- coding:utf-8 -*-

"""
WPTools Fetch module.
"""

from __future__ import print_function

import pycurl
import requests
import sys

from . import __title__, __contact__, __version__
from io import BytesIO
from string import Template


class WPToolsFetch:

    ENDPOINT = "http://en.wikipedia.org"
    ACTION_QUERY = Template(("${API}/w/api.php?action=query"
                             "&titles=${titles}"
                             "&format=json"
                             "&formatversion=2"
                             "&prop=revisions"  # latest revision
                             "&rvprop=content"  # content of latest revision
                             "&redirects"
                             "&continue="))
    QUERY = {"html": Template(("${WIKI}/w/api.php?action=parse"
                               "&format=json"
                               "&page=${page}"
                               "&prop=text"
                               "&contentmodel=text"
                               "&disablelimitreport="
                               "&disableeditsection="
                               "&disabletoc=")),
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
    TIMEOUT = 30

    def __init__(self, wiki, lead, verbose):
        self.wiki = wiki or self.ENDPOINT
        self.lead = lead
        self.verbose = verbose

    def curl(self, url, agent):
        """speed"""

        def report(crl):
            kbps = crl.getinfo(crl.SPEED_DOWNLOAD) / 1000.0
            out = {"url": url,
                   "user-agent": agent,
                   "content": crl.getinfo(crl.CONTENT_TYPE),
                   "status": crl.getinfo(crl.RESPONSE_CODE),
                   "bytes": crl.getinfo(crl.SIZE_DOWNLOAD),
                   "seconds": "%5.3f" % crl.getinfo(crl.TOTAL_TIME),
                   "kB/s": "%3.1f" % kbps}
            for key in out:
                print("%s: %s" % (key, out[key]), file=sys.stderr)

        bfr = BytesIO()
        crl = pycurl.Curl()
        crl.setopt(crl.URL, url)
        crl.setopt(crl.USERAGENT, agent)
        crl.setopt(crl.FOLLOWLOCATION, True)
        crl.setopt(crl.CONNECTTIMEOUT, self.TIMEOUT)
        crl.setopt(crl.WRITEFUNCTION, bfr.write)
        crl.perform()
        if self.verbose:
            report(crl)
        crl.close()
        body = bfr.getvalue()
        bfr.close()
        return body

    def query(self, content, page):
        page = page.replace(" ", "+")
        qry = self.QUERY[content].substitute(WIKI=self.wiki, page=page)
        if self.lead:
            return qry + "&section=0"
        return qry

    def request(self, url, hdr, output):
        print("GET %s\nHDR %s\nOUT %s" % (url, hdr, output), file=sys.stderr)
        r = requests.get(url, headers=hdr, timeout=self.TIMEOUT)
        if r.status_code != 200:
            raise ValueError("HTTP status code = %d" % r.status_code)
        return r.content


def get_html(title, lead, test, wiki, verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    qry = obj.query('html', title)
    if test:
        return qry
    return obj.curl(qry, user_agent())


def get_infobox():
    pass


def get_parsetree(title, lead, test, wiki, verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    qry = obj.query('parsetree', title)
    if test:
        return qry
    return obj.curl(qry, user_agent())


def get_wikitext(title, lead, test, wiki, verbose=False):
    obj = WPToolsFetch(wiki, lead, verbose)
    url = obj.query('wikitext', title)
    if test:
        return url
    return obj.curl(url, user_agent())


def user_agent(api=False):
    return "%s/%s (+%s)" % (__title__, __version__, __contact__)

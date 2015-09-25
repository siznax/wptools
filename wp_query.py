#!/usr/bin/env python
"""
Query MediaWiki API given titles, format

INPUT
    titles  "fuzzy" Wiki titles
    format  see FORMATS (default=json)

OUTPUT
    articles in format selected

References
    https://www.mediawiki.org/wiki/API:Main_page
    https://www.mediawiki.org/wiki/API:Tutorial
    https://www.mediawiki.org/wiki/API:Data_formats
"""

from __future__ import print_function

__author__ = "siznax"
__version__ = "15 Sep 2015"

import argparse
import json
import requests
import sys
import time
import urllib

from string import Template

DEFAULT = "json"
ENDPOINT = "http://en.wikipedia.org/w/api.php"
FORMATS = ['json', 'php', 'xml', 'wikitext']
QUERY = Template(("${API}?titles=${titles}"
                  "&format=${_format}"
                  "&formatversion=2"
                  "&action=query"
                  "&prop=revisions"  # latest revision
                  "&rvprop=content"  # content of latest revision
                  "&redirects"
                  "&continue="))
UA_NAME = "wptools.wp_query"
UA_URL = "https://github.com/siznax/wptools"
UA_VERSION = "0.0.1"


def _stderr(msg):
    print(msg, file=sys.stderr)
    sys.stderr.flush()
    sys.stdout.flush()


def _user_agent():
    # get this from env in web app context
    return "%s/%s (+%s)" % (UA_NAME, UA_VERSION, UA_URL)


def _wikitext(_json):
    text = ""
    for page in json.loads(_json)["query"]["pages"]:
        text += "\n= %s =\n" % page["title"]
        text += page["revisions"][0]["content"]
    return text


def query(titles, _format, lead):
    """returns MW/API query formed given titles, format"""
    if isinstance(titles, str):
        titles = [titles]
    titles = "|".join([urllib.quote(t) for t in titles])
    qry = QUERY.substitute(API=ENDPOINT, titles=titles, _format=_format)
    if lead:
        qry += "&rvsection=0"
    return qry


def data(title, _format=DEFAULT, lead=False):
    """returns data from MW/API given titles, format"""

    r_format = _format
    if r_format == 'wikitext':
        _format = 'json'

    url = query(title, _format, lead)
    _stderr("query: " + url)

    headers = {'User-Agent': _user_agent()}
    _stderr("request headers: %s" % headers)

    result = requests.get(url, headers=headers)
    _stderr("status code: %d" % result.status_code)

    text = result.text
    _stderr("bytes: %d" % sys.getsizeof(text))

    if r_format == 'wikitext':
        text = _wikitext(text)

    return text


def _main(titles, fmt, lead):
    print(data(titles, fmt, lead).encode('utf8'))


if __name__ == "__main__":
    desc = ("Query MediaWiki API given titles, format\n"
            "https://www.mediawiki.org/wiki/API:Main_page")
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("titles", nargs='+',
                      help="one or more article titles")
    argp.add_argument("-f", "-format", choices=FORMATS, default=DEFAULT,
                      help="output format (default=%s)" % DEFAULT)
    argp.add_argument("-l", "-lead", action='store_true',
                      help="only 'lead' section (rvsection=0)")
    args = argp.parse_args()

    start = time.time()
    _main(args.titles, args.f, args.l)
    _stderr("%5.3f seconds" % (time.time() - start))

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

__author__ = "@siznax"
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


def _stderr(msg):
    print(msg, file=sys.stderr)
    sys.stderr.flush()
    sys.stdout.flush()


def _user_agent():
    # MyCoolTool/1.1 (https://example.org/MyCoolTool/; \
    # MyCoolTool@example.org) BasedOnSuperLib/1.4
    return "python-requests/" + requests.__version__


def _wikitext(_json):
    text = ""
    for page in json.loads(_json)["query"]["pages"]:
        text += "\n= %s =\n" % page["title"]
        text += page["revisions"][0]["content"]
    return text


def query(titles, _format):
    """returns MW/API query formed given titles, format"""
    if isinstance(titles, str):
        titles = [titles]
    titles = "|".join([urllib.quote(t) for t in titles])
    qry = QUERY.substitute(API=ENDPOINT, titles=titles, _format=_format)
    return qry


def data(title, _format=DEFAULT):
    """returns data from MW/API given titles, format"""

    r_format = _format
    if r_format == 'wikitext':
        _format = 'json'

    url = query(title, _format)
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


def _main(titles, fmt):
    print(data(titles, fmt).encode('utf8'))


if __name__ == "__main__":
    desc = ("Query MediaWiki API given titles, format\n"
            "https://www.mediawiki.org/wiki/API:Main_page")
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("titles", nargs='+',
                      help="one or more article titles")
    argp.add_argument("-format", choices=FORMATS, default=DEFAULT,
                      help="output format (default=%s)" % DEFAULT)
    args = argp.parse_args()

    start = time.time()
    _main(args.titles, args.format)
    _stderr("%5.3f seconds" % (time.time() - start))

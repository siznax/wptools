#!/usr/bin/env python
"""
Wikipedia article(s) from title(s) via MediaWiki API

INPUT
    titles  "fuzzy" Wiki titles
    format  see FORMATS (default=json)

OUTPUT
    articles in format selected

References
    https://www.mediawiki.org/wiki/API:Main_page
    https://www.mediawiki.org/wiki/API:Tutorial
"""

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import requests
import sys
import time
import urllib

from string import Template

DEFAULT = "json"
ENDPOINT = "http://en.wikipedia.org/w/api.php"
FORMATS = ['json', 'php', 'xml', 'jsonfm']
QUERY = Template(("${API}?titles=${titles}"
                  "&format=${_format}"
                  "&formatversion=2"
                  "&action=query"
                  "&prop=revisions"
                  "&rvprop=content"
                  "&redirects"
                  "&continue="))


def _stderr(msg):
    print(msg, file=sys.stderr)
    sys.stderr.flush()
    sys.stdout.flush()


def query(titles, _format):
    """returns Mediawiki API query given title(s), format."""
    if isinstance(titles, str):
        titles = [titles]
    titles = "|".join([urllib.quote(t) for t in titles])
    qry = QUERY.substitute(API=ENDPOINT, titles=titles, _format=_format)
    _stderr("query: " + qry)
    return qry


def dump(title, _format=DEFAULT):
    """dump Wikipedia article(s) given title(s), format."""
    url = query(title, _format)
    user_agent = "python-requests/" + requests.__version__
    headers = {'User-Agent': user_agent}
    _stderr("request headers: %s" % headers)
    result = requests.get(url, headers=headers)
    _stderr("status code: %d" % result.status_code)
    text = result.text.encode('utf8')
    _stderr("bytes: %d" % isys.getsizeof(text))
    return text


def _main(titles, fmt):
    print(dump(titles, fmt))


if __name__ == "__main__":
    desc = ("Dump Wikipedia article(s) via Mediawiki API\n"
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

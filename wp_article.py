#!/usr/bin/env python
"""
dump Wikipedia article(s) via Mediawiki API
"""

__author__ = "siznax"
__date__ = 2014

import argparse
import requests
import urllib

from string import Template

API_EN = "http://en.wikipedia.org/w/api.php"
DEFAULT = "txt"  # TODO: txt is deprecated in favor of json
FORMATS = ['json', 'php', 'wddx', 'xml', 'yaml', 'jsonfm', 'txt',
           'dbg', 'dump']
QUERY = Template("${API}?titles=${titles}&format=${_format}&action=query"
                 "&prop=revisions&rvprop=content&redirects&continue=")


def query(titles, _format):
    """returns Mediawiki API query given title(s), format."""
    if isinstance(titles, str):
        titles = [titles]
    titles = "|".join([urllib.quote(t) for t in titles])
    return QUERY.substitute(API=API_EN, titles=titles, _format=_format)


def dump(title, _format=DEFAULT):
    """dump Wikipedia article(s) given title(s), format."""
    url = query(title, _format)
    user_agent = "python-requests/" + requests.__version__
    result = requests.get(url, headers={'User-Agent': user_agent})
    return result.text.encode('utf8')


def main(args):
    print dump(args.title, args.format)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(description="")
    argp.add_argument("title", nargs='+',
                      help="one or more article titles")
    argp.add_argument("-fmt", "--format", choices=FORMATS, default=DEFAULT,
                      help="output format (default=dump)")
    args = argp.parse_args()
    main(args)

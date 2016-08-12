#!/usr/bin/env python
"""
Query MediaWiki API for article Infobox

References
    https://en.wikipedia.org/wiki/Help:Infobox
    https://meta.wikimedia.org/wiki/Wiki_syntax
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

import argparse
import json
import sys
import time

import wptools


def infobox(title, test, verbose, wiki):
    start = time.time()
    data = wptools.infobox(title, test, verbose, wiki)
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


def main():
    desc = "Query MediaWiki API for article Infobox"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title",
                      help="article title")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    wiki = wptools.fetch.WPToolsFetch.ENDPOINT
    argp.add_argument("-w", "-wiki", default=wiki, help="wiki (%s)" % wiki)

    args = argp.parse_args()

    infobox(args.title, args.t, args.v, args.w)


if __name__ == "__main__":
    main()

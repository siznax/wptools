#!/usr/bin/env python
"""
Query MediaWiki API for plain text of article

References
    https://en.wikipedia.org/wiki/Parse_tree
    https://www.mediawiki.org/wiki/API:Main_page
    https://www.mediawiki.org/wiki/User:Kephir/XML_parse_tree
"""

from __future__ import print_function

import argparse
import sys
import time

import wptools


def text(title, compact, lead, test, verbose, wiki):
    start = time.time()
    text = wptools.text(title, compact, lead, test, verbose, wiki)
    try:
        print(text)
    except:
        print(text.encode('utf-8'))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


def main():
    desc = "Query MediaWiki API for plain text of article"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title", help="article title")
    argp.add_argument("-c", "-compact", action='store_true',
                      help="collapse newlines")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="only lead section")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    wiki = wptools.fetch.WPToolsFetch.ENDPOINT
    argp.add_argument("-w", "-wiki", default=wiki, help="wiki (%s)" % wiki)

    args = argp.parse_args()

    text(args.title, args.c, args.l, args.t, args.v, args.w)


if __name__ == "__main__":
    main()

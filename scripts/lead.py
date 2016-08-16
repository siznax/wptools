#!/usr/bin/env python
"""
Extract lead section from MediaWiki HTML Query

References
     https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
"""

from __future__ import print_function

import argparse
import sys
import time

import wptools


def text(title, compact, plain, test, verbose, wiki):
    start = time.time()
    html = wptools.lead(title, plain, compact, test, verbose, wiki)
    try:
        print(html)
    except:
        print(html.encode('utf-8'))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


def main():
    desc = "Query MediaWiki API for plain text of article"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title", help="article title")
    argp.add_argument("-c", "-compact", action='store_true',
                      help="collapse newlines (text only)")
    argp.add_argument("-p", "-plain", action='store_true',
                      help="return plain TEXT")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    wiki = wptools.fetch.WPToolsFetch.ENDPOINT
    argp.add_argument("-w", "-wiki", default=wiki, help="wiki (%s)" % wiki)

    args = argp.parse_args()

    text(args.title, args.c, args.p, args.t, args.v, args.w)


if __name__ == "__main__":
    main()

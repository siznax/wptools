#!/usr/bin/env python -u
"""
Query MediaWiki API for article HTML
"""

from __future__ import print_function

import argparse
import os
import sys
import time
import wptools


def main(title, lead, test, wiki, verbose):
    start = time.time()
    data = wptools.get_html(title, lead, test, wiki, verbose)
    if test:
        print(data)
        sys.exit(os.EX_OK)
    print(wptools.html(data, lead))
    if verbose:
        print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


if __name__ == "__main__":
    desc = "Query MediaWiki API for article HTML"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title", help="article title")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="only lead section")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    argp.add_argument("-w", "-wiki",
                      default=wptools.WPToolsFetch.ENDPOINT,
                      help="wiki (%s)" % wptools.WPToolsFetch.ENDPOINT)
    args = argp.parse_args()

    main(args.title, args.l, args.t, args.w, args.v)

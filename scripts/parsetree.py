#!/usr/bin/env python
"""
Query MediaWiki API for article Parse tree

References
    https://en.wikipedia.org/wiki/Parse_tree
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

import argparse
import sys
import time
import wptools


def parsetree(title, lead, test, wiki):
    start = time.time()
    print(wptools.parsetree(title, lead, test, wiki))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


def main():
    desc = "Query MediaWiki API for article Parse tree"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title",
                      help="article title")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="lead section only")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    wiki = wptools.fetch.WPToolsFetch.ENDPOINT
    argp.add_argument("-w", "-wiki", default=wiki, help="wiki (%s)" % wiki)

    args = argp.parse_args()

    parsetree(args.title, args.l, args.t, args.w)


if __name__ == "__main__":
    main()

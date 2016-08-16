#!/usr/bin/env python
"""
Query MediaWiki API for article wikitext

References
    https://meta.wikimedia.org/wiki/Wiki_syntax
    https://www.mediawiki.org/wiki/API:Data_formats
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

import argparse
import sys
import time

import wptools


def wikitext(title, lead, test, wiki):
    start = time.time()
    text = wptools.wikitext(title, lead, test, wiki)
    output = text.encode('utf-8')
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)
    return output


def main():

    desc = "Query MediaWiki API for article wikitext"
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

    safe_exit(wikitext(args.title, args.l, args.t, args.w))


def safe_exit(output):
    """exit without breaking pipes."""
    try:
        sys.stdout.write(output)
        sys.stdout.flush()
    except IOError:
        pass


if __name__ == "__main__":
    main()

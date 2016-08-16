#!/usr/bin/env python -u
"""
Query MediaWiki API for article HTML
"""

from __future__ import print_function

import argparse
import sys
import time
import wptools


def html(title, lead, test, verbose, wiki):
    start = time.time()
    output = wptools.html(title, lead, test, verbose, wiki).encode('utf-8')
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)
    return output


def main():
    desc = "Query MediaWiki API for article HTML"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title", help="article title")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="only lead section")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    wiki = wptools.fetch.WPToolsFetch.ENDPOINT
    argp.add_argument("-w", "-wiki", default=wiki, help="wiki (%s)" % wiki)

    args = argp.parse_args()

    safe_exit(html(args.title, args.l, args.t, args.v, args.w))


def safe_exit(output):
    """exit without breaking pipes."""
    try:
        sys.stdout.write(output)
        sys.stdout.flush()
    except IOError:
        pass


if __name__ == "__main__":
    main()

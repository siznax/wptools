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
import os
import sys
import time


def main(title, lead, test, wiki):
    start = time.time()
    data = wptools.get_wikitext(title, lead, test, wiki)
    if test:
        print(data)
        sys.exit(os.EX_OK)
    print(wptools.wikitext(data))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


if __name__ == "__main__":

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import wptools

    desc = "Query MediaWiki API for article wikitext"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title",
                      help="article title")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="lead section only")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-w", "-wiki",
                      default=wptools.WPToolsFetch.ENDPOINT,
                      help="wiki (%s)" % wptools.WPToolsFetch.ENDPOINT)
    args = argp.parse_args()

    main(args.title, args.l, args.t, args.w)

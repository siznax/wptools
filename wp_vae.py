#!/usr/bin/env python
"""
Extract Vital Articles Expanded (10K) titles

INPUT

    HTML  from <https://meta.wikimedia.org/wiki/\
List_of_articles_every_Wikipedia_should_have/Expanded>
    xpath like '//div[@id="mw-content-text"]//div//li//a'

OUTPUT

    list of vital articles

See also
    https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Expanded
    https://meta.wikimedia.org/wiki/Essentialpedia
"""

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import html5lib
import mimetypes
import sys
import time

DEFAULT_XPATH = '//div[@id="mw-content-text"]//div//li//a'
VAE_URL = ("https://meta.wikimedia.org/wiki/"
           "List_of_articles_every_Wikipedia_should_have/Expanded")


def parse(html, xpath):
    count = 0
    etree = html5lib.parse(html,
                           treebuilder='lxml',
                           namespaceHTMLElements=False)
    for item in etree.xpath(xpath):
        if item.text:
            count += 1
            print(item.text.encode('utf-8'))
            sys.stdout.flush()
    return count


def main(fname, xpath=DEFAULT_XPATH):
    ftype = mimetypes.guess_type(fname)[0]
    if ftype != 'text/html':
        raise ValueError("invalid file type: %s" % ftype)
    with open(fname) as fh:
        found = parse(fh.read().decode('utf-8'), xpath)
        print("found %s titles" % found, file=sys.stderr)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Extract Vital Articles Expanded (10K) titles")
    argp.add_argument("fname", help="HTML filename")
    argp.add_argument("-xpath", default=DEFAULT_XPATH,
                      help="xpath expression (default=%s)" % DEFAULT_XPATH)
    args = argp.parse_args()

    start = time.time()
    main(args.fname, args.xpath)
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

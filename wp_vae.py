#!/usr/bin/env python
"""
Extract Wikipedia Vital Articles Expanded

INPUT

    HTML from https://simple.wikipedia.org/wiki/Wikipedia:VAE
    xpath like //div[@id=\"mw-content-text\"]//li//@href

OUTPUT

    STDOUT list of vital articles
    STDERR summary

See also
    https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Expanded
"""

# TODO: compare https://en.wikipedia.org/wiki/Wikipedia:VA/E

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import html5lib
import sys
import time

from collections import defaultdict


class WP_VAE:
    """parse and count hrefs found"""

    found = 0

    def __init__(self):
        pass

    def parse(self, html, xpath):
        """robustly parse MediaWiki HTML, group results"""
        output = defaultdict(list)
        etree = html5lib.parse(html,
                               treebuilder='lxml',
                               namespaceHTMLElements=False)
        result = etree.xpath(xpath)
        for item in result:
            self.found += 1
            fitem = _filter(item)
            print(fitem)
            output[item[0]].append(fitem)
        return output


def _filter(item):
    """normalize wiki links"""
    if 'redlink' in item:
        return '/wiki/' + item.split('&')[0].split('=')[1]
    return item


def read(fname):
    with open(fname) as fh:
        return fh.read()


def main(html, xpath):
    vae = WP_VAE()
    links = vae.parse(read(html), xpath)
    print("found (%d) links" % vae.found, file=sys.stderr)
    for item in links:
        print("    %s: %d" % (item, len(links[item])), file=sys.stderr)
    print("%5.3f seconds" % time.clock(), file=sys.stderr)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Extract Wikipedia Vital Articles Extended")
    argp.add_argument(
        "html",
        help="e.g. https://simple.wikipedia.org/wiki/Wikipedia:VAE")
    argp.add_argument(
        "xpath",
        help="e.g. //div[@id=\"mw-content-text\"]//li//@href")
    args = argp.parse_args()

    main(args.html, args.xpath)

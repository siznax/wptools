#!/usr/bin/env python
"""
Split Wikipedia XML Dump into alphabetical bz2 files

This expects to operate on the (currently ~12GB)...
latest/enwiki-latest-pages-articles.xml.bz2

The goal here is to speed extracting an article from the so-called
"XML Dump" by splitting it up alphabetically.

It may be feasible to simply index the Dump, e.g.

    A <byte position>
    B <byte position>
    C <byte position>

But it looks like the Dump is not strictly sorted:

    500 <title>Augustus</title>
    501 <title>Geography of Antarctica</title>
    502 <title>Economy of Antarctica</title>
    503 <title>Government of Antarctica</title>
    504 <title>Transport in Antarctica</title>
    505 <title>Military of Antarctica</title>
    506 <title>Geography of Alabama</title>
    507 <title>List of Governors of Alabama</title>
    508 <title>Apocrypha</title>

To be resolved:

 * Is it sorted well enough to extract Vital Articles?
 * Is it feasible to use a streaming parser on this huge file,
   like cElementTree?

References
    https://en.wikipedia.org/wiki/Wikipedia:Database_download
    https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Expanded
    http://effbot.org/zone/celementtree.htm
"""

from __future__ import print_function

__author__ = "siznax"
__version__ = "29 Sep 2015"

import argparse
import bz2
import sys
import time

CHUNK_SIZE = 1024
MAX_MEGABYTES = 10

from wp_parser import WPParser


class SplitParser(WPParser):

    def __init__(self):
        WPParser.__init__(self)

    def process(self, elem):
        title = elem.split("\n")[1]
        if "<title>" not in title:
            print(elem[:64])
            raise ValueError("process elem failed!")
        print("%s %d" % (title, len(elem)))
        sys.stdout.flush()


def _main(fname, max_mb, chunk_size):
    max_bytes = 1024**2 * max_mb
    sp = SplitParser()
    tell = 0
    with bz2.BZ2File(fname, 'r') as zh:
        while zh.tell() < max_bytes:
            try:
                sp.parse(zh.read(chunk_size))
            except:
                print("Exception at byte position: %d" % zh.tell())
                raise
        tell = zh.tell()
    print("%d bytes read" % tell)
    print("%d elems found" % sp.elems_found)
    print("%d elems processed" % sp.elems_processed)


if __name__ == "__main__":
    desc = "Split Wikipedia XML Dump into alphabetical bz2 files"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("fname", help="Wikipedia XML Dump bz2 filename")
    argp.add_argument("-m", "-megabytes", type=int, default=MAX_MEGABYTES,
                      help="max MB to parse (default=%d)" % MAX_MEGABYTES)
    argp.add_argument("-c", "-chunksize", type=int, default=CHUNK_SIZE,
                      help="chunk size to read (default=%d)" % CHUNK_SIZE)
    args = argp.parse_args()

    start = time.time()
    _main(args.fname, args.m, args.c)
    print("%5.3f seconds" % (time.time() - start))

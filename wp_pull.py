#!/usr/bin/env python
"""
Pull article from Wikipedia XML Dump (bz2) or part (gz)

INPUT
    title   article title
    dump    XML Dump bzip2 file
    -index  index bzip2 file (optional)

OUTPUT
    article wikitext

See also
    wp_parser
    wp_index
"""

from __future__ import print_function

__author__ = "siznax"
__version__ = "30 Sep 2015"

import argparse
import bz2
import gzip
import os
import sys
import time

from wp_parser import WPLineParser
from wp_index import page_title

CHUNK_SIZE = 1024
MAX_READ = 1024**2 * 10  # 10 MiB


class PullParser(WPLineParser):

    def __init__(self, title):
        WPLineParser.__init__(self)
        self.title = title
        self.found_article = False

    def process(self, elem):
        title = page_title(elem)
        if title == self.title:
            print(elem)
            self.found_article = True


def dump_pos(title, index):
    """returns XML Dump (bzip2) offset from (gzip) index file"""
    if not os.path.exists(index):
        print("index file not found: %s" % index)
        sys.exit(os.EX_USAGE)
    with gzip.open(index, 'rb') as zh:
        for line in zh:
            spl = line.split()
            if " ".join(spl[:-1]) == title:
                return int(spl[-1])


def _bz2_offset(title, index, offset):
    """compute seek offset into bzip2 file"""
    pos = None
    if index and offset:
        print("-index doesn't make sense with -offset")
        sys.exit(os.EX_USAGE)
    if index:
        pos = dump_pos(title, index)
        if not pos:
            raise StandardError("could not find dump pos in index!")
        # Shetlands 70.647 seconds
        # pos = pos - pos % 900  # Shetlands 68.058 seconds
        pos = pos - pos % 1000  # Shetlands 57.789 seconds
    if offset:
        pos = offset - offset % 1000
    return pos


def _read_bz2(title, dump, index, offset):
    bread = 0
    pos = _bz2_offset(title, index, offset)
    pp = PullParser(title)
    with bz2.BZ2File(dump, 'rb') as zh:
        if pos:
            print("seek %d" % pos, file=sys.stderr)
            zh.seek(pos)
        while not pp.found_article:
            data = zh.readlines(CHUNK_SIZE)
            bread += CHUNK_SIZE
            if not data:
                print("reached EOF %d" % zh.tell())
                sys.exit(os.EOF)
            pp.parse(data)
            if bread >= MAX_READ:
                print("reached MAX_READ %d" % bread)
                sys.exit(os.EX_UNAVAILABLE)


def _read_gz(title, dump):
    lp = PullParser(title)
    with gzip.open(dump, 'rb') as gz:
        for line in gz:
            lp.parse(line)
            if lp.found_article:
                return


def _main(title, dump, index, offset):
    if not os.path.exists(dump):
        print("dump file not found: %s" % dump)
        sys.exit(os.EX_USAGE)
    if dump.endswith('.bz2'):
        _read_bz2(title, dump, index, offset)
    else:
        if index or offset:
            print("-index or -offset makes no sense with gzip")
            sys.exit(os.EX_USAGE)
        _read_gz(title, dump)


if __name__ == "__main__":
    desc = "Pull article from Wikipedia XML Dump (bz2) or part (gz)"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title", help="article title")
    argp.add_argument("dump", help="XML Dump (bz2) or part (gz)")
    argp.add_argument("-i", "-index", help="use index (bzip2) file")
    argp.add_argument("-o", "-offset", type=int,
                      help="byte offset into dump")
    args = argp.parse_args()

    start = time.time()
    _main(args.title, args.dump, args.i, args.o)
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

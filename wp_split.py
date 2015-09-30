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
import os
import re
import sys
import string
import time
import traceback

DEFAULT_CHUNK_KB = 1
ONE_KB = 1000
ONE_MB = 1000**2
MAX_MEGABYTES = 10

from wp_parser import WPParser


class SplitParser(WPParser):

    def __init__(self, dest, offset):
        WPParser.__init__(self)
        self._files = dict()
        self.bytes_read = 0
        self.dest = dest
        self.first_title = ""
        self.first_title_start = 0
        self.offset = offset
        self.tell = 0
        self.title = ""
        self.title_start = 0

    def open_files(self):
        if not self.dest:
            return
        os.mkdir(self.dest)
        for char in string.digits + string.ascii_uppercase:
            path = "%s/%s" % (self.dest, char)
            print("+ open %s" % path)
            self._files[char] = open(path, 'a')

    def close_files(self):
        if not self.dest:
            return
        for path, handle in self._files.iteritems():
            tell = handle.tell()
            handle.close()
            if tell:
                print("- close %s %d" % (path, tell))

    def process(self, elem):
        m = re.search(r"<title>([^<]*)<", elem)
        if not m:
            print(elem[:64])
            raise ValueError("title not found!")
        title = m.group(1)
        title_start = self.offset + self.byte_count - len(elem)
        if not self.title:
            self.first_title = title
            self.first_title_start = title_start
        self.title = title
        self.title_start = title_start
        if not self.dest:
            # print("%s %s" % (title, len(elem)))
            return
        first_char = ascii_bin(title)
        if first_char in self._files:
            _file = self._files[first_char]
            _file.write(bz2.compress(elem))
        else:
            print("ORPHAN %s" % title)


def ascii_bin(title):
    """returns first 0-9 or A-Z character in upper(title)"""
    try:
        return [x for x in title.upper()
                if 47 < ord(x) < 58 or 64 < ord(x) < 91][0]
    except:
        return title


def setup(dest, offset):
    if os.path.exists(dest):
        print("Destination exists: %s" % dest, file=sys.stderr)
        sys.exit(os.EX_IOERR)
    sp = SplitParser(dest, offset)
    sp.open_files()
    return sp


def gobble(sp, fname, chunk_size, max_mb, offset):
    chunk_size = ONE_KB * chunk_size
    max_bytes = ONE_MB * max_mb
    with bz2.BZ2File(fname, 'r') as zh:
        zh.seek(offset)
        try:
            while sp.bytes_read < max_bytes:
                sp.parse(zh.read(chunk_size))
                sp.tell = zh.tell()
                sp.bytes_read = sp.tell - offset
                if sp.tell % ONE_MB*10 == 0:
                    print("  %s %d" % (sp.title, sp.title_start))
        except KeyboardInterrupt:
            teardown(sp)
            sys.exit(os.EX_SOFTWARE)
        except Exception as detail:
            print("Exception at byte position: %d" % zh.tell())
            traceback.print_exc()


def teardown(sp):
    sp.close_files()
    print("pages found: %d" % sp.elems_found)
    print("titles processed: %d" % sp.elems_processed)
    print("first: %s %d" % (sp.first_title, sp.first_title_start))
    print("last: %s %d" % (sp.title, sp.title_start))
    print("read: %d MB" % (sp.bytes_read / ONE_MB))
    print("tell: %s" % sp.tell)


def _main(fname, max_mb, chunk_size, dest, offset):
    sp = setup(dest, offset)
    gobble(sp, fname, chunk_size, max_mb, offset)
    teardown(sp)


if __name__ == "__main__":
    desc = "Split Wikipedia XML Dump into alphabetical bz2 files"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("fname", help="Wikipedia XML Dump bz2 filename")
    argp.add_argument("-c", "-chunksize", type=int, default=DEFAULT_CHUNK_KB,
                      help="chunk size in KB (default=%d)" % DEFAULT_CHUNK_KB)
    argp.add_argument("-d", "-dest", default="",
                      help="write results to dest (dir)")
    argp.add_argument("-m", "-maxbytes", type=int, default=MAX_MEGABYTES,
                      help="max bytes in MB (default=%d)" % MAX_MEGABYTES)
    argp.add_argument("-o", "-offset", type=int, default=0,
                      help="seek to byte offset")
    args = argp.parse_args()

    start = time.time()
    _main(args.fname, args.m, args.c, args.d, args.o)
    print("%5.3f seconds" % (time.time() - start))

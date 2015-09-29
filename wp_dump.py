#!/usr/bin/env python
"""
Get article from Wikipedia XML Dump in streaming fashion

This expects to operate on the (currently ~12GB)
latest/enwiki-latest-pages-articles.xml.bz2 or a section of it.

INPUT
    fname  XML Dump filename (bz2)
    title  (optional) article title to fetch

OUTPUT
    Article XML and/or titles scanned

References
    https://en.wikipedia.org/wiki/Wikipedia:Database_download
"""

from __future__ import print_function

import argparse
import bz2
import re
import mimetypes
import sys
import time

__author__ = "siznax"
__version__ = "24 Sep 2015"


def _emit_titles(data):
    titles = re.findall(r'<title>.*</title>', data)
    for item in titles:
        print(item)
        sys.stdout.flush()


def _main(fname, title, verbose, scan):
    ftype = mimetypes.guess_type(fname)[1]
    if ftype != 'bzip2':
        raise ValueError("invalid file type: %s" % ftype)
    if not title:
        scan = True
    if scan:
        title = None
        verbose = True
    with bz2.BZ2File(fname) as zdata:
        total = 0
        found = False
        article = []
        while True:
            data = zdata.read(1024)
            total += zdata.tell()
            tag = "<title>%s</title>" % title
            if found:
                if '</page>' in data:
                    chunk = data.split("</page>")[0] + "</page>"
                    article.append(chunk)
                    break
                else:
                    article.append(data)
            if tag in data:
                found = True
                if '<page>' in data:
                    chunk = '<page>' + data.split("<page>")[1]
                    article.append(chunk)
                else:
                    article.append(data)
            if verbose:
                _emit_titles(data)
        print("\n".join(article))
        print("%d bytes read" % total, file=sys.stderr)


if __name__ == "__main__":
    desc = "Dump article from Wikipedia XML dump by title"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("fname", help="Wikipedia XML Dump filename")
    argp.add_argument("-s", "-scan", action='store_true',
                      help="scan for titles only")
    argp.add_argument("-title", help="Wikipedia article title")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="emit titles while scanning")
    args = argp.parse_args()

    start = time.time()
    _main(args.fname, args.title, args.v, args.s)
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

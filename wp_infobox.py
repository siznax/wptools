#!/usr/bin/env python
"""
Dump Wikipedia article(s) Infobox wiki-text

INPUT
    title  Wiki article title(s)
           optionally, local filename

OUTPUT
    infobox wiki-text

References
    https://en.wikipedia.org/wiki/Help:Infobox
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import os
import re
import sys
import time
import wp_article


def infobox(wp_txt):
    """
    Parse Infobox text from Mediawiki API json output
    """
    output = []
    region = False
    braces = 0
    lines = wp_txt.split("\\n")
    if len(lines) < 3:
        raise RuntimeError("too few lines!")
    for line in lines:
        match = re.search(r'({{[^ ]*box)', line, flags=re.IGNORECASE)
        braces += len(re.findall(r'{{', line))
        braces -= len(re.findall(r'}}', line))
        if match:
            region = True
            boxtype = match.group(1)
            line = re.sub(r'^.*{{[^ ]*box', boxtype, line)
        if region:
            output.append(line.lstrip())
            if braces <= 0:
                region = False
    return "\n".join(output)


def main(args):
    if os.path.exists(args.title[0]):
        with open(args.title[0]) as fh:
            print(infobox(fh.read()))
    else:
        print(infobox(wp_article.dump("|".join(args.title))))


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Wikipedia article Infobox wiki-text from title(s)")
    argp.add_argument("title", nargs='+',
                      help="Wiki article title(s) optionally, local filename")
    args = argp.parse_args()
    start = time.time()
    main(args)
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


# test cases TBD
#
# Aerocar
# GitHub
# Heroku
# Stack Overflow

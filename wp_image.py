#!/usr/bin/env python
"""
Get article image file from title or file
"""

from __future__ import print_function

import os
import argparse
import json
import mimetypes
import re
import wp_file
import wp_query

__author__ = "siznax"
__version__ = "25 Sep 2015"

DEFAULT_NS = "commons"


def _extract(images, expand, ns):
    output = []
    for item in images:
        match = re.search(r"\[\[(.*)\]\]", item)
        if match:
            item = match.group(1)
        match = re.search(r"([^\|]*)|", item)
        if match:
            item = match.group(1)
        if expand:
            item = wp_file.url(item.encode('utf-8'), ns)
        output.append(item)
    return output


def _walk(data):
    images = []
    for page in data["query"]["pages"]:
        for rev in page['revisions']:
            for line in rev['content'].split("\n"):
                if re.search(r'image\d{0,} {0,}=', line):
                    image = line.split("=")[1].strip()
                    images.append(image)
    return images


def _main(titles, expand, ns):
    if os.path.exists(titles[0]):
        fname = titles[0]
        ftype = mimetypes.guess_type(fname)[0]
        if ftype != 'application/json':
            raise ValueError("invalid file type: %s" % ftype)
        with open(fname) as fh:
            data = json.loads(fh.read())
    else:
        data = json.loads(wp_query.data(titles))
    images = _walk(data)
    images = _extract(images, expand, ns)
    for img in images:
        print(img)


if __name__ == "__main__":
    desc = "Get image file from article if extant"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("titles", nargs='+',
                      help="article titles or filename")
    argp.add_argument("-e", "-expand", action='store_true',
                      help="expand image names to URLs")
    argp.add_argument(
        "-n", "-namespace", choices={'commons', 'en'}, default=DEFAULT_NS,
        help="URL namespace (default=%s)" % DEFAULT_NS)
    args = argp.parse_args()
    _main(args.titles, args.e, args.n)

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
import wp_query


__author__ = "siznax"
__version__ = "25 Sep 2015"


def _extract(images):
    output = []
    for item in images:
        match = re.search(r"\[\[(.*)\]\]", item)
        if match:
            item = match.group(1)
        match = re.search(r"([^\|]*)|", item)
        if match:
            item = match.group(1)
        output.append(item)
    return output


def _walk(data):
    images = []
    for page in data["query"]["pages"]:
        for rev in page['revisions']:
            for line in rev['content'].split("\n"):
                if re.search(r'image {0,}=', line):
                    image = line.split("=")[1].strip()
                    images.append(image)
    return images


def _main(titles):
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
    images = _extract(images)
    for img in images:
        print(img)


if __name__ == "__main__":
    desc = "Get image file from article if extant"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("titles", nargs='+',
                      help="article titles or filename")
    args = argp.parse_args()
    _main(args.titles)

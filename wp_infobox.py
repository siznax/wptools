#!/usr/bin/env python
"""
Infobox wiki-text from titles (via API) or file

INPUT
    Wikipedia article title(s) (or filename)

OUTPUT
    Infobox(es) as wiki-text, dict, or json

References
    https://en.wikipedia.org/wiki/Help:Infobox
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import json
import os
import re
import sys
import time
import wp_query

from collections import defaultdict

DEFAULT = 'dict'
FORMATS = ['dict', 'json', 'text']


def from_api(titles, _format=DEFAULT):
    """returns Infoboxen from api"""
    return _output(_parse(_articles(titles)), _format)


def from_file(fname, _format=DEFAULT):
    """returns Infoboxen from input file"""
    with open(fname) as fh:
        return _output(_parse(json.loads(fh.read())), _format)


def _output(boxes, _format):
    """returns Infoboxen as text, dict, or json"""
    if _format == 'dict':
        return _boxes_to_dict(boxes)
    if _format == 'json':
        return json.dumps(boxes)
    if _format == 'text':
        return _boxes_to_text(boxes)


def _boxes_to_dict(boxes):
    """return list of dicts from list of infoboxes"""
    for i, box in enumerate(boxes):
        _dict = defaultdict(str)
        for line in box['wikitext'].split("\n"):
            _dict['title'] = box['title']
            _dict['wikitext'] = box['wikitext']
            if '=' in line:
                terms = line.split('=')
                key = terms[0].replace(' ', '').replace('|', '')
                _dict[key] = terms[1].strip()
        boxes[i] = dict(_dict)
    return boxes


def _boxes_to_text(boxes):
    """return wikitext from list of infoboxes"""
    text = ""
    for box in boxes:
        text += "\n= %s =\n" % box['title']
        text += box['wikitext'] + "\n"
    return text


def _parse(api_json):
    """returns [{title, box}, ...] from API JSON"""
    boxes = []
    # print("pages: %d" % len(api_json["query"]['pages']), file=sys.stderr)
    try:
        for page in api_json["query"]["pages"]:
            wikitext = page["revisions"][0]["content"]
            infobox = _infobox(wikitext)
            if infobox:
                boxes.append({'title': page["title"],
                              'wikitext': infobox})
    except:
        print(page)
        raise RuntimeError("Unable to parse result! Check your API query.")
    return boxes


def _infobox(text):
    """returns Infobox wiki-text from text blob"""
    #
    # TODO: consider returning LIST of infoboxen from each article
    # instead of the break below. (see Abba article, which also has a
    # {{Navbox)
    #
    output = []
    region = False
    braces = 0
    lines = text.split("\n")
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
                break
    return "\n".join(output)


def _articles(titles):
    """returns JSON object from list of titles"""
    if isinstance(titles, str):
        titles = [titles]
    return json.loads(wp_query.data("|".join(titles)))


def _main(titles, _format):
    """emits Infoboxen from api or local file"""
    if os.path.exists(titles[0]):
        return from_file(titles[0], _format)
    else:
        return from_api(titles, _format)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Wikipedia article Infobox(es) wiki-text from titles")
    argp.add_argument("titles", nargs='+',
                      help="article titles (optionally, local filename)")
    argp.add_argument("-format", choices={'text', 'json'}, default='text',
                      help="output format (default=text)")
    args = argp.parse_args()

    start = time.time()
    print(_main(args.titles, args.format).encode('utf-8'))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


# test cases TBD
#
# Aardvark
# Abba
# Accordion
# Aerocar
# GitHub
# Heroku
# Stack Overflow

#!/usr/bin/env python
"""
GET Wikipedia article content from URL or filename

INPUT
    Wikipedia URL or filename
    input file expected to be Wikipedia HTML

OUTPUT
    full article (sans boilerplate) or summary (lead_section) only
    as HTML or Markdown text

References
    https://pypi.python.org/pypi/html2text
    https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section

This is basically an alternative path to article content outside of
the MediaWiki API, which is often quite slow. The problem is that you
don't get ``wikitext``, but you can get raw HTML or Markdown
text. It's not entirely deprecated, but ``wp_query`` and
``wp_summary`` are recommended for bulk processing.
"""

from __future__ import print_function

import argparse
import html5lib
import html2text
import lxml
import os
import requests

__author__ = "siznax"
__version__ = "24 Sep 2015"

XPATH = '//*[@id="mw-content-text"]'


def _user_agent():
    return ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/45.0.2454.85 Safari/537.36")


def _tostring(elem, strip_tags=False):
    if strip_tags:
        return lxml.etree.tostring(elem, method="text", encoding="utf-8")
    return lxml.etree.tostring(elem)


def _process(html, xpath, lead=False, strip_tags=False):
    content = []
    etree = html5lib.parse(html,
                           treebuilder='lxml',
                           namespaceHTMLElements=False)
    root = etree.xpath(xpath)
    for item in root[0]:
        if lead:
            if item.tag.startswith("h"):
                break
            if item.tag == "p":
                content.append(_tostring(item, strip_tags))
        else:
            content.append(_tostring(item, strip_tags))
    return "\n".join(content)


def _main(url, lead, markdown, strip):
    output = ""
    if os.path.exists(url):
        with open(url) as fh:
            output = _process(fh, XPATH, lead, strip)
    else:
        if not args.url.startswith('http'):
            base = "https://en.wikipedia.org/wiki"
            url = "%s/%s" % (base, url.replace(" ", "_"))
        print("GET %s" % url, end=None)
        r = requests.get(url, headers={'user-agent': _user_agent()})
        print(r.status_code)
        output = _process(r.content, XPATH, lead, strip)
    if markdown:
        print(html2text.html2text(output).encode('utf-8'))
    else:
        print(output)


if __name__ == "__main__":
    desc = "GET Wikipedia article from URL or filename via HTTP"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("url", help="Wikipedia article URL or filename")
    argp.add_argument("-l", "-lead", action='store_true',
                      help="lead paragraphs (summary) only")
    argp.add_argument("-m", "-markdown", action='store_true',
                      help="convert content to markdown text")
    argp.add_argument("-s", "-strip", action='store_true',
                      help="strip tags")
    args = argp.parse_args()
    _main(args.url, args.l, args.m, args.s)

#!/usr/bin/env python -u
# -*- coding:utf-8 -*-
"""
Command line interface to wptools.
"""

from __future__ import print_function

import argparse
import re
import sys
import time
import textwrap
import wptools

from wptools.query import WPToolsQuery


def _html_image(page):
    """
    returns HTML img tag
    """
    source = _image(page)
    if not source:
        return
    alt = page.data.get('label') or page.data.get('title')
    img = "<img src=\"%s\"" % source
    img += " alt=\"%s\" title=\"%s\" " % (alt, alt)
    img += "align=\"right\" width=\"240\">"
    return img


def _html_title(page):
    """
    returns Wiki-linked HTML title
    """
    link = "<a href=\"%s\">%s</a>" % (page.data.get('url'),
                                      page.data.get('title'))
    desc = page.data.get('description')
    if desc:
        link += "&mdash;<i>%s</i>" % desc
    else:
        link += "&mdash;<i>description</i>"
    if link:
        return "<p>%s</p>" % link


def _image(page):
    """
    returns (preferred) image from wptools object
    """
    pageimage = page.images(token='pageimage')
    if pageimage:
        return pageimage[0]['url']


def _page_html(page):
    """
    returns assembled HTML output
    """
    out = []
    out.append(_html_title(page))
    out.append(_html_image(page))
    out.append(page.data.get('extract'))
    return "\n".join([x for x in out if x])


def _page_text(page, nowrap=False):
    """
    returns assembled text output
    """
    title = page.data['title']
    title = "%s\n%s" % (title, "=" * len(title))

    desc = page.data.get('description')
    if desc:
        desc = "_%s_" % desc

    img = _text_image(page)

    pars = page.data.get('extext')

    if pars:
        # pars = pars.replace(' * ', '\n * ')
        pars = re.sub(r'[ ]+\*[ ]+', '* ', pars)

    if pars and not nowrap:
        parlist = []
        for par in pars.split("\n\n"):
            parlist.append("\n".join(textwrap.wrap(par)))

        disambiguation = page.data.get('disambiguation')
        if disambiguation:
            parlist.append(' * ' + "\n * ".join(page.data.get('links')))

        pars = "\n\n".join(parlist)

    url = '<%s>' % page.data['url']

    txt = []
    txt.append(title)
    txt.append(desc)
    txt.append(url)
    txt.append(pars)
    txt.append(img)

    return "\n\n".join([x for x in txt if x])


def _safe_exit(start, output):
    """
    exit without breaking pipes
    """
    try:
        sys.stdout.write(output)
        sys.stdout.flush()
    except TypeError:  # python3
        sys.stdout.write(str(output, 'utf-8'))
        sys.stdout.flush()
    except IOError:
        pass

    seconds = time.time() - start
    print("\n\n%5.3f seconds" % (seconds), file=sys.stderr)


def _text_image(page):
    """
    returns text image URL
    """
    img = None
    alt = page.data.get('label') or page.data.get('title')
    source = _image(page)
    if source:
        img = "![%s](%s)" % (alt, source)
    return img


def get(args):
    """
    invoke wptools and assemble selected output
    """

    html = args.H
    lang = args.l
    nowrap = args.n
    query = args.q
    silent = args.s
    title = args.t
    verbose = args.v
    wiki = args.w

    if query:
        qobj = WPToolsQuery(lang=lang, wiki=wiki)
        if title:
            return qobj.query(title)
        return qobj.random()

    page = wptools.page(title, lang=lang, silent=silent,
                        verbose=verbose, wiki=wiki)

    try:
        page.get_query()
    except (StandardError, ValueError, LookupError):
        return "NOT_FOUND"

    if not page.data.get('extext'):
        out = page.cache['query']['query']

    out = _page_text(page, nowrap)
    if html:
        out = _page_html(page)

    try:
        return out.encode('utf-8')
    except KeyError:
        return out


def parse_args():
    """
    parse main() args
    """
    description = (
        "Get Wikipedia article info and Wikidata via MediaWiki APIs.\n\n"
        "Gets a random English Wikipedia article by default, or in the\n"
        "language -lang, or from the wikisite -wiki, or by specific\n"
        "title -title. The output is a plain text extract unless -HTML.")
    epilog = ("Powered by https://github.com/siznax/wptools/ %s"
              % wptools.__version__)
    argp = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog)
    argp.add_argument("-H", "-HTML", action='store_true',
                      help="output HTML extract")
    argp.add_argument("-l", "-lang", default='en',
                      help="language code")
    argp.add_argument("-n", "-nowrap", action='store_true',
                      help="do not wrap text")
    argp.add_argument("-q", "-query", action='store_true',
                      help="show query and exit")
    argp.add_argument("-s", "-silent", action='store_true',
                      help="quiet output to stderr")
    argp.add_argument("-t", "-title", help="get a specific title")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stderr")
    argp.add_argument("-w", "-wiki",
                      help="use alternative wikisite")
    return argp.parse_args()


def main(args=None):
    """
    invoke wptools and exit safely
    """
    if not args:
        args = parse_args()
    start = time.time()
    output = get(args)
    _safe_exit(start, output)


if __name__ == "__main__":
    main(parse_args())

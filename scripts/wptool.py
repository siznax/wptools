#!/usr/bin/env python -u
# -*- coding:utf-8 -*-
"""
Command line interface to wptools.
"""

from __future__ import print_function

import argparse
import sys
import time
import textwrap
import wptools

from wptools.fetch import WPToolsFetch


def _html_image(item):
    """
    returns HTML img tag
    """
    source = _image(item)
    if not source:
        return
    alt = item.title
    if item.label:
        alt = item.label
    img = "<img src=\"%s\"" % source
    img += " alt=\"%s\" title=\"%s\" " % (alt, alt)
    img += "align=\"right\" width=\"240\">"
    return img


def _html_title(item):
    """
    returns Wiki-linked HTML title
    """
    link = "<a href=\"%s\">%s</a>" % (item.url, item.title)
    if item.description:
        link += "&mdash;<i>%s</i>" % item.description
    else:
        link += "&mdash;<i>description</i>"
    if link:
        return "<p>%s</p>" % link


def _image(item):
    """
    returns (preferred) image from wptools object
    """
    try:
        return item.image('image')['url']
    except TypeError:
        return None


def _item_html(item):
    """
    returns assembled HTML output
    """
    out = []
    out.append(_html_title(item))
    out.append(_html_image(item))
    out.append(item.extract)
    return "\n".join([x for x in out if x])


def _item_text(item, nowrap=False):
    """
    returns assembled text output
    """
    title = item.title.upper()
    if hasattr(item, 'description') and item.description:
        title += u'\u2014' + "%s" % item.description
    title = "\n".join(textwrap.wrap(title))

    img = _text_image(item)

    if nowrap:
        pars = item.extext
    else:
        parlist = []
        for par in item.extext.split("\n\n"):
            parlist.append("\n".join(textwrap.wrap(par)))
        pars = "\n\n".join(parlist)

    txt = []
    txt.append(title)
    txt.append(img)
    txt.append(pars)

    head = "\n\n".join([x for x in txt if x])

    tail = "\n\n<%s>\n" % item.url
    if item.wikibase:
        tail += "<https://wikidata.org/wiki/%s>\n" % item.wikibase

    return head + tail


def _safe_exit(output):
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


def _text_image(item):
    """
    returns text image URL
    """
    img = None
    alt = item.title
    if item.label:
        alt = item.label
    source = _image(item)
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

    start = time.time()

    if query:
        fetch = WPToolsFetch(lang=lang, verbose=verbose, wiki=wiki)
        if title:
            return fetch.query('query', title)
        return fetch.query('random', None)

    item = wptools.page(title, lang=lang, silent=silent,
                        verbose=verbose, wiki=wiki)
    item.get_query()

    if not hasattr(item, 'extract') or not item.extract:
        return "NOT_FOUND"

    out = _item_text(item, nowrap)
    if html:
        out = _item_html(item)

    if not silent:
        print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

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
    argp.add_argument("-s", "-shh", action='store_true',
                      help="quiet output to stderr")
    argp.add_argument("-t", "-title", help="get a specific title")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stderr")
    argp.add_argument("-w", "-wiki",
                      help="use alternative wikisite")
    return argp.parse_args()


def main(args):
    """
    invoke wptools and exit safely
    """
    _safe_exit(get(args))


if __name__ == "__main__":
    main(parse_args())

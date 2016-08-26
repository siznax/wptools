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


def _html_image(item):
    source = _image(item)
    if not source:
        return
    alt = item.title
    if item.Label:
        alt = item.Label
    img = "<img src=\"%s\"" % source
    img += " alt=\"%s\" title=\"%s\" " % (alt, alt)
    img += "align=\"right\" width=\"240\">"
    return img


def _html_title(item):
    link = "<a href=\"%s\">%s</a>" % (item.url, item.title)
    if item.Description:
        link += "&mdash;<i>%s</i>" % item.Description
    else:
        link += "&mdash;<i>description</i>"
    if link:
        return "<p>%s</p>" % link
    return None


def _image(item):
    """
    returns (preferred) image from wptools object
    """
    if hasattr(item, 'Image') and item.Image:
        return item.Image
    elif hasattr(item, 'pageimage') and item.pageimage:
        return item.pageimage
    elif hasattr(item, 'thumbnail') and item.thumbnail:
        return item.thumbnail
    else:
        return None


def _item_html(item):
    out = []
    out.append(_html_title(item))
    out.append(_html_image(item))
    out.append(item.extract)
    return "\n".join([x for x in out if x])


def _item_text(item, nowrap=False):
    title = item.title.upper()
    if hasattr(item, 'Description') and item.Description:
        title += u'\u2014' + "_%s_" % item.Description
    title = "\n".join(textwrap.wrap(title))

    img = _text_image(item)

    if nowrap:
        pars = item.extext
    else:
        pars = []
        for par in item.extext.split("\n\n"):
            pars.append("\n".join(textwrap.wrap(par)))
        pars = "\n\n".join(pars)

    txt = []
    txt.append(title)
    txt.append(img)
    txt.append(pars)
    txt = "\n\n".join([x for x in txt if x])

    tail = item.url
    if item.wikibase:
        tail += "\n" + item.wikibase

    return txt + tail


def _safe_exit(output):
    """exit without breaking pipes."""
    try:
        sys.stdout.write(output)
        sys.stdout.flush()
    except IOError:
        pass


def _text_image(item):
    img = None
    alt = item.title
    if item.Label:
        alt = item.Label
    source = _image(item)
    if source:
        img = "![%s](%s)" % (alt, source)
    return img


def get(html, lang, nowrap, query, silent, title, verbose, wiki):
    """wptools.get() and emit selected output"""
    start = time.time()

    if query:
        f = wptools.fetch.WPToolsFetch(lang=lang, verbose=verbose,
                                       wiki=wiki)
        if title:
            return f.query('query', title)
        return f.query('random', None)

    item = wptools.page(title=title, lang=lang, silent=silent,
                        verbose=verbose, wiki=wiki)
    item.get()

    if not hasattr(item, 'extract') or not item.extract:
        return "NOT_FOUND"

    out = _item_text(item, nowrap)
    if html:
        out = _item_html(item)

    if not silent:
        print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

    try:
        return out.encode('utf-8')
    except:
        return out


def main():
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

    args = argp.parse_args()

    _safe_exit(get(args.H, args.l, args.n, args.q, args.s, args.t,
                   args.v, args.w))


if __name__ == "__main__":
    main()

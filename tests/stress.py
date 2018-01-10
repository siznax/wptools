#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Stress-test Wptools
~~~~~~~~~~~~~~~~~~~

Endlessly GET page info from ALL Wikimedia APIs in MANY languages
"""

from __future__ import print_function

import argparse
import random
import sys
import time

import wptools

DEFAULT_DELAY = 3
DEFAULT_LANGUAGE = 'en'

# connection refused 'ge'
# wikidata fail 'zh-min-nan'
LANGUAGES = [
    'en', 'ceb', 'sv', 'de', 'nl', 'fr', 'ru', 'it', 'es', 'war',
    'pl', 'vi', 'ja', 'pt', 'zh', 'uk', 'fa', 'ca', 'ar', 'no', 'sh',
    'fi', 'hu', 'id', 'ko', 'cs', 'ro', 'sr', 'ms', 'tr', 'eu', 'eo',
    'bg', 'da', 'hy', 'min', 'kk', 'sk', 'he', 'lt', 'hr', 'ce', 'et',
    'sl', 'be', 'el', 'nn', 'uz', 'simple', 'la', 'az', 'ur', 'hi',
    'vo', 'th', 'ka', 'ta', 'cy', 'mk', 'mg', 'oc', 'tl', 'lv', 'ky',
    'bs', 'tt', 'new', 'tg', 'sq', 'te', 'pms', 'br', 'bn', 'ml',
    'ht', 'jv', 'ast', 'lb', 'mr', 'af', 'sco', 'pnb', 'ga', 'is',
    'cv', 'ba', 'azb', 'fy', 'su', 'sw', 'my', 'lmo', 'an', 'yo',
    'ne', 'gu', 'io', 'pa', 'nds', 'scn', 'bpy', 'als', 'bar', 'ku',
    'kn', 'ia', 'qu', 'ckb', 'mn', 'arz']


def languages():
    """
    Many sites not fully supporting APIs. See LANGUAGES.
    """
    return LANGUAGES

    # site = wptools.site()
    # site.get_sites()
    # sites = site.data['sites']
    # wps = [x for x in sites if 'wikipedia' in x]
    # return [x.split('/')[-1].split('.')[0] for x in wps]


def popular(lang):
    """
    returns list of most popular pages
    """
    site = wptools.site(silent=True)
    if lang:
        site.get_info("%s.wikipedia.org" % lang)
    else:
        site.get_info()
    return [x['title'] for x in site.data['mostviewed']]


def print_header(delay, lang, pages):
    """
    print header for stress test
    """
    langstr = lang
    if langstr is None:
        langstr = len(languages())

    pagestr = len(pages)
    if pagestr == 1:
        pagestr = "+"

    msg = []
    msg.append("WPTOOLS STRESS TEST")
    msg.append(time.asctime(time.gmtime()))
    msg.append("delay: %d lang: %s pages: %s" % (delay, langstr, pagestr))
    msgstr = " ".join(msg)

    header = [msgstr]
    header.append("=" * len(msgstr))
    header.append("Python " + sys.version)
    header.append('-' * len(msgstr))

    if len(pages) > 1:
        print("Getting top %s.wikipedia.org pages" % lang)
        for i, title in enumerate(pages[:10]):
            print(" %d. %s" % (i + 1, title))

    print("\n".join(header))


def main(args):
    """
    GET top pages or random pages forever
    """
    delay = args.delay
    lang = args.lang
    top = args.top

    start = int(time.time())

    pages = ['forever']
    if top:
        pages = popular(lang)

    print_header(delay, lang, pages)

    try:
        count = 0
        requests = 0
        elapsed = 0

        while len(pages) > 0:
            language = lang or random.choice(languages())
            if top and not lang:
                language = 'en'

            page = wptools.page(lang=language, silent=True)
            if top:
                page = wptools.page(pages.pop(0), lang=language, silent=True)

            page.get()

            preview = page.data.get('extext')
            if preview:
                preview = preview.strip().replace("\n", '')[:64]

            url = page.data.get('url')

            elapsed = int(time.time()) - start

            count += 1
            nrq = len(page.data.get('requests'))
            requests += nrq
            rps = float(0)
            if elapsed > 0:
                rps = float(requests) / elapsed
            frps = '{:.1f}'.format(rps)

            print("[%d] %d %s %s" % (count, nrq, frps, url))
            print("%s %s" % (page.data.get('wikibase'), preview))

            time.sleep(delay)

    except KeyboardInterrupt:
        print("Done. %d requests %d seconds" % (requests, elapsed))

    except:
        page.flags['silent'] = False
        page.show()
        print("EXCEPTION %d requests %d seconds" % (requests, elapsed))
        raise


def parse_args():
    """
    parse args for main()
    """
    argp = argparse.ArgumentParser()
    argp.add_argument('-d', '--delay', help='delay in seconds',
                      type=int, default=DEFAULT_DELAY)
    argp.add_argument('-l', '--lang', help='language code')
    argp.add_argument('-t', '--top', action='store_true', help='get top pages')
    return argp.parse_args()


if __name__ == "__main__":
    main(parse_args())

#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Stress-test Wptools
~~~~~~~~~~~~~~~~~~~

Endlessly GET page info from ALL Wikimedia APIs in MANY languages
"""

from __future__ import print_function

import random
import time

import wptools

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


def main(delay=1):
    """
    GET random pages forever
    """

    print("%d languages" % len(LANGUAGES))

    start = int(time.time())
    count = 0
    while True:
        count += 1
        elapsed = int(time.time()) - start

        lang = random.choice(LANGUAGES)
        page = wptools.page(lang=lang, silent=True)
        page.get()

        print("[%d](%d) %s" % (count, elapsed, page.data.get('url')))

        preview = page.data.get('extext')
        if preview:
            preview = preview.strip().replace("\n", '')[:72]

        print("  %s %s" % (page.data.get('wikibase'), preview))

        time.sleep(delay)


if __name__ == "__main__":
    main()

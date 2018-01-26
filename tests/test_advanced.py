#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
WPTools tests that use the network
"""

from __future__ import print_function

import argparse
import random
import unittest

import tests.titles as titles
import wptools

LANG = [
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
    'kn', 'ia', 'qu', 'ckb', 'mn', 'arz',
]

NOPAGE = 'aspofinwepobw'

WIKIS = [
    'commons.wikimedia.org',
    'en.wikibooks.org',
    'en.wikinews.org',
    'en.wikiquote.org',
    'en.wikisource.org',
    'en.wikiversity.org',
    'en.wikivoyage.org',
    'en.wiktionary.org',
]


class WPToolsBreakTest(unittest.TestCase):
    """
    test formerly breaking issues
    """
    def slash_in_title(self):
        """
        Slash in title causes LookupError in get_restbase() Issue #94
        """
        rest = wptools.restbase('/dev/null')
        rest.get_restbase('/page/summary/', show=False)
        self.assertTrue('exrest' in rest.data)
        self.assertEqual(page.data['title'], 'Null_device')

    def test_boxterm(self):
        """
        Spanish taxobox not captured. Issue #91
        """
        page = wptools.page('Okapi', lang='es', boxterm='Ficha',
                            skip=['imageinfo'])
        page.get_parse(show=False)
        self.assertTrue(len(page.data['infobox']) > 0)

    def test_normalized_filename(self):
        """
        Ensure parse-image does not cause infinite loop. The
        normalized API result image title did not match orginal
        parse-image file name... Issue #93
        """
        page = wptools.page('Aphra Behn')
        page.get_parse(show=False)
        self.assertTrue(len(page.data['requests']) < 3)


class WPToolsPickTest(unittest.TestCase):
    """
    SELECTED (cherry-picked) TESTS
    """

    def test_selected(self):
        """
        Test overall functionality from random i18n choice
        """
        title = titles.title()
        page = wptools.page(title['title'], lang=title['lang'])
        page.get(show=False)
        self.assertTrue(page.data['pageid'] is not None)

    def test_not_found(self):
        """
        Try to get a non-existent page
        """
        try:
            wptools.page(NOPAGE, silent=True).get(False)
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            pass

    def test_lookup_unicode_error(self):
        """
        Raise LookupError without UnicodeDecodeError. Issue #29
        """
        try:
            wptools.page('Д北_TEST', silent=True).get(False)
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            pass


class WPToolsRandomTest(unittest.TestCase):
    """
    RANDOM TESTS
    """

    def test_random(self):
        """
        Get random title from random language wiki
        """
        page = wptools.page(lang=random.choice(LANG))
        page.get(show=False)
        self.assertTrue(page.data['pageid'] is not None)

    def test_random_wiki(self):
        """
        Get random title from random Wikmedia project
        """
        page = wptools.page(wiki=random.choice(WIKIS))
        self.assertTrue(page.data['pageid'] is not None)


class WPToolsRestBaseTest(unittest.TestCase):
    """
    RESTBase TESTS
    """


class WPToolsSiteTest(unittest.TestCase):
    """
    Site TESTS
    """
    def test_site_get_info(self):
        """
        Get info about a random site
        """
        site = wptools.site(silent=True)

        site.get_sites()
        self.assertTrue(site.data['random'] is not None)

        site.get_info(site.data['random'])
        self.assertTrue(site.data['visitors'] >= 0)

        site.top()


class WPToolsToolTest(unittest.TestCase):
    """
    WPTOOL TESTS
    """

    @staticmethod
    def test_wptool():
        '''
        Get random page via wptool
        '''
        from scripts.wptool import main
        from collections import namedtuple
        args = namedtuple('Args', ['H', 'l', 'n', 'q', 's', 't', 'v', 'w'])
        cli = {'H': False, 'l': 'en', 'n': False, 'q': False, 's': True,
               't': '', 'v': False, 'w': ''}
        main(args(**cli))


class WPToolsUtilsTest(unittest.TestCase):
    """
    Utils Tests
    """

class WPToolsWikidataTest(unittest.TestCase):
    """
    Wikidata Tests
    """
    def test_wikidata_random(self):
        title = titles.title()
        page = wptools.page(title['title'], lang=title['lang'])
        from pprint import pprint
        page.get_query(show=False).get_wikidata()
        self.assertTrue(len(page.data['claims']) > 5)
        self.assertTrue(len(page.data['labels']) > 5)
        self.assertTrue(len(page.data['wikidata']) > 5)


if __name__ == '__main__':
    # unittest.main()

    from unittest import TestLoader
    suites = {
        'break': TestLoader().loadTestsFromTestCase(WPToolsBreakTest),
        'pick': TestLoader().loadTestsFromTestCase(WPToolsPickTest),
        'rand': TestLoader().loadTestsFromTestCase(WPToolsRandomTest),
        'restbase': TestLoader().loadTestsFromTestCase(WPToolsRestBaseTest),
        'site': TestLoader().loadTestsFromTestCase(WPToolsSiteTest),
        'tool': TestLoader().loadTestsFromTestCase(WPToolsToolTest),
        'utils': TestLoader().loadTestsFromTestCase(WPToolsUtilsTest),
        'wikidata': TestLoader().loadTestsFromTestCase(WPToolsWikidataTest),
    }
    suites['all'] = unittest.TestSuite(suites.values())

    argp = argparse.ArgumentParser()
    argp.add_argument('suite', choices=suites.keys())
    args = argp.parse_args()

    unittest.TextTestRunner().run(suites[args.suite])

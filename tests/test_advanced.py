#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import random
import unittest
import wptools


lang = ['de', 'es', 'fr', 'hi', 'it', 'ja', 'nl', 'ru', 'sv', 'vi', 'zh']


class WPToolsBadTest(unittest.TestCase):
    """
    BAD API REQUEST TESTS
    """

    def test_redirect(self):
        """
        Get redirected
        """
        b = wptools.page('Ben Franklin').get_query(False)
        self.assertTrue(b.url.endswith('Benjamin_Franklin'))

    def test_missing(self):
        """
        Get missing page
        """
        try:
            wptools.page(pageid=1).get(False)
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            print(detail)

    def test_unknown_lang(self):
        """
        Mediawiki site function not supported
        """
        # "jp" Wikinews (unknown language code)
        b = wptools.page(wiki='jp.wikinews.org')
        self.assertTrue(b.fatal)


class WPToolsPickTest(unittest.TestCase):
    """
    SELECTED (cherry-picked) TESTS
    """

    def test_selected(self):
        """
        Get selected title
        """
        t = wptools.test.title()
        p = wptools.page(t['title'], lang=t['lang']).get_query(False)
        self.assertTrue(p.pageid is not None)

    def test_wikibase(self):
        """
        Get everything wikibase only
        """
        p = wptools.page(wikibase='Q43303').get_wikidata(False, False)
        self.assertEqual(p.title, 'Malcolm_X')

    def test_wikidata_title(self):
        """
        Get wikidata from title only
        """
        w = wptools.page('Les Misérables').get_wikidata(False, False)
        self.assertTrue(w.wikibase is not None)

    def test_wikidata_claims(self):
        p = wptools.page('Paris').get_wikidata(False)
        self.assertTrue('latitude' in p.wikidata['coordinates'])
        self.assertEqual(p.wikidata['country'], 'France')
        self.assertTrue(len(p.wikidata['instance']) > 3)

    def test_mixed_lang(self):
        """
        Get mixed language
        """
        p = wptools.page('Abraham Lincoln', lang='zh').get_query(False)
        self.assertEqual(p.wikibase, 'Q91')

    def test_complex_infobox(self):
        """
        Successfully populate complex infobox dict
        """
        p = wptools.page('Aung San Suu Kyi').get_parse(False)
        self.assertGreaterEqual(len(p.infobox), 32)
        self.assertTrue('errors' not in p.infobox)

    def test_thumbnail(self):
        """
        Get a thumbnail image URL
        """
        p = wptools.page('Frida Kahlo').get_query(False)
        self.assertTrue('url' in p.image('thumb'))

    def test_pageid(self):
        """
        Get a page by pageid
        """
        p = wptools.page(pageid=851640).get_query(False)
        self.assertTrue(p.title == 'Helianthus')

    def test_disambiguation_wikibase(self):
        """
        Get an unambiguous page by wikibase
        """
        p = wptools.page(wikibase='Q528917')
        p.get_wikidata(False).get_query(False)
        self.assertTrue(p.pageid == 20974062)

    def test_lookup_unicode_error(self):
        """
        Potentially raise UnicodeDecodeError on LookupError
        """
        try:
            p = wptools.page('阿Vane').get(False)  # issue 29
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            print(detail)

    def test_imageinfo(self):
        """
        Ensure get_imageinfo() updates images
        """
        a = wptools.page("Alice's Adventures in Wonderland").get_query(False)
        self.assertTrue('url' in a.image('pageimage'))


class WPToolsRandomTest(unittest.TestCase):
    """
    RANDOM TESTS
    """

    def test_random(self):
        """
        Get a random title
        """
        r = wptools.page()
        self.assertTrue(r.pageid is not None)

    def test_random_lang(self):
        """
        Get random title by language
        """
        r = wptools.page(lang=random.choice(lang))
        self.assertTrue(r.pageid is not None)

    def test_random_wiki(self):
        """
        Get random title by wiki
        """
        r = wptools.page(wiki='commons.wikimedia.org')
        self.assertTrue(r.pageid is not None)


class WPToolsRestBaseTest(unittest.TestCase):
    """
    RESTBase TESTS
    """

    def test_get_rest(self):
        t = wptools.test.title()
        r = wptools.page(t['title'], lang=t['lang'])
        r.get_rest()
        self.assertTrue(r.lead is not None)


class WPToolsToolTest(unittest.TestCase):
    """
    WPTOOL TESTS
    """

    def test_wptool(self):
        from scripts.wptool import main
        from collections import namedtuple
        args = namedtuple('Args', ['H', 'l', 'n', 'q', 's', 't', 'v', 'w'])
        cli = {'H': False, 'l': 'en', 'n': False, 'q': False, 's': True,
               't': '', 'v': False, 'w': ''}
        main(args(**cli))


if __name__ == '__main__':
    # unittest.main()

    from unittest import TestLoader
    suites = {
        'bad':  TestLoader().loadTestsFromTestCase(WPToolsBadTest),
        'pick': TestLoader().loadTestsFromTestCase(WPToolsPickTest),
        'rand': TestLoader().loadTestsFromTestCase(WPToolsRandomTest),
        'rest': TestLoader().loadTestsFromTestCase(WPToolsRestBaseTest),
        'tool': TestLoader().loadTestsFromTestCase(WPToolsToolTest),
    }
    suites['all'] = unittest.TestSuite(suites.values())

    argp = argparse.ArgumentParser()
    argp.add_argument('suite', choices=suites.keys())
    args = argp.parse_args()

    unittest.TextTestRunner().run(suites[args.suite])

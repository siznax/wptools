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
        self.assertEqual(b.title, 'Benjamin_Franklin')

    def test_missing(self):
        """
        Get missing title
        """
        b = wptools.page('_____').get_query(False)
        self.assertTrue(b.pageid is None)

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
        self.assertTrue(p.wikidata['coordinates'] is not None)
        self.assertEqual(p.wikidata['continent'], 'Europe')
        self.assertEqual(p.wikidata['country'], 'France')

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
        p = wptools.page('Frida Kahlo').get_rest(False)
        self.assertTrue(p.thumbnail.startswith('http'))

    def test_pageid(self):
        """
        Get a page by pageid
        """
        p = wptools.page(pageid=851640).get_query(False)
        self.assertTrue(p.title == 'Helianthus')


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
        r.get_rest(show=False)
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

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
        b = wptools.page('Abe Lincoln').get_query(False)
        self.assertEqual(b.title, "Abraham_Lincoln")

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
        self.assertTrue(hasattr(b, 'fatal'))


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
        self.assertTrue(hasattr(p, 'pageid'))

    def test_wikibase(self):
        """
        Get everything wikibase only
        """
        p = wptools.page(wikibase='Q43303').get_wikidata(False)
        self.assertEqual(p.title, "Malcolm_X")

    def test_wikidata_title(self):
        """
        Get wikidata from title only
        """
        w = wptools.page('Les Misérables').get_wikidata(False)
        self.assertTrue(w.wikibase is not None)

    def test_mixed_lang(self):
        """
        Get mixed language
        """
        p = wptools.page('Abraham Lincoln', lang='zh').get_query(False)
        self.assertEqual(p.wikibase, "Q91")

    def test_complex_infobox(self):
        """
        Successfully populate complex infobox dict
        """
        p = wptools.page('Abe Lincoln').get_parse(False)
        self.assertGreaterEqual(len(p.infobox), 42)


class WPToolsRandomTest(unittest.TestCase):
    """
    RANDOM TESTS
    """

    def test_random(self):
        """
        Get a random title
        """
        r = wptools.page()
        self.assertTrue(hasattr(r, 'pageid'))

    def test_random_lang(self):
        """
        Get random title by language
        """
        r = wptools.page(lang=random.choice(lang))
        self.assertTrue(hasattr(r, 'pageid'))

    def test_random_wiki(self):
        """
        Get random title by wiki
        """
        r = wptools.page(wiki='commons.wikimedia.org')
        self.assertTrue(hasattr(r, 'pageid'))


class WPToolsRestBaseTest(unittest.TestCase):
    """
    RESTBase TESTS
    """

    def test_get_rest(self):
        t = wptools.test.title()
        r = wptools.page(t['title'], lang=t['lang'])
        r.get_rest(show=False)
        self.assertTrue(hasattr(r, 'lead'))


class WPToolsToolTest(unittest.TestCase):
    """
    WPTOOL TESTS
    """

    def test_wptool(self):
        from scripts.wptool import main


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

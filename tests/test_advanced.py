#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
WPTools advanced tests
"""

from __future__ import print_function

import argparse
import random
import unittest

import tests.titles as titles
import tests.wikidata_images as wikidata_images
import wptools

LANG = ['de', 'es', 'fr', 'hi', 'it', 'ja', 'nl', 'ru', 'sv', 'vi', 'zh']


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
        try:
            wptools.page(wiki='jp.wikinews.org')
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            print(detail)


class WPToolsPickTest(unittest.TestCase):
    """
    SELECTED (cherry-picked) TESTS
    """

    def test_selected(self):
        """
        Get selected title
        """
        t = titles.title()
        p = wptools.page(t['title'], lang=t['lang']).get_query(False)
        self.assertTrue(p.pageid is not None)

    def test_wikibase(self):
        """
        Get everything wikibase only
        """
        p = wptools.page(wikibase='Q43303').get_wikidata(False)
        self.assertEqual(p.title, 'Malcolm_X')
        self.assertEqual(p.what, 'human')
        self.assertEqual(p.wikibase, 'Q43303')
        self.assertTrue(p.label is not None)
        self.assertTrue(p.description is not None)
        self.assertTrue(p.images.pop()['file'] is not None)
        self.assertTrue(len(p.wikidata) > 5)

    def test_wikidata_title(self):
        """
        Get wikidata from title only
        """
        w = wptools.page('Les Misérables').get_wikidata(False)
        self.assertTrue(w.wikibase is not None)

    def test_wikidata_claims(self):
        """
        Get wikidata claims
        """
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
            wptools.page('阿Vane').get(False)  # issue 29
            self.fail("failed to raise LookupError")
        except LookupError as detail:
            print(detail)

    def test_imageinfo(self):
        """
        Ensure get_imageinfo() updates images
        """
        a = wptools.page('Aardvark').get_query(False)
        self.assertTrue('url' in a.image('thumb'))


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
        self.assertTrue(r.title is not None)

    def test_random_lang(self):
        """
        Get random title by language
        """
        r = wptools.page(lang=random.choice(LANG))
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
        """
        Get RESTBase entry points
        """
        page = wptools.page('test')
        page.get_rest()
        self.assertEqual(page.endpoint, '/page/')

    def test_get_rest_html(self):
        """
        Get RESTBase HTML
        """
        page = wptools.page()
        page.get_rest('html')
        self.assertTrue('/html/' in page.endpoint)
        self.assertTrue(page.html.startswith('<!DOCTYPE'))
        self.assertTrue(page.html.endswith('</html>'))

    def test_get_rest_lead(self):
        """
        Get RESTBase lead section
        """
        page = wptools.page()
        page.get_rest('mobile-sections-lead')
        self.assertTrue(page.lead.startswith('<span'))
        self.assertTrue('page' in page.modified)
        self.assertTrue(page.pageid is not None)
        self.assertTrue(page.wikibase is not None)

    def test_get_rest_summary(self):
        """
        Get RESTBase page summary
        """
        page = wptools.page()
        page.get_rest('summary')
        self.assertTrue(page.exhtml.startswith('<p>'))
        self.assertTrue(page.pageid is not None)


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

    def test_infobox_subelements(self):
        """
        Get infobox data with sub-elements. Issue #66
        """
        p = wptools.page("ONE OK ROCK", lang='ja').get_parse()
        self.assertGreater(len(p.infobox['Genre'].split('<br')), 5)

    def test_infobox_children(self):
        """
        Get infobox data with list values. Issue #62
        """
        p = wptools.page('Lewisit', lang='de').get_parse()
        self.assertGreater(len(p.infobox['Dichte'].split('*')), 1)

    def test_complex_infobox(self):
        """
        Successfully populate complex infobox dict
        """
        p = wptools.page('Aung San Suu Kyi').get_parse(False)
        self.assertGreaterEqual(len(p.infobox), 32)
        self.assertTrue('errors' not in p.infobox)


class WPToolsWikidataTest(unittest.TestCase):
    """
    Wikidata Tests
    """

    def test_wikidata_images(self):
        """
        Get wikidata images from cache.
        """
        page = wptools.page('test_wikidata_images')
        page.cache['wikidata'] = wikidata_images.cache
        page._set_wikidata()
        self.assertEqual(len(page.images), 3)


if __name__ == '__main__':
    # unittest.main()

    from unittest import TestLoader
    suites = {
        'bad':  TestLoader().loadTestsFromTestCase(WPToolsBadTest),
        'pick': TestLoader().loadTestsFromTestCase(WPToolsPickTest),
        'rand': TestLoader().loadTestsFromTestCase(WPToolsRandomTest),
        'rest': TestLoader().loadTestsFromTestCase(WPToolsRestBaseTest),
        'tool': TestLoader().loadTestsFromTestCase(WPToolsToolTest),
        'utils': TestLoader().loadTestsFromTestCase(WPToolsUtilsTest),
        'wikidata': TestLoader().loadTestsFromTestCase(WPToolsWikidataTest),
    }
    suites['all'] = unittest.TestSuite(suites.values())

    argp = argparse.ArgumentParser()
    argp.add_argument('suite', choices=suites.keys())
    args = argp.parse_args()

    unittest.TextTestRunner().run(suites[args.suite])

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import random
import unittest
import wptools


lang = ['es', 'fr', 'hi', 'ja', 'zh', 'ru']


class WPToolsBadTest(unittest.TestCase):
    """
    BAD API REQUEST TESTS
    """

    def test_redirect(self):
        """
        Get redirected
        """
        wptools.page(title='Abe Lincoln').get()

    def test_missing(self):
        """
        Get missing title
        """
        wptools.page(title='ƀļēřğ').get()

    def test_uknown_lang(self):
        """
        Mediawiki site function not supported
        """
        # "jp" Wikinews (unknown language code)
        g = wptools.page(wiki='jp.wikinews.org').get()
        assert g.fatal is not None


class WPToolsPickTest(unittest.TestCase):
    """
    SELECTED (cherry-picked) TESTS
    """

    def test_multibyte(self):
        """
        Get everything multibyte request
        """
        wptools.page('托爾金', lang='zh')  # 托爾金 (zh) Tolkien

    def test_wikibase(self):
        """
        Get everything wikibase only
        """
        wptools.page(wikibase='Q43303').get()  # Q43303=Malcolm_X

    def test_selected(self):
        """
        Get selected title
        """
        rtitle = wptools.test.title()
        wptools.page(lang=rtitle['lang'],
                     title=rtitle['title']).get()

    def test_mixed_lang(self):
        """
        Get everything mixed languages
        """
        g = wptools.page(title='Abraham Lincoln', lang='zh').get()
        assert g.Description is not None

    def test_complex_infobox(self):
        """
        Successfully populate complex infobox dict
        """
        g = wptools.page('Abe Lincoln').get()
        self.assertGreaterEqual(len(g.infobox), 42)


class WPToolsRandomTest(unittest.TestCase):
    """
    RANDOM TESTS
    """

    def test_random(self):
        """
        Get random everything
        """
        wptools.page().get()

    def test_random_lang(self):
        """
        Get everything from random item in another language
        """
        wptools.page(lang=random.choice(lang)).get()

    def test_random_wiki(self):
        """
        Get random item from another wiki
        """
        wptools.page(wiki='en.wikinews.org').get()


class WPToolsRestBaseTest(unittest.TestCase):
    """
    RESTBase TESTS
    """

    def test_get_rest(self):
        t = wptools.test.title()
        r = wptools.page(lang=t['lang'], title=t['title'])
        r.get_query()
        r.get_wikidata()
        r.get_rest()
        if hasattr(r, 'g_rest') and 'html' in r.g_rest:
            print r.g_rest['html'].encode('utf-8')
            print "\n<hr>\n"
            print r.lead.encode('utf-8')


class WPToolsToolTest(unittest.TestCase):
    """
    WPTOOL TESTS
    """

    def test_wptool(self):
        from scripts.wptool import main
        main()


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

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Basic tests for WPTools.
"""

import unittest
import wptools


class WPToolsTestCase(unittest.TestCase):

    def test_entry_points(self):

        wptools.core
        wptools.fetch
        wptools.utils
        wptools.test

        from scripts.wptool import main


class WPToolsCoreTestCase(unittest.TestCase):

    def test_caching(self):
        abc = wptools.page('abc')
        abc.claims = {'Q1': 'test'}
        abc.cache['claims'] = {'response'}
        abc.cache['imageinfo'] = {'response'}
        abc.images = [{'url': 'URL'}]
        abc.cache['parse'] = {'response'}
        abc.cache['query'] = {'response'}
        abc.cache['rest'] = {'response'}
        abc.cache['wikidata'] = {'response'}
        abc.get_claims()
        abc.get_imageinfo()
        abc.get_parse()
        abc.get_query()
        abc.get_rest()
        abc.get_wikidata()
        self.assertTrue(not abc.pageid)

    def test_wptool(self):
        from scripts.wptool import main
        from collections import namedtuple
        args = namedtuple('Args', ['H', 'l', 'n', 'q', 's', 't', 'v', 'w'])
        cli = {'H': False, 'l': 'en', 'n': False, 'q': True, 's': True,
               't': '', 'v': False, 'w': ''}
        main(args(**cli))


class WPtoolsFetchTestCase(unittest.TestCase):

    def test_variant(self):
        f = wptools.fetch.WPToolsFetch(variant='zh-cn')
        self.assertTrue(f.query('query', 'a').endswith('&variant=zh-cn'))

class WPToolsUtilsTestCase(unittest.TestCase):

    def test_snip_html_metadata(self):
        """
        Ignore elem.metadata
        """
        from wptools.utils import snip_html
        txt = "<small class=\"metadata\">a</small>b"
        ans = '<span><span ignored></span>b</span>'
        self.assertEqual(snip_html(txt), ans)

    def test_snip_html_reference(self):
        from wptools.utils import snip_html
        txt = "a<sup class=\"reference\"><a href>[b]</a></sup>c"
        ans = "a<span><span ignored></span>c</span>"
        self.assertEqual(snip_html(txt), ans)


if __name__ == '__main__':
    unittest.main()

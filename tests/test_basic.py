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

    def test_get_query(self):
        import query
        page = wptools.page('test_get_query')
        page.cache['query'] = query.cache
        page._set_query_data()
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertTrue(page.extext.startswith('**Douglas'))
        self.assertTrue(page.extract.startswith('<p><b>Douglas'))
        self.assertTrue(len(page.images) > 1)
        self.assertEqual(page.label, 'Douglas Adams')
        self.assertEqual(page.lang, 'en')
        self.assertTrue('page' in page.modified)
        self.assertEqual(page.pageid, 8091)
        self.assertTrue(wptools.utils.is_text(page.random))
        self.assertEqual(page.title, 'Douglas_Adams')
        self.assertTrue(page.url.startswith('http'))
        self.assertTrue(page.url_raw.startswith('http'))
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertTrue(page.wikidata_url.startswith('http'))

    def test_caching(self):
        abc = wptools.page('test_caching')
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


class WPToolsFetchTestCase(unittest.TestCase):

    def test_variant(self):
        f = wptools.fetch.WPToolsFetch(variant='zh-cn')
        self.assertTrue(f.query('query', 'a').endswith('&variant=zh-cn'))


class WPToolsToolTestCase(unittest.TestCase):

    def test_wptool(self):
        from scripts.wptool import main
        from collections import namedtuple
        args = namedtuple('Args', ['H', 'l', 'n', 'q', 's', 't', 'v', 'w'])
        cli = {'H': False, 'l': 'en', 'n': False, 'q': True, 's': True,
               't': '', 'v': False, 'w': ''}
        main(args(**cli))


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

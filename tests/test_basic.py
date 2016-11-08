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

    def test_get_rest(self):
        import rest
        page = wptools.page('test_get_rest')
        page.cache['rest'] = rest.cache
        page._set_rest_data()
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertEqual(page.lang, 'en')
        self.assertEqual(len(page.images), 2)
        self.assertEqual(page.image('image')['kind'], 'rest-image')
        self.assertEqual(page.image('thumb')['kind'], 'rest-thumb')
        self.assertTrue(len(page.lead) > 1024 * 3)
        self.assertTrue(page.lead.startswith('<span'))
        self.assertTrue('page' in page.modified)
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertTrue(page.url.endswith('Adams'))
        self.assertTrue('Douglas_Adams' in page.url_raw)

    def test_get_imageinfo(self):
        import claims, imageinfo
        page = wptools.page('test_get_imageinfo')
        page.images = [{'file': 'Douglas adams portrait cropped.jpg',
                        'kind': 'test'}]
        page.cache['imageinfo'] = imageinfo.cache
        page._set_imageinfo_data()
        image = page.images[0]
        self.assertTrue(image['file'].startswith('File:'))
        self.assertTrue('/c/c0/' in image['url'])
        self.assertTrue('/commons.' in image['descriptionurl'])
        self.assertTrue(image['size'] > 1024)
        self.assertTrue(image['width'] > 240)
        self.assertTrue(image['height'] > 320)

    def test_get_claims(self):
        import claims, wikidata
        page = wptools.page('test_get_claims')
        page.cache['wikidata'] = wikidata.cache
        page._set_wikidata()
        page.cache['claims'] = claims.cache
        page._set_claims_data()
        self.assertEqual(len(page.claims), 11)
        self.assertEqual(len(page.props), 10)
        self.assertTrue(str(page.what), 'human')
        self.assertTrue('science' in page.wikidata['genre'].lower())
        self.assertTrue('Mostly Harmless' in page.wikidata['work'])

    def test_get_wikidata(self):
        import wikidata
        page = wptools.page('test_get_wikidata')
        page.cache['wikidata'] = wikidata.cache
        page._set_wikidata()
        self.assertEqual(len(page.claims), 11)
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertEqual(page.label, 'Douglas Adams')
        self.assertEqual(page.images[0]['kind'], 'wikidata-image')
        self.assertTrue('wikidata' in page.modified)
        self.assertEqual(len(page.props), 10)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertEqual(len(page.wikidata), 5)
        self.assertTrue(str(page.wikidata['birth']).startswith('+1952'))
        self.assertTrue(page.wikidata_url.endswith('Q42'))

    def test_get_parse(self):
        import parse
        page = wptools.page('test_get_parse')
        page.cache['parse'] = parse.cache
        page._set_parse_data()
        self.assertEqual(len(page.infobox), 15)
        self.assertTrue('satire' in page.infobox['genre'])
        self.assertEqual(page.lang, 'en')
        self.assertEqual(len(page.links), 2)
        self.assertEqual(page.pageid, 8091)
        self.assertTrue(len(page.parsetree) > 1024 * 64)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertTrue(page.wikidata_url.startswith('http'))
        self.assertTrue(len(page.wikitext) > 1024 * 64)

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
        self.assertTrue(page.url.endswith('Adams'))
        self.assertTrue('Douglas_Adams' in page.url_raw)
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertTrue(page.wikidata_url.endswith('Q42'))

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

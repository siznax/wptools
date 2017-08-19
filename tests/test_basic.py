#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Basic tests for WPTools.
"""

import unittest
import wptools

from . import category
from . import claims
from . import imageinfo
from . import parse
from . import query
from . import rest_lead
from . import rest_html
from . import rest_summary
from . import wikidata


class WPToolsTestCase(unittest.TestCase):

    def test_entry_points(self):

        wptools.core
        wptools.fetch
        wptools.utils


class WPToolsCategoryTestCase(unittest.TestCase):

    def test_category_init(self):
        self.assertRaises(ValueError, wptools.cat)
        self.assertRaises(ValueError, wptools.cat, pageid='not int')
        self.assertRaises(ValueError, wptools.cat, 'Test', pageid=123)

    def test_category_get_members(self):
        cat = wptools.cat('test_category_get_members', silent=True)
        cat.cache['category'] = category.cache
        cat._set_category_data()
        self.assertTrue(len(cat.members), 92)


class WPToolsCoreTestCase(unittest.TestCase):

    def test_get_rest_html(self):
        """RESTBase /page/html"""
        page = wptools.page('test_get_rest_html', silent=True)
        page.cache['rest'] = rest_html.cache
        page._set_rest_data()
        self.assertTrue(len(page.html) > 1024 * 250)
        self.assertTrue(page.html.startswith('<!DOCTYPE'))
        self.assertTrue(page.html.endswith('</html>'))

    def test_get_rest_lead(self):
        """RESTBase /page/mobile-sections-lead"""
        page = wptools.page('test_get_rest_lead', silent=True)
        page.cache['rest'] = rest_lead.cache
        page._set_rest_data()
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertEqual(len(page.images), 1)
        self.assertEqual(page.image('image')['kind'], 'rest-image')
        self.assertTrue(len(page.lead) > 1024 * 6)
        self.assertTrue(page.lead.startswith('<span'))
        self.assertTrue('page' in page.modified)
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertTrue(page.url.endswith('Douglas_Adams'))
        self.assertEqual(str(page.wikibase), 'Q42')

    def test_get_rest_summary(self):
        """RESTBase /page/summary"""
        page = wptools.page('test_get_rest_summary', silent=True)
        page.cache['rest'] = rest_summary.cache
        page._set_rest_data()
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertTrue(len(page.exrest) < 1024)
        self.assertTrue(len(page.exhtml) < 1024)
        self.assertTrue(page.exrest.startswith('Douglas'))
        self.assertTrue(page.exhtml.startswith('<p>'))
        self.assertEqual(len(page.images), 2)
        self.assertEqual(page.image('image')['kind'], 'rest-image')
        self.assertEqual(page.image('thumb')['kind'], 'rest-thumb')
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertTrue(page.url.endswith('Douglas_Adams'))

    def test_get_imageinfo(self):
        page = wptools.page('test_get_imageinfo', silent=True)
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
        page = wptools.page('test_get_claims', silent=True)
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
        page = wptools.page('test_get_wikidata', silent=True)
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
        page = wptools.page('test_get_parse', silent=True)
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
        page = wptools.page('test_get_query', silent=True)
        page.cache['query'] = query.cache
        page._set_query_data()
        self.assertEqual(len(page.categories), 29)
        self.assertEqual(len(page.languages), 69)
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertEqual(page.label, 'Douglas Adams')
        self.assertEqual(page.lang, 'en')
        self.assertEqual(page.length, 60069)
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(page.title, 'Douglas_Adams')
        self.assertEqual(page.watchers, 447)
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertTrue('Douglas_Adams' in page.url_raw)
        self.assertTrue('page' in page.modified)
        self.assertTrue(len(page.images) > 1)
        self.assertTrue(page.extext.startswith('**Douglas'))
        self.assertTrue(page.extract.startswith('<p><b>Douglas'))
        self.assertTrue(page.url.endswith('Adams'))
        self.assertTrue(page.wikidata_url.endswith('Q42'))
        self.assertTrue(wptools.utils.is_text(page.random))

    def test_caching(self):
        abc = wptools.page('test_caching', silent=True)
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

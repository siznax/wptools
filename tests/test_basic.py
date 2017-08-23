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
        wptools.query
        wptools.request
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
        self.assertEqual(len(page.image), 1)
        self.assertEqual(page.pageimage('image')['kind'], 'rest-image')
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
        self.assertEqual(len(page.image), 2)
        self.assertEqual(page.pageimage('image')['kind'], 'rest-image')
        self.assertEqual(page.pageimage('thumb')['kind'], 'rest-thumb')
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(str(page.title), 'Douglas_Adams')
        self.assertTrue(page.url.endswith('Douglas_Adams'))

    def test_get_imageinfo(self):
        page = wptools.page('test_get_imageinfo', silent=True)
        page.image = [{'file': 'Douglas adams portrait cropped.jpg',
                       'kind': 'test'}]
        page.cache['imageinfo'] = imageinfo.cache
        page._set_imageinfo_data()
        image = page.image[0]
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
        self.assertEqual(page.image[0]['kind'], 'wikidata-image')
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
        self.assertEqual(len(page.files), 12)
        self.assertEqual(len(page.languages), 70)
        self.assertEqual(page.description, 'English writer and humorist')
        self.assertEqual(page.label, 'Douglas Adams')
        self.assertEqual(page.lang, 'en')
        self.assertEqual(page.length, 60069)
        self.assertEqual(page.pageid, 8091)
        self.assertEqual(page.title, 'Douglas_Adams')
        self.assertEqual(page.views, 1362)
        self.assertEqual(page.watchers, 447)
        self.assertEqual(str(page.wikibase), 'Q42')
        self.assertTrue('Douglas_Adams' in page.url_raw)
        self.assertTrue('page' in page.modified)
        self.assertTrue(len(page.image) > 1)
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
        abc.image = [{'url': 'URL'}]
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


class WPToolsQueryTestCase(unittest.TestCase):


    def test_query_init(self):
        qobj = wptools.query.WPToolsQuery()
        self.assertEqual(qobj.lang, 'en')
        self.assertEqual(qobj.uri, 'https://en.wikipedia.org')
        self.assertEqual(qobj.wiki, 'en.wikipedia.org')

    def test_query_init_wiki(self):
        qobj = wptools.query.WPToolsQuery(wiki='http://example.com')
        self.assertEqual(qobj.domain, 'example.com')
        self.assertEqual(qobj.uri, 'http://example.com')

    def test_query_init_lang(self):
        qobj = wptools.query.WPToolsQuery(lang='zz')
        self.assertEqual(qobj.lang, 'zz')
        self.assertEqual(qobj.domain, 'zz.wikipedia.org')
        self.assertEqual(qobj.uri, 'https://zz.wikipedia.org')

    def test_query_category(self):
        qobj = wptools.query.WPToolsQuery()

        qstr = qobj.category(title='TEST')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('&list=categorymembers' in qstr)
        self.assertTrue('&cmtitle=TEST' in qstr)
        self.assertTrue('&cmpageid' not in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (category) TEST')

        qstr = qobj.category(None, pageid=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('&list=categorymembers' in qstr)
        self.assertTrue('&cmpageid=123' in qstr)
        self.assertTrue('&cmtitle' not in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (category) 123')

    def test_query_claims(self):
        qobj = wptools.query.WPToolsQuery()
        qstr = qobj.claims(qids=['Q1', 'Q2', 'Q3'])
        self.assertTrue(qstr.startswith('https://www.wikidata.org'))
        self.assertTrue('?action=wbgetentities' in qstr)
        self.assertTrue('&ids=Q1|Q2|Q3' in qstr)
        self.assertEqual(qobj.status, 'www.wikidata.org (claims) Q1|Q2|Q3')

    def test_query_domain_name(self):
        domain = wptools.query.domain_name('http://example.com/a//b/c/')
        self.assertEqual(domain, 'example.com')

    def test_query_imageinfo(self):
        qobj = wptools.query.WPToolsQuery()
        qstr = qobj.imageinfo(files=['A', 'B', 'C'])
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=query' in qstr)
        self.assertTrue('&prop=imageinfo' in qstr)
        self.assertTrue('&titles=A|B|C' in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (imageinfo) A|B|C')

    def test_query_query(self):
        qobj = wptools.query.WPToolsQuery()

        qstr = qobj.query(titles='TEST')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=query' in qstr)
        self.assertTrue('&titles=TEST')
        self.assertEqual(qobj.status, 'en.wikipedia.org (query) TEST')

        qstr = qobj.query(None, pageids=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=query' in qstr)
        self.assertTrue('&pageids=123')
        self.assertEqual(qobj.status, 'en.wikipedia.org (query) 123')

    def test_query_parse(self):
        qobj = wptools.query.WPToolsQuery()

        qstr = qobj.parse(title='TEST')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=parse' in qstr)
        self.assertTrue('&page=TEST')
        self.assertEqual(qobj.status, 'en.wikipedia.org (parse) TEST')

        qstr = qobj.parse(None, pageid=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=parse' in qstr)
        self.assertTrue('&redirects' not in qstr)
        self.assertTrue('&pageid=123')
        self.assertEqual(qobj.status, 'en.wikipedia.org (parse) 123')

    def test_query_random(self):
        qobj = wptools.query.WPToolsQuery()
        qstr = qobj.random()
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=query' in qstr)
        self.assertTrue('&list=random' in qstr)
        self.assertTrue('en.wikipedia.org (random)' in qobj.status)

    def test_query_rest(self):
        qobj = wptools.query.WPToolsQuery()
        qstr = qobj.rest(endpoint='/TEST/')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('/api/rest' in qstr)
        self.assertTrue(qstr.endswith('/TEST/'))
        self.assertEqual(qobj.status, 'en.wikipedia.org (rest) /TEST/')

    def test_query_set_status(self):
        qobj = wptools.query.WPToolsQuery()

        qobj.set_status('TEST_ACTION', 'TEST_TARGET')
        self.assertEqual(qobj.status,
                         'en.wikipedia.org (TEST_ACTION) TEST_TARGET')
        qobj.set_status('--------------------------------------------------',
                        '--------------------------------------------------')
        self.assertTrue(len(qobj.status) == 80)

    def test_query_wiki_uri(self):
        qobj = wptools.query.WPToolsQuery()
        uri = qobj.wiki_uri(wiki='http://example.com/')
        self.assertEqual(uri, 'http://example.com/')

    def test_query_wikidata(self):
        qobj = wptools.query.WPToolsQuery()

        qstr = qobj.wikidata(title='TEST')
        self.assertTrue(qstr.startswith('https://www.wikidata.org'))
        self.assertTrue('?action=wbgetentities' in qstr)
        self.assertTrue('&sites=enwiki' in qstr)
        self.assertTrue('&titles=TEST' in qstr)
        self.assertEqual(qobj.status, 'www.wikidata.org (wikidata) TEST')

        qstr = qobj.wikidata(None, wikibase='Q1')
        self.assertTrue(qstr.startswith('https://www.wikidata.org'))
        self.assertTrue('?action=wbgetentities' in qstr)
        self.assertTrue('&sites' not in qstr)
        self.assertTrue('&titles' not in qstr)
        self.assertTrue('&ids=Q1' in qstr)
        self.assertEqual(qobj.status, 'www.wikidata.org (wikidata) Q1')

    def test_query_variant_parse(self):
        qobj = wptools.query.WPToolsQuery(variant='zh-cn')
        qstr = qobj.parse('TEST')
        self.assertTrue('&variant=zh-cn' in qstr)

    def test_query_variant_query(self):
        qobj = wptools.query.WPToolsQuery(variant='zh-cn')
        qstr = qobj.query('TEST')
        self.assertTrue('&variant=zh-cn' in qstr)

    def test_query_variant_wikidata(self):
        qobj = wptools.query.WPToolsQuery(variant='zh-cn')
        qstr = qobj.wikidata('TEST')
        self.assertTrue('&languages=zh-cn' in qstr)


class WPToolsRequestTestCase(unittest.TestCase):

    def test_request_init(self):
        req = wptools.request.WPToolsRequest()
        self.assertEqual(req.silent, False)
        self.assertEqual(req.verbose, False)
        self.assertTrue(isinstance(req.cobj, wptools.request.pycurl.Curl))

    def test_request_curl_info(self):
        req = wptools.request.WPToolsRequest()
        info = wptools.request.curl_info(req.cobj)
        self.assertEqual(info.get('status'), 0)
        self.assertEqual(info.get('bytes'), 0.0)
        self.assertEqual(info.get('content'), None)
        self.assertTrue('wptools' in info.get('user-agent'))

    def test_request_curl_setup(self):
        req = wptools.request.WPToolsRequest()
        req.curl_setup()
        info = req.cobj.getinfo(wptools.request.pycurl.EFFECTIVE_URL)
        self.assertEqual(info, '')
        info = req.cobj.getinfo(wptools.request.pycurl.RESPONSE_CODE)
        self.assertEqual(info, 0)

    def test_request_user_agent(self):
        agent = wptools.request.user_agent()
        self.assertTrue(agent.startswith('wptools'))
        self.assertTrue('(https://github.com/siznax/wptools)' in agent)


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

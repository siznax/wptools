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

    @staticmethod
    def test_entry_points():
        wptools.core
        wptools.query
        wptools.request
        wptools.utils

        wptools.page
        wptools.category
        wptools.restbase
        wptools.wikidata


class WPToolsCategoryTestCase(unittest.TestCase):

    def test_category_init(self):
        self.assertRaises(ValueError, wptools.category, pageid='TEST')
        self.assertRaises(ValueError, wptools.category, 'TEST', pageid=123)
        cat = wptools.category('TEST')
        self.assertEqual(cat.params, {'lang': 'en', 'title': 'TEST'})

    def test_category_caching(self):
        cat = wptools.category('TEST', silent=True)
        cat.cache['category'] = {'response': None}
        cat.get_members()
        self.assertEqual(len(cat.data), 0)

    def test_category_get_members(self):
        cat = wptools.category('TEST')
        cat.cache['category'] = category.cache
        cat._set_data('category')
        self.assertTrue(len(cat.data['members']), 92)

    def test_category_get_members_namespace(self):
        cat = wptools.category('TEST', namespace=0)
        cat.cache['category'] = category.cache
        cat._set_data('category')
        self.assertTrue(len(cat.data['members']), 92)

    def test_category_query(self):
        cat = wptools.category('TEST')
        qobj = wptools.query.WPToolsQuery()
        self.assertEqual(cat._query('random', qobj),
                         ('https://en.wikipedia.org/w/api.php?'
                          'action=query&format=json&formatversion=2'
                          '&list=random&rnlimit=1&rnnamespace=14'))
        self.assertEqual(cat._query('category', qobj),
                         ('https://en.wikipedia.org/w/api.php?'
                          'action=query&format=json&formatversion=2'
                          '&list=categorymembers&cmlimit=500&cmtitle=TEST'))


class WPToolsCoreTestCase(unittest.TestCase):

    def test_core_load_missing(self):
        page = wptools.page('TEST')

        # empty response
        page.cache = {'query': {'query': 'QUERY', 'response': ''}}
        self.assertRaises(ValueError, page._load_response, 'query')

        # bad JSON
        page.cache = {'query': {'query': 'QUERY', 'response': '{TEST}'}}
        self.assertRaises(ValueError, page._load_response, 'query')

        # warnings
        page.cache = {'query':
                      {'query': 'QUERY',
                       'response': '{"warnings":{"query":{ "warnings":"TEST"}}}'}}
        page._load_response('query')

        # API error
        page.cache = {'parse':
                      {'query': 'QUERY',
                       'response': '{"error": {"code": "TEST"}}'}}
        self.assertRaises(LookupError, page._load_response, 'parse')

        # missing parse
        page.cache = {'parse': {'query': 'QUERY', 'response': '{}'}}
        self.assertRaises(LookupError, page._load_response, 'parse')

        # missing query
        page.cache = {'query':
                      {'query': 'QUERY',
                       'response': '{"query":{"pages":[{"missing": true}]}}'}}
        self.assertRaises(LookupError, page._load_response, 'query')

        # missing wikidata
        page.cache = {'wikidata':
                      {'query': 'QUERY',
                       'response': '{"entities":{"-1": {"missing": ""}}}'}}
        self.assertRaises(LookupError, page._load_response, 'wikidata')

        # show
        page.cache = {'query': query.cache}
        page.flags['skip'] = ['imageinfo']
        page._set_data('query')
        page.show()

    def test_core_info(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.info()), ['query'])
        self.assertEqual(page.info('query')['status'], 200)

    def test_core_query(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.query()), ['query'])

        qstr = page.query('query')
        start = 'https://en.wikipedia.org/w/api.php?action=query'
        end = '&titles=Douglas_Adams'
        self.assertTrue(qstr.startswith(start))
        self.assertTrue(qstr.endswith(end))

    def test_core_response(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.response()), ['query'])
        self.assertTrue('query' in page.response('query'))

    def test_core_safestr(self):
        self.assertEqual(wptools.core.safestr(None), None)
        self.assertEqual(wptools.core.safestr(1), '1')
        self.assertTrue(isinstance(wptools.core.safestr(u'ü'), str))


class WPToolsPageTestCase(unittest.TestCase):

    def test_core_init(self):
        page = wptools.page('TEST', skip='SKIP')
        self.assertEqual(page.flags,
                         {'silent': False, 'skip': 'SKIP', 'verbose': False})

        page = wptools.page('TEST', variant='VARIANT')
        self.assertEqual(page.params,
                         {'endpoint': '/page/', 'lang': 'en',
                          'title': 'TEST', 'variant': 'VARIANT'})

        page = wptools.page('TEST', wiki='WIKI')
        self.assertEqual(page.params,
                         {'endpoint': '/page/', 'lang': 'en',
                          'title': 'TEST', 'wiki': 'WIKI'})

    def test_page_init(self):
        page = wptools.page('TEST', silent=True)
        self.assertEqual(page.params,
                         {'endpoint': '/page/', 'lang': 'en', 'title': 'TEST'})
        self.assertEqual(page.flags, {'silent': True, 'verbose': False})

        page = wptools.page('TEST', endpoint='ENDPOINT', silent=True)
        self.assertEqual(page.params,
                         {'endpoint': 'ENDPOINT',
                          'lang': 'en', 'title': 'TEST'})

        page = wptools.page(pageid=123, silent=True)
        self.assertEqual(page.params,
                         {'endpoint': '/page/', 'lang': 'en',
                          'pageid': 123})

        page = wptools.page(wikibase='Q42', silent=True)
        self.assertEqual(page.params,
                         {'endpoint': '/page/', 'lang': 'en',
                          'wikibase': 'Q42'})

    def test_page_caching(self):
        page = wptools.page('TEST', silent=True)

        page.cache['parse'] = {'response': None}
        page.cache['query'] = {'response': None}
        page.cache['restbase'] = {'response': None}
        page.cache['wikidata'] = {'response': None}

        page.get_parse()
        page.get_query()
        page.get_restbase()
        page.get_wikidata()

        self.assertEqual(len(page.data), 0)

    def test_page_get_parse(self):
        page = wptools.page('test_get_parse', silent=True)

        page.cache['parse'] = parse.cache
        page._set_parse_data()

        data = page.data
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(len(data['infobox']), 15)
        self.assertEqual(len(data['links']), 2)
        self.assertEqual(len(data['parsetree']), 78594)
        self.assertEqual(len(data['wikitext']), 65836)
        self.assertEqual(str(data['title']), 'Douglas Adams')
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('satire' in data['infobox']['genre'])
        self.assertTrue(data['wikidata_url'].startswith('http'))
        self.assertEqual(str(data['image'][0]['file']),
                         'Douglas adams portrait cropped.jpg')

    def test_page_get_query(self):
        page = wptools.page('test_get_query', silent=True)

        page.cache['query'] = query.cache
        page._set_query_data()

        data = page.data
        self.assertEqual(data['description'], 'English writer and humorist')
        self.assertEqual(data['label'], 'Douglas Adams')
        self.assertEqual(data['length'], 60069)
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(data['views'], 1362)
        self.assertEqual(data['watchers'], 447)
        self.assertEqual(len(data['categories']), 29)
        self.assertEqual(len(data['files']), 12)
        self.assertEqual(len(data['image']), 2)
        self.assertEqual(len(data['languages']), 70)
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('page' in data['modified'])
        self.assertTrue(data['extext'].startswith('**Douglas'))
        self.assertTrue(data['extract'].startswith('<p><b>Douglas'))
        self.assertTrue(data['url'].endswith('Douglas_Adams'))
        self.assertTrue(data['url_raw'].endswith('_Adams?action=raw'))
        self.assertTrue(data['wikidata_url'].endswith('Q42'))
        self.assertTrue(wptools.utils.is_text(page.data['random']))

    def test_page_get_imageinfo(self):
        page = wptools.page('test_get_imageinfo', silent=True)

        page.data['image'] = [{
            'file': 'Douglas adams portrait cropped.jpg',
            'kind': 'test'}]
        page.cache['imageinfo'] = imageinfo.cache
        page._set_imageinfo_data()

        image = page.data['image'][0]
        self.assertTrue('/c/c0/' in image['url'])
        self.assertTrue('/commons.' in image['descriptionurl'])
        self.assertTrue(image['file'].startswith('File:'))
        self.assertEqual(image['height'], 386)
        self.assertEqual(image['size'], 32915)
        self.assertEqual(image['width'], 333)

    def test_page_get_restbase(self):
        page = wptools.page('TEST', endpoint='summary', silent=True)
        page.cache = {'restbase': rest_summary.cache}
        page._set_data('restbase')
        data = page.data
        self.assertEqual(data['pageid'], 8091)
        self.assertTrue(data['exhtml'].startswith("<p><b>Douglas"))
        self.assertTrue(data['exrest'].startswith("Douglas"))

    def test_page_get_wikidata(self):
        page = wptools.page('TEST', wikibase='WIKIBASE', silent=True)
        page.cache = {'wikidata': wikidata.cache}
        page.flags['skip'] = ['claims', 'imageinfo']
        page._set_data('wikidata')
        data = page.data
        self.assertEqual(data['wikibase'], 'Q42')
        self.assertEqual(len(data['properties']), 10)
        self.assertEqual(len(data['claims']), 11)
        self.assertEqual(len(data['wikidata']), 5)


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
        self.assertEqual(qobj.status,
                         'en.wikipedia.org (categorymembers) TEST')

        qstr = qobj.category(None, pageid=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('&list=categorymembers' in qstr)
        self.assertTrue('&cmpageid=123' in qstr)
        self.assertTrue('&cmtitle' not in qstr)
        self.assertEqual(qobj.status,
                         'en.wikipedia.org (categorymembers) 123')

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
        self.assertTrue('&titles=TEST' in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (query) TEST')

        qstr = qobj.query(None, pageids=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=query' in qstr)
        self.assertTrue('&pageids=123' in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (query) 123')

    def test_query_parse(self):
        qobj = wptools.query.WPToolsQuery()

        qstr = qobj.parse(title='TEST')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=parse' in qstr)
        self.assertTrue('&page=TEST' in qstr)
        self.assertEqual(qobj.status, 'en.wikipedia.org (parse) TEST')

        qstr = qobj.parse(None, pageid=123)
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('?action=parse' in qstr)
        self.assertTrue('&redirects' not in qstr)
        self.assertTrue('&pageid=123' in qstr)
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
        qstr = qobj.restbase(endpoint='/TEST/')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('/api/rest' in qstr)
        self.assertTrue(qstr.endswith('/TEST/'))
        self.assertEqual(qobj.status, 'en.wikipedia.org (restbase) /TEST/')

    def test_query_set_status(self):
        qobj = wptools.query.WPToolsQuery()

        qobj.set_status('TEST_ACTION', 'TEST_TARGET')
        self.assertEqual(qobj.status,
                         'en.wikipedia.org (TEST_ACTION) TEST_TARGET')
        qobj.set_status('--------------------------------------------------',
                        '--------------------------------------------------')
        self.assertEqual(len(qobj.status), 68)

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


class WPToolsRESTBaseTestCase(unittest.TestCase):

    def test_restbase_init(self):
        page = wptools.restbase()
        self.assertEqual(page.params, {'endpoint': '/page/', 'lang': 'en'})

        page = wptools.restbase('TEST', endpoint='html')
        self.assertEqual(page.params,
                         {'endpoint': '/page/html/TEST',
                          'lang': 'en',
                          'title': 'TEST'})

        page = wptools.restbase(endpoint='summary/TEST')
        self.assertEqual(page.params,
                         {'endpoint': '/page/summary/TEST',
                          'lang': 'en',
                          'title': 'TEST'})

        self.assertRaises(ValueError, wptools.restbase, endpoint='TEST')

        self.assertRaises(ValueError, wptools.restbase,
                          'TEST', endpoint='summary/TEST_TEST')

    def test_get_restbase_html(self):
        page = wptools.restbase(endpoint='html/TEST', silent=True)
        page.cache['restbase'] = rest_html.cache
        page._set_data('restbase')

        html = page.data['html']

        self.assertTrue(len(html), 264870)
        self.assertTrue(html.startswith('<!DOCTYPE'))
        self.assertTrue(html.endswith('</html>'))

    def test_get_restbase_lead(self):
        endpoint = 'mobile-sections-lead/TEST'
        page = wptools.restbase(endpoint=endpoint, silent=True)
        page.cache['restbase'] = rest_lead.cache
        page._set_data('restbase')

        params = page.params
        data = page.data

        self.assertEqual(data['description'], 'English writer and humorist')
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(len(data['lead']), 6577)
        self.assertEqual(params['title'], 'TEST')
        self.assertEqual(str(data['title']), 'Douglas_Adams')
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('page' in data['modified'])
        self.assertTrue(data['lead'].startswith('<span'))
        self.assertTrue(len(data['image']), 1)

    def test_get_restbase_summary(self):
        page = wptools.restbase(endpoint='summary/TEST', silent=True)
        page.cache['restbase'] = rest_summary.cache
        page._set_data('restbase')

        data = page.data

        self.assertEqual(len(data['image']), 2)
        self.assertEqual(data['description'], 'English writer and humorist')
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(str(data['title']), 'Douglas_Adams')
        self.assertEqual(len(data['exhtml']), 967)
        self.assertEqual(len(data['exrest']), 894)
        self.assertTrue(data['exhtml'].startswith('<p>'))
        self.assertTrue(data['exrest'].startswith('Douglas'))


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


class WPToolsWikidataTestCase(unittest.TestCase):

    def test_wikidata_init(self):
        page = wptools.wikidata('TEST', silent=True)
        self.assertEqual(page.params, {'lang': 'en', 'title': 'TEST'})

        page = wptools.wikidata(wikibase='Q42', silent=True)
        self.assertEqual(page.params, {'lang': 'en', 'wikibase': 'Q42'})

    def test_wikidata_get_claims(self):
        page = wptools.wikidata(silent=True)
        page.cache['wikidata'] = wikidata.cache
        page.cache['claims'] = claims.cache
        page._set_data('wikidata')
        page._set_data('claims')

        data = page.data

        self.assertEqual(len(data['claims']), 11)
        self.assertEqual(len(data['properties']), 10)
        self.assertEqual(str(data['what']), 'human')
        self.assertEqual(str(data['wikidata']['genre']),
                         'comic science fiction')
        self.assertTrue('Mostly Harmless' in data['wikidata']['work'])

    def test_wikidata_get_wikidata(self):
        page = wptools.wikidata(silent=True)
        page.cache['wikidata'] = wikidata.cache
        page._set_data('wikidata')

        data = page.data

        self.assertEqual(len(data['claims']), 11)
        self.assertEqual(len(data['properties']), 10)
        self.assertEqual(len(data['wikidata']), 10)
        self.assertEqual(data['description'], 'English writer and humorist')
        self.assertEqual(data['image'][0]['kind'], 'wikidata-image')
        self.assertEqual(data['label'], 'Douglas Adams')
        self.assertEqual(str(data['title']), 'Douglas_Adams')
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('wikidata' in data['modified'])
        self.assertTrue(data['wikidata_url'].endswith('Q42'))
        self.assertTrue(str(data['wikidata']['birth']).startswith('+1952'))

    def test_wikidata_disambig(self):
        """
        Ensure title param is set given only wikibase
        """
        page = wptools.wikidata(wikibase='TEST')
        page.cache = {'wikidata': wikidata.cache}
        page._set_wikidata()
        self.assertEqual(str(page.params['title']), 'Douglas_Adams')


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

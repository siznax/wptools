#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Basic tests for WPTools.
"""

import unittest
import wptools

from . import category
from . import category_cmcontinue
from . import disambiguation
from . import imageinfo
from . import labels_1
from . import labels_2
from . import labels_3
from . import labels_wanted
from . import parse
from . import parse_infobox
from . import parse_62
from . import parse_66
from . import parse_91
from . import parse_109
from . import query
from . import query_plcontinue
from . import querymore
from . import querymore_blcontinue
from . import random_query
from . import redirect
from . import rest_page
from . import rest_html
from . import rest_lead
from . import rest_summary
from . import siteinfo
from . import sitematrix
from . import siteviews
from . import wikidata
from . import wikidata_deleted
from . import wikidata_novalue_snak

SILENT_FLAG = True
SKIP_FLAG = ['imageinfo', 'labels']


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
        wptools.site
        wptools.wikidata


class WPToolsCategoryTestCase(unittest.TestCase):

    def test_category_init(self):
        self.assertRaises(ValueError, wptools.category, pageid='TEST')
        self.assertRaises(ValueError, wptools.category, 'TEST', pageid=123)

        cat = wptools.category('TEST')
        self.assertEqual(cat.params, {'lang': 'en', 'title': 'TEST'})
        self.assertTrue('requests' not in cat.data)

        try:
            cat = wptools.category(namespace='NOTINT')
            self.fail("failed to raise ValueError")
        except ValueError:
            pass

    def test_category_random(self):
        cat = wptools.category('TEST')
        cat.cache = {'random': random_query.cache}
        cat._set_data('random')
        self.assertEqual(cat.data['title'], 'RANDOM TEST TITLE')

    def test_category_caching(self):
        cat = wptools.category('TEST', silent=SILENT_FLAG)
        cat.cache['category'] = {'response': None}
        cat.get_members()
        self.assertEqual(len(cat.data), 0)
        self.assertTrue('requests' not in cat.data)

    def test_category_get_members(self):
        cat = wptools.category('TEST')
        cat.cache['category'] = category.cache
        cat._set_data('category')
        self.assertEqual(len(cat.data['members']), 68)
        self.assertEqual(len(cat.data['subcategories']), 24)
        self.assertTrue('requests' not in cat.data)

    def test_category_get_members_namespace(self):
        cat = wptools.category('TEST', namespace=0)
        cat.cache['category'] = category.cache
        cat._set_data('category')
        self.assertEqual(len(cat.data['members']), 68)
        self.assertTrue('requests' not in cat.data)

    def test_category_get_members_continue(self):
        cat = wptools.category('TEST')
        cat.cache['category'] = category_cmcontinue.cache
        cat._set_data('category')
        self.assertTrue('continue' in cat.data)
        self.assertEqual(len(cat.data['members']), 1)

        qry = cat._query('category', wptools.query.WPToolsQuery())
        self.assertTrue('&cmcontinue=page|' in qry)
        self.assertTrue(qry.endswith('|42525291'))

        cat.cache['category'] = category.cache
        cat._set_data('category')
        self.assertTrue('cmcontinue' not in cat.data)
        self.assertEqual(len(cat.data['members']), 69)

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
        self.assertTrue('requests' not in cat.data)


class WPToolsCoreTestCase(unittest.TestCase):

    def test_core_not_implemented(self):

        class TEST(wptools.core.WPTools):
            def __init__(self):
                pass

        page = TEST()

        try:
            page._query(None, None)
            self.fail("failed to raise NotImplementedError")
        except NotImplementedError:
            pass

        try:
            page._set_data(None)
            self.fail("failed to raise NotImplementedError")
        except NotImplementedError:
            pass

    def test_core_load_missing(self):
        page = wptools.page('TEST')

        # empty response
        page.cache = {'query': {'query': 'QUERY', 'response': ''}}
        self.assertRaises(ValueError, page._load_response, 'query')

        # bad JSON
        page.cache = {'query': {'query': 'QUERY', 'response': '{TEST}'}}
        self.assertRaises(ValueError, page._load_response, 'query')

        # warnings
        page.cache = {
            'query':
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
        page.flags['skip'] = SKIP_FLAG
        page._set_data('query')
        page.show()
        self.assertTrue('requests' not in page.data)

    def test_core_info(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.info()), ['query'])
        self.assertEqual(page.info('query')['status'], 200)
        self.assertTrue('requests' not in page.data)

    def test_core_query(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.query()), ['query'])
        qstr = page.query('query')
        start = 'https://en.wikipedia.org/w/api.php?action=query'
        end = '&titles=Douglas%20Adams'
        self.assertTrue(qstr.startswith(start))
        self.assertTrue(qstr.endswith(end))
        self.assertTrue('requests' not in page.data)

    def test_core_response(self):
        page = wptools.page('TEST')
        page.cache = {'query': query.cache}
        self.assertEqual(list(page.response()), ['query'])
        self.assertTrue('query' in page.response('query'))
        self.assertTrue('requests' not in page.data)

    def test_core_safestr(self):
        self.assertEqual(wptools.core.safestr(None), None)
        self.assertEqual(wptools.core.safestr(1), '1')
        self.assertTrue(isinstance(wptools.core.safestr(u'ü'), str))

    def test_core_get(self):
        page = wptools.page('TEST')
        try:
            page._get('TEST', False, None, 0)
            self.fail("failed to raise ValueError")
        except ValueError:
            pass

    def test_core_request_limit(self):
        page = wptools.page('TEST')
        page.REQUEST_LIMIT = 0
        page.data['requests'] = ['TEST']
        try:
            page._get('TEST', False, None, 0)
            self.fail("failed to raise StopIteration")
        except StopIteration:
            pass

    def test_core_show(self):
        page = wptools.page('TEST')
        page.data['TEST1'] = None
        page.data['TEST2'] = tuple(range(3))
        page.show()

    def test_core_get_random(self):
        # MAKE ACTUAL REQUEST! (for to maximize coverage)
        page = wptools.page('TEST')
        page._get('random', True, None, 0)
        self.assertTrue('random' in page.cache)
        self.assertTrue('pageid' in page.data)


class WPToolsPageTestCase(unittest.TestCase):

    def test_core_init(self):
        page = wptools.page('TEST', skip='SKIP')
        self.assertEqual(page.flags,
                         {'silent': False, 'skip': 'SKIP', 'verbose': False})

        page = wptools.page('TEST', variant='VARIANT')
        self.assertEqual(page.params,
                         {'lang': 'en', 'title': 'TEST', 'variant': 'VARIANT'})

        page = wptools.page('TEST', wiki='WIKI')
        self.assertEqual(page.params,
                         {'lang': 'en', 'title': 'TEST', 'wiki': 'WIKI'})

    def test_page_init(self):
        page = wptools.page('TEST', silent=True)
        self.assertEqual(page.params, {'lang': 'en', 'title': 'TEST'})
        self.assertEqual(page.flags, {'silent': True, 'verbose': False})

        page = wptools.page(pageid=123, silent=SILENT_FLAG)
        self.assertEqual(page.params, {'lang': 'en', 'pageid': 123})

        page = wptools.page(wikibase='Q42', silent=SILENT_FLAG)
        self.assertEqual(page.params, {'lang': 'en', 'wikibase': 'Q42'})

        self.assertTrue('requests' not in page.data)

    def test_page_caching(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)

        page.cache['parse'] = {'response': None}
        page.cache['query'] = {'response': None}
        page.cache['restbase'] = {'response': None}
        page.cache['wikidata'] = {'response': None}

        page.get_parse()
        page.get_query()
        page.get_restbase()
        page.get_wikidata()

        self.assertEqual(len(page.data), 0)
        self.assertTrue('requests' not in page.data)

    def test_page_query(self):
        page = wptools.page('TEST')
        qobj = wptools.query.WPToolsQuery()

        qstr = page._query('random', qobj)
        self.assertTrue('list=random' in qstr)

        qstr = page._query('query', qobj)
        self.assertTrue('action=query' in qstr)
        self.assertTrue('pageprops' in qstr)

        qstr = page._query('querymore', qobj)
        self.assertTrue('action=query' in qstr)
        self.assertTrue('&bllimit=500' in qstr)
        self.assertTrue('&cllimit=500' in qstr)
        self.assertTrue('&imlimit=500' in qstr)
        self.assertTrue('&lllimit=500&' in qstr)
        self.assertTrue('&pclimit=500' in qstr)

        qstr = page._query('parse', qobj)
        self.assertTrue('action=parse' in qstr)
        self.assertTrue('parsetree' in qstr)

        page.data['entities'] = ['Q1', 'Q2', 'Q3']
        qstr = page._query('labels', qobj)
        self.assertTrue('action=wbgetentities' in qstr)
        self.assertTrue('ids=Q1|Q2|Q3' in qstr)

        qstr = page._query('wikidata', qobj)
        self.assertTrue('action=wbgetentities' in qstr)

        page.params.update({'rest_endpoint': '/page/summary/'})
        qstr = page._query('restbase', qobj)
        self.assertTrue('api/rest' in qstr)

        self.assertTrue('requests' not in page.data)

    def test_page_get(self):
        """
        test page.get() without making any requests, is for coverage
        """
        wptools.request.WPToolsRequest.DISABLED = True
        skip = ['parse', 'query', 'restbase', 'wikiata']

        page = wptools.page('TEST', skip=skip)
        page.get()

        page = wptools.page('TEST', wikibase='TEST', skip=skip)
        page.get()

    def test_page_get_parse(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse.cache}
        page._set_data('parse')
        data = page.data
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(len(data['infobox']), 13)
        self.assertEqual(len(data['iwlinks']), 2)
        self.assertEqual(len(data['parsetree']), 78594)
        self.assertEqual(len(data['wikitext']), 65836)
        self.assertEqual(str(data['title']), 'Douglas Adams')
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('satire' in data['infobox']['genre'])
        self.assertTrue(data['wikidata_url'].startswith('http'))
        self.assertEqual(str(data['image'][0]['file']),
                         'File:Douglas adams portrait cropped.jpg')

        self.assertTrue('requests' not in page.data)


    def test_page_get_parse_infobox(self):
        """
        Ensure cover images are captured from infobox
        """
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse_infobox.cache}
        page._set_data('parse')
        data = page.data
        self.assertEqual(len(data['infobox']), 16)
        self.assertEqual(len(page.images()), 1)
        self.assertEqual(page.images('kind'),
                         [{'kind': 'parse-cover'}])
        self.assertEqual(page.images()[0]['file'],
                         u'File:John Coltrane - Blue Train.jpg')
        self.assertTrue('requests' not in page.data)


    def test_page_get_parse_62(self):
        """
        Get infobox data with list values. Issue #62
        """
        page = wptools.page('Lewisit', lang='de',
                            skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse_62.cache}
        page._set_data('parse')
        infobox = page.data['infobox']
        self.assertEqual(len(infobox['Dichte'].split('*')), 3)
        self.assertEqual(len(infobox['Schmelzpunkt'].split('*')), 3)
        self.assertEqual(len(infobox['Siedepunkt'].split('*')), 3)
        self.assertEqual(len(infobox['Brechungsindex'].split('*')), 3)
        self.assertEqual(len(infobox['ToxDaten'].split('*')), 3)
        self.assertEqual(len(infobox['Andere Namen'].split('*')), 6)
        self.assertTrue('requests' not in page.data)

    def test_page_get_parse_66(self):
        """
        Get infobox data with sub-elements. Issue #66
        """
        page = wptools.page("ONE OK ROCK", lang='ja',
                            skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse_66.cache}
        page._set_data('parse')
        infobox = page.data['infobox']
        self.assertEqual(len(infobox['Genre'].split('<br')), 8)
        self.assertTrue('requests' not in page.data)

    def test_page_get_parse_91(self):
        """
        Get infobox data with unusual wikitext syntax
        """
        page = wptools.page('Okapi', lang='fr',
                            skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse_91.cache}
        page._set_data('parse')
        infobox = page.data['infobox']
        self.assertEqual(len(infobox['boxes']), 13)
        self.assertTrue(u'Taxobox début' in page.data['infobox']['boxes'][0])
        self.assertEqual(list(infobox['boxes'][9].keys()), ['Taxobox UICN'])
        self.assertTrue('requests' not in page.data)

    def test_page_get_parse_109(self):
        """
        Get infobox data with mix of links, templates, tail text
        """
        page = wptools.page('Orléans-cléry', lang='fr',
                            skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse_109.cache}
        page._set_data('parse')
        infobox = page.data['infobox']
        self.assertTrue('[[cabernet franc]]' in infobox[u'cépages'])
        self.assertEqual(infobox[u'volproduction'],
                         u'{{unité|848|hectolitres}} en [[2009]]')
        self.assertEqual(infobox[u'densité'],
                         u'minimum de {{unité|5000|pieds}} par hectare')
        self.assertTrue('requests' not in page.data)

    def test_page_get_parse_boxterm(self):
        page = wptools.page('TEST', boxterm='TEST',
                            skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'parse': parse.cache}
        page._set_data('parse')
        self.assertTrue(page.data['infobox'] is None)
        self.assertTrue('requests' not in page.data)

    def test_page_get_query(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'query': query.cache}
        page._set_data('query')
        data = page.data
        self.assertEqual(data['description'], u'author')
        self.assertEqual(data['label'], 'Douglas Adams')
        self.assertEqual(data['length'], 62123)
        self.assertEqual(data['pageid'], 8091)
        self.assertEqual(data['watchers'], 460)
        self.assertEqual(len(data['aliases']), 3)
        self.assertEqual(len(data['assessments']), 10)
        self.assertEqual(len(data['image']), 2)
        self.assertEqual(len(data['links']), 384)
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('page' in data['modified'])
        self.assertTrue(data['extext'].startswith('**Douglas'))
        self.assertTrue(data['extract'].startswith('<p><b>Douglas'))
        self.assertTrue(data['url'].endswith('Douglas_Adams'))
        self.assertTrue(data['url_raw'].endswith('_Adams?action=raw'))
        self.assertTrue(data['wikidata_url'].endswith('Q42'))
        self.assertTrue(wptools.utils.is_text(page.data['random']))

        self.assertTrue('requests' not in page.data)

    def test_page_get_more(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)
        page.cache = {'querymore': querymore.cache}
        page.get_more()
        page._set_data('querymore')
        self.assertEqual(len(page.data['backlinks']), 500)
        self.assertTrue(len(page.data['categories']), 29)
        self.assertTrue(len(page.data['files']), 12)
        self.assertTrue(len(page.data['languages']), 70)
        self.assertTrue(page.data['contributors'], 1317)
        self.assertTrue(page.data['views'], 1398)

        self.assertTrue('requests' not in page.data)

    def test_page_get_query_continue(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache['query'] = query.cache
        page._set_data('query')
        self.assertEqual(len(page.data['links']), 384)

        page.cache = {'query': query_plcontinue.cache}
        page._set_data('query')
        self.assertTrue('continue' in page.data)
        self.assertEqual(page.data['continue'],
                         {'plcontinue': u'144146|0|Perl_Data_Language'})
        self.assertEqual(len(page.data['links']), 385)

        qry = page._query('query', wptools.query.WPToolsQuery())
        self.assertTrue(qry.endswith('&plcontinue=144146|0|Perl_Data_Language'))

    def test_page_get_more_continue(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache['querymore'] = querymore.cache
        page._set_data('querymore')
        self.assertEqual(len(page.data['backlinks']), 500)
        self.assertEqual(page.data['continue'], {'blcontinue': u'4|2028922'})

        page.cache = {'querymore': querymore_blcontinue.cache}
        page._set_data('querymore')
        self.assertTrue('continue' in page.data)
        self.assertEqual(len(page.data['backlinks']), 501)

        qry = page._query('querymore', wptools.query.WPToolsQuery())
        self.assertTrue(qry.endswith('&blcontinue=0|2062757'))

    def test_page_get_imageinfo(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)

        self.assertRaises(ValueError, page.get_imageinfo)

        page.cache = {'imageinfo': imageinfo.cache}
        page.data['image'] = [{'kind': 'parse-image',
                               'file': 'Douglas adams portrait cropped.jpg'}]

        page._normalize_images()
        query = page._query('imageinfo', wptools.query.WPToolsQuery())
        self.assertTrue('File%3ADouglas' in query)

        page._set_data('imageinfo')
        image = page.data['image'][0]
        self.assertTrue('/c/c0/' in image['url'])
        self.assertTrue('/commons.' in image['descriptionurl'])
        self.assertTrue(image['file'].startswith('File:'))
        self.assertEqual(image['height'], 386)
        self.assertEqual(image['size'], 32915)
        self.assertEqual(image['width'], 333)

        self.assertTrue('requests' not in page.data)

    def test_page_get_random(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'random': query.cache}
        page._set_data('random')
        page.get_random()
        self.assertEqual(page.data['pageid'], 7614573)
        self.assertEqual(page.data['title'], u'Aidenbachstraße (Munich U-Bahn)')

        self.assertTrue('requests' not in page.data)

    def test_page_get_restbase(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)
        page.params.update({'rest_endpoint': 'summary'})
        page.cache = {'restbase': rest_summary.cache}
        page._set_data('restbase')
        data = page.data
        self.assertEqual(data['pageid'], 8091)
        self.assertTrue(data['exhtml'].startswith("<p><b>Douglas"))
        self.assertTrue(data['exrest'].startswith("Douglas"))

        self.assertTrue('requests' not in page.data)

    def test_page_get_wikidata(self):
        page = wptools.page('TEST',
                            wikibase='WIKIBASE',
                            skip=SKIP_FLAG,
                            silent=SILENT_FLAG)

        page.cache = {'wikidata': wikidata.cache}
        page._set_data('wikidata')

        page.cache['labels'] = labels_1.cache
        page._set_data('labels')

        page.cache['labels'] = labels_2.cache
        page._set_data('labels')

        page.cache['labels'] = labels_3.cache
        page._set_data('labels')

        page._post_labels_updates()

        page.cache['imageinfo'] = imageinfo.cache
        page._set_data('imageinfo')

        data = page.data
        self.assertEqual(data['wikibase'], 'Q42')
        self.assertEqual(data['image'][0]['kind'], 'wikidata-image')
        self.assertEqual(len(data['claims']), 102)
        self.assertEqual(len(data['labels']), 147)
        self.assertEqual(len(data['wikidata']), 102)

        self.assertTrue('requests' not in page.data)

    def test_page_pageimage(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)
        page.pageimage()
        page.data['image'] = [{'kind': 'TEST'}, {'kind': 'TESTMORE'}]
        page.pageimage()
        page.pageimage('MORE')

        self.assertTrue('requests' not in page.data)

    def test_page_get_disambiguation(self):
        page = wptools.page('TEST', silent=SILENT_FLAG)
        page.cache = {'query': disambiguation.cache}
        page._set_data('query')
        data = page.data
        self.assertEqual(data['disambiguation'], 10)
        self.assertEqual(len(data['links']), 10)

        self.assertTrue('requests' not in page.data)

    def test_page_get_redirect(self):
        page = wptools.page('TEST', skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'query': redirect.cache}
        page._set_data('query')
        data = page.data
        self.assertEqual(data['redirected'][0]['from'], u'Adams, Douglas')
        self.assertEqual(len(data['redirects']), 12)

        self.assertTrue('requests' not in page.data)


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

    def test_query_init_endpoint(self):
        qobj = wptools.query.WPToolsQuery(endpoint='ENDPOINT')
        self.assertEqual(qobj.endpoint, 'ENDPOINT')
        self.assertEqual(qobj.uri, 'https://en.wikipedia.org')
        self.assertTrue('.orgENDPOINT?' in qobj.category('CAT'))
        self.assertTrue('.orgENDPOINT?' in qobj.labels(['QID']))
        self.assertTrue('.orgENDPOINT?' in qobj.imageinfo(['FILE']))
        self.assertTrue('.orgENDPOINT?' in qobj.parse('TITLE'))
        self.assertTrue('.orgENDPOINT?' in qobj.query('TITLE'))
        self.assertTrue('.orgENDPOINT?' in qobj.querymore('TITLE'))
        self.assertTrue('.orgENDPOINT?' in qobj.site('siteinfo'))
        self.assertTrue('.orgENDPOINT?' in qobj.wikidata('TITLE'))

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

    def test_query_labels(self):
        qobj = wptools.query.WPToolsQuery()
        qstr = qobj.labels(qids=['Q1', 'Q2', 'Q3'])
        self.assertTrue(qstr.startswith('https://www.wikidata.org'))
        self.assertTrue('?action=wbgetentities' in qstr)
        self.assertTrue('&ids=Q1|Q2|Q3' in qstr)
        self.assertEqual(qobj.status, 'www.wikidata.org (labels) Q1|Q2|Q3')

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
        qstr = qobj.restbase(endpoint='/TEST/', title='TEST')
        self.assertTrue(qstr.startswith('https://en.wikipedia.org'))
        self.assertTrue('/api/rest' in qstr)
        self.assertTrue(qstr.endswith('/TEST/TEST'))
        self.assertEqual(qobj.status, 'en.wikipedia.org (restbase) /TEST/TEST')

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
        self.assertEqual(page.params, {'lang': 'en'})
        self.assertTrue('requests' not in page.data)

    def test_get_restbase_page(self):
        page = wptools.restbase('/page/', silent=SILENT_FLAG)
        page.cache['restbase'] = rest_page.cache
        page._set_data('restbase')
        self.assertTrue('requests' not in page.data)

    def test_get_restbase_html(self):
        page = wptools.restbase('TEST', silent=SILENT_FLAG)
        page.cache['restbase'] = rest_html.cache
        page._set_data('restbase')

        html = page.data['html']

        self.assertTrue(len(html), 264870)
        self.assertTrue(html.startswith('<!DOCTYPE'))
        self.assertTrue(html.endswith('</html>'))

        self.assertTrue('requests' not in page.data)

    def test_get_restbase_lead(self):
        page = wptools.restbase('TEST', silent=SILENT_FLAG)
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

        self.assertTrue('requests' not in page.data)

    def test_get_restbase_summary(self):
        page = wptools.restbase('TEST', silent=SILENT_FLAG)
        page.params.update({'rest_endpoint': '/page/summary/'})
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

        self.assertTrue('requests' not in page.data)


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
        self.assertEqual(info.get('content-type'), None)
        self.assertTrue('wptools' in info.get('user-agent'))

    def test_request_curl_setup(self):
        req = wptools.request.WPToolsRequest(verbose=True)
        req.curl_setup(proxy='TEST_PROXY', timeout=666)
        info = req.cobj.getinfo(wptools.request.pycurl.EFFECTIVE_URL)
        self.assertEqual(info, '')
        info = req.cobj.getinfo(wptools.request.pycurl.RESPONSE_CODE)
        self.assertEqual(info, 0)

    def test_request_curl_proxy_setup(self):
        req = wptools.request.WPToolsRequest(verbose=True)
        test_proxy = {
            'PROXY': 'TEST_PROXY',
            'PORT': 0,
            'USERPWD': 'TEST_USER:PWD'
        }
        req.curl_setup(proxy=test_proxy)

    def test_request_user_agent(self):
        agent = wptools.request.user_agent()
        self.assertTrue(agent.startswith('wptools'))
        self.assertTrue('(https://github.com/siznax/wptools)' in agent)

    def test_request_get(self):
        req = wptools.request.WPToolsRequest()
        try:
            req.get('TEST_URL', 'TEST_STATUS')
            self.fail("failed to raise pycurl error")
        except:
            pass


class WPToolsSiteTestCase(unittest.TestCase):

    def test_site_init(self):
        site = wptools.site()
        self.assertEqual(site.params, {'lang': 'en'})
        self.assertEqual(site.flags, {'silent': False, 'verbose': False})

    def test_site_query(self):
        site = wptools.site()

        qobj = wptools.query.WPToolsQuery(wiki='commons.wikimedia.org')
        query = site._query('sitematrix', qobj)
        self.assertTrue(query.startswith('https://commons.wikimedia.org'))

        qobj = wptools.query.WPToolsQuery()
        query = site._query('siteinfo', qobj)
        self.assertTrue('&meta=siteinfo|siteviews' in query)
        self.assertTrue('&siprop=general|statistics' in query)
        self.assertTrue('&list=mostviewed&pvimlimit=max' in query)
        query = site._query('sitevisitors', qobj)
        self.assertTrue('&meta=siteviews&pvismetric=uniques' in query)

        self.assertTrue('requests' not in site.data)

    def test_site_get_sites(self):
        site = wptools.site(silent=SILENT_FLAG)
        site.cache = {'sitematrix': sitematrix.cache}

        site.get_sites()
        site._set_data('sitematrix')
        self.assertEqual(len(site.data['sites']), 741)
        self.assertTrue(site.data.get('random') is not None)

        site.get_sites(domain='wikipedia.org')
        site._set_data('sitematrix')
        self.assertEqual(len(site.data['sites']), 290)

        # filter by domain
        site.params.update({'domain': 'wikipedia.org'})
        site._set_data('sitematrix')
        data = site.data
        self.assertEqual(len(data['sites']), 290)

        self.assertTrue('requests' not in site.data)

    def test_site_get_siteinfo(self):
        site = wptools.site(silent=SILENT_FLAG)
        site.cache = {'siteinfo': siteinfo.cache,
                      'sitevisitors': siteviews.cache}
        site.get_info(wiki='en.wikipedia.org')
        site._set_data('siteinfo')
        site._set_data('sitevisitors')
        data = site.data
        self.assertEqual(data['activeusers'], 126428)
        self.assertEqual(data['admins'], 1248)
        self.assertEqual(data['articles'], 5478623)
        self.assertEqual(data['edits'], 910438071)
        self.assertEqual(data['images'], 854622)
        self.assertEqual(len(data['info']), 49)
        self.assertEqual(data['pages'], 43112467)
        self.assertEqual(data['site'], 'enwiki')
        self.assertEqual(data['users'], 31786628)

        self.assertEqual(len(data['mostviewed']), 478)
        self.assertEqual(data['siteviews'], 233991363)
        self.assertEqual(data['visitors'], 63079969)

        site.top()
        site.top(wiki='en.wikipedia.org', limit=10)

        self.assertTrue('requests' not in site.data)


class WPToolsWikidataTestCase(unittest.TestCase):

    def test_wikidata_init(self):
        page = wptools.wikidata('TEST', silent=SILENT_FLAG)
        self.assertEqual(page.params, {'lang': 'en', 'title': 'TEST'})

        page = wptools.wikidata(wikibase='Q42', silent=SILENT_FLAG)
        self.assertEqual(page.params, {'lang': 'en', 'wikibase': 'Q42'})

        page = wptools.wikidata()
        try:
            page.get_wikidata()
            self.fail("failed to raise LookupError")
        except LookupError:
            pass

        try:
            page.wanted_labels('TEST')
            self.fail("failed to raise ValueError")
        except ValueError:
            pass

        self.assertTrue('requests' not in page.data)

    def test_wikidata_get_labels(self):
        page = wptools.wikidata(skip=SKIP_FLAG,
                                silent=SILENT_FLAG)
        page.cache = {'labels':  labels_1.cache,
                      'wikidata': wikidata.cache}

        page._set_data('wikidata')
        page._set_data('labels')
        page._post_labels_updates()

        data = page.data
        self.assertEqual(len(data['claims']), 102)
        self.assertEqual(len(data['labels']), 50)
        self.assertEqual(len(data['wikidata']), 27)

        page.get_labels()  # No entities found

        self.assertTrue('requests' not in page.data)

    def test_wikidata_get_wikidata(self):
        page = wptools.wikidata(skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache = {'wikidata': wikidata.cache}
        page._set_data('wikidata')

        page.cache['labels'] = labels_1.cache
        page._set_data('labels')
        page.cache['labels'] = labels_2.cache
        page._set_data('labels')
        page.cache['labels'] = labels_3.cache
        page._set_data('labels')

        page._post_labels_updates()

        page.cache['imageinfo'] = imageinfo.cache
        page._set_data('imageinfo')

        self.assertTrue('requests' not in page.data)

        data = page.data
        self.assertEqual(data['description'], u'English writer and humorist')
        self.assertEqual(data['label'], 'Douglas Adams')
        self.assertEqual(len(data['claims']), 102)
        self.assertEqual(len(data['labels']), 147)
        self.assertEqual(len(data['wikidata']), 102)
        self.assertEqual(str(data['title']), 'Douglas_Adams')
        self.assertEqual(str(data['what']), 'human')
        self.assertEqual(str(data['wikibase']), 'Q42')
        self.assertTrue('wikidata' in data['modified'])
        self.assertTrue(data['wikidata_url'].endswith('Q42'))

        self.assertTrue('requests' not in page.data)

    def test_wikidata_disambig(self):
        """
        Ensure title param is set given only wikibase
        """
        page = wptools.wikidata(skip=SKIP_FLAG, wikibase='TEST')
        page.cache = {'wikidata': wikidata.cache}
        page._set_wikidata()
        self.assertEqual(str(page.params['title']), 'Douglas_Adams')

        self.assertTrue('requests' not in page.data)

    def test_wikidata_get_wanted(self):
        page = wptools.wikidata('TEST', skip=SKIP_FLAG)
        page.wanted_labels(['P31', 'Q5'])

        page.cache = {'wikidata': wikidata.cache}
        page._set_data('wikidata')

        page.cache['labels'] = labels_wanted.cache
        page._set_data('labels')

        page._post_labels_updates()

        data = page.data
        self.assertEqual(len(data['wikidata']), 1)
        self.assertTrue('instance of (P31)' in data['wikidata'])

    def test_wikidata_query(self):
        page = wptools.wikidata('TEST')
        qobj = wptools.query.WPToolsQuery()

        page.data['entities'] = ['TEST']
        qry = page._query('labels', qobj)
        self.assertTrue(qry.endswith('TEST'))

        qry = page._query('wikidata', qobj)
        self.assertTrue(qry.endswith('TEST'))

    def test_wikidata_image(self):
        """
        ensure we don't add wikidata-image if file info extant
        """
        page = wptools.wikidata(skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache = {'wikidata': wikidata.cache}
        page._set_data('wikidata')

        page.data['image'] = [
            {'file': 'Douglas adams portrait cropped.jpg'}]

        page.cache['labels'] = labels_2.cache  # P18 in here
        page._set_data('labels')
        page._post_labels_updates()

        self.assertTrue('requests' not in page.data)

        data = page.data
        self.assertTrue(len(data['image']), 1)
        self.assertTrue('wikidata-image' not in data['image'])

    def test_wikidata_missing(self):
        page = wptools.wikidata(skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache = {'wikidata': wikidata.cache}
        page._set_data('wikidata')

        del page.data['claims']['P31']

        page.cache['labels'] = labels_wanted.cache
        page._set_data('labels')
        page._post_labels_updates()

        self.assertTrue('requests' not in page.data)

        data = page.data
        self.assertTrue('what' not in data['wikidata'])

    def test_wikidata_deleted(self):
        page = wptools.wikidata(skip=SKIP_FLAG, silent=SILENT_FLAG)

        page.cache = {'wikidata': wikidata_deleted.cache}

        try:
            page._set_data('wikidata')
            self.fail("failed to raise LookupError")
        except LookupError:
            pass

        self.assertTrue('requests' not in page.data)

    def test_wikidata_no_value_snak(self):
        page = wptools.wikidata(skip=SKIP_FLAG, silent=SILENT_FLAG)
        page.cache = {'wikidata': wikidata_novalue_snak.cache}
        page._set_data('wikidata')
        self.assertEqual(len(page.data['claims']), 2)


class WPToolsToolTestCase(unittest.TestCase):

    def test_wptool(self):
        from scripts.wptool import main
        from collections import namedtuple
        args = namedtuple('Args', ['H', 'l', 'n', 'q', 's', 't', 'v', 'w'])
        cli = {'H': False, 'l': 'en', 'n': False, 'q': True, 's': True,
               't': '', 'v': False, 'w': ''}
        main(args(**cli))


if __name__ == '__main__':
    unittest.main()

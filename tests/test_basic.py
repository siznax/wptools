#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Basic tests for WPTools.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import wptools


class WPToolsTestCase(unittest.TestCase):

    def test_entry_points(self):

        wptools.extract
        wptools.fetch
        wptools.utils


class ExtractTestCase(unittest.TestCase):

    def test_qry_wikitext(self):
        from wptools.extract import qry_wikitext
        # wptools.fetch.get_wikitext('Aardvark')
        d = r'{"parse":{"title":"Aardvark","pageid":680,"wikitext":{"*":"{{speciesbox\n| genus = Orycteropus\n}}"}}}'
        ans = qry_wikitext(d)
        self.assertEqual(ans, "{{speciesbox\n| genus = Orycteropus\n}}")

    def test_qry_infobox(self):
        from wptools.extract import qry_infobox
        # wptools.fetch.get_parsetree('Aardvark')
        p = "<template><title>speciesbox</title><part><name> genus </name><equals>=</equals><value> Orycteropus</value></part></template>"
        d = r'{"parse":{"title":"Aardvark","pageid":680,"parsetree":{"*":"' + p + '"}}}'
        ans = qry_infobox(d, _format='dict')['genus']
        self.assertEqual(ans, 'Orycteropus')

    def test_qry_parsetree(self):
        from wptools.extract import qry_parsetree
        # wptools.fetch.get_parsetree('Aardvark')
        d = r'{"parse":{"title":"Aardvark","pageid":680,"parsetree":{"*":"<root/>"}}}'
        self.assertEqual(qry_parsetree(d), '<root/>')

    def test_qry_text(self):
        from wptools.extract import qry_text
        # wptools.fetch.get_html('Aardvark', lead=True)
        h = '<p>The <b>aardvark</b>'
        d = r'{"parse":{"title":"Aardvark","pageid":680,"text":{"*":"' + h + '"}}}'
        ans = qry_text(d, lead=True)
        self.assertEqual(ans, 'The **aardvark**')

    def test_qry_html(self):
        from wptools.extract import qry_html
        # wptools.fetch.get_html('Aardvark', lead=True)
        d = r'{"parse":{"title":"Aardvark","pageid":680,"text":{"*":"<html>"}}}'
        self.assertEqual(qry_html(d), '<html>')

    def test_html_disambig(self):
        from wptools.extract import qry_html
        d = r'{"parse":{"title":"Misfits","pageid":151422,"text":{"*":"<p><b>Misfits</b> may refer to:</p>"}}}'
        self.assertEqual(qry_html(d), 'DISAMBIGUATION Misfits')

    def test_no_templates(self):  # Active galactic nucleus
        from wptools.extract import html_lead
        self.assertEqual(html_lead("<p>lead</p>"), "<p>lead</p>")

    def test_cite_error(self):  # 14th Dalai Lama (15 Oct 2015)
        from wptools.extract import plain_text_cleanup
        self.assertEqual(plain_text_cleanup("lead\nCite error"), "lead")


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

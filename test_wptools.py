#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Tests for WPTools."""

import unittest
import wptools


class WPToolsTestCase(unittest.TestCase):

    def test_entry_points(self):

        wptools.extract
        wptools.fetch
        wptools.utils


class ExtractTestCase(unittest.TestCase):

    def test_html_lead(self):
        # Ag Qoyunlu
        # Dhyan Chand
        # Einstein
        from wptools.extract import html_lead
        data = ("<p>1</p><table/>"
                "<p>2</p>"
                "<p>3</p><ol/>")
        ans = html_lead(data)
        self.assertEqual(ans, "<p>1</p>\n<p>2</p>\n<p>3</p>")

    def test_no_templates(self):
        # Active galactic nucleus
        from wptools.extract import html_lead
        ans = html_lead("<p>lead</p>")
        self.assertEqual(ans, "<p>lead</p>")

    def test_cite_error(self):
        # 14th Dalai Lama (15 Oct 2015)
        from wptools.extract import plain_text_cleanup
        data = ("lead\nCite error")
        ans = plain_text_cleanup(data)
        self.assertEqual(ans, "lead")


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

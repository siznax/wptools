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
        from wptools.extract import html_lead
        data = ("<div/>"
                "<p>lead</p><div>lead</div>"
                "<ol/><table/>")
        ans = html_lead(data)
        self.assertEqual(ans, "<p>lead</p>\n<div>lead</div>")

    def test_html_lead_no_templates(self):
        # Active galactic nucleus returns None
        from wptools.extract import html_lead
        ans = html_lead("<p>lead</p>")
        self.assertEqual(ans, "<p>lead</p>")

    # transient? Active galactic nucleus
    #     lxml.etree.XMLSyntaxError: line 267: Tag bdi invalid


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

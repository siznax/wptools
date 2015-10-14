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
        data = ("<div>templates</div>"
                "<p>lead</p><div>lead</div>"
                "<ol>references</ol>")
        ans = html_lead(data)
        self.assertEqual(ans, "<p>lead</p>\n<div>lead</div>")


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

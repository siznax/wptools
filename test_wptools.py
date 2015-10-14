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
        data = ("<div><table><td><p>no</p></td></table></div>"
                "<p>yes</p>"
                "<div><p>no</p></div>")
        ans = html_lead(data)
        self.assertEqual(ans, "<p>yes</p>")


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

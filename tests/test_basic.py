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

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Basic tests for WPTools.
"""

import unittest
import wptools


class WPToolsTestCase(unittest.TestCase):

    def test_entry_points(self):

        wptools.core
        wptools.fetch
        wptools.utils

        from scripts.wptool import main


class WPToolsCoreTestCase(unittest.TestCase):

    def test(self):
        pass


class WPtoolsFetchTestCase(unittest.TestCase):

    def test(self):
        pass


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

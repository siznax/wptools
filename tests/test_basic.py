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

        wptools.core
        wptools.fetch
        wptools.utils

        from scripts.wptool import main


class CoreTestCase(unittest.TestCase):

    def test(self):
        pass


class FetchTestCase(unittest.TestCase):

    def test(self):
        pass


class UtilsTestCase(unittest.TestCase):

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()

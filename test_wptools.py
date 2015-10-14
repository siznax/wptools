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

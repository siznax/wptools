#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import unittest
import wptools

# langs that exposed an issue
langs = ['es', 'fr', 'hi', 'ja', 'zh', 'ru']

# titles that exposed an issue
titles = [
    "Flannery O'Connor",
    "Jeanne d'Arc",
    'Abe Lincoln',
    'Benjamin Franklin',
    'Borges',
    'Bruce Lee',
    'Buddha',
    'Cervantes',
    'Denis Diderot',
    'Ella Fitzgerald',
    'Encyclopédie',
    'Fela Kuti',
    'François-Marie Arouet'
    'Frida Kahlo',
    'Harriet Tubman',
    'Malala Yousafzai',
    'Malcolm X',
    'Monkey King',
    'Napoleon',
    'Paris',
    'Quaternion',
    'Shakespeare',
    'Stephen Fry',
    'Анна Ахматова',
    'Анто́н Па́влович Че́хов',
    'Фёдор Миха́йлович Достое́вский',
    '武俠',
    '浮世絵',
    '漢語',
    '相撲',
    '穐吉敏子',
]


class WPToolTest(unittest.TestCase):
    """
    WPTOOL TESTS
    """

    def test_wptool(self):
        from scripts.wptool import main as wptool
        wptool()


class WPToolsBadRequestTest(unittest.TestCase):
    """
    BAD API REQUEST TESTS
    """

    def test_redirect(self):
        """
        Get redirected
        """
        wptools.page(title='Abe Lincoln').get()

    def test_missing(self):
        """
        Get missing title
        """
        wptools.page(title='ƀļēřğ').get()

    def test_uknown_lang(self):
        """
        Mediawiki site function not supported
        """
        # "jp" Wikinews (unknown language code)
        g = wptools.page(wiki='jp.wikinews.org').get()
        assert g.fatal is not None


class WPToolsRandomTest(unittest.TestCase):
    """
    RANDOM TESTS
    """

    def test_random(self):
        """
        Get random everything
        """
        wptools.page().get()

    def test_random_lang(self):
        """
        Get everything from random item in another language
        """
        wptools.page(lang=random.choice(langs)).get()

    def test_random_wiki(self):
        """
        Get random item from another wiki
        """
        wptools.page(wiki='en.wikinews.org').get()


class WPToolsSelectedTest(unittest.TestCase):
    """
    SELECTED TESTS
    """

    def test_multibyte(self):
        """
        Get everything multibyte request
        """
        wptools.page('托爾金', lang='zh')  # 托爾金 (zh) Tolkien

    def test_wikibase(self):
        """
        Get everything wikibase only
        """
        wptools.page(wikibase='Q43303').get()  # Q43303=Malcolm_X

    def test_selected(self):
        """
        Get selected title
        """
        wptools.page(title=random.choice(titles)).get()

    def test_mixed_lang(self):
        """
        Get everything mixed languages
        """
        g = wptools.page(title='Abraham Lincoln', lang='zh').get()
        assert g.Description is not None


class WPToolsRestBaseTest(unittest.TestCase):
    """
    RESTBase TESTS
    """

    def test_get_rest(self):
        r = wptools.page()
        r.get_parse()
        r.get_query()
        r.get_wikidata()
        r.get_rest()
        if hasattr(r, 'g_rest') and 'html' in r.g_rest:
            print r.g_rest['html'].encode('utf-8')
            print "\n<hr>\n"
            print r.lead.encode('utf-8')


class WPToolsInfoboxTest(unittest.TestCase):

    def test_complex_infobox(self):
        """
        Successfully populate complex infobox dict
        """
        g = wptools.page('Abe Lincoln').get()
        self.assertGreaterEqual(len(g.infobox), 42)


if __name__ == '__main__':
    unittest.main()

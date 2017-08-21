# -*- coding:utf-8 -*-

"""
WPTools Site module
~~~~~~~~~~~~~~~~~~~

Support for getting Mediawiki site info.
"""


class WPToolsSite(object):
    """
    WPToolsSite class
    """

    mostviewed = None
    siteinfo = None
    siteviews = None
    uniqueviews = None

    def __init__(self):
        """
        Returns a WPToolsSite object.
        """
        pass

    def get_mostviewed(self):
        """
        https://www.mediawiki.org/wiki/Extension:PageViewInfo
        """
        pass

    def get_siteinfo(self):
        """
        Overall site information
        https://www.mediawiki.org/wiki/API:Siteinfo
        """
        pass

    def get_siteviews(self):
        """
        Average daily site views for past 60 days
        https://www.mediawiki.org/wiki/Extension:PageViewInfo
        """
        pass

    def get_uniqueviews(self):
        """
        Average daily unique views for past 60 days
        https://www.mediawiki.org/wiki/Extension:PageViewInfo
        """
        pass

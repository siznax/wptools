# -*- coding:utf-8 -*-

"""
WPTools Site module
~~~~~~~~~~~~~~~~~~~

Support for getting Mediawiki site info.
"""

import random

from . import core


class WPToolsSite(core.WPTools):
    """
    WPToolsSite class
    """

    mostviewed = None
    siteinfo = None
    siteviews = None
    uniqueviews = None

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsSite object.
        """
        super(WPToolsSite, self).__init__(*args, **kwargs)

        self.params['wiki'] = 'commons.wikimedia.org'

    def _query(self, action, qobj):
        """
        returns query string
        """
        return qobj.site(action)

    def _set_data(self, action):
        """
        capture Wikidata API response data
        """
        self._set_site_data(action)

    def _set_site_data(self, action):
        """
        capture API site data in data attribute
        """
        data = self._load_response(action)

        matrix = data.get('sitematrix')
        if matrix:
            self.data['matrix'] = sitelist(matrix)
            self.data['random'] = random.choice(self.data['matrix'])

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

    def get_sitematrix(self, show=True, proxy=None, timeout=0):
        """
        Get Mediawiki sites via Extension:SiteMatrix
        https://www.mediawiki.org/wiki/Extension:SiteMatrix
        """
        self._get('sitematrix', show, proxy, timeout)

        return self

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


def sitelist(matrix, domain='wikipedia.org'):
    """
    Returns a list of 'wikipedia.org' sites from a SiteMatrix
    """
    _list = []
    for item in matrix:
        sites = []

        if isinstance(matrix[item], list):
            sites = matrix[item]
        elif isinstance(matrix[item], dict):
            sites = matrix[item]['site']

        for site in sites:
            if len(site.keys()) > 4:  # closed, fishbowl, private
                continue
            if domain in site['url']:
                _list.append(site['url'])

    return _list

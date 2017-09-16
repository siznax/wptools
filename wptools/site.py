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

    COMMONS = 'commons.wikimedia.org'

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsSite object.
        """
        super(WPToolsSite, self).__init__(*args, **kwargs)

    def _query(self, action, qobj):
        """
        returns query string
        """
        return qobj.site(action)

    def _set_data(self, action):
        """
        capture Wikidata API response data
        """
        if action == 'sitematrix':
            self._set_sitematrix()
        elif action == 'siteinfo':
            self._set_siteinfo()
        elif action == 'pageviews' or 'visitors':
            self._set_siteviews(action)

    def _set_siteinfo(self):
        """
        capture API sitematrix data in data attribute
        """
        data = self._load_response('siteinfo').get('query')

        general = data.get('general')

        self.params.update({'title': general.get('sitename')})
        self.params.update({'lang': general.get('lang')})
        self.data['site'] = general.get('wikiid')

        info = {}
        for item in general:
            ginfo = general.get(item)
            if ginfo:
                info[item] = ginfo
        self.data['info'] = info

        stats = data.get('statistics')
        for item in stats:
            self.data[item] = stats[item]

    def _set_sitematrix(self):
        """
        capture API sitematrix data in data attribute
        """
        data = self._load_response('sitematrix')

        self.params.update({'title': self.COMMONS})

        matrix = data.get('sitematrix')
        if matrix:
            self.data['sites'] = self._sitelist(matrix)
            self.data['random'] = random.choice(self.data['sites'])

    def _set_siteviews(self, action):
        """
        capture API pageview/visitor data in data attribute
        """
        data = self._load_response(action).get('query')

        siteviews = data.get('siteviews')
        if siteviews:
            values = [x for x in siteviews.values() if x]
            if values:
                self.data[action] = int(sum(values) / len(values))
            else:
                self.data[action] = 0

    def _sitelist(self, matrix):
        """
        Returns a list of 'wikipedia.org' sites from a SiteMatrix

        Optional params:
        - [domain]: filter sites on this domain, e.g. 'wiktionary.org'
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
                domain = self.params.get('domain')
                if domain:
                    if domain in site['url']:
                        _list.append(site['url'])
                else:
                    _list.append(site['url'])

        return _list

    def get_mostviewed(self, show=True, proxy=None, timeout=0):
        """
        https://www.mediawiki.org/wiki/Extension:PageViewInfo
        """
        pass

    def get_siteinfo(self, wiki=None, show=True, proxy=None, timeout=0):
        """
        GET site information (statistics, general) via
        https://www.mediawiki.org/wiki/API:Siteinfo

        Optional arguments:
        - [wiki]: <str> alternate wiki site (default=en.wikipedia.org)
        """
        if wiki:
            self.params.update({'wiki': wiki})

        self._get('siteinfo', show, proxy, timeout)

        return self

    def get_sites(self, show=True, proxy=None, timeout=0):
        """
        GET Wikimedia sites via Extension:SiteMatrix
        https://www.mediawiki.org/wiki/Extension:SiteMatrix
        """
        self.params.update({'wiki': self.COMMONS})

        self._get('sitematrix', show, proxy, timeout)

        del self.params['wiki']

        return self

    def get_pageviews(self, wiki=None, show=True, proxy=None, timeout=0):
        """
        GET average daily site views for past 60 days
        https://www.mediawiki.org/wiki/Extension:PageViewInfo

        Optional arguments:
        - [wiki]: <str> alternate wiki site (default=en.wikipedia.org)
        """
        if wiki:
            self.params.update({'wiki': wiki})

        self._get('pageviews', show, proxy, timeout)

        return self

    def get_visitors(self, wiki=None, show=True, proxy=None, timeout=0):
        """
        GET average daily unique visitors for past 60 days
        https://www.mediawiki.org/wiki/Extension:PageViewInfo

        Optional arguments:
        - [wiki]: <str> alternate wiki site (default=en.wikipedia.org)
        """
        if wiki:
            self.params.update({'wiki': wiki})

        self._get('visitors', show, proxy, timeout)

        return self

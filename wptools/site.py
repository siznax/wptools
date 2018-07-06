# -*- coding:utf-8 -*-

"""
WPTools Site module
~~~~~~~~~~~~~~~~~~~

Support for getting Mediawiki site info.
"""

from __future__ import print_function

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

        Optional keyword {params}:
        - [endpoint]: <str> alternative API endpoint (default=/w/api.php)
        - [lang]: <str> Mediawiki language code (default=en)
        - [wiki]: <str> alternative wiki site (default=wikipedia.org)

        Optional keyword {flags}:
        - [silent]: <bool> do not echo page data if True
        - [skip]: <list> skip actions in this list
        - [verbose]: <bool> verbose output to stderr if True
        """
        super(WPToolsSite, self).__init__(*args, **kwargs)

        endpoint = kwargs.get('endpoint')
        if endpoint:
            self.params.update({'endpoint': endpoint})

    def _query(self, action, qobj):
        """
        returns query string
        """
        return qobj.site(action)

    def _set_data(self, action):
        """
        capture Wikidata API response data
        """
        if action == 'siteinfo':
            self._set_siteinfo()
        elif action == 'sitematrix':
            self._set_sitematrix()
        elif action == 'sitevisitors':
            self._set_sitevisitors()

    def _set_siteinfo(self):
        """
        capture API sitematrix data in data attribute
        """
        data = self._load_response('siteinfo').get('query')

        mostviewed = data.get('mostviewed')
        self.data['mostviewed'] = []
        for item in mostviewed[1:]:
            if item['ns'] == 0:
                self.data['mostviewed'].append(item)

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

        siteviews = data.get('siteviews')
        if siteviews:
            values = [x for x in siteviews.values() if x]
            if values:
                self.data['siteviews'] = int(sum(values) / len(values))
            else:
                self.data['siteviews'] = 0

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

    def _set_sitevisitors(self):
        """
        capture API pageview/visitor data in data attribute
        """
        data = self._load_response('sitevisitors').get('query')

        siteviews = data.get('siteviews')
        if siteviews:
            values = [x for x in siteviews.values() if x]
            if values:
                self.data['visitors'] = int(sum(values) / len(values))
            else:
                self.data['visitors'] = 0

    def _sitelist(self, matrix):
        """
        Returns a list of sites from a SiteMatrix, optionally filtered
        by 'domain' param
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

    def get_info(self, wiki=None, show=True, proxy=None, timeout=0):
        """
        GET site info (general, statistics, siteviews, mostviewed) via
        https://www.mediawiki.org/wiki/API:Siteinfo, and
        https://www.mediawiki.org/wiki/Extension:PageViewInfo

        Optional arguments:
        - [wiki]: <str> alternate wiki site (default=en.wikipedia.org)
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - info: <dict> API:Siteinfo
        - mostviewed: <list> mostviewed articles {ns=0, title, count}
        - site: <str> sitename, e.g. 'enwiki'
        - siteviews: <int> sitewide pageview totals over last WEEK
        - visitors: <int> sitewide unique visitor total over last WEEK
        - various counts: activeusers, admins, articles, edits, images
          jobs, pages, queued-massmessages, siteviews, users, visitors
        """
        if wiki:
            self.params.update({'wiki': wiki})

        self._get('siteinfo', show=False, proxy=proxy, timeout=timeout)
        self._get('sitevisitors', show, proxy, timeout)

        return self

    def get_sites(self, domain=None, show=True, proxy=None, timeout=0):
        """
        GET Wikimedia sites via Extension:SiteMatrix
        https://www.mediawiki.org/wiki/Extension:SiteMatrix

        Optional params:
        - [domain]: filter sites on this domain, e.g. 'wiktionary.org'

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - random: randomly selected wiki site
        - sites: <list> of wiki sites (hundreds) from commons SiteMatrix
        """
        if domain:
            self.params.update({'domain': domain})

        self.params.update({'wiki': self.COMMONS})

        self._get('sitematrix', show, proxy, timeout)

        del self.params['wiki']

        return self

    def top(self, wiki=None, limit=25):
        """
        Print list of top viewed articles (ns=0) over the last WEEK
        https://www.mediawiki.org/wiki/Extension:PageViewInfo

        Optional params:
        - [wiki]: <str> alternate wiki site (default=en.wikipedia.org)
        - [limit]: <int> show up to limit articles (max=500)

        See also:
        https://en.wikipedia.org/wiki/Wikipedia_talk:Top_25_Report
        """
        if wiki:
            self.params.update({'wiki': wiki})

        if 'siteinfo' not in self.cache:
            self.get_info(show=False)

        print("%s mostviewed articles:" % (self.data['site']))

        count = 0
        for item in self.data['mostviewed']:
            if item['ns'] == 0:
                count += 1
                print("%d. %s (%s)" % (count, item['title'],
                                       "{:,}".format(item['count'])))
            if count >= limit:
                break

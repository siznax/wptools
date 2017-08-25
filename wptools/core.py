# -*- coding:utf-8 -*-

"""
WPTools core module
~~~~~~~~~~~~~~~~~~~

Support for accessing Mediawiki foundation APIs.
"""

from . import query
from . import request
from . import utils


class WPTools(object):
    """
    WPtools core class
    """

    def __init__(self, **kwargs):
        """
        Initializes a WPTools core object

        See also:
            wptools.page.WPToolsPage
            wptools.category.WPToolsCategory
        """
        self.cache = {}
        self.data = {}
        self.flags = {
            'silent': kwargs.get('silent') or False,
            'skip': kwargs.get('skip') or [],
            'verbose': kwargs.get('verbose') or False}
        self.params = {
            'lang': kwargs.get('lang') or 'en',
            'variant': kwargs.get('variant'),
            'wiki': kwargs.get('wiki') or 'wikipedia.org'}

    def _get(self, action, show, proxy, timeout):
        """
        make HTTP request and cache response
        """
        silent = self.flags['silent']

        if action in self.cache:
            if action != 'imageinfo':
                utils.stderr("%s results in cache" % action, silent)
                return

        if action in self.flags['skip']:
            utils.stderr("skipping %s" % action)
            return

        req = self._request(proxy, timeout)
        qobj = query.WPToolsQuery(lang=self.params['lang'],
                                  wiki=self.params['wiki'],
                                  variant=self.params['variant'])
        qstr = self._query(action, qobj)

        cache = {}
        cache['query'] = qstr
        cache['response'] = req.get(qstr, qobj.status)
        cache['info'] = req.info
        self.cache[action] = cache

        self._set_data(action)

        if show:
            self.show()

    def _load_response(self, action):
        """
        returns API reponse from cache or raises ValueError
        """
        try:
            _query = self.cache[action]['query'].replace('&format=json', '')
            data = utils.json_loads(self.cache[action]['response'])

            if data.get('error'):
                raise LookupError

            if action == 'parse' and not data.get('parse'):
                raise LookupError

            if action == 'query':
                if [x for x in data['query']['pages'] if x.get('missing')]:
                    raise LookupError

            if action == 'wikidata' and '-1' in data.get('entities'):
                raise LookupError

            return data

        except (LookupError, ValueError):
            raise LookupError(_query)

    def _query(self, action, qobj):
        """
        Implemented by sub-classes
        """
        pass

    def _request(self, proxy, timeout):
        """
        Returns WPToolsRequest object
        """
        return request.WPToolsRequest(self.flags['silent'],
                                      self.flags['verbose'],
                                      proxy, timeout)

    def _set_data(self, action):
        """
        Pack data from API response
        """
        pass

    def info(self, action=None):
        '''
        returns cached request info for given action,
        or list of cached actions
        '''
        if action in self.cache:
            return self.cache[action]['info']
        return self.cache.keys() or None

    def query(self, action=None):
        '''
        returns cached query string (without &format=json) for given action,
        or list of cached actions
        '''
        if action in self.cache:
            return self.cache[action]['query'].replace('&format=json', '')
        return self.cache.keys() or None

    def response(self, action=None):
        '''
        returns cached response (as dict) for given action,
        or list of cached actions
        '''
        if action in self.cache:
            return utils.json_loads(self.cache[action]['response'])
        return self.cache.keys() or None

    def show(self, maxwidth=78):
        """
        Pretty-print instance data
        """
        if not self.data:
            return

        seed = self.params['seed'] or self.data['title']
        output = ["%s (%s)" % (seed, self.params['lang'])]

        for item in self.data:

            prefix = item
            value = self.data[item]

            if isinstance(value, dict):
                prefix = "%s: <dict(%d)>" % (prefix, len(value))
                value = ', '.join(value.keys())
            elif isinstance(value, int):
                prefix = "%s:" % prefix
            elif isinstance(value, list):
                prefix = "%s: <list(%d)>" % (prefix, len(value))
                value = ', '.join((str(x) for x in value))
            elif isinstance(value, tuple):
                prefix = "%s: <tuple(%d)>" % (prefix, len(value))
                value = ', '.join((str(x) for x in value))
            elif utils.is_text(value):
                value = value.strip().replace('\n', '')
                if len(value) > (maxwidth - len(prefix)):
                    prefix = "%s: <str(%d)>" % (prefix, len(value))
                else:
                    prefix = "%s:" % prefix

            output.append("  %s %s" % (prefix, value))

        output.append('}')

        if not self.flags['silent']:
            for line in output:
                if len(line) >= 80:
                    line = line[:77] + '...'
                utils.stderr(line)

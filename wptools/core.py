# -*- coding:utf-8 -*-

"""
WPTools core module
~~~~~~~~~~~~~~~~~~~

Support for accessing Mediawiki foundation APIs.
"""

from wptools.query import WPToolsQuery

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
            'wiki': kwargs.get('wiki')}

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

        # make the request
        qobj = WPToolsQuery(lang=self.params['lang'],
                            wiki=self.params['wiki'],
                            variant=self.params['variant'])
        qstr = self._query(action, qobj)
        req = self._request(proxy, timeout)
        response = req.get(qstr, qobj.status)
        info = req.info

        # cache the response
        cache = {}
        cache['query'] = qstr
        cache['response'] = response
        cache['info'] = info
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

            if action == 'wikidata' and '-1' in data.get('entities'):
                raise LookupError

            return data

        except (LookupError, ValueError):
            raise LookupError(_query)

    def _query(self, action, qobj):
        """
        Abstract method that returns WPToolsQuery string
        """
        raise NotImplementedError("A subclass must implement this method.")

    def _request(self, proxy, timeout):
        """
        Returns WPToolsRequest object
        """
        return request.WPToolsRequest(self.flags['silent'],
                                      self.flags['verbose'],
                                      proxy, timeout)

    def _set_data(self, action):
        """
        Abstract method to capture API response data
        """
        raise NotImplementedError("A subclass must implement this method.")

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

    def show(self, force=False):
        """
        Pretty-print instance data
        """
        if self.flags['silent'] and not force:
            return
        if not self.data:
            return

        ptitle = self.params.get('title')
        dtitle = self.data.get('title')
        pageid = self.params.get('pageid')

        seed = dtitle or ptitle or pageid
        if utils.is_text(seed):
            seed = seed.replace('_', ' ')

        output = ["%s (%s)" % (seed, self.params['lang'])]

        output.append('{')

        maxwidth = WPToolsQuery.MAXWIDTH

        for item in sorted(self.data):

            if self.data[item] is None:
                continue

            prefix = item
            value = self.data[item]

            if isinstance(value, dict):
                prefix = "%s: <dict(%d)>" % (prefix, len(value))
                value = ', '.join(value.keys())
            elif isinstance(value, int):
                prefix = "%s:" % prefix
            elif isinstance(value, list):
                prefix = "%s: <list(%d)>" % (prefix, len(value))
                value = ', '.join((safestr(x) for x in value))
            elif isinstance(value, tuple):
                prefix = "%s: <tuple(%d)>" % (prefix, len(value))
                value = ', '.join((safestr(x) for x in value))
            elif utils.is_text(value):
                value = value.strip().replace('\n', '')
                if len(value) > (maxwidth - len(prefix)):
                    prefix = "%s: <str(%d)>" % (prefix, len(value))
                else:
                    prefix = "%s:" % prefix

            output.append("  %s %s" % (prefix, value))

        output.append('}')

        prettyprint(output)


def prettyprint(datastr):
    """
    Print page data strings to stderr
    """
    maxwidth = WPToolsQuery.MAXWIDTH
    rpad = WPToolsQuery.RPAD

    extent = maxwidth - (rpad + 2)
    for line in datastr:
        if len(line) >= maxwidth:
            line = line[:extent] + '...'
        utils.stderr(line)


def safestr(text):
    """
    Safely convert unicode to a string
    """
    try:
        return str(text)
    except UnicodeEncodeError:
        return str(text.encode('utf-8'))

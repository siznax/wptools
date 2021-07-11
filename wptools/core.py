# -*- coding:utf-8 -*-

"""
WPTools core module
~~~~~~~~~~~~~~~~~~~

Support for accessing Wikimedia foundation APIs.
"""

from time import sleep
import urllib.parse

from wptools.query import WPToolsQuery

from . import utils

import requests
class WPTools(object):
    """
    WPtools (abstract) core class
    """

    REQUEST_DELAY = 0
    REQUEST_LIMIT = 50

    cache = None
    data = None
    flags = None
    params = None

    def __init__(self, *args, **kwargs):
        """
        Abstract initialization for...
        - wptools.page
        - wptools.category
        - wptools.restbase
        - wptools.wikidata
        """
        self.cache = {}
        self.data = {}

        self.flags = {
            'silent': kwargs.get('silent') or False,
            'verbose': kwargs.get('verbose') or False
        }

        self.params = {
            'lang': kwargs.get('lang') or 'en',
        }

        if len(args) > 0 and args[0]:  # first positional arg is title
            self.params.update({'title': args[0]})

        if kwargs.get('skip'):
            self.flags.update({'skip': kwargs.get('skip')})

        if kwargs.get('variant'):
            self.params.update({'variant': kwargs.get('variant')})

        if kwargs.get('wiki'):
            self.params.update({'wiki': kwargs.get('wiki')})

    def _build_showstr(self, seed):
        """
        Returns show() display string for data attribute
        """
        output = ["%s (%s) data" % (seed, self.params['lang'])]

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
                if 'pageid' not in prefix:
                    value = "{:,}".format(value)
            elif isinstance(value, list):
                prefix = "%s: <list(%d)>" % (prefix, len(value))
                value = ', '.join((safestr(x) for x in value if x))
            elif isinstance(value, tuple):
                prefix = "%s: <tuple(%d)>" % (prefix, len(value))
                value = ', '.join((safestr(x) for x in value if x))
            elif utils.is_text(value):
                value = value.strip().replace('\n', '')
                if len(value) > (maxwidth - len(prefix)):
                    prefix = "%s: <str(%d)>" % (prefix, len(value))
                else:
                    prefix = "%s:" % prefix

            output.append("  %s %s" % (prefix, value))

        output.append('}')

        return output

    def _continue_params(self):
        """
        Returns query string fragment continue parameters
        """
        if not self.data.get('continue'):
            return

        params = []
        for item in self.data['continue']:
            params.append("&%s=%s" % (item, urllib.parse.quote_plus(self.data['continue'][item])))

        return ''.join(params)

    def _handle_continuations(self, response, cache_key):
        """
        Select continue params and clear cache or last continue params
        """
        rcontinue = response.get('continue')
        listen = ['blcontinue', 'cmcontinue', 'plcontinue']
        cparams = {}

        if rcontinue:
            for flag in listen:
                if rcontinue.get(flag):
                    cparams[flag] = rcontinue.get(flag)

        if cparams:
            self.data['continue'] = cparams
            del self.cache[cache_key]
        else:  # no more continuations
            if 'continue' in self.data:
                del self.data['continue']

    def _get(self, action, show, proxy, timeout):
        """
        make HTTP request and cache response
        """
        silent = self.flags['silent']

        if action in self.cache:
            if action != 'imageinfo' and action != 'labels':
                utils.stderr("+ %s results in cache" % action, silent)
                return
        else:
            self.cache[action] = {}

        if self.flags.get('skip') and action in self.flags['skip']:
            if not self.flags['silent']:
                utils.stderr("+ skipping %s" % action)
            return

        if 'requests' not in self.data:
            self.data['requests'] = []

        if len(self.data['requests']) >= self.REQUEST_LIMIT:
            raise StopIteration("Hit REQUEST_LIMIT = %d" % self.REQUEST_LIMIT)

        if self.data['requests'] and self.REQUEST_DELAY:
            utils.stderr("REQUEST_DELAY = %d seconds" % self.REQUEST_DELAY)
            sleep(self.REQUEST_DELAY)

        # make the request
        qobj = WPToolsQuery(lang=self.params['lang'],
                            variant=self.params.get('variant'),
                            wiki=self.params.get('wiki'),
                            endpoint=self.params.get('endpoint'))
        qstr = self._query(action, qobj)
        response = requests.get(qstr, qobj.status)
        self.cache[action]['query'] = qstr
        self.cache[action]['response'] = response.json()

        self.data['requests'].append(action)

        self._set_data(action)

        if show and not self.flags.get('silent'):
            self.show()

    def _load_response(self, action):
        """
        returns API reponse from cache or raises ValueError
        """
        _query = self.cache[action]['query'].replace('&format=json', '')
        response = self.cache[action]['response']

        if not response:
            raise ValueError("Empty response: %s" % self.params)

        data = response

        if data.get('warnings'):
            if 'WARNINGS' in self.data:
                self.data['WARNINGS'].update(data['warnings'])
            else:
                self.data['WARNINGS'] = data['warnings']

        if data.get('error'):
            utils.stderr("API error: %s" % data.get('error'))
            raise LookupError(_query)

        if 'query' in action and data.get('query'):
            if data['query'].get('pages'):
                if data['query']['pages'][0].get('missing'):
                    raise LookupError(_query)

        if action == 'parse' and not data.get('parse'):
            raise LookupError(_query)

        if action == 'wikidata':
            handle_wikidata_errors(data, _query)

        return data

    def _query(self, action, qobj):
        """
        Abstract method that returns WPToolsQuery string
        """
        raise NotImplementedError("A subclass must implement this method.")

    def _set_data(self, action):
        """
        Abstract method to capture API response data
        """
        raise NotImplementedError("A subclass must implement this method.")

    def info(self, action=None):
        """
        returns cached request info for given action,
        or list of cached actions
        """
        if action in self.cache:
            return self.cache[action]['info']
        return self.cache.keys() or None

    def query(self, action=None):
        """
        returns cached query string (without &format=json) for given action,
        or list of cached actions
        """
        if action in self.cache:
            return self.cache[action]['query'].replace('&format=json', '')
        return self.cache.keys() or None

    def response(self, action=None):
        """
        returns cached response (as dict) for given action,
        or list of cached actions
        """
        if action in self.cache:
            return self.cache[action]['response']
        return self.cache.keys() or None

    def show(self):
        """
        Pretty-print instance data
        """
        if not self.data:
            return

        if self.data.get('continue'):
            return

        ptitle = self.params.get('title')
        dtitle = self.data.get('title')
        pageid = self.params.get('pageid')

        seed = dtitle or ptitle or pageid
        if utils.is_text(seed):
            seed = seed.replace('_', ' ')

        prettyprint(self._build_showstr(seed))


def handle_wikidata_errors(data, query):
    """
    Raises LookupError if wikidata error found
    """
    entities = data.get('entities')

    if not entities:
        raise LookupError(query)
    elif '-1' in entities:
        raise LookupError(query)
    else:
        item = list(entities.values())[0]
        if 'missing' in item:
            errmsg = "wikidata item %s has been deleted" % item['id']
            raise LookupError(errmsg)


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
    if text is None:
        return
    try:
        return str(text)
    except UnicodeEncodeError:
        return str(text.encode('utf-8'))

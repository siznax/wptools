# -*- coding:utf-8 -*-

"""
WPTools Category module
~~~~~~~~~~~~~~~~~~~~~~~

Support for getting Mediawiki category info.
"""

from . import core


class WPToolsCategory(core.WPTools):
    """
    WPToolsCategory class
    """

    members = None
    namespace = None
    pageid = None
    title = None

    def __init__(self, *args, **kwargs):
        """
        Returns a wptools category object.

        Arguments:
        - namespace: <int> filter on this namespace (0=article, 14=category)
        - pageid: <int> category pageid
        - title: <str> category title

        See also
          https://www.mediawiki.org/wiki/Manual:Namespace
        """
        super(WPToolsCategory, self).__init__(**kwargs)

        pageid = kwargs.get('pageid')
        namespace = kwargs.get('namespace')

        title = None
        if len(args) > 0:
            title = args[0]

        if pageid and title:
            raise ValueError("cannot use both title AND pageid")

        if namespace or namespace == 0:
            try:
                self.namespace = int(namespace)
            except ValueError:
                raise ValueError("invalid namespace")

        if pageid:
            try:
                kwargs['pageid'] = int(pageid)
            except ValueError:
                raise ValueError("invalid pageid")

        self.params.update({'title': title,
                            'pageid': pageid,
                            'namespace': namespace,
                            'seed': title or pageid})

        if not pageid and not title:
            # raise ValueError("need category title OR pageid")
            self.get_random()

    def _query(self, action, qobj):
        """
        Form query to enumerate category
        """
        title = self.params['title']
        pageid = self.params['pageid']

        if action == 'random':
            return qobj.random(namespace=14)
        elif action == 'category':
            if title and pageid:
                title = None
            return qobj.category(title=title, pageid=pageid)

    def _set_data(self, action):
        """
        Set category member data from API response
        """
        data = self._load_response(action)

        if action == 'category':
            members = data.get('query').get('categorymembers')
            self.data.update({'members': members})

        if action == 'random':
            rand = data['query']['random'][0]
            data = {'pageid': rand.get('id'),
                    'title': rand.get('title')}
            self.data.update(data)
            self.params.update(data)

    def get_members(self, show=True, proxy=None, timeout=0):
        """
        Mediawiki:API (action=query) for category members

        Arguments:
        - proxy: <str> use this HTTP proxy
        - show: <bool> echo category attributes if True
        - timeout: <int> seconds to wait before timeout

        Attributes affected:
        - members: <list> category members [{ns, pageid, title}]

        See also
          https://www.mediawiki.org/wiki/API:Categorymembers
        """
        title = self.params['title']
        pageid = self.params['pageid']

        if not title and not pageid:
            raise LookupError("needs category title or pageid")

        self._get('category', show, proxy, timeout)

        return self

    def get_random(self, show=True, proxy=None, timeout=0):
        """
        Make MediaWiki:API (action=query) request for random category

        Arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - pageid: <int> Wikipedia database ID
        - title: <str> article title

        See:
        https://www.mediawiki.org/wiki/API:Random
        """
        self._get('random', show, proxy, timeout)

        # flush cache to allow repeated random requests
        del self.cache['random']

        return self

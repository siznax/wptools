# -*- coding:utf-8 -*-

"""
WPToolsCategory module.
~~~~~~~~~~~~~~~~~~~~~~~
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

        pageid = kwargs.get('pageid')
        namespace = kwargs.get('namespace')

        if pageid and len(args) > 0:
            raise ValueError("cannot use both title AND pageid")

        if not pageid and len(args) == 0:
            raise ValueError("need category title OR pageid")

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

        super(WPToolsCategory, self).__init__(*args, **kwargs)

    def _query(self, action, _fetch):
        """
        Form query to enumerate category
        """
        return _fetch.query(action, {
            'limit': 500,
            'namespace': self.namespace,
            'pageid': self.pageid,
            'title': self.title})

    def _set_category_data(self):
        """
        Set category member data from API response
        """
        data = self._load_response('category')
        self.members = data.get('query').get('categorymembers')

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
        if not self.title and not self.pageid:
            raise LookupError("get_category needs category title or pageid")

        self._request('category', False, proxy, timeout)

        self._set_category_data()

        if show:
            self.show()

        return self

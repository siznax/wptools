# -*- coding:utf-8 -*-

"""
WPTools Query module
~~~~~~~~~~~~~~~~~~~~

Support for forming WMF API query strings.

* WMF: https://wikimediafoundation.org/wiki/Our_projects
* Mediawiki: https://www.mediawiki.org/wiki/API:Main_page
* Wikidata: https://www.wikidata.org/wiki/Wikidata:Data_access
* RESTBase: https://www.mediawiki.org/wiki/RESTBase
"""


class WPToolsQuery(object):
    """
    WPToolsQuery class
    """

    action = None
    lang = None
    options = None
    params = None
    props = None
    target = None
    variant = None
    wiki = None

    def __init__(self):
        """
        Returns a WPToolsQuery object
        """
        pass

    def querystring(self):
        """
        Returns the final request query string
        """
        pass

    def statusline(self):
        """
        Returns request status line
        """
        pass

# -*- coding: utf-8 -*-

"""
Wikipedia tools (for Humans)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python and command-line MediaWiki access for Humans

- get page extracts, image, Infobox data, Wikidata, and more
- get a random page, category, or site
- get page statistics
- get category members
- get site info and stats
- get data in any language
"""

__author__ = "siznax"
__contact__ = "https://github.com/siznax/wptools"
__license__ = "MIT"
__title__ = "wptools"
__version__ = "0.4.11"

from . import core
from . import query
from . import request
from . import site
from . import utils

from .category import WPToolsCategory as category
from .page import WPToolsPage as page
from .restbase import WPToolsRESTBase as restbase
from .site import WPToolsSite as site
from .wikidata import WPToolsWikidata as wikidata

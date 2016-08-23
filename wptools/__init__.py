# -*- coding: utf-8 -*-

"""
Wikipedia tools (for Humans)

Easily get Wikipedia article info and Wikidata via MediaWiki APIs.

- get an HTML or plain text "extract" (lead, summary, etc.)
- get a representative image (or thumbnail)
- get an Infobox as a python dictionary
- get the Wikidata item ID by title
- get Wikidata by property name
- get random data!
"""

__author__ = "siznax"
__contact__ = "https://github.com/siznax/wptools"
__license__ = "MIT"
__title__ = "wptools"
__version__ = "0.0.5"

from . import utils
from . import fetch
from .core import WPTools as wptools

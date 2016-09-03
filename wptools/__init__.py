# -*- coding: utf-8 -*-

"""
Wikipedia tools (for Humans)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get Wikipedia article info and Wikidata via MediaWiki APIs:

- get an HTML or plain text "extract" (lead or summary)
- get a representative image, pageimage, thumbnail
- get an Infobox as a python dictionary
- get selected Wikidata properties
- get a Wikidata item by title
- get info in any language
- get random info
"""

__author__ = "siznax"
__contact__ = "https://github.com/siznax/wptools"
__license__ = "MIT"
__title__ = "wptools"
__version__ = "0.1.2"

from . import fetch
from . import utils
from . import test

from .core import WPTools as page

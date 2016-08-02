# -*- coding: utf-8 -*-

"""
Wikipedia tools (for Humans)

Get the plain text, wikitext, HTML, or parse tree of an article via
MediaWiki API. You may get the whole article in those formats, just
the "lead" section (summary), the Infobox (if extant), or a
representative image for the article.
"""

__author__ = "siznax"
__contact__ = "https://github.com/siznax/wptools"
__license__ = "MIT"
__title__ = "wptools"
__version__ = "0.0.2"

from . import utils
from .extract import html, infobox, parsetree, text, wikitext
from .fetch import get_html, get_images, get_infobox
from .fetch import get_parsetree, get_wikitext
from .fetch import WPToolsFetch

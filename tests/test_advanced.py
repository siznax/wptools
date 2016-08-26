# -*- coding:utf-8 -*-

import wptools


# WPTOOLS ADVANCED TESTS
# ======================
#
# See also ./scripts/wptool.py (no arguments does random everything)


# STRESS TESTS
# ------------
# These are good in development, making actual HTTP requests.

# Get random item everything
# EXPECT: no breakage
#
wptools.page().get()

# Get everything from random item in another language
# EXPECT: no breakage
#
# wptools.page(lang='ja').get()

# Get random item from another wiki
# EXPECT: no breakage
#
# wptools.page(wiki='en.wikinews.org').get()


# FULLY HYDRATE
# -------------
# These can be done with simulated HTTP responses. 

# Get specific title
# EXPECT: should populate everything
#
# wptools.page('Shakespeare').get()

# Get specific title w/redirect
# EXPECT: should populate everything
#
# wptools.page(title='Abe Lincoln').get()

# Get everything in another language
# EXPECT: should populate everything
#
# wptools.page('Napoleon', lang='fr').get()

# Get everything wikibase only
# Q43303 Malcolm_X
# EXPECT: should populate everything
#
# wptools.page(wikibase='Q43303').get()

# Get everything multibyte request
# e.g. 托爾金 (zh) Tolkien
# EXPECT: should populate everything
#
# wptools.page('托爾金', lang='zh')

# Get everything mixed languages
# EXPECT: should populate everything
#
# wptools.page(title='Abe Lincoln', lang='zh').get()


# COMPLEX INFOBOXEN
# -----------------
# Just need to supply a tmp/parsetree.xml

# Successfully populate complex infobox dict
# EXPECT: <dict(42)>
#
# wptools.page('Abe Lincoln').get()
   

# BAD REQUESTS
# ------------
# More failed requests needed here.

# Mediawiki site function not supported
# e.g. "jp" Wikinews (unknown language code)
# EXPECT: error message, self.fatal = True
#
# wptools.page(wiki='jp.wikinews.org').get()


# Random Points of Interest
# -------------------------
# Need more analysis.

# no image, no infobox
# wptools.page('audio mining').get()

# has country (P17) and point in time (P585)
# wptools.page(wikibase='Q34664').get_wikidata()
# print h.g_wikidata['query']

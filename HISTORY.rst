.. :changelog:

Release History
---------------

0.4.17 (2018-08-16)
+++++++++++++++++++

* Support proxy authentication (#130)
* Support page links continuations (#129)
* Support alternate API endpoints (#127)
* Merged @mcepl update to package tests (#125)
* Put API warnings in data attribute (#120)
* Support getting backlinks w/continuations (#119, #122)
* Always respect silent flag (#118)
* Improved infobox parsing (#91, #109)
* Added image (license, assessment) metadata (#104, #105)
* Fixed Wikidata pageid, image bugs (#101, #102)
* Added support for category continuations, subcategories (#99)
* Merged @RobbieClarken fix for non-value Wikidata snaktypes (#98)
* Merged @seansay fix for deleted Wikidata item (#97)
* Fixed TypeError on Windows 10 (#95)
* Fixed RESTBase LookupError on slash titles (#94)
* Added boxterm param for more Infobox reach (#91)
* Improved stress tests, wptool CLI script output
* Fixed get_imageinfo() issue (#93)
* Getting ALL Wikidata (#56)
* Surfaced redirects, disambiguation links (#25)
* Increased test coverage to 95%, pylint score 10.0
* Added more page data, split off expensive queries
* Implemented basic category and site functionality
* Changed page._WIKIPROPS to wikidata.LABELS
* Refactored attributes to only cache, data, flags, params
* Unified Wikimedia APIs access pattern via wptools.core


0.3 (2017-08-13)
++++++++++++++++

* Implemented general RESTBase /page/ access (#67)
* Merged @rikima's contrib plus py3 patch (#66)
* Made page.info(), query(), response() methods useable
* Improved wiki documentation (see Actions, Attributes)


0.2.3 (2017-04-17)
++++++++++++++++++

* Merge @aplz improvement: fetch full lists in infobox values (#62)
* Put HTML extract with wikilinks into 'exhtml'
* Fix AttributeError bug (#47)
* Refactoring fixes


0.2 (2016-11-06)
++++++++++++++++++

* Many fixes/improvements with help of @seansay (thank you!)
* Raise LookupError on API missing page/title
* Consolidated images and caches
* Support get_query() by pageid
* Support proxy, timeout on all API entrypoints
* Support for language variants (e.g. variant='zh-cn')
* Support for non-https wikis via wiki='http://example.com'
* Automatically get_imageinfo() via MediaWiki API:Imageinfo
* moved NOTES.md to wiki


0.1.7 (2016-09-20)
++++++++++++++++++

* Minor fixes
* Provide local SSL certs with python-certifi
* Enabled extending Wikidata properties
* Improved cache checking


0.1.4 (2016-09-06)
++++++++++++++++++

* Python 3 support!
* Implemented get_claims()
* Patch get_rest() path, tests/test_advanced
* Implemented get_wikidata() by title, lang
* Geo coordinates Property:P625 from Wikidata
* Added RESTBase support, lead attribute
* Made wptools.page() the atomic object


0.1.0 (2016-08-25)
++++++++++++++++++

* Many fixes, enhancements.
* ONE CLI SCRIPT TO RULE THEM ALL: wptool.
* Much testing of random (title, lang, and wiki).
* Allow chaining get_s or just get().
* Enabled full-hydration from wikibase only.
* Block further requests on fatal error.
* Get 240x thumbnails instead of default 50x.
* Harmonized silent and verbose arguments.
* Mock-up tests/test_advanced.py.
* Made NOTES.md a knowledge base.
* Use _humans_ in README examples. ;-)


0.0.5 (2016-08-23)
++++++++++++++++++

* Major re-write.
* Exposed core.WPTools as entrypoint.
* Added get_parse(), get_query(), and get_wikidata().
* Added get(self) to query all APIs.
* Added show(self) method to display fetched attrs.
* Show instance attributes after each request.
* Ignore requests if attrs will not be updated.
* Enabled language support across APIs.
* Gets random article if no arguments.
* CLI scripts and tests disabled pending update.


0.0.4 (2016-08-16)
++++++++++++++++++

* Added wptools.lead.
* Added safe_exit() to CLI scripts.
* Removed a fair amount of unused code.


0.0.3 (2016-08-12)
++++++++++++++++++

* Implemented wptools.image choices.
* Added wptools.api to simplify python i/f and CLI scripts.
* Merged @0x9900's CLI dist fixes.
* A little more test coverage.
* Starting to look like a legit module.


0.0.1 (2015)
++++++++++++

* Still better than alternatives for working with articles.


0.0.0 (2012)
++++++++++++

* It seems to work!

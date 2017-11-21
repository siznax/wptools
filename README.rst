Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

.. image:: https://travis-ci.org/siznax/wptools.svg?branch=master
        :target: https://travis-ci.org/siznax/wptools

.. image:: https://coveralls.io/repos/github/siznax/wptools/badge.svg?branch=master
        :target: https://coveralls.io/github/siznax/wptools

Python and command-line MediaWiki access for Humans

- get page extracts, image, Infobox data, Wikidata, and more
- get a random page, category, or site
- get page statistics
- get category members
- get site info and stats
- get data in any language

This package is intended to make it as easy as possible to get data
from MediaWiki instances, expose more Wikidata, and extend Wikimedia
APIs just for kicks. We say "(for Humans)" because that is a goal_.
Questions, feedback, and especially contributions_ are welcome!


Install
-------

.. code-block:: bash

    $ pip install wptools
    ✨🦄✨


Example
-------

.. code-block:: python

    >>> import wptools


.. code-block:: python

    >>> page = wptools.page('Gandhi')


.. code-block:: python

    >>> page.get()
    en.wikipedia.org (query) Gandhi
    en.wikipedia.org (parse) 19379
    www.wikidata.org (wikidata) Q1001
    www.wikidata.org (labels) Q1280678|P535|Q18338317|P434|Q1860|P376...
    www.wikidata.org (labels) P18|P19|P1066|P509|P345|Q16382|P1006|P3...
    www.wikidata.org (labels) Q2140674|Q1282294|Q21200566|P409|Q26490...
    www.wikidata.org (labels) P3417|P4431|P2949|P69|Q129286|Q9441|P42...
    en.wikipedia.org (restbase) /page/summary/Mahatma_Gandhi
    en.wikipedia.org (imageinfo) File:Portrait Gandhi.jpg|File:MKGandhi.jpg
    Mahatma Gandhi (en) data
    {
      aliases: <list(10)> M K Gandhi, Mohandas Gandhi, Bapu, Gandhi, M...
      claims: <dict(106)> P646, P535, P906, P434, P648, P3762, P1273, ...
      description: <str(67)> pre-eminent leader of Indian nationalism ...
      exhtml: <str(1144)> <p>Mahātmā <b>Mohandas Karamchand Gandhi</b>...
      exrest: <str(907)> Mahātmā Mohandas Karamchand Gandhi (; Hindust...
      extext: <str(2999)> Mahātmā **Mohandas Karamchand Gandhi** ( ; H...
      extract: <str(3292)> <p>Mahātmā <b>Mohandas Karamchand Gandhi</b...
      image: <list(6)> {'kind': 'query-pageimage', u'descriptionshortu...
      infobox: <dict(25)> known_for, other_names, image, signature, bi...
      iwlinks: <list(10)> https://biblio.wiki/wiki/Mohandas_K._Gandhi,...
      label: Mahatma Gandhi
      labels: <dict(163)> Q1280678, P535, Q18338317, Q131149, P434, Q1...
      length: 262,058
      links: <list(500)> 10 Janpath, 14th Dalai Lama, 1915 Singapore M...
      modified: <dict(2)> wikidata, page
      pageid: 19379
      parsetree: <str(330951)> <root><template><title>Redirect</title>...
      random: Salt
      redirected: <list(1)> {u'to': u'Mahatma Gandhi', u'from': u'Gandhi'}
      redirects: <list(53)> {u'ns': 0, u'pageid': 55342, u'title': u'M...
      requests: <list(9)> query, parse, wikidata, labels, labels, labe...
      title: Mahatma_Gandhi
      url: https://en.wikipedia.org/wiki/Mahatma_Gandhi
      url_raw: https://en.wikipedia.org/wiki/Mahatma_Gandhi?action=raw
      watchers: 1,770
      what: human
      wikibase: Q1001
      wikidata: <dict(105)> Geni.com profile ID (P2600), National Libr...
      wikidata_url: https://www.wikidata.org/wiki/Q1001
      wikitext: <str(260607)> {{Redirect|Gandhi}}{{pp-move-indef}}{{pp...
    }


.. code-block:: python

    >>> page.get_more()
    en.wikipedia.org (querymore) Gandhi
    Mahatma Gandhi (en) data
    {
      categories: <list(68)> Category:1869 births, Category:1948 death...
      contributors: 2,608
      files: <list(52)> File:Aum Om red.svg, File:Commons-logo.svg, Fi...
      languages: <list(167)> {u'lang': u'af', u'title': u'Mahatma Gand...
      views: 24,565
    }


Documentation
-------------

See our wiki_.


Please enjoy!


@siznax 👹


.. _contributions: https://github.com/siznax/wptools/blob/master/CONTRIBUTING.md
.. _goal: http://docs.python-requests.org/en/master/user/intro/
.. _wiki: https://github.com/siznax/wptools/wiki

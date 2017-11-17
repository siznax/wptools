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
    www.wikidata.org (claims) Q5|Q129286|Q6512732|Q668
    en.wikipedia.org (restbase) /page/summary/Mahatma_Gandhi
    en.wikipedia.org (imageinfo) File:Portrait Gandhi.jpg|File:MKGandhi.jpg
    Mahatma Gandhi (en) data
    {
      aliases: <list(10)> M K Gandhi, Mohandas Gandhi, Bapu, Gandhi, M...
      claims: <dict(4)> Q5, Q129286, Q6512732, Q668
      description: <str(67)> pre-eminent leader of Indian nationalism ...
      exhtml: <str(1064)> <p>Mahātmā <b>Mohandas Karamchand Gandhi</b>...
      exrest: <str(896)> Mahātmā Mohandas Karamchand Gandhi (; Hindust...
      extext: <str(2985)> Mahātmā **Mohandas Karamchand Gandhi** (; Hi...
      extract: <str(3212)> <p>Mahātmā <b>Mohandas Karamchand Gandhi</b...
      image: <list(6)> {'kind': 'query-pageimage', u'descriptionshortu...
      infobox: <dict(25)> known_for, other_names, image, signature, bi...
      label: Mahatma Gandhi
      length: 264,127
      links: <list(10)> https://biblio.wiki/wiki/Mohandas_K._Gandhi, h...
      modified: <dict(2)> wikidata, page
      pageid: 19379
      parsetree: <str(333405)> <root><template><title>Redirect</title>...
      properties: <dict(7)> P27, P569, P345, P18, P910, P31, P570
      random: Catlins River
      redirected: <list(1)> {u'to': u'Mahatma Gandhi', u'from': u'Gandhi'}
      redirects: <list(53)> {u'ns': 0, u'pageid': 55342, u'title': u'M...
      title: Mahatma_Gandhi
      url: https://en.wikipedia.org/wiki/Mahatma_Gandhi
      url_raw: https://en.wikipedia.org/wiki/Mahatma_Gandhi?action=raw
      watchers: 1,732
      what: human
      wikibase: Q1001
      wikidata: <dict(7)> category, death, citizenship, image, instanc...
      wikidata_url: https://www.wikidata.org/wiki/Q1001
      wikitext: <str(262663)> {{Redirect|Gandhi}}{{pp-move-indef}}{{pp...
    }

.. code-block:: python

    >>> page.get_more()
    en.wikipedia.org (querymore) Mahatma Gandhi
    Mahatma Gandhi (en) data
    {
      categories: <list(67)> Category:1869 births, Category:1948 death...
      contributors: 2,608
      files: <list(52)> File:Aum Om red.svg, File:Commons-logo.svg, Fi...
      languages: <list(167)> {u'lang': u'af', u'title': u'Mahatma Gand...
      title: Mahatma Gandhi
      views: 21,490
    }


Documentation
-------------

See our wiki_.


Please enjoy!


@siznax 👹


.. _contributions: https://github.com/siznax/wptools/blob/master/CONTRIBUTING.md
.. _goal: http://docs.python-requests.org/en/master/user/intro/
.. _wiki: https://github.com/siznax/wptools/wiki

Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

.. image:: https://travis-ci.org/siznax/wptools.svg?branch=master
        :target: https://travis-ci.org/siznax/wptools

.. image:: https://coveralls.io/repos/github/siznax/wptools/badge.svg?branch=master
        :target: https://coveralls.io/github/siznax/wptools

Python and command-line MediaWiki access for Humans.

- get an HTML or plain text "extract" (lead or summary)
- get a representative image (pageimage, thumb, etc.)
- get an Infobox as a python dictionary
- get any/all Wikidata by title
- get info in any language
- get category info
- get random info

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

    >>> page = wptools.page('Gandhi')
    Gandhi (en)
    {
      lang: en
      title: Gandhi
    }

    >>> page.get()
    en.wikipedia.org (query) Gandhi
    en.wikipedia.org (parse) 19379
    www.wikidata.org (wikidata) Q1001
    www.wikidata.org (claims) Q5|Q129286|Q6512732|Q668
    en.wikipedia.org (imageinfo) File:Portrait Gandhi.jpg|File:MKGandhi.jpg
    Mahatma_Gandhi (en)
    {
      cache: <dict(5)> {claims, imageinfo, parse, query, wikidata}
      categories: <list(66)>
      claims: <dict(4)> {Q129286, Q5, Q6512732, Q668}
      contributors: 2118
      description: pre-eminent leader of Indian nationalism during British-ruled India
      extext: <str(2980)> **Mohandas Karamchand Gandhi** (; Hindustani: ...
      extract: <str(3184)> <p><b>Mohandas Karamchand Gandhi</b> (<span><...
      files: <list(53)>
      image: <list(4)>
      infobox: <dict(22)> {alma_mater, alt, birth_date, birth_name, birt...
      label: Mahatma Gandhi
      lang: en
      languages: <list(167)>
      length: 264260
      links: <list(10)>
      modified: <dict(2)> {page, wikidata}
      pageid: 19379
      parsetree: <str(333230)> <root><template><title>Redirect</title><p...
      props: <dict(7)> {P18, P27, P31, P345, P569, P570, P910}
      random: Ikioi Shōta
      title: Mahatma_Gandhi
      url: https://en.wikipedia.org/wiki/Mahatma_Gandhi
      url_raw: https://en.wikipedia.org/wiki/Mahatma_Gandhi?action=raw
      views: 21400
      watchers: 1724
      what: human
      wikibase: Q1001
      wikidata: <dict(7)> {IMDB, birth, category, citizenship, death, im...
      wikidata_url: https://www.wikidata.org/wiki/Q1001
      wikitext: <str(262639)> {{Redirect|Gandhi}}{{pp-move-indef}}{{pp-s...
    }


Documentation
-------------

See our wiki_.


Please enjoy!


@siznax 👹


.. _contributions: https://github.com/siznax/wptools/blob/master/CONTRIBUTING.md
.. _goal: http://docs.python-requests.org/en/master/user/intro/
.. _wiki: https://github.com/siznax/wptools/wiki

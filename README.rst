Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Python and command-line MediaWiki access for Humans.

- get an HTML or plain text "extract" (lead or summary)
- get a representative image, pageimage, thumbnail
- get an Infobox as a python dictionary
- get selected Wikidata properties
- get a Wikidata item by title
- get info in any language
- get random info

This package is intended to make it as easy as possible to get data
from MediaWiki instances, expose more Wikidata, and extend the
MediaWiki API just for kicks. We say "(for Humans)" because that is a
goal_. Please see NOTES_ for details. Questions, feedback, and
especially contributions_ are welcome!

.. _NOTES: https://github.com/siznax/wptools/blob/master/NOTES.md
.. _contributions: https://github.com/siznax/wptools/blob/master/CONTRIBUTING.md
.. _goal: http://docs.python-requests.org/en/master/user/intro/


- Install_
- Usage_
- Examples_
- Methods_
- Requests_
- wptool_


.. _Install:

Install
-------

.. code-block:: bash

    $ pip install wptools
    ✨🦄✨


.. _Usage:

Usage
-----

.. code-block:: python

    >>> import wptools


An instance can be initialized by:

**wptools.page** (self)

- ``None``: <NoneType>
- ``lang``: <str> MediaWiki `language code`_ (default='en')
- ``title``: <unicode> a MediaWiki article title
- ``wiki``: <str> any MediaWiki site
- ``wikibase``: <str> Wikidata `entity ID`_

.. _`language code`: https://meta.wikimedia.org/wiki/Table_of_Wikimedia_projects
.. _`entity ID`: https://www.wikidata.org/wiki/Wikidata:Glossary#Entities.2C_items.2C_properties_and_queries


The simplest way to begin is with a title:

.. code-block:: python

    >>> f = wptools.page("Flannery O'Connor")
    Flannery_O'Connor (en)
    {
      lang: en
      title: Flannery_O'Connor
    }


The default language is 'en' (English):

.. code-block:: python

    >>> t = wptools.page('穐吉敏子')
    穐吉敏子 (en)
    {
      lang: en
      title: 穐吉敏子
    }


Leaving off arguments invokes a random_ lookup in English:

.. code-block:: python

    >>> r = wptools.page()
    en.wikipedia.org (action=random) None
    Sylvia_Rivera (en)
    {
      lang: en
      pageid: 3296309
      title: Sylvia_Rivera
    }

.. _random: https://www.mediawiki.org/wiki/API:Random


If you give only *lang*, you get a random_ article in that language:

.. code-block:: python

    >>> zh = wptools.page(lang='zh')
    zh.wikipedia.org (action=random) None
    哈莉特·塔布曼 (zh)
    {
      lang: zh
      pageid: 211070
      title: 哈莉特·塔布曼
    }


You can also start with a *wikibase* item:

.. code-block:: python

    >>> q = wptools.page(wikibase='Q43303')
    Q43303 (en)
    {
      lang: en
      wikibase: Q43303
    }


Or, another *wiki* site:

.. code-block:: python

    >>> m = wptools.page(wiki='en.wikiquote.org')
    en.wikiquote.org (action=random) None

    Malala_Yousafzai (en)
    {
      lang: en
      title: Malala_Yousafzai
    }


Instance attributes echo automatically. You can turn that off with
``silent=True``:

.. code-block:: python

    >>> r = wptools.page(silent=True)


Request details echo to *stderr* with ``verbose=True``:

.. code-block:: python

    >>> r = wptools.page(verbose=True)



.. _Examples:

Examples
--------

Get a representative image:

.. code-block:: python

    >>> frida = wptools.page("Frida Kahlo").get()
    >>> frida.image

    u'https://upload.wikimedia.org/wikipedia/commons/0/06/Frida_Kahlo,_by_Guillermo_Kahlo.jpg'

..

    .. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg/160px-Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg

    ``frida.thumbnail``


Get a text (or HTML) extract:

.. code-block:: python

    >>> ella = wptools.page('Ella Fitzgerald').get_query()
    >>> print ella.extext

    **Ella Jane Fitzgerald** (April 25, 1917 – June 15, 1996) was an
    American jazz singer often referred to as the First Lady of Song,
    Queen of Jazz and Lady Ella. She was noted for her purity of tone,
    impeccable diction, phrasing and intonation, and a "horn-like"
    improvisational ability, particularly in her scat singing.
    ...

    >>> print ella.extract

    <p><b>Ella Jane Fitzgerald</b> (April 25, 1917 – June 15, 1996) was an
    American jazz singer often referred to as the First Lady of Song,
    Queen of Jazz and Lady Ella. She was noted for her purity of tone,
    impeccable diction, phrasing and intonation, and a "horn-like"
    improvisational ability, particularly in her scat singing.</p>
    ...


Get an Infobox_ as a python object:

.. code-block:: python

    >>> fela = wptools.page('Fela Kuti').get_parse()
    >>> fela.infobox['instrument']

    'Saxophone, vocals, keyboards, trumpet, guitar, drums'


Get wikidata by title:

.. code-block:: python

    >>> fry = wptools.page('Stephen Fry').get_wikidata()
    >>> fry.wikibase

    u'https://www.wikidata.org/wiki/Q192912'


Get geographic coordinates:

.. code-block:: python

    >>> paris = wptools.page('Paris').get_wikidata()
    >>> paris.coordinates
    '48.8565777778,2.35182777778'


Resolve wikidata claims_:

.. code-block:: python

    >>> m = wptools.page('Madurai').get_wikidata()
    en.wikipedia.org (action=wikidata) Madurai
    Madurai (en)
    {
      claims: <dict(2)> {Q48, Q668}
      ...
    }

    >>> m.get_claims()
    en.wikipedia.org (action=wikidata) Q48|Q668
    Madurai (en)
    {
      continent: Asia (Q48)
      country: India (Q668)
      ...
    }

.. _claims: https://www.wikidata.org/wiki/Wikidata:Glossary#Claims_and_statements


Get *special* `lead section`_ HTML:

.. code-block:: python

    >>> b = wptools.page("Buddha")
    >>> b.get_rest()
    >>> b.lead
    u'<p heading><a href="https://en.wikipedia.org/wiki/Buddha">Buddh...
    <img pageimage src="https://upload.wikimedia.org/wikipedia/common...
    <p snipped><span><b>Gautama Buddha</b>, also known as <b>Siddh&#2...
    Gautama taught a <a href="https://en.wikipedia.org/wiki/Middle_Wa...
    Gautama is the primary figure in Buddhism. He is recognized by Bu...
    <p metadata>Last modified: 2016-09-01T08:15:49Z</p>'


Get all the things by *wikibase*:

.. code-block:: python

    >>> jill = wptools.page(wikibase='Q6192915').get()
    >>> jill.show()

    Jill_Lepore (en)
    {
      description: American historian
      label: Jill Lepore
      extext: <str(1018)> **Jill Lepore** (born August 27, 1966) is an A...
      extract: <str(1109)> <p><b>Jill Lepore</b> (born August 27, 1966) ...
      g_parse: <dict(3)> {info, query, response}
      g_query: <dict(3)> {info, query, response}
      g_wikidata: <dict(3)> {info, query, response}
      infobox: <dict(39)> {academic_advisors, alma_mater, alt, author_ab...
      lang: en
      pageid: 22469182
      parsetree: <str(19661)> <root><template><title>Infobox scientist</...
      random: Spanish immigration to Chile
      title: Jill_Lepore
      url: https://en.wikipedia.org/wiki/Jill_Lepore
      urlraw: https://en.wikipedia.org/wiki/Jill_Lepore?action=raw
      wikibase: Q6192915
      wikitext: <str(13011)> {{Infobox scientist| name = Jill Lepore| na...
    }


.. _Methods:

Methods
-------

Get help on instance methods like this:

.. code-block:: python

    >>> help(wptools.core)
    >>> help(<instance>)


**get** (self)

make all requests necessary to populate all the things

- get_query()
- get_parse()
- get_wikidata()


**get_claims** (self)

Wikidata:API (action=wbgetentities) for labels of claims

- e.g. turns claim {'Q298': 'country'} into country: Chile
- use get_wikidata() to populate claims


**get_parse** (self)

MediaWiki:API `action=parse`_ request for:

- infobox: <dict> Infobox_ data as python dictionary
- links: <list> interwiki links (iwlinks_)
- pageid: <int> MediaWiki database ID
- parsetree: <unicode> `XML parse tree`_
- wikibase: <unicode> Wikidata `entity ID`_ or wikidata URL
- wikitext: <unicode> raw wikitext URL

.. _Infobox: https://en.wikipedia.org/wiki/Template:Infobox
.. _`XML parse tree`: https://www.mediawiki.org/wiki/User:Kephir/XML_parse_tree
.. _`action=parse`: https://en.wikipedia.org/w/api.php?action=help&modules=parse
.. _iwlinks: https://www.mediawiki.org/wiki/API:Iwlinks


**get_query** (self)

MediaWiki:API `action=query`_ request for:

- extext: <unicode> plain text (Markdown_) extract
- extract: <unicode> HTML extract via `Extension:TextExtract`_
- images: <dict> {qimage, qthumb}
- pageid: <int> MediaWiki database ID
- pageimage: <unicode> pageimage URL via `Extension:PageImages`_
- random: <unicode> a random article title with every request!
- thumbnail: <unicode> thumbnail URL via `Extension:PageImages`_
- url: <unicode> the canonical wiki URL
- urlraw: <unicode> ostensible raw wikitext URL

.. _Markdown: https://en.wikipedia.org/wiki/Markdown
.. _`Extension:PageImages`: https://www.mediawiki.org/wiki/Extension:PageImages
.. _`Extension:TextExtract`: https://www.mediawiki.org/wiki/Extension:TextExtracts
.. _`action=query`: https://en.wikipedia.org/w/api.php?action=help&modules=query


**get_random** (self)

MediaWiki:API `action=query`_ request for:

- pageid: <int> MediaWiki database ID
- title: <unicode> article title


**get_rest** (self)

RESTBase_ ``/page/mobile-text/`` request for:

- description: <unicode> apparently, Wikidata description
- images: <dict> {rimage, rthumb}
- lastmodified: <str> ISO8601 date and time
- lead: <str> encyclopedia-like `lead section`_
- pageimage: <unicode> apparently, ``action=query`` pageimage
- thumbnail: <unicode> larger ``action=query`` thumbnail
- url: <unicode> the canonical wiki URL
- urlraw: <unicode> ostensible raw wikitext URL

The *lead* attribute assembles a stand-alone, encyclopedia-like HTML fragment:

- ``<p heading>`` wiki-linked title and description
- ``<img {type}>`` {image, pageimage, or thumbnail}
- ``<p snipped>`` lead paragraphs with (noprint, reference, &c.) snipped
- ``<p metadata>`` available metadata (e.g. Last modified, coordinates)

.. _`lead section`: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
.. _RESTBase: https://www.mediawiki.org/wiki/RESTBase


**get_wikidata** (self)

Wikidata:API `action=wbgetentities`_ request for:

- claims: <dict> Wikidata claims (see get_claims)
- coordinates: <str> P625_ Geographic coordinates (lat,lon)
- description: <unicode> Wikidata description
- image: <unicode> Wikidata Property:P18_ image URL
- images: <dict> {wimage}
- label: <unicode> Wikidata label

.. _P625: https://www.wikidata.org/wiki/Property:P625
.. _Property:P18: https://www.wikidata.org/wiki/Property:P18
.. _`action=wbgetentities`: https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities


**show** (self)

pretty-print instance attributes


.. _Requests:

Requests
--------

Detailed request info can be found in these instance attributes:

- g_claims: <dict> {info, query, response}
- g_parse: <dict> {info, query, response}
- g_query: <dict> {info, query, response}
- g_rest: <dict> {html, info, query, response}
- g_wikidata: <dict> {info, query, response}


The ``wptools`` user-agent_ will look like this:

wptools/*version* (https://github.com/siznax/wptools) *pycurl libs*

.. _user-agent: https://meta.wikimedia.org/wiki/User-Agent_policy


.. _wptool:

wptool
------

Basic functionality on the command-line is provided by the ``wptool`` command.

.. code-block:: bash

    $ wptool -h
    usage: wptool [-h] [-H] [-l L] [-n] [-q] [-s] [-t T] [-v] [-w W]

    Get Wikipedia article info and Wikidata via MediaWiki APIs.

    Gets a random English Wikipedia article by default, or in the
    language -lang, or from the wikisite -wiki, or by specific
    title -title. The output is a plain text extract unless -HTML.

    optional arguments:
      -h, --help      show this help message and exit
      -H, -HTML       output HTML extract
      -l L, -lang L   language code
      -n, -nowrap     do not wrap text
      -q, -query      show query and exit
      -s, -shh        quiet output to stderr
      -t T, -title T  get a specific title
      -v, -verbose    HTTP status to stderr
      -w W, -wiki W   use alternative wikisite

    Powered by https://github.com/siznax/wptools/


For example:

.. code-block:: bash

    $ wptool -t "Jeanne d'Arc" -l fr -s
    JEANNE_D'ARC—_sainte et héroïne de l'histoire de France_

    ![Jeanne d'Arc](https://upload.wikimedia.org/wikipedia/commons/3/39/...)

    **Jeanne d'Arc**, née vers 1412 à Domrémy village du duché de Bar dont
    une partie relevait du royaume de France pour le temporel et de
    l'évêché de Toul pour le spirituel (actuellement dans le département
    des Vosges en Lorraine), et morte sur le bûcher le 30 mai 1431 à
    Rouen, capitale du duché de Normandie alors possession du royaume
    d'Angleterre, est une héroïne de l'histoire de France, chef de guerre
    et sainte de l'Église catholique, surnommée depuis le XVIe siècle «
    _la Pucelle d'Orléans_ » et, depuis le XIXe siècle, « _mère de la
    nation française_ ».
    ...

    https://fr.wikipedia.org/wiki/Jeanne_d%27Arc
    https://www.wikidata.org/wiki/Q7226


Please enjoy!


@siznax 👹

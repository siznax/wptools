Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Python and command-line MediaWiki access for Humans:

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
.. _contributions: https://github.com/siznax/wptools/issues
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

An instance can be initialized by:

- ``title``: <unicode> a MediaWiki article title
- ``lang``: <str> MediaWiki `language code`_ (default='en')
- ``wikibase``: <str> Wikidata `entity ID`_

.. _`language code`: https://meta.wikimedia.org/wiki/Table_of_Wikimedia_projects
.. _`entity ID`: https://www.wikidata.org/wiki/Wikidata:Glossary#Entities.2C_items.2C_properties_and_queries


The simplest way to begin is with a title:

.. code-block:: python

    >>> from wptools import wptools as wptools
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


Instance attributes are echoed automatically. You can turn that off
with ``silent=True``.

.. code-block:: python

    >>> r = wptools.page(silent=True).get()
    >>>


.. _Examples:

Examples
--------

Get a representative image:

.. code-block:: python

    >>> frida = wptools.page("Frida Kahlo").get()
    >>> frida.Image

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


Get a *wikibase* by title:

.. code-block:: python

    >>> fry = wptools.page('Stephen Fry').get_parse()
    >>> fry.wikibase

    u'Q192912'


Get all the things by *wikibase*:

.. code-block:: python

    >>> jill = wptools.page(wikibase='Q6192915').get()
    >>> jill.show()

    Jill_Lepore (en)
    {
      Description: American historian
      Label: Jill Lepore
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


Get info from another *wiki*:

.. code-block:: python

    >>> m = wptools.page(wiki='en.wikiquote.org')
    en.wikiquote.org (action=random) None

    Malala_Yousafzai (en)
    {
      lang: en
      title: Malala_Yousafzai
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
- images: <dict> {image, pageimages, thumbnail}
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


**get_wikidata** (self)

Wikidata:API `action=wbgetentities`_ request for:

- Description: <unicode> Wikidata description
- Image: <unicode> Wikidata Property:P18_ image URL
- Label: <unicode> Wikidata label

.. _Property:P18: https://www.wikidata.org/wiki/Property:P18
.. _`action=wbgetentities`: https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities


**show** (self)

pretty-print instance attributes


.. _Requests:

Requests
--------

Detailed request info can be found in these instance attributes:

- g_parse: <dict> {info, query, response}
- g_query: <dict> {info, query, response}
- g_wikidata: <dict> {info, query, response}


The ``wptools`` user-agent_ will look like this:

*wptools/0.0.5 (https://github.com/siznax/wptools) PycURL/7.43.0 libcurl/7.43.0 SecureTransport zlib/1.2.5*

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

    ![Jeanne d'Arc](https://upload.wikimedia.org/wikipedia/commons/3/39/Joan_of_arc_miniature_graded.jpg)

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


@siznax

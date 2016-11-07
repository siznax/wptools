Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

.. image:: https://img.shields.io/badge/license-MIT-green.svg
        :target: https://github.com/siznax/wptools/blob/master/LICENSE

Python and command-line MediaWiki access for Humans.

- get an HTML or plain text "extract" (lead or summary)
- get a representative image (pageimage, thumb, etc.)
- get an Infobox as a python dictionary
- get any/all Wikidata by title
- get info in any language
- get random info

This package is intended to make it as easy as possible to get data
from MediaWiki instances, expose more Wikidata, and extend the
MediaWiki API just for kicks. We say "(for Humans)" because that is a
goal_. See our wiki_ to learn more. Questions, feedback, and
especially contributions_ are welcome!

.. _contributions: https://github.com/siznax/wptools/blob/master/CONTRIBUTING.md
.. _goal: http://docs.python-requests.org/en/master/user/intro/
.. _wiki: https://github.com/siznax/wptools/wiki


- Install_
- Usage_
- Examples_
- Methods_
- wptool_


Install
-------

.. code-block:: bash

    $ pip install wptools
    ✨🦄✨



Usage
-----

.. code-block:: python

    >>> import wptools


An instance can be initialized by:

**wptools.page** (self)

- ``None``: <NoneType>
- ``lang``: <str> MediaWiki `language code`_ (default='en')
- ``pageid``: <int> a MediaWiki Page ID
- ``title``: <str> a MediaWiki article title
- ``wiki``: <str> any MediaWiki site
- ``wikibase``: <str> Wikidata item `entity ID`_

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
    en.wikipedia.org (random) None
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
    zh.wikipedia.org (random) None
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
    en.wikiquote.org (random) None
    Malala_Yousafzai (en)
    {
      lang: en
      pageid: 146817
      title: Malala_Yousafzai
      wiki: en.wikiquote.org
    }


Instance attributes echo automatically. You can turn that off with
``silent=True``:

.. code-block:: python

    >>> r = wptools.page(silent=True)


Request details echo to *stderr* with ``verbose=True``:

.. code-block:: python

    >>> r = wptools.page(verbose=True)


All API entrypoints support setting ``proxy`` and ``timeout`` (in seconds):

.. code-block:: python

    >>> r.get(proxy='http://example.com:80', timeout=5)



Examples
--------

Get a representative image:

.. code-block:: python

    >>> frida = wptools.page('Frida Kahlo').get_query()
    en.wikipedia.org (query) Frida_Kahlo
    en.wikipedia.org (imageinfo) File:Frida Kahlo, by Guillermo Kahlo.jpg|Fi...

    >>> frida.image('page')['url']
    u'https://upload.wikimedia.org/wikipedia/commons/0/06/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg'

    >>> frida.image('thumb')['url']
    u'https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg/160px-Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg'

..

    .. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg/160px-Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg

**Note**: A page's image can come from the ``pageimage`` or
``thumbnail`` (via ``get_query()``), from an Infobox (via
``get_parse()``), from Wikidata Property:P18_ (via
``get_wikidata()``), or from the RESTBase ``image`` or ``thumb`` (via
``get_rest()``). See the Images_ wiki page for details.

.. _Images: https://github.com/siznax/wptools/wiki/Images


Get a text (or HTML) extract:

.. code-block:: python

    >>> ella = wptools.page('Ella Fitzgerald').get_query()
    en.wikipedia.org (query) Ella_Fitzgerald
    en.wikipedia.org (imageinfo) File:Ella Fitzgerald (Gottlieb 02871).jpg|F...

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
    en.wikipedia.org (parse) Fela_Kuti
    en.wikipedia.org (imageinfo) File:Fela Kuti.jpg

    >>> fela.infobox['instrument']
    'Saxophone, vocals, keyboards, trumpet, guitar, drums'

**Note**: Getting data from Infoboxen may be unavoidable, but getting
Wikidata (via ``get_wikidata()``) is preferred. Wikidata is
structured_ but (sometimes) data poor, while Infoboxen are
unstructured and (frequently) data rich. Please consider updating_
Wikidata if the information you want is only available in a MediaWiki
instance so that others may benefit from open, `linked data`_.

.. _structured: https://www.wikidata.org/wiki/Wikidata:Introduction
.. _updating: https://www.wikidata.org/wiki/Wikidata:Contribute
.. _`linked data`: https://en.wikipedia.org/wiki/Linked_data


Get an (album, book, film, etc.) cover image:

.. code-block:: python

    >>> blue = wptools.page('Blue Train (album)').get_parse()
    en.wikipedia.org (parse) Blue_Train_(album)
    en.wikipedia.org (imageinfo) File:John Coltrane - Blue Train.jpg

    >>> blue.image('cover')['url']
    u'https://upload.wikimedia.org/wikipedia/en/6/68/John_Coltrane_-_Blue_Train.jpg'

..

    .. image:: https://upload.wikimedia.org/wikipedia/en/6/68/John_Coltrane_-_Blue_Train.jpg


Get wikidata by *title*:

.. code-block:: python

    >>> fry = wptools.page('Stephen Fry').get_wikidata()
    www.wikidata.org (wikidata) Stephen_Fry
    www.wikidata.org (claims) Q8817795|Q5|Q7066|Q145
    en.wikipedia.org (imageinfo) File:Stephen Fry cropped.jpg
    Stephen_Fry (en)
    {
      cache: <dict(2)> {claims, wikidata}
      claims: <dict(4)> {Q145, Q5, Q7066, Q8817795}
      description: English comedian, actor, writer, presenter, and activist
      images: <dict(1)> {wikidata-image}
      label: Stephen Fry
      lang: en
      modified: <dict(1)> {wikidata}
      props: <dict(8)> {P135, P18, P27, P31, P345, P569, P856, P910}
      title: Stephen_Fry
      what: human
      wikibase: Q192912
      wikidata: <dict(8)> {IMDB, birth, category, citizenship, image, in...
      wikidata_url: https://www.wikidata.org/wiki/Q192912
    }

**Note**: Resolved properties and claims are stored in the
``wikidata`` attribute. Wikidata properties are selected by
``_WIKIPROPS``.  Properties (e.g. P17_ "country") are stored in
``props`` and those properties that have Wikidata items for values
(e.g. Q142_ for "France") are stored in ``claims`` and resolved by
another Wikidata API call (as shown above). See the `Wikidata page`_
in our wiki for more details.

.. _P17: https://www.wikidata.org/wiki/Property:P17
.. _Q142: https://www.wikidata.org/wiki/Q142
.. _`Wikidata page`: https://github.com/siznax/wptools/wiki/Wikidata


Extend Wikidata claims_ to be resolved:

.. code-block:: python

    >>> simone = wptools.page('Simone de Beauvoir')
    >>> simone._WIKIPROPS['P21'] = 'gender'
    >>> simone.get_wikidata()
    www.wikidata.org (wikidata) Simone_de_Beauvoir
    www.wikidata.org (claims) Q142|Q5|Q3411417|Q859773|Q151578|Q1214721|Q470...
    en.wikipedia.org (imageinfo) File:Simone de Beauvoir.jpg

    >>> simone.wikidata['gender']
    'female'


.. _claims: https://www.wikidata.org/wiki/Wikidata:Glossary#Claims_and_statements


Get special (experimental) `lead section`_ HTML:

.. code-block:: python

    >>> buddha = wptools.page('Buddha').get_rest()
    en.wikipedia.org (/page/mobile-text/) Buddha
    en.wikipedia.org (imageinfo) File:Buddha in Sarnath Museum (Dhammajak Mutra).jpg

    >>> buddha.lead
    <img query-thumbnail src="https://upload.wikimedia.org/wikipedia/commons...
    <span heading><a href="https://en.wikipedia.org/wiki/Gautama_Buddha">Gau...
    <span snipped><span><b>Gautama Buddha</b>, also known as <b>Siddhārtha G...
    Gautama taught a <a href="https://en.wikipedia.org/wiki/Middle_Way" titl...
    Gautama is the primary figure in Buddhism. He is recognized by Buddhists...
    <span metadata>Modified: 2016-10-13T09:44:13Z</span>

**Note**: The *lead* attribute contains an assembled stand-alone,
encyclopedia-like HTML fragment:

- ``<img {kind}>`` selected image
- ``<span heading>`` wiki-linked title and description
- ``<span snipped>`` lead paragraphs with noprint, reference, etc. snipped
- ``<span metadata>`` available metadata (e.g. modified date)


Get all the things:

.. code-block:: python

    >>> jill = wptools.page('Jill Lepore').get()
    en.wikipedia.org (query) Jill_Lepore
    en.wikipedia.org (parse) 22469182
    www.wikidata.org (wikidata) Q6192915
    www.wikidata.org (claims) Q30|Q5
    Jill_Lepore (en)
    {
      cache: <dict(4)> {claims, parse, query, wikidata}
      claims: <dict(2)> {Q30, Q5}
      description: American historian
      extext: <str(1016)> **Jill Lepore** (born August 27, 1966) is an A...
      extract: <str(1114)> <p><b>Jill Lepore</b> (born August 27, 1966) ...
      infobox: <dict(38)> {academic_advisors, alma_mater, alt, author_ab...
      label: Jill Lepore
      lang: en
      modified: <dict(2)> {page, wikidata}
      pageid: 22469182
      parsetree: <str(50677)> <root><template><title>Infobox scientist</...
      props: <dict(3)> {P27, P31, P569}
      random: Ramesh Bidhuri
      title: Jill_Lepore
      url: https://en.wikipedia.org/wiki/Jill_Lepore
      url_raw: https://en.wikipedia.org/wiki/Jill_Lepore?action=raw
      what: human
      wikibase: Q6192915
      wikidata: <dict(3)> {birth, citizenship, instance}
      wikidata_url: https://www.wikidata.org/wiki/Q6192915
      wikitext: <str(22540)> {{Infobox scientist| name = Jill Lepore| na...
    }


All API queries and results are cached in the ``cache`` attribute:

.. code-block::

    page.cache
    {
      claims:    {query, response, info},
      imageinfo: {query, response, info},
      parse:     {query, response, info},
      query:     {query, response, info},
      wikidata:  {query, response, info}
    }

The ``wptools`` user-agent_ will look like this:

.. code-block::

    wptools/<version> (https://github.com/siznax/wptools) <libs>

.. _user-agent: https://meta.wikimedia.org/wiki/User-Agent_policy



Methods
-------

Get help on instance methods like this:

.. code-block:: python

    >>> help(wptools.core)
    >>> help(<instance>)


**get** (self)

make all requests necessary to populate all the things, probably:

- get_query()
- get_parse()
- get_wikidata()


**get_claims** (self)

Wikidata:API `action=wbgetentities`_ for labels of claims

- e.g. {'Q298': 'country'} resolves to {'country': 'Chile'}
- use get_wikidata() to populate claims


**get_imageinfo** (self)

MediaWiki request for `API:Imageinfo`_

- images: <dict> updates image URLs, sizes, etc.

.. _`API:Imageinfo`: https://www.mediawiki.org/wiki/API:Imageinfo


**get_parse** (self)

MediaWiki:API `action=parse`_ request for:

- images: <dict> {parse-image, parse-cover}
- infobox: <dict> Infobox_ data as python dictionary
- links: <list> interwiki links (iwlinks_)
- pageid: <int> MediaWiki database ID
- parsetree: <str> `XML parse tree`_
- wikibase: <str> Wikidata `entity ID`_ or wikidata URL
- wikitext: <str> raw wikitext URL

.. _Infobox: https://en.wikipedia.org/wiki/Template:Infobox
.. _`XML parse tree`: https://www.mediawiki.org/wiki/User:Kephir/XML_parse_tree
.. _`action=parse`: https://en.wikipedia.org/w/api.php?action=help&modules=parse
.. _iwlinks: https://www.mediawiki.org/wiki/API:Iwlinks


**get_query** (self)

MediaWiki:API `action=query`_ request for:

- description: <str> Wikidata description (via pageterms)
- extext: <str> plain text (Markdown_) extract
- extract: <str> HTML extract via `Extension:TextExtract`_
- images: <dict> {query-pageimage, query-thumbnail}
- label: <str> Wikidata label (via pageterms)
- modified (page): <str> ISO8601 date and time
- pageid: <int> MediaWiki database ID
- random: <str> a random article title with every request!
- url: <str> the canonical wiki URL
- url_raw: <str> ostensible raw wikitext URL

.. _Markdown: https://en.wikipedia.org/wiki/Markdown
.. _`Extension:TextExtract`: https://www.mediawiki.org/wiki/Extension:TextExtracts
.. _`action=query`: https://en.wikipedia.org/w/api.php?action=help&modules=query


**get_random** (self)

MediaWiki:API `action=query`_ request for:

- pageid: <int> MediaWiki database ID
- title: <str> article title


**get_rest** (self)

RESTBase_ ``/page/mobile-text/`` request for:

- description: <str> apparently, Wikidata description
- images: <dict> {rest-image, rest-thumb}
- lead: <str> encyclopedia-like `lead section`_
- modified (page): <str> ISO8601 date and time
- url: <str> the canonical wiki URL
- url_raw: <str> ostensible raw wikitext URL

.. _`lead section`: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
.. _RESTBase: https://www.mediawiki.org/wiki/RESTBase


**get_wikidata** (self)

Wikidata:API `action=wbgetentities`_ request for:

- claims: <dict> Wikidata claims (to be resolved)
- description: <str> Wikidata description
- images: <dict> {wikidata-image} Wikidata Property:P18_
- label: <str> Wikidata label
- modified (wikidata): <str> ISO8601 date and time
- props: <dict> Wikidata properties
- what: <str> Wikidata Property:P31_ "instance of"
- wikibase: <str> Wikidata item ID
- wikidata: <dict> resolved Wikidata properties
- wikidata_url: <str> Wikidata URL

.. _Property:P18: https://www.wikidata.org/wiki/Property:P18
.. _Property:P31: https://www.wikidata.org/wiki/Property:P31
.. _`action=wbgetentities`: https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities


**image** (self, token)

Returns first image info with kind containing token (e.g. 'thumb')


**show** (self)

Pretty-print instance attributes.



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
    JEANNE_D'ARC—sainte et héroïne de l'histoire de France

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

    <https://fr.wikipedia.org/wiki/Jeanne_d%27Arc>
    <https://www.wikidata.org/wiki/Q7226>


Please enjoy!


@siznax 👹

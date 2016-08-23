Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Easily get Wikipedia article info and Wikidata via MediaWiki APIs.

- get an HTML or plain text "extract" (lead or summary)
- get a representative image, pageimage, thumbnail
- get an Infobox as a python dictionary
- get selected Wikidata properties
- get a Wikidata item by title
- get info in any language
- get random info

This package is intended to make it as easy as possible to get data
from MediaWiki instances, expose more Wikidata, and extend MediaWiki
API functions just for kicks. We say "(for Humans)" because that is a
goal_.

Questions, feedback, and especially contributions are happily welcome!

.. _goal: http://docs.python-requests.org/en/master/user/intro/


Install
-------

.. code-block:: bash

    $ pip install wptools
    🍻


Usage
-----

A ``wptools`` instance can be initialized by:

- ``title``: <unicode> a MediaWiki article title
- ``lang``: <str> MediaWiki `language code`_ (default='en')
- ``wikibase``: <str> Wikidata `entity ID`_

.. _`language code`: https://meta.wikimedia.org/wiki/Table_of_Wikimedia_projects
.. _`entity ID`: https://www.wikidata.org/wiki/Wikidata:Glossary#Entities.2C_items.2C_properties_and_queries


The simplest way to begin is with a title:

.. code-block:: python

    >>> c = wptools.wptools('Cosmos')
    Cosmos (en)
    {
      lang: en
      title: Cosmos
    }


The default language is 'en' (English):

.. code-block:: python

    >>> j = wptools.wptools('J・R・R・トールキン')
    J・R・R・トールキン (en)
    {
      lang: en
      title: J・R・R・トールキン
    }

You can also start with a Wikidata `entity ID`_ (*wikibase*)

.. code-block:: python

    >>> q = wptools.wptools(wikibase='Q42')
    Q42 (en)
    {
      lang: en
      wikibase: Q42
    }


Leaving off arguments invokes a random_ lookup in English:

.. code-block:: python

    >>> import wptools
    >>> wptools.wptools()
    en.wikipedia.org (action=random) None
    Borg_Island (en)
    {
      lang: en
      pageid: 29332964
      title: Borg_Island
    }


If you give only *lang*, you get a random_ article in that language:

.. code-block:: python

    >>> wptools.wptools(lang='jp')
    jp.wikipedia.org (action=random) None
    摺物 (jp)
    {
      lang: jp
      pageid: 2482304
      title: 摺物
    }

.. _random: https://www.mediawiki.org/wiki/API:Random


Methods
^^^^^^^

The methods below may yield the attributes noted for a given instance.

**get** (self)

Tries all get_s below, filling all available attributes.


**get_parse** (self)  *MediaWiki:API* `action=parse`_

|    title (lang) <instance>
|    {
|      infobox: <dict> Infobox_ data as python dictionary
|      links: <list> interwiki links (iwlinks_)
|      pageid: <int> Wikipedia database ID
|      parsetree: <unicode> `XML parse tree`_
|      wikibase: <unicode> Wikidata `entity ID`_ or wikidata URL
|      wikitext: <unicode> raw wikitext URL
|    }

.. _Infobox: https://en.wikipedia.org/wiki/Template:Infobox
.. _`XML parse tree`: https://www.mediawiki.org/wiki/User:Kephir/XML_parse_tree
.. _`action=parse`: https://en.wikipedia.org/w/api.php?action=help&modules=parse
.. _iwlinks: https://www.mediawiki.org/wiki/API:Iwlinks


**get_query** (self)  *MediaWiki:API* `action=query`_

|    title (lang) <instance>
|    {
|      extext: <unicode> plain text (Markdown_) extract
|      extract: <unicode> HTML extract via `Extension:TextExtract`_
|      images: <dict> {image, pageimages, thumbnail}
|      pageid: <int> Wikipedia database ID
|      pageimage: <unicode> pageimage URL via `Extension:PageImages`_
|      random: <unicode> a random article title with every request!
|      url: <unicode> the canonical wiki URL
|      urlraw: <unicode> raw wikitext URL
|    }

.. _Markdown: https://en.wikipedia.org/wiki/Markdown
.. _`Extension:PageImages`: https://www.mediawiki.org/wiki/Extension:PageImages
.. _`Extension:TextExtract`: https://www.mediawiki.org/wiki/Extension:TextExtracts
.. _`action=query`: https://en.wikipedia.org/w/api.php?action=help&modules=query


**get_random** (self) *MediaWiki:API* `action=query`_

|    title (lang) <instance>
|    {
|      pageid: <int> Wikipedia database ID
|      title: <unicode> article title
|    }


**get_wikidata** (self) *Wikidata:API* `action=wbgetentities`_

|    title (lang) <instance>
|    {
|      image: <unicode> Wikidata Property:P18_ image URL
|      description: <unicode> Wikidata description
|      label: <unicode> Wikidata label
|    }

.. _Property:P18: https://www.wikidata.org/wiki/Property:P18
.. _`action=wbgetentities`: https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities


API requests populate the following attributes:

|    title (lang) <instance>
|    {
|      g_parse: <dict> {info, query, response}
|      g_query: <dict> {info, query, response}
|      g_wikidata: <dict> {info, query, response}
|    }


Api-User-Agent
""""""""""""""

The ``wptools`` user-agent_ will look something like this:

::

    wptools/0.0.5 (https://github.com/siznax/wptools) PycURL/7.43.0 libcurl/7.43.0 SecureTransport zlib/1.2.5

.. _user-agent: https://meta.wikimedia.org/wiki/User-Agent_policy


Examples
^^^^^^^^

You can get a (Markdown_) text *extract*:

.. code-block:: python

    >>> a = wptools.wptools('aardvark')
    >>> a.get_query()
    en.wikipedia.org (action=query) aardvark
    >>> print a.extext
    The **aardvark** (/ˈɑːrd.vɑːrk/ _**ARD**-vark_; _Orycteropus afer_) is a
    medium-sized, burrowing, nocturnal mammal native to Africa. It is the only
    living species of the order Tubulidentata, although other prehistoric species
    and genera of Tubulidentata are known. Unlike other insectivores, it has a
    long pig-like snout, which is used to sniff out food. It roams over most of
    the southern two-thirds of the African continent, avoiding areas that are
    mainly rocky. A nocturnal feeder, it subsists on ants and termites, which it
    will dig out of their hills using its sharp claws and powerful legs. It also
    digs to create burrows in which to live and rear its young. It receives a
    "least concern" rating from the IUCN, although its numbers seem to be
    decreasing.


Or, get an Infobox_ and some Wikidata_:

.. code-block:: python

    >>> n = wptools.wptools('Napoleon', lang='fr')
    >>> n.get_parse().get_wikidata()
    fr.wikipedia.org (action=parse) Napoleon
    www.wikidata.org (action=wikidata) Q517
    Napoléon_Ier (fr)
    {
      Description: chef d'État français
      Image: https://upload.wikimedia.org/wikipedia/commons/b/b5/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project_2.jpg
      Label: Napoléon Ier
      infobox: <dict(64)> {charte, conjoint, couronnement 1, date de déc...
    }
    >>> len(n.infobox.keys())
    64

.. _Wikidata: https://www.wikidata.org/


Get Wikidata_ directly from a Wikidata `entity ID`_ (*wikibase*):

.. code-block:: python

    >>> q = wptools.wptools(wikibase='Q42')
    >>> q.get_wikidata()
    www.wikidata.org (action=wikidata) Q42
    https://www.wikidata.org/wiki/Q42 (en)
    {
      Description: English writer and humorist
      Image: https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg
      Label: Douglas Adams
      g_wikidata: <dict(3)> {info, query, response}
      lang: en
      wikibase: https://www.wikidata.org/wiki/Q42
    }


Or, just get everything available all at once—why not‽

.. code-block:: python

    >>> w = wptools.wptools('Shakespeare')
    >>> w.get()
    en.wikipedia.org (action=query) Shakespeare
    en.wikipedia.org (action=parse) William_Shakespeare
    www.wikidata.org (action=wikidata) Q692
    William_Shakespeare (en)
    {
      Description: English playwright and poet
      Image: https://upload.wikimedia.org/wikipedia/commons/2/2a/Hw-shakespeare.png
      Label: William Shakespeare
      extext: <str(2572)> **William Shakespeare** (/ˈʃeɪkspɪər/; 26...
      extract: <str(2985)> <p><b>William Shakespeare</b> (<span><span>/<...
      g_parse: <dict(3)> {info, query, response}
      g_query: <dict(3)> {info, query, response}
      g_wikidata: <dict(3)> {info, query, response}
      images: <dict(3)> {Image, pageimage, thumbnail}
      infobox: <dict(14)> {birth_date, birth_place, caption, children, d...
      lang: en
      links: <list(8)>
      pageid: 32897
      pageimage: https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg
      parsetree: <str(185585)> <root><template><title>About</title><part...
      random: MobiasBanca
      thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Shakespeare.jpg/39px-Shakespeare.jpg
      title: William_Shakespeare
      url: https://en.wikipedia.org/wiki/William_Shakespeare
      urlraw: https://en.wikipedia.org/wiki/William_Shakespeare?action=raw
      wikibase: https://www.wikidata.org/wiki/Q692
      wikitext: <str(100349)> {{About|the poet and playwright|other pers...
    }


Sometimes, you can mix languages!

.. code-block:: python

    >>> t = wptools.wptools(title='Tolkien', lang='zh')
    >>> t.get()
    zh.wikipedia.org (action=query) Tolkien
    zh.wikipedia.org (action=parse) J·R·R·托爾金
    www.wikidata.org (action=wikidata) Q892
    J·R·R·托爾金 (zh)
    {
      Description: 英国作家
      Image: https://upload.wikimedia.org/wikipedia/commons/b/b4/Tolkien_1916.jpg
      Label: J·R·R·托尔金
      extext: <str(1704)> **約翰·羅納德·魯埃爾·托爾金**，...
      extract: <str(2067)> <p><b>約翰·羅納德·魯埃爾·托爾金...
      infobox: <dict(16)> {birth_name, birthdate, birthplace, caption, d...
      lang: zh
      url: https://zh.wikipedia.org/wiki/J%C2%B7R%C2%B7R%C2%B7%E6%89%98%E7%88%BE%E9%87%91
      urlraw: https://zh.wikipedia.org/wiki/J·R·R·托爾金?action=raw
      wikibase: https://www.wikidata.org/wiki/Q892
    }


And, of course, you can get info from other wikisites:

.. code-block:: python

    >>> wptools.wptools(wiki='en.wikinews.org')
    en.wikinews.org (action=random) None
    Main_belt_asteroid_No._274301_named_'Wikipedia' (en)
    {
      lang: en
      pageid: 659423
      title: Main_belt_asteroid_No._274301_named_'Wikipedia'
    }


Enjoy!


@siznax

Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Easily get Wikipedia article info and Wikidata via MediaWiki APIs.

- get an HTML or plain text "extract" (lead or summary)
- get a representative image (or thumbnail)
- get an Infobox as a python dictionary
- get selected Wikidata properties
- get a Wikidata item by title
- get random info

These are purpose-built methods intended to make it as easy as
possible to get common data from MediaWiki instances, expose more
Wikidata, and extend or augment MediaWiki API functions.  We say "(for
Humans)" because that is a goal in the same spirit as @kennethreitz
`requests`_. Contributions are welcome!


Install
=======

.. code-block:: shell

  $ pip install wptools


Usage
=====

.. code-block:: shell

  >>> import wptools
  >>> a = wptools.wptools('a')
  a (en)
  {
    lang: en
    title: a
  }

The methods below may yield the attributes noted for a given instance.

::

  get(self)
    Tries all get_s below, filling available attributes

  get_parse(self)  MediaWiki:API action=parse
    infobox - Infobox data as python dictionary
    links - inter-wiki links (iwlinks)
    pageid - Wikipedia database ID
    parse - parse {query, request, response} data
    parsetree - parse tree
    wikibase - wikibase_item (id) or wikidata URL
    wikitext - raw wikitext

  get_query(self)  MediaWiki:API action=query
    extext - plain text extract (from extract)
    extract - HTML extract, see Extension:TextExtract
    images - {image, pageimages, thumbnail}
    pageid - Wikipedia database ID
    pageimage - see Extension:PageImages
    query - query {query, request, response} data
    random - a random article title with every request!
    url - the canonical wiki URL
    urlraw - raw wikitext URL

  get_wikidata(self)  Wikidata:API action=wbgetentities
    image - Wikidata Property:P18, like DBPedia foaf:depiction
    description - Wikidata description
    label - Wikidata label


API request data can be found in the following attributes:

::

  g_parse: <dict(3)> {info, query, response}
  g_query: <dict(3)> {info, query, response}
  g_wikidata: <dict(3)> {info, query, response}


Examples
--------

Get a random article:

.. code-block:: shell

  >>> import wptools
  >>> wptools.wptools()
  en.wikipedia.org (action=random) None
  Borg_Island (en)
  {
    lang: en
    pageid: 29332964
    title: Borg_Island
  }


Get a random *Japanese* article:

.. code-block:: shell

  >>> wptools.wptools(lang='jp')
  jp.wikipedia.org (action=random) None
  土御門殿 (jp)
  {
    lang: jp
    pageid: 526200
    title: 土御門殿
  }


Get a *text extract*:

.. code-block:: shell

  >>> a = wptools.wptools('aardvark')
  >>> a.get_query()
  en.wikipedia.org (action=query) aardvark
  >>> print t.extext
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


Get an *infobox* and some *wikidata*:

.. code-block:: shell

  >>> n = wptools.wptools('Napoleon', lang='fr')
  >>> n.get_parse().get_wikidata()
  fr.wikipedia.org (action=parse) Napoleon
  www.wikidata.org (action=wikidata) Q517
  Napoléon_Ier (fr)
  {
    Description: chef d'État français
    Image: https://upload.wikimedia.org/wikipedia/commons/b/b5/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project_2.jpg
    Label: Napoléon Ier
    ...
    infobox: <dict(64)> {charte, conjoint, couronnement 1, date de déc...
  }


Get *wikidata* directly using *wikibase* item:

.. code-block:: shell

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


Get everything available all at once!

.. code-block:: shell

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


Mix languages!

.. code-block:: shell

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
    ...
    infobox: <dict(16)> {birth_name, birthdate, birthplace, caption, d...
    lang: zh
    ...
    wikibase: https://www.wikidata.org/wiki/Q892
  }


@siznax


.. _requests: http://docs.python-requests.org/en/master/user/intro/

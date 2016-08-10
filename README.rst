Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Get the plain text, wikitext, HTML, or parse tree of an article via
MediaWiki API. You may get the whole article in those formats, just
the "lead" section (summary), the Infobox (if extant), or a
representative image for the article.


See also: `MediaWiki API:Client code`_

.. _`MediaWiki API:Client code`: https://www.mediawiki.org/wiki/API:Client_code

P.S. "(for Humans)" à la @kennethreitz, in parentheses because that is a goal.


Install
=======

.. code-block:: shell

    $ pip install wptools


Usage
=====

python examples
---------------

Get the lead section of an article as Markdown text

.. code-block:: python

    >>> import wptools
    >>> t = wptools.text(wptools.get_html("Aardvark", True), True)
    >>> print t[:72]
    The **aardvark** (/ˈɑːrd.vɑːrk/ _**ARD**-vark_; _Orycteropus afer_)

Get an article's Infobox_ as a python object

.. _Infobox: https://en.wikipedia.org/wiki/Help:Infobox

.. code-block:: python

    >>> import json, wptools
    >>> p = wptools.get_parsetree("Aardvark", False, False, 'en.wikipedia.org')
    >>> i = wptools.infobox(p)
    >>> d = json.loads(i)
    >>> print d['genus']
    Orycteropus


CLI examples
------------

Get article HTML

.. code-block:: shell

  $ scripts/html.py Aardvark -l | fold | head
  <p>The <b>aardvark</b> (<span class="nowrap"><span class="IPA nopopups"><a href=
  "/wiki/Help:IPA_for_English" title="Help:IPA for English">/<span style="border-b
  ottom:1px dotted"><span title="/&#712;/ primary stress follows">&#712;</span><sp
  an title="/&#593;r/ 'ar' in 'bard'">&#593;r</span><span title="'d' in 'dye'">d</
  span><span title="/./ syllable break">.</span><span title="'v' in 'vie'">v</span
  ><span title="/&#593;r/ 'ar' in 'bard'">&#593;r</span><span title="'k' in 'kind'
  ">k</span></span>/</a></span></span> <span title="English pronunciation respelli
  ng"><a href="/wiki/Wikipedia:Pronunciation_respelling_key" title="Wikipedia:Pron
  unciation respelling key"><i><b><span class="smallcaps"><span style="FONT-VARIAN
  T: SMALL-CAPS; TEXT-TRANSFORM: LOWERCASE;">ARD</span></span></b>-vark</i></a></s

Get article Infobox

.. code-block:: shell

  $ scripts/infobox.py Aardvark | jsonlint | fold
  {
    "status": "LC",
    "range_map": "Aardvark area.png",
    "binomial_authority": "([[Peter Simon Pallas|Pallas]], 1766)",
    "grandparent_authority": "[[John Edward Gray|Gray]], 1821",
    "trend": "unknown",
    "image": "Porc formiguer.JPG",
    "status_system": "iucn3.1",
    "subdivision_ranks": "[[Subspecies]]",
    "wptools.extract ERROR": "<title>speciesbox\n</title>",
    "image_caption": "",
    "greatgrandparent_authority": "[[Thomas Henry Huxley|Huxley]], 1872",
    "status_ref": "",
    "subdivision": "See Text",
    "name": "Aardvark",
    "range_map_caption": "Aardvark range",
    "display_parents": "4",
    "fossil_range": "<template><title>Fossil range</title><part><name index=\"1\"/
  ><value>5</value></part><part><name index=\"2\"/><value>0</value></part></templa
  te>&lt;small&gt;Early [[Pliocene]] &#8211; Recent&lt;/small&gt;",
    "species": "afer",
    "parent_authority": "[[Georges Cuvier|G. Cuvier]], 1798",
    "genus": "Orycteropus"
  }

Get article `Parse tree`_

.. _`Parse tree`: https://en.wikipedia.org/wiki/Parse_tree

.. code-block:: shell

  $ scripts/parsetree.py Aardvark | fold | head
  <root><template><title>Other uses</title></template>
  <template lineStart="1"><title>pp-move-indef</title></template>
  <template lineStart="1"><title>Use dmy dates</title><part><name>date</name>=<val
  ue>July 2012</value></part></template>
  <template lineStart="1"><title>speciesbox
  </title><part><name> genus </name>=<value> Orycteropus
  </value></part><part><name> species </name>=<value> afer
  </value></part><part><name> name </name>=<value> Aardvark
  </value></part><part><name> fossil_range </name>=<value> <template><title>Fossil
   range</title><part><name index="1"/><value>5</value></part><part><name index="2

Get plain text of article

.. code-block:: shell

  $ scripts/text.py Aardvark -l | fold -s
  The **aardvark** (/ˈɑrd.vɑrk/ _**ARD**-vark_; _Orycteropus afer_) is a
  medium-sized, burrowing, nocturnal mammal native to Africa. It is the only
  living species of the order Tubulidentata, although other prehistoric species
  and genera of Tubulidentata are known. Unlike other insectivores, it has a long
  pig-like snout, which is used to sniff out food. It roams over most of the
  southern two-thirds of the African continent, avoiding mainly rocky areas. A
  nocturnal feeder, it subsists on ants and termites, which it will dig out of
  their hills using its sharp claws and powerful legs. It also digs to create
  burrows in which to live and rear its young. It receives a "least concern"
  rating from the IUCN; although its numbers seem to be decreasing.

Get article wikitext_

.. _wikitext: https://meta.wikimedia.org/wiki/Wiki_syntax

.. code-block:: shell

  $ scripts/wikitext.py Aardvark -l | head
  {{Other uses}}
  {{pp-move-indef}}
  {{Use dmy dates|date=July 2012}}
  {{speciesbox
  | genus = Orycteropus
  | species = afer
  | name = Aardvark
  | fossil_range = {{Fossil range|5|0}}<small>Early [[Pliocene]] – Recent</small>
  | status = LC
  | status_system = iucn3.1


@siznax

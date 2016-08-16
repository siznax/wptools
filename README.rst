Wikipedia tools (for Humans)
============================

.. image:: https://img.shields.io/pypi/v/wptools.svg
        :target: https://pypi.python.org/pypi/wptools/

Get the plain text, wikitext, HTML, or parse tree of an article via
`MediaWiki API`_. You may get the whole article in those formats,
just the "lead_" section (summary), the Infobox_ (if extant), or a
representative image_ for the article.

These are purpose-built python methods intended to ease use for
common requests (by me anyway ;) in the style of @kennethreitz
`requests`_. We say "(for Humans)" because that is a goal.

You can learn more about the API paths we use here: `NOTES.txt`_,
and the many other wrappers for the MediaWiki API that do more or
less here: `MediaWiki API:Client code`_. A newer (and perhaps
more performant) path to content is provided by RESTBase_ which we
hope to make use of.

Contributions are happily welcome!


Install
=======

.. code-block:: shell

    $ pip install wptools


Usage
=====

python examples
---------------

Get an article as HTML:

.. code-block:: python

  >>> import wptools
  >>> wptools.html('Aardvark')
  <div role="note" class="hatnote">For other uses, see <a href="/wiki/Aa...

Get the `lead section`_ of an article:

.. code-block:: python

  >>> wptools.lead('Aardvark')
  <p>The <b>aardvark</b> (<span class="nowrap"><span class="IPA nopopups">...

Get the `lead section`_ of an article *as plain text*:

.. code-block:: python

  >>> wptools.lead('Aardvark', plain=True)
  The **aardvark** (/ˈɑːrd.vɑːrk/ _**ARD**-vark_; _Orycteropus afer_)...

Get an article's Infobox_ as a python object:

.. code-block:: python

  >>> wptools.infobox("Aardvark")['genus']
  Orycteropus

Get an article's `thumbnail image`_ (or full original image):

.. code-block:: python

  >>> wptools.images("Aardvark")["thumbnail"]["source"]
  u'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Porc_formiguer.JPG/320px-Porc_formiguer.JPG'

  >>> wptools.images("Aardvark")["source"]
  u'https://upload.wikimedia.org/wikipedia/commons/8/8a/Porc_formiguer.JPG'

Get the Wikitext_ behind an article:

.. code-block:: python

  >>> wptools.wikitext('Aardvark')
  {{Other uses}}{{pp-move-indef}}{{Use dmy dates|date=July 2012}}{{species...


All ``wptools.api`` interfaces are available as CLI scripts:

::

  wp_html
  wp_image
  wp_infobox
  wp_lead
  wp_parsetree
  wp_text
  wp_wikitext


CLI examples
------------

Get the `lead section`_ as plain text:

.. code-block:: shell

  $ wp_lead Aardvark -p | fold -s
  The **aardvark** (/ˈɑːrd.vɑːrk/ _**ARD**-vark_; _Orycteropus afer_) is a
  medium-sized, burrowing, nocturnal mammal native to Africa. It is the only
  living species of the order Tubulidentata, although other prehistoric species
  and genera of Tubulidentata are known. Unlike other insectivores, it has a long
  pig-like snout, which is used to sniff out food. It roams over most of the
  southern two-thirds of the African continent, avoiding areas that are mainly
  rocky. A nocturnal feeder, it subsists on ants and termites, which it will dig
  out of their hills using its sharp claws and powerful legs. It also digs to
  create burrows in which to live and rear its young. It receives a "least
  concern" rating from the IUCN, although its numbers seem to be decreasing.


Get the `lead section`_ as HTML:

.. code-block:: shell

  $ wp_lead Aardvark | fold | head
  <p>The <b>aardvark</b> (<span class="nowrap"><span class="IPA nopopups"><a href=
  "/wiki/Help:IPA_for_English" title="Help:IPA for English">/<span style="border-b
  ottom:1px dotted"><span title="/&#712;/ primary stress follows">&#712;</span><sp
  an title="/&#593;&#720;r/ 'ar' in 'bard'">&#593;&#720;r</span><span title="'d' i
  n 'dye'">d</span><span title="/./ syllable break">.</span><span title="'v' in 'v
  ie'">v</span><span title="/&#593;&#720;r/ 'ar' in 'bard'">&#593;&#720;r</span><s
  pan title="'k' in 'kind'">k</span></span>/</a></span></span> <span title="Englis
  h pronunciation respelling"><a href="/wiki/Help:Pronunciation_respelling_key" ti
  tle="Help:Pronunciation respelling key"><i><b><span class="smallcaps"><span styl
  e="font-variant: small-caps; text-transform: lowercase;">ARD</span></span></b>-v

Get the Infobox_:

.. code-block:: shell

  $ wp_infobox Aardvark | jsonlint | fold
  {
      "binomial_authority": "([[Peter Simon Pallas|Pallas]], 1766)",
      "display_parents": "4",
      "fossil_range": "<template><title>Fossil range</title><part><name in...",
      "genus": "Orycteropus",
      "grandparent_authority": "[[John Edward Gray|Gray]], 1821",
      "greatgrandparent_authority": "[[Thomas Henry Huxley|Huxley]], 1872",
      "image": "Porc formiguer.JPG",
      "image_caption": "",
      "name": "Aardvark",
      "parent_authority": "[[Georges Cuvier|G. Cuvier]], 1798",
      "range_map": "Aardvark area.png",
      "range_map_caption": "Aardvark range",
      "species": "afer",
      "status": "LC",
      "status_ref": "",
      "status_system": "iucn3.1",
      "subdivision": "See Text",
      "subdivision_ranks": "[[Subspecies]]",
      "trend": "unknown",
      "wptools.extract ERROR": "<title>speciesbox\n</title>"
  }

Get the Wikitext_:

.. code-block:: shell

  $ wp_wikitext Aardvark | head
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

Get an article's `Parse tree`_:

.. code-block:: shell

  $ wp_parsetree Aardvark | fold | head
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



@siznax


.. _Infobox: https://en.wikipedia.org/wiki/Help:Infobox
.. _RESTBase: https://www.mediawiki.org/wiki/RESTBase
.. _Wikitext: https://www.mediawiki.org/wiki/Wikitext
.. _`NOTES.txt`: https://github.com/siznax/wptools/blob/master/NOTES.txt
.. _`MediaWiki API:Client code`: https://www.mediawiki.org/wiki/API:Client_code
.. _`MediaWiki API`: https://www.mediawiki.org/wiki/API:Main_page
.. _`Parse tree`: https://en.wikipedia.org/wiki/Parse_tree
.. _`lead section`: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
.. _`thumbnail image`: https://www.mediawiki.org/wiki/Extension:PageImages
.. _image: https://www.mediawiki.org/wiki/Extension:PageImages
.. _lead: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section
.. _requests: http://docs.python-requests.org/en/master/user/intro/

## Wikipedia Tools library

Get the plain text, wikitext, HTML, or parse tree of an article via
MediaWiki API. You may get the whole article in those formats, just
the "lead" section (summary), or just the Infobox (if extant). You
can get this information as an object in python, or in various text
formats (e.g. json) at the command line.

See ``pydoc wptools`` for module docs. See ``<func> -h`` for
command-line help.

Command-line functions:

### [html](https://github.com/siznax/wptools/blob/master/html.py)

Get article HTML

```shell
$ html.py Aardvark -l | fold | head
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
```


### [infobox](https://github.com/siznax/wptools/blob/master/infobox.py)

Get article [Infobox](https://en.wikipedia.org/wiki/Help:Infobox)

```shell
$ infobox.py Aardvark | jsonlint
{
  "status": "LC",
  "range_map": "Aardvark area.png",
  "binomial_authority": "([[Peter Simon Pallas|Pallas]], 1766)",
  "grandparent_authority": "[[John Edward Gray|Gray]], 1821",
  "trend": "unknown",
  "image": "Porc formiguer.JPG",
  "status_system": "iucn3.1",
  "subdivision_ranks": "[[Subspecies]]",
  "image_caption": "",
  "greatgrandparent_authority": "[[Thomas Henry Huxley|Huxley]], 1872",
  "status_ref": "",
  "subdivision": "See Text",
  "name": "Aardvark",
  "range_map_caption": "Aardvark range",
  "display_parents": "4",
  "fossil_range": "<template><title>Fossil range</title><part><name index=\"1\"/><value>5</value></part><part><name index=\"2\"/><value>0</value></part></template>&lt;small&gt;Early [[Pliocene]] &#8211; Recent&lt;/small&gt;\n",
  "species": "afer",
  "parent_authority": "[[Georges Cuvier|G. Cuvier]], 1798",
  "genus": "Orycteropus"
}
```


### [parsetree](https://github.com/siznax/wptools/blob/master/parsetree.py)

Get article [Parse tree](https://en.wikipedia.org/wiki/Parse_tree)

```shell
$ parsetree.py Aardvark | fold | head
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
```


### [text](https://github.com/siznax/wptools/blob/master/text.py)

Get plain text of article

```shell
$ text.py Aardvark -l | fold -s
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
```


### [wikitext](https://github.com/siznax/wptools/blob/master/wikitext.py)

Get article [wikitext](https://meta.wikimedia.org/wiki/Wiki_syntax)

```shell
$ wikitext.py Aardvark -l | head
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
```


@siznax

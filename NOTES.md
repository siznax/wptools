WPTools NOTES
=============

This is the current wptools knowledge base.

_“For reading, there will never be enough time” —Harold Bloom_

* https://www.mediawiki.org/wiki/API:Main_page
* https://www.mediawiki.org/wiki/Web_APIs_hub
* https://www.wikidata.org/wiki/Wikidata:Data_access
* https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_records

This project is listed here as "wptools":
https://www.mediawiki.org/wiki/API:Client_code#Python


Table of Contents
-----------------

* DBPedia
* Extracts
* Hovercards
* Humans
* Images
* Infobox
* Language Codes and Wikisites
* MediaWiki API
* Parse tree
* RESTBase
* URL Shortener
* WikiData
* Wikitext


DBPedia
-------

It's not clear to me how to make use of DBPedia yet.
http://dbpedia.org/page/Napoleon

* depiction => a better page_image (but see wikidata Property:P18)
* abstract => yet another version of lead section text (this may be
  Extention:TextExtracts)


Extracts
--------

Currently we get an extract of only the "lead section" (content before
the first setion) using ``action=query`` with ``&prop=extracts`` and
``&exintro``. The lead section is essentially a summary of the article.

* https://www.mediawiki.org/wiki/Extension:TextExtracts
* https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section

Example

https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles=Abraham_Lincoln

We get the extract in HTML and put it in the attribute _extract_, which
we convert to Markdown text and put that into _extext_.


Hovercards
----------

This is going to be a great feature that may yield more useful API
functions.

* https://www.mediawiki.org/wiki/Beta_Features/Hovercards
* https://www.mediawiki.org/wiki/Extension:Popups


Humans
------

A goal of this project is to make it easier for humans—all humans.
Let's have a preference for using Women, People of Color, and LGBTQ
(lesbian, gay, bisexual, transgender, and queer) people in our
examples.

**README.md**

1. Flannery O'Connor - American novelist, short story writer
2. 穐吉敏子 (ja) Toshiko Akiyoshi - Japanese American jazz musician
3. Sylvia Rivera - American bisexual transgender activist and trans woman
4. 哈莉特·塔布曼 (zh) Harriet Tubman - African-American abolitionist and humanitarian
5. Q43303 Malcolm X - American human rights activist
6. Malala Yousafzai - Pakistani children's education activist
7. Frida Kahlo - Mexican painter
8. Ella Fitzgerald - American jazz singer
9. Fela Kuti - Nigerian musician and activist
10. Stephen Fry - English comedian, actor, writer, presenter, and activist
11. Jill Lepore - American historian
12. Jeann d'Arc - folk heroine and Roman Catholic saint


Images
------

* https://www.mediawiki.org/wiki/API:Images
* https://www.mediawiki.org/wiki/Extension:PageImages
* https://github.com/siznax/wptools/issues/14 Figure out "best" image


Infobox
-------

We're getting the Infoboxen from parse tree XML, and converting it to
a dict with ``wptools.utils.template_to_dict(ptree)``.

* https://en.wikipedia.org/wiki/Help:Infobox
* https://meta.wikimedia.org/wiki/Wiki_syntax


Language Codes and Wikisites
----------------------------

Here's a list of language codes (even non-standard ones) currently in use:
https://meta.wikimedia.org/wiki/Table_of_Wikimedia_projects

Another list sorted by number of articles
https://meta.wikimedia.org/wiki/List_of_Wikipedias


MediaWiki API
-------------

https://www.mediawiki.org/wiki/Special:ApiSandbox


Parse tree
----------

We get the XML parse tree by ``action=query`` and put it into the
_parsetree_ attribute.

* https://www.mediawiki.org/wiki/User:Kephir/XML_parse_tree
* https://www.mediawiki.org/wiki/API:Parsing_wikitext
* https://www.mediawiki.org/wiki/Alternative_parsers
* https://en.wikipedia.org/wiki/Parse_tree


RESTBase
--------

https://en.wikipedia.org/api/rest_v1/

    /page/mobile-text/ => OK for lead HTML
        json["sections"[0]["items"]
        - ignore hatnote
        - prune references
        - prune IPA audio
    
    /page/mobile-sections-lead/ => NOPE
        json["sections"][0]["text"]
        - first paragraph, followed by Infobox, lead section remainder
        - needs parsing to extract lead paragraphs
    
    /page/summary/ => NOPE
        json["extract"]
        - first few sentences of plain text (truncated lead)
        + close to Google text


URL Shortener
-------------

It would be especially useful for commons media URLs.

* https://www.mediawiki.org/wiki/Extension:UrlShortener
* https://www.mediawiki.org/wiki/Requests_for_comment/URL_shortener


WikiData
--------

We get wikidata through (action=wbgetentities)
https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

* https://www.mediawiki.org/wiki/Wikibase/DataModel#Overview_of_the_data_model
* https://www.wikidata.org/wiki/Help:Wikidata_datamodel
* https://www.mediawiki.org/wiki/Wikibase/API#wbgetentities
* https://www.mediawiki.org/wiki/API:Presenting_Wikidata_knowledge

Properties

* [P17](https://www.wikidata.org/wiki/Property:P17): country
* [P18](https://www.wikidata.org/wiki/Property:P18): image
* [P30](https://www.wikidata.org/wiki/Property:P30): continent
* [P585](https://www.wikidata.org/wiki/Property:P585): point in time
* [P625](https://www.wikidata.org/wiki/Property:P625): coordinate location
* [P1343](https://www.wikidata.org/wiki/Property:P1343): described by source


Wikitext
--------

We get wikitext by ``action=parse`` and put it in the _wikitext_
attribute.

* https://www.mediawiki.org/wiki/API:Data_formats
* https://www.mediawiki.org/wiki/API:Parsing_wikitext

Probably the most direct way to get to wikitext:
https://en.wikipedia.org/wiki/Abraham_Lincoln?action=raw&section=0

But fails if there is '.' in the title:
https://en.wikipedia.org/wiki/J._R._R._Tolkien?action=raw


@siznax

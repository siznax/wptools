WPTools NOTES
=============

These preliminary notes are being migrated piecemeal to our wiki:
https://github.com/siznax/wptools/wiki

This project is listed in the MediaWiki API docs as "wptools":  
https://www.mediawiki.org/wiki/API:Client_code#Python

Table of Contents
-----------------

* [DBPedia](#dbpedia)
* [Extracts](#extracts)
* [Hovercards](#hovercards)
* [Humans](https://github.com/siznax/wptools/wiki/Humans)
* [Images](#images)
* [Infobox](#infobox)
* [Language Codes and Wikisites](#language-codes-and-wikisites)
* [MediaWiki API](#mediawiki-api)
* [Parse tree](#parse-tree)
* [RESTBase](#restbase)
* [URL Shortener](#url-shortener)
* [WikiData](https://github.com/siznax/wptools/wiki/Wikidata)
* [Wikitext](#wikitext)


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

Another list sorted by number of articles:  
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


Wikitext
--------

We get wikitext by ``action=parse`` and put it in the _wikitext_ attribute.

* https://www.mediawiki.org/wiki/API:Data_formats
* https://www.mediawiki.org/wiki/API:Parsing_wikitext

The most direct way to get to wikitext is to add ``action=raw``:  
https://en.wikipedia.org/wiki/Abraham_Lincoln?action=raw&section=0

But this seems to fail if there is '.' in the title, e.g.  
https://en.wikipedia.org/wiki/J._R._R._Tolkien?action=raw


@siznax

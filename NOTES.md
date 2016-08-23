WPTools NOTES
=============

DBPedia
-------

http://dbpedia.org/page/Napoleon

* depiction => a better page_image (but see wikidata Property:P18)
* abstract => yet another version of lead section text (this may be
  Extention:TextExtracts)


Image
-----

For a representative image, we probably want Wikidata:P18. You can
probably get away with using 'thumbnail' (Mediawiki:Query) or
'pageimage' (Mediawiki:Query), but they can be oddly inappropriate,
e.g.

    Napoleon (en)
    {
      "pageimage": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Grandes_Armes_Imp%C3%A9riales_%281804-1815%292.svg",
      "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Grandes_Armes_Imp%C3%A9riales_%281804-1815%292.svg/43px-Grandes_Armes_Imp%C3%A9riales_%281804-1815%292.svg.png",
    }

The images above are both rendering of "Imperial Coat of Arms", but
what we really want is a _portrait_ of Napoleon! We can get it from
Wikidata:P18:

    Napoleon (en)
    {
      "image": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project_2.jpg",
    }


Extension:TextExtracts
----------------------

* https://www.mediawiki.org/wiki/Extension:TextExtracts
* https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles=Aardvark


MediaWiki API
=============

https://www.mediawiki.org/wiki/Special:ApiSandbox


RESTBase
========

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


WikiData
--------

* https://www.mediawiki.org/wiki/Wikibase/DataModel#Overview_of_the_data_model
* https://www.wikidata.org/wiki/Help:Wikidata_datamodel
* https://www.mediawiki.org/wiki/Wikibase/API#wbgetentities
* https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

Property:P18 (image)
https://www.wikidata.org/w/api.php?action=wbgetentities&ids=P18&languages=en

Property:P1343 (described by source) - where the info came from
https://www.wikidata.org/wiki/Property:P1343


Wikitext
--------

Probably the most direct way to get to wikitext:
https://en.wikipedia.org/wiki/Abraham_Lincoln?action=raw&section=0

but fails if there is '.' in the title:
https://en.wikipedia.org/wiki/J._R._R._Tolkien?action=raw


@siznax

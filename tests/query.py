# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&bltitle=Douglas%20Adams&bllimit=500&exintro&formatversion=2&inprop=url|watchers&list=random|backlinks&pithumbsize=240&pllimit=500&ppprop=disambiguation|wikibase_item&prop=extracts|info|links|pageassessments|pageimages|pageprops|pageterms|redirects&redirects&rdlimit=500&rnlimit=1&rnnamespace=0&titles=Douglas%20Adams'

response = r"""
{
    "batchcomplete": true,
    "continue": {
        "rncontinue": "0.548769885863|0.54876998239|33024909|0",
        "blcontinue": "0|2062757",
        "continue": "-||extracts|info|links|pageassessments|pageimages|pageprops|pageterms|redirects"
    },
    "warnings": {
        "extracts": {
            "warnings": "HTML may be malformed and/or unbalanced and may omit inline images. Use at your own risk. Known problems are listed at https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats."
        }
    },
    "query": {
        "pages": [
            {
                "pageid": 8091,
                "ns": 0,
                "title": "Douglas Adams",
                "extract": "<p><b>Douglas Noel Adams</b> (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humorist, satirist and dramatist.</p>\n<p>Adams was author of <i>The Hitchhiker's Guide to the Galaxy</i>, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.</p>\n<p>Adams also wrote <i>Dirk Gently's Holistic Detective Agency</i> (1987) and <i>The Long Dark Tea-Time of the Soul</i> (1988), and co-wrote <i>The Meaning of Liff</i> (1983), <i>The Deeper Meaning of Liff</i> (1990), <i>Last Chance to See</i> (1990), and three stories for the television series <i>Doctor Who</i>; he also served as script editor for the show's seventeenth season in 1979. A posthumous collection of his works, including an unfinished novel, was published as <i>The Salmon of Doubt</i> in 2002.</p>\n<p>Adams was an advocate for environmentalism and conservation, a lover of fast cars, cameras, technological innovation and the Apple Macintosh, and a \"devout atheist\".</p>\n<p></p>",
                "contentmodel": "wikitext",
                "pagelanguage": "en",
                "pagelanguagehtmlcode": "en",
                "pagelanguagedir": "ltr",
                "touched": "2018-05-04T10:07:50Z",
                "lastrevid": 839576561,
                "length": 60460,
                "watchers": 463,
                "fullurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
                "editurl": "https://en.wikipedia.org/w/index.php?title=Douglas_Adams&action=edit",
                "canonicalurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
                "links": [
                    {
                        "ns": 0,
                        "title": ".Mac"
                    },
                    {
                        "ns": 0,
                        "title": "18610 Arthurdent"
                    },
                    {
                        "ns": 0,
                        "title": "25924 Douglasadams"
                    },
                    {
                        "ns": 0,
                        "title": "42 Puzzle"
                    },
                    {
                        "ns": 0,
                        "title": "69,105"
                    },
                    {
                        "ns": 0,
                        "title": "A Christmas Fairly Story"
                    },
                    {
                        "ns": 0,
                        "title": "A Mind Forever Voyaging"
                    },
                    {
                        "ns": 0,
                        "title": "Activision"
                    },
                    {
                        "ns": 0,
                        "title": "Albert Vezza"
                    },
                    {
                        "ns": 0,
                        "title": "American Atheists"
                    },
                    {
                        "ns": 0,
                        "title": "Amy Briggs"
                    },
                    {
                        "ns": 0,
                        "title": "And Another Thing... (novel)"
                    },
                    {
                        "ns": 0,
                        "title": "Anthony Read"
                    },
                    {
                        "ns": 0,
                        "title": "AppleMasters"
                    },
                    {
                        "ns": 0,
                        "title": "Apple Macintosh"
                    },
                    {
                        "ns": 0,
                        "title": "Apricot Computers"
                    },
                    {
                        "ns": 0,
                        "title": "Archive on 4"
                    },
                    {
                        "ns": 0,
                        "title": "Artemis Fowl (series)"
                    },
                    {
                        "ns": 0,
                        "title": "Arthur: The Quest for Excalibur"
                    },
                    {
                        "ns": 0,
                        "title": "Arthur Dent"
                    },
                    {
                        "ns": 0,
                        "title": "Atheist"
                    },
                    {
                        "ns": 0,
                        "title": "Audiobook"
                    },
                    {
                        "ns": 0,
                        "title": "Author"
                    },
                    {
                        "ns": 0,
                        "title": "BAFTA"
                    },
                    {
                        "ns": 0,
                        "title": "BBC"
                    },
                    {
                        "ns": 0,
                        "title": "BBC7"
                    },
                    {
                        "ns": 0,
                        "title": "BBC Micro"
                    },
                    {
                        "ns": 0,
                        "title": "BBC One"
                    },
                    {
                        "ns": 0,
                        "title": "BBC Online"
                    },
                    {
                        "ns": 0,
                        "title": "BBC Radio 4"
                    },
                    {
                        "ns": 0,
                        "title": "BBC Radio Four"
                    },
                    {
                        "ns": 0,
                        "title": "BBC Two"
                    },
                    {
                        "ns": 0,
                        "title": "BIBSYS"
                    },
                    {
                        "ns": 0,
                        "title": "Ballyhoo (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "BattleTech: The Crescent Hawk's Inception"
                    },
                    {
                        "ns": 0,
                        "title": "BattleTech: The Crescent Hawk's Revenge"
                    },
                    {
                        "ns": 0,
                        "title": "Beyond Zork"
                    },
                    {
                        "ns": 0,
                        "title": "Biblioteca Nacional de España"
                    },
                    {
                        "ns": 0,
                        "title": "Bibliothèque nationale de France"
                    },
                    {
                        "ns": 0,
                        "title": "Bidenichthys beeblebroxi"
                    },
                    {
                        "ns": 0,
                        "title": "Big Finish Productions"
                    },
                    {
                        "ns": 0,
                        "title": "Black Cinderella Two Goes East"
                    },
                    {
                        "ns": 0,
                        "title": "Black rhino"
                    },
                    {
                        "ns": 0,
                        "title": "Black rhinoceros"
                    },
                    {
                        "ns": 0,
                        "title": "Blue plaque"
                    },
                    {
                        "ns": 0,
                        "title": "Bob Bates"
                    },
                    {
                        "ns": 0,
                        "title": "Book at Bedtime"
                    },
                    {
                        "ns": 0,
                        "title": "Border Zone (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Brain Damage (song)"
                    },
                    {
                        "ns": 0,
                        "title": "Brazil"
                    },
                    {
                        "ns": 0,
                        "title": "Brentwood, Essex"
                    },
                    {
                        "ns": 0,
                        "title": "Brentwood School (England)"
                    },
                    {
                        "ns": 0,
                        "title": "Brentwood School (Essex)"
                    },
                    {
                        "ns": 0,
                        "title": "Brian Moriarty"
                    },
                    {
                        "ns": 0,
                        "title": "Bruce Daniels"
                    },
                    {
                        "ns": 0,
                        "title": "Bureaucracy (computer game)"
                    },
                    {
                        "ns": 0,
                        "title": "Bureaucracy (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Cambridge"
                    },
                    {
                        "ns": 0,
                        "title": "Cambridge Z88"
                    },
                    {
                        "ns": 0,
                        "title": "Channel9.msdn.com"
                    },
                    {
                        "ns": 0,
                        "title": "Channel 9 (discussion forum)"
                    },
                    {
                        "ns": 0,
                        "title": "Charles Thomson (artist)"
                    },
                    {
                        "ns": 0,
                        "title": "Chinese river dolphin"
                    },
                    {
                        "ns": 0,
                        "title": "Christopher Cerf (musician and television producer)"
                    },
                    {
                        "ns": 0,
                        "title": "Christopher H. Bidmead"
                    },
                    {
                        "ns": 0,
                        "title": "CiNii"
                    },
                    {
                        "ns": 0,
                        "title": "Circuit's Edge"
                    },
                    {
                        "ns": 0,
                        "title": "City of Death"
                    },
                    {
                        "ns": 0,
                        "title": "Classic Text Adventure Masterpieces of Infocom"
                    },
                    {
                        "ns": 0,
                        "title": "Cocoa (API)"
                    },
                    {
                        "ns": 0,
                        "title": "Codie"
                    },
                    {
                        "ns": 0,
                        "title": "Collaborative writing"
                    },
                    {
                        "ns": 0,
                        "title": "Commodore PET"
                    },
                    {
                        "ns": 0,
                        "title": "Conservation movement"
                    },
                    {
                        "ns": 0,
                        "title": "Cornerstone (software)"
                    },
                    {
                        "ns": 0,
                        "title": "Cutthroats (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Dave Lebling"
                    },
                    {
                        "ns": 0,
                        "title": "David Agnew"
                    },
                    {
                        "ns": 0,
                        "title": "David Fisher (writer)"
                    },
                    {
                        "ns": 0,
                        "title": "David Gilmour"
                    },
                    {
                        "ns": 0,
                        "title": "David Irving"
                    },
                    {
                        "ns": 0,
                        "title": "Deadline (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Destiny of the Daleks"
                    },
                    {
                        "ns": 0,
                        "title": "Dian Fossey"
                    },
                    {
                        "ns": 0,
                        "title": "Digital Equipment Corporation"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk (play)"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Gently"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Gently's Holistic Detective Agency"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Gently's Holistic Detective Agency (TV series)"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Gently's Holistic Detective Agency (radio serial)"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Gently (TV series)"
                    },
                    {
                        "ns": 0,
                        "title": "Dirk Maggs"
                    },
                    {
                        "ns": 0,
                        "title": "Disney"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor Snuggles"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor Who"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor Who (season 16)"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor Who spin-offs"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor in the House (TV series)"
                    },
                    {
                        "ns": 0,
                        "title": "Doctor on the Go"
                    },
                    {
                        "ns": 0,
                        "title": "Don't Panic: The Official Hitchhiker's Guide to the Galaxy Companion"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams's Guide to The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams's Starship Titanic"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams (disambiguation)"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams at the BBC"
                    },
                    {
                        "ns": 0,
                        "title": "Dramatist"
                    },
                    {
                        "ns": 0,
                        "title": "E-book"
                    },
                    {
                        "ns": 0,
                        "title": "Eagle (comic)"
                    },
                    {
                        "ns": 0,
                        "title": "Early adopter"
                    },
                    {
                        "ns": 0,
                        "title": "East End of London"
                    },
                    {
                        "ns": 0,
                        "title": "Eclipse (song)"
                    },
                    {
                        "ns": 0,
                        "title": "Edinburgh Fringe"
                    },
                    {
                        "ns": 0,
                        "title": "Embedded Systems Conference"
                    },
                    {
                        "ns": 0,
                        "title": "Embedded system"
                    },
                    {
                        "ns": 0,
                        "title": "Enchanter (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Encyclopedia Galactica"
                    },
                    {
                        "ns": 0,
                        "title": "Endangered species"
                    },
                    {
                        "ns": 0,
                        "title": "English literature"
                    },
                    {
                        "ns": 0,
                        "title": "Environmental activist"
                    },
                    {
                        "ns": 0,
                        "title": "Eoin Colfer"
                    },
                    {
                        "ns": 0,
                        "title": "Erechthias beeblebroxi"
                    },
                    {
                        "ns": 0,
                        "title": "Essayist"
                    },
                    {
                        "ns": 0,
                        "title": "Exhibition (scholarship)"
                    },
                    {
                        "ns": 0,
                        "title": "Find a Grave"
                    },
                    {
                        "ns": 0,
                        "title": "Fine-tuned Universe"
                    },
                    {
                        "ns": 0,
                        "title": "Fooblitzky"
                    },
                    {
                        "ns": 0,
                        "title": "Footlights"
                    },
                    {
                        "ns": 0,
                        "title": "Ford Prefect (character)"
                    },
                    {
                        "ns": 0,
                        "title": "Gareth Roberts (writer)"
                    },
                    {
                        "ns": 0,
                        "title": "Geoffrey Perkins"
                    },
                    {
                        "ns": 0,
                        "title": "Get Lamp"
                    },
                    {
                        "ns": 0,
                        "title": "Google Doodle"
                    },
                    {
                        "ns": 0,
                        "title": "Graham Chapman"
                    },
                    {
                        "ns": 0,
                        "title": "Graham Williams (television producer)"
                    },
                    {
                        "ns": 0,
                        "title": "Great Ape Project"
                    },
                    {
                        "ns": 0,
                        "title": "Gregory Hines"
                    },
                    {
                        "ns": 0,
                        "title": "Griff Rhys Jones"
                    },
                    {
                        "ns": 0,
                        "title": "Grue (monster)"
                    },
                    {
                        "ns": 0,
                        "title": "H2g2"
                    },
                    {
                        "ns": 0,
                        "title": "Harmony Books"
                    },
                    {
                        "ns": 0,
                        "title": "Harvey Mudd College"
                    },
                    {
                        "ns": 0,
                        "title": "Hello, sailor"
                    },
                    {
                        "ns": 0,
                        "title": "Highgate Cemetery"
                    },
                    {
                        "ns": 0,
                        "title": "Hitch-hiker's Guide to Europe"
                    },
                    {
                        "ns": 0,
                        "title": "Hitchcon"
                    },
                    {
                        "ns": 0,
                        "title": "Hitchhiker: A Biography of Douglas Adams"
                    },
                    {
                        "ns": 0,
                        "title": "Hollywood Hijinx"
                    },
                    {
                        "ns": 0,
                        "title": "Hugo Award"
                    },
                    {
                        "ns": 0,
                        "title": "Hugo Award for Best Dramatic Presentation"
                    },
                    {
                        "ns": 0,
                        "title": "Hyperland"
                    },
                    {
                        "ns": 0,
                        "title": "Hypertext"
                    },
                    {
                        "ns": 0,
                        "title": "IMDb"
                    },
                    {
                        "ns": 0,
                        "title": "IMovie"
                    },
                    {
                        "ns": 0,
                        "title": "ITV (TV network)"
                    },
                    {
                        "ns": 0,
                        "title": "Implementer (video games)"
                    },
                    {
                        "ns": 0,
                        "title": "Infidel (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "InfoTaskForce"
                    },
                    {
                        "ns": 0,
                        "title": "Infocom"
                    },
                    {
                        "ns": 0,
                        "title": "Innsbruck"
                    },
                    {
                        "ns": 0,
                        "title": "Integrated Authority File"
                    },
                    {
                        "ns": 0,
                        "title": "Interactive fiction"
                    },
                    {
                        "ns": 0,
                        "title": "International Standard Book Number"
                    },
                    {
                        "ns": 0,
                        "title": "International Standard Name Identifier"
                    },
                    {
                        "ns": 0,
                        "title": "International Standard Serial Number"
                    },
                    {
                        "ns": 0,
                        "title": "InvisiClues"
                    },
                    {
                        "ns": 0,
                        "title": "Islington"
                    },
                    {
                        "ns": 0,
                        "title": "Istituto Centrale per il Catalogo Unico"
                    },
                    {
                        "ns": 0,
                        "title": "Jack Straw"
                    },
                    {
                        "ns": 0,
                        "title": "James Clavell's Shōgun"
                    },
                    {
                        "ns": 0,
                        "title": "James Goss (producer)"
                    },
                    {
                        "ns": 0,
                        "title": "Jane Belson"
                    },
                    {
                        "ns": 0,
                        "title": "Joe Ybarra"
                    },
                    {
                        "ns": 0,
                        "title": "John Cleese"
                    },
                    {
                        "ns": 0,
                        "title": "John Lloyd (producer)"
                    },
                    {
                        "ns": 0,
                        "title": "Journey (1989 video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Kakapo"
                    },
                    {
                        "ns": 0,
                        "title": "Karey Kirkpatrick"
                    },
                    {
                        "ns": 0,
                        "title": "Kim Fuller"
                    },
                    {
                        "ns": 0,
                        "title": "Knowledge Navigator"
                    },
                    {
                        "ns": 0,
                        "title": "LIBRIS"
                    },
                    {
                        "ns": 0,
                        "title": "Labyrinth: The Computer Game"
                    },
                    {
                        "ns": 0,
                        "title": "Last Chance to See"
                    },
                    {
                        "ns": 0,
                        "title": "Leather Goddesses of Phobos"
                    },
                    {
                        "ns": 0,
                        "title": "Leather Goddesses of Phobos 2: Gas Pump Girls Meet the Pulsating Inconvenience from Planet X!"
                    },
                    {
                        "ns": 0,
                        "title": "Legend Entertainment"
                    },
                    {
                        "ns": 0,
                        "title": "Legends of Zork"
                    },
                    {
                        "ns": 0,
                        "title": "Library of Congress Control Number"
                    },
                    {
                        "ns": 0,
                        "title": "Life, the Universe and Everything"
                    },
                    {
                        "ns": 0,
                        "title": "List of Doctor Who episodes (1963–1989)"
                    },
                    {
                        "ns": 0,
                        "title": "List of Monty Python's Flying Circus episodes"
                    },
                    {
                        "ns": 0,
                        "title": "List of humorists"
                    },
                    {
                        "ns": 0,
                        "title": "List of minor The Hitchhiker's Guide to the Galaxy characters"
                    },
                    {
                        "ns": 0,
                        "title": "List of races and species in The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "List of recurring Monty Python's Flying Circus characters"
                    },
                    {
                        "ns": 0,
                        "title": "Lucasfilm Games"
                    },
                    {
                        "ns": 0,
                        "title": "MacUser"
                    },
                    {
                        "ns": 0,
                        "title": "Mac OS X"
                    },
                    {
                        "ns": 0,
                        "title": "Marc Blank"
                    },
                    {
                        "ns": 0,
                        "title": "Mark Carwardine"
                    },
                    {
                        "ns": 0,
                        "title": "Marvin the Paranoid Android"
                    },
                    {
                        "ns": 0,
                        "title": "Michael Berlyn"
                    },
                    {
                        "ns": 0,
                        "title": "Michael Palin"
                    },
                    {
                        "ns": 0,
                        "title": "Microsoft"
                    },
                    {
                        "ns": 0,
                        "title": "Mines of Titan"
                    },
                    {
                        "ns": 0,
                        "title": "Minor Planet Center"
                    },
                    {
                        "ns": 0,
                        "title": "Minor Planet Circular"
                    },
                    {
                        "ns": 0,
                        "title": "Montecito, California"
                    },
                    {
                        "ns": 0,
                        "title": "Monty Python"
                    },
                    {
                        "ns": 0,
                        "title": "Monty Python's Flying Circus"
                    },
                    {
                        "ns": 0,
                        "title": "Moonmist"
                    },
                    {
                        "ns": 0,
                        "title": "Mostly Harmless"
                    },
                    {
                        "ns": 0,
                        "title": "Mount Kilimanjaro"
                    },
                    {
                        "ns": 0,
                        "title": "Mountain gorilla"
                    },
                    {
                        "ns": 0,
                        "title": "MusicBrainz"
                    },
                    {
                        "ns": 0,
                        "title": "Myocardial infarction"
                    },
                    {
                        "ns": 0,
                        "title": "National Diet Library"
                    },
                    {
                        "ns": 0,
                        "title": "National Library of Australia"
                    },
                    {
                        "ns": 0,
                        "title": "National Library of the Czech Republic"
                    },
                    {
                        "ns": 0,
                        "title": "National Public Radio"
                    },
                    {
                        "ns": 0,
                        "title": "Natural history"
                    },
                    {
                        "ns": 0,
                        "title": "Neil Gaiman"
                    },
                    {
                        "ns": 0,
                        "title": "Neil Innes"
                    },
                    {
                        "ns": 0,
                        "title": "Noel Edmonds"
                    },
                    {
                        "ns": 0,
                        "title": "Nord and Bert Couldn't Make Head or Tail of It"
                    },
                    {
                        "ns": 0,
                        "title": "Northern white rhinoceros"
                    },
                    {
                        "ns": 0,
                        "title": "Not the Nine O'Clock News"
                    },
                    {
                        "ns": 0,
                        "title": "One of These Nights"
                    },
                    {
                        "ns": 0,
                        "title": "Out of the Trees"
                    },
                    {
                        "ns": 0,
                        "title": "Paola Cavalieri"
                    },
                    {
                        "ns": 0,
                        "title": "Patient Abuse"
                    },
                    {
                        "ns": 0,
                        "title": "Paul McCartney"
                    },
                    {
                        "ns": 0,
                        "title": "Paul McGann"
                    },
                    {
                        "ns": 0,
                        "title": "Paul Neil Milne Johnstone"
                    },
                    {
                        "ns": 0,
                        "title": "Paul Wickens"
                    },
                    {
                        "ns": 0,
                        "title": "Peter Fincham"
                    },
                    {
                        "ns": 0,
                        "title": "Peter Singer"
                    },
                    {
                        "ns": 0,
                        "title": "Peter Stothard"
                    },
                    {
                        "ns": 0,
                        "title": "Phrases from The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "Pilot (Dirk Gently)"
                    },
                    {
                        "ns": 0,
                        "title": "Pink Floyd"
                    },
                    {
                        "ns": 0,
                        "title": "Places in The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "Planetfall"
                    },
                    {
                        "ns": 0,
                        "title": "Plundered Hearts"
                    },
                    {
                        "ns": 0,
                        "title": "Preparatory school (UK)"
                    },
                    {
                        "ns": 0,
                        "title": "Procol Harum"
                    },
                    {
                        "ns": 0,
                        "title": "Professional Developers Conference"
                    },
                    {
                        "ns": 0,
                        "title": "Professor Chronotis"
                    },
                    {
                        "ns": 0,
                        "title": "Quarterstaff: The Tomb of Setmoth"
                    },
                    {
                        "ns": 0,
                        "title": "RSPCA"
                    },
                    {
                        "ns": 0,
                        "title": "Radio Academy"
                    },
                    {
                        "ns": 0,
                        "title": "Rainbow 100"
                    },
                    {
                        "ns": 0,
                        "title": "Return to Zork"
                    },
                    {
                        "ns": 0,
                        "title": "Richard Dawkins"
                    },
                    {
                        "ns": 0,
                        "title": "Robin Day"
                    },
                    {
                        "ns": 0,
                        "title": "Russian State Library"
                    },
                    {
                        "ns": 0,
                        "title": "SNAC"
                    },
                    {
                        "ns": 0,
                        "title": "Sally Emerson"
                    },
                    {
                        "ns": 0,
                        "title": "Salon (website)"
                    },
                    {
                        "ns": 0,
                        "title": "Santa Barbara, California"
                    },
                    {
                        "ns": 0,
                        "title": "Satirist"
                    },
                    {
                        "ns": 0,
                        "title": "Save the Rhino"
                    },
                    {
                        "ns": 0,
                        "title": "Script editor"
                    },
                    {
                        "ns": 0,
                        "title": "Scriptwriter"
                    },
                    {
                        "ns": 0,
                        "title": "Seastalker"
                    },
                    {
                        "ns": 0,
                        "title": "Shada (Doctor Who)"
                    },
                    {
                        "ns": 0,
                        "title": "Sherlock: The Riddle of the Crown Jewels"
                    },
                    {
                        "ns": 0,
                        "title": "Sic"
                    },
                    {
                        "ns": 0,
                        "title": "Simon & Schuster"
                    },
                    {
                        "ns": 0,
                        "title": "Simon Brett"
                    },
                    {
                        "ns": 0,
                        "title": "Simon Jones (actor)"
                    },
                    {
                        "ns": 0,
                        "title": "Slartibartfast"
                    },
                    {
                        "ns": 0,
                        "title": "So Long, and Thanks for All the Fish"
                    },
                    {
                        "ns": 0,
                        "title": "Somebody else's problem"
                    },
                    {
                        "ns": 0,
                        "title": "Sorcerer (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Spellbreaker"
                    },
                    {
                        "ns": 0,
                        "title": "St. Cedd's College, Cambridge"
                    },
                    {
                        "ns": 0,
                        "title": "St John's College, Cambridge"
                    },
                    {
                        "ns": 0,
                        "title": "St Martin-in-the-Fields"
                    },
                    {
                        "ns": 0,
                        "title": "Starcross (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Starship Titanic"
                    },
                    {
                        "ns": 0,
                        "title": "Stationfall"
                    },
                    {
                        "ns": 0,
                        "title": "Stephen Fry"
                    },
                    {
                        "ns": 0,
                        "title": "Steve Meretzky"
                    },
                    {
                        "ns": 0,
                        "title": "Steven Moffat"
                    },
                    {
                        "ns": 0,
                        "title": "Strike action"
                    },
                    {
                        "ns": 0,
                        "title": "Stuckism"
                    },
                    {
                        "ns": 0,
                        "title": "Suspect (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Suspended (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Système universitaire de documentation"
                    },
                    {
                        "ns": 0,
                        "title": "TED (conference)"
                    },
                    {
                        "ns": 0,
                        "title": "Tandy 1000"
                    },
                    {
                        "ns": 0,
                        "title": "Tanzania"
                    },
                    {
                        "ns": 0,
                        "title": "Technological innovation"
                    },
                    {
                        "ns": 0,
                        "title": "Technology in The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "Ted Nelson"
                    },
                    {
                        "ns": 0,
                        "title": "Terry Jones"
                    },
                    {
                        "ns": 0,
                        "title": "The Album of the Soundtrack of the Trailer of the Film of Monty Python and the Holy Grail"
                    },
                    {
                        "ns": 0,
                        "title": "The Beatles"
                    },
                    {
                        "ns": 0,
                        "title": "The Burkiss Way"
                    },
                    {
                        "ns": 0,
                        "title": "The Daily Telegraph"
                    },
                    {
                        "ns": 0,
                        "title": "The Deeper Meaning of Liff"
                    },
                    {
                        "ns": 0,
                        "title": "The Digital Village"
                    },
                    {
                        "ns": 0,
                        "title": "The Division Bell"
                    },
                    {
                        "ns": 0,
                        "title": "The Doctor (Doctor Who)"
                    },
                    {
                        "ns": 0,
                        "title": "The God Delusion"
                    },
                    {
                        "ns": 0,
                        "title": "The Guardian"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Future"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy: The Original Radio Scripts"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (TV series)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (book)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (computer game)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (fictional)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (film)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (novel)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (radio series)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy Primary and Secondary Phases"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy Tertiary to Hexagonal Phases"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy Tertiary to Quintessential Phases"
                    },
                    {
                        "ns": 0,
                        "title": "The Hitchhiker's Guide to the Galaxy cast lists"
                    },
                    {
                        "ns": 0,
                        "title": "The Independent on Sunday"
                    },
                    {
                        "ns": 0,
                        "title": "The Key to Time"
                    },
                    {
                        "ns": 0,
                        "title": "The Long Dark Tea-Time of the Soul"
                    },
                    {
                        "ns": 0,
                        "title": "The Long Dark Tea-Time of the Soul (radio serial)"
                    },
                    {
                        "ns": 0,
                        "title": "The Lost Treasures of Infocom"
                    },
                    {
                        "ns": 0,
                        "title": "The Lurking Horror"
                    },
                    {
                        "ns": 0,
                        "title": "The Meaning of Liff"
                    },
                    {
                        "ns": 0,
                        "title": "The News Huddlines"
                    },
                    {
                        "ns": 0,
                        "title": "The Pirate Planet"
                    },
                    {
                        "ns": 0,
                        "title": "The Private Life of Genghis Khan"
                    },
                    {
                        "ns": 0,
                        "title": "The Restaurant at the End of the Universe"
                    },
                    {
                        "ns": 0,
                        "title": "The Salmon of Doubt"
                    },
                    {
                        "ns": 0,
                        "title": "The Snowmen"
                    },
                    {
                        "ns": 0,
                        "title": "The Times"
                    },
                    {
                        "ns": 0,
                        "title": "The Utterly Utterly Merry Comic Relief Christmas Book"
                    },
                    {
                        "ns": 0,
                        "title": "The Witness (1983 video game)"
                    },
                    {
                        "ns": 0,
                        "title": "Tim Anderson (programmer)"
                    },
                    {
                        "ns": 0,
                        "title": "Timeline of The Hitchhiker's Guide to the Galaxy versions"
                    },
                    {
                        "ns": 0,
                        "title": "Tom Baker"
                    },
                    {
                        "ns": 0,
                        "title": "Tombs & Treasure"
                    },
                    {
                        "ns": 0,
                        "title": "Towel Day"
                    },
                    {
                        "ns": 0,
                        "title": "Trafalgar Square"
                    },
                    {
                        "ns": 0,
                        "title": "Trillian (character)"
                    },
                    {
                        "ns": 0,
                        "title": "Trinity (video game)"
                    },
                    {
                        "ns": 0,
                        "title": "USENET"
                    },
                    {
                        "ns": 0,
                        "title": "University of Cambridge"
                    },
                    {
                        "ns": 0,
                        "title": "Upper Street"
                    },
                    {
                        "ns": 0,
                        "title": "Virtual International Authority File"
                    },
                    {
                        "ns": 0,
                        "title": "Vogon"
                    },
                    {
                        "ns": 0,
                        "title": "Wayback Machine"
                    },
                    {
                        "ns": 0,
                        "title": "Webcast"
                    },
                    {
                        "ns": 0,
                        "title": "Week Ending"
                    },
                    {
                        "ns": 0,
                        "title": "West End of London"
                    },
                    {
                        "ns": 0,
                        "title": "Westwood Studios"
                    },
                    {
                        "ns": 0,
                        "title": "William Blake"
                    },
                    {
                        "ns": 0,
                        "title": "William Todd-Jones"
                    },
                    {
                        "ns": 0,
                        "title": "Wish You Were Here (1975 song)"
                    },
                    {
                        "ns": 0,
                        "title": "Wishbringer"
                    },
                    {
                        "ns": 0,
                        "title": "Word processor"
                    },
                    {
                        "ns": 0,
                        "title": "WorldCat"
                    },
                    {
                        "ns": 0,
                        "title": "Writer's block"
                    },
                    {
                        "ns": 0,
                        "title": "Young Zaphod Plays It Safe"
                    },
                    {
                        "ns": 0,
                        "title": "Z-machine"
                    },
                    {
                        "ns": 0,
                        "title": "Zaire"
                    },
                    {
                        "ns": 0,
                        "title": "Zaphod Beeblebrox"
                    },
                    {
                        "ns": 0,
                        "title": "Zork"
                    },
                    {
                        "ns": 0,
                        "title": "Zork: Grand Inquisitor"
                    },
                    {
                        "ns": 0,
                        "title": "Zork: The Undiscovered Underground"
                    },
                    {
                        "ns": 0,
                        "title": "Zork I"
                    },
                    {
                        "ns": 0,
                        "title": "Zork II"
                    },
                    {
                        "ns": 0,
                        "title": "Zork III"
                    },
                    {
                        "ns": 0,
                        "title": "Zork Nemesis"
                    },
                    {
                        "ns": 0,
                        "title": "Zork Zero"
                    },
                    {
                        "ns": 0,
                        "title": "Zork books"
                    },
                    {
                        "ns": 4,
                        "title": "Wikipedia:LIBRARY"
                    },
                    {
                        "ns": 10,
                        "title": "Template:Dirk Gently"
                    },
                    {
                        "ns": 10,
                        "title": "Template:Douglas Adams"
                    },
                    {
                        "ns": 10,
                        "title": "Template:Infocom games"
                    },
                    {
                        "ns": 10,
                        "title": "Template:The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 11,
                        "title": "Template talk:Dirk Gently"
                    },
                    {
                        "ns": 11,
                        "title": "Template talk:Douglas Adams"
                    },
                    {
                        "ns": 11,
                        "title": "Template talk:Infocom games"
                    },
                    {
                        "ns": 11,
                        "title": "Template talk:The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 12,
                        "title": "Help:Authority control"
                    },
                    {
                        "ns": 14,
                        "title": "Category:CS1 maint: Extra text: authors list"
                    },
                    {
                        "ns": 14,
                        "title": "Category:CS1 maint: Extra text: editors list"
                    },
                    {
                        "ns": 14,
                        "title": "Category:CS1 maint: Multiple names: authors list"
                    },
                    {
                        "ns": 14,
                        "title": "Category:The Hitchhiker's Guide to the Galaxy"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Use British English from October 2013"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Use dmy dates from April 2015"
                    },
                    {
                        "ns": 100,
                        "title": "Portal:Hitchhiker's"
                    }
                ],
                "pageassessments": {
                    "Biography": {
                        "class": "B",
                        "importance": ""
                    },
                    "Wikipedia 1.0": {
                        "class": "C",
                        "importance": "Mid"
                    },
                    "Science Fiction": {
                        "class": "C",
                        "importance": "Mid"
                    },
                    "Comedy": {
                        "class": "B",
                        "importance": "Mid"
                    },
                    "London": {
                        "class": "B",
                        "importance": "Low"
                    },
                    "Atheism": {
                        "class": "B",
                        "importance": "Low"
                    },
                    "BBC": {
                        "class": "B",
                        "importance": "Low"
                    },
                    "Monty Python": {
                        "class": "B",
                        "importance": "Mid"
                    },
                    "Hitchhiker's Guide to the Galaxy": {
                        "class": "",
                        "importance": ""
                    },
                    "Doctor Who": {
                        "class": "B",
                        "importance": "Low"
                    }
                },
                "thumbnail": {
                    "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Douglas_adams_portrait_cropped.jpg/207px-Douglas_adams_portrait_cropped.jpg",
                    "width": 207,
                    "height": 240
                },
                "pageimage": "Douglas_adams_portrait_cropped.jpg",
                "pageprops": {
                    "wikibase_item": "Q42"
                },
                "terms": {
                    "alias": [
                        "Douglas N. Adams",
                        "Douglas Noel Adams",
                        "Douglas Noël Adams"
                    ],
                    "description": [
                        "author"
                    ],
                    "label": [
                        "Douglas Adams"
                    ]
                },
                "redirects": [
                    {
                        "pageid": 421613,
                        "ns": 0,
                        "title": "Douglas Noël Adams"
                    },
                    {
                        "pageid": 442167,
                        "ns": 0,
                        "title": "Douglas Adams Biography"
                    },
                    {
                        "pageid": 555606,
                        "ns": 0,
                        "title": "Douglas Noel Adams"
                    },
                    {
                        "pageid": 697699,
                        "ns": 0,
                        "title": "Bop Ad"
                    },
                    {
                        "pageid": 742979,
                        "ns": 0,
                        "title": "Adams, Douglas"
                    },
                    {
                        "pageid": 799056,
                        "ns": 0,
                        "title": "Adams, Douglas Noel"
                    },
                    {
                        "pageid": 911959,
                        "ns": 0,
                        "title": "Douglas adams"
                    },
                    {
                        "pageid": 944266,
                        "ns": 0,
                        "title": "Douglass adams"
                    },
                    {
                        "pageid": 19511273,
                        "ns": 0,
                        "title": "Jane Belson"
                    },
                    {
                        "pageid": 31976318,
                        "ns": 0,
                        "title": "Douglas Adams bibliography"
                    },
                    {
                        "pageid": 35473253,
                        "ns": 0,
                        "title": "Adams, Douglas Noël"
                    },
                    {
                        "pageid": 41687224,
                        "ns": 0,
                        "title": "Adamsian"
                    }
                ]
            }
        ],
        "random": [
            {
                "id": 38647742,
                "ns": 0,
                "title": "Deh-e Sukhteh, Manj"
            }
        ],
        "backlinks": [
            {
                "pageid": 1132,
                "ns": 0,
                "title": "The Ashes"
            },
            {
                "pageid": 1868,
                "ns": 1,
                "title": "Talk:The Ashes"
            },
            {
                "pageid": 4961,
                "ns": 0,
                "title": "Bovril"
            },
            {
                "pageid": 7626,
                "ns": 0,
                "title": "Cetacea"
            },
            {
                "pageid": 8192,
                "ns": 0,
                "title": "Detective fiction"
            },
            {
                "pageid": 8209,
                "ns": 0,
                "title": "Doctor Who"
            },
            {
                "pageid": 13024,
                "ns": 0,
                "title": "Graham Chapman"
            },
            {
                "pageid": 13044,
                "ns": 0,
                "title": "Gin and tonic"
            },
            {
                "pageid": 13744,
                "ns": 0,
                "title": "List of humorists"
            },
            {
                "pageid": 14788,
                "ns": 0,
                "title": "Infocom"
            },
            {
                "pageid": 14789,
                "ns": 0,
                "title": "Interactive fiction"
            },
            {
                "pageid": 15858,
                "ns": 0,
                "title": "John Cleese"
            },
            {
                "pageid": 15907,
                "ns": 0,
                "title": "Jabberwocky"
            },
            {
                "pageid": 17967,
                "ns": 0,
                "title": "Liar paradox"
            },
            {
                "pageid": 18942,
                "ns": 0,
                "title": "Monty Python"
            },
            {
                "pageid": 19354,
                "ns": 0,
                "title": "May 25"
            },
            {
                "pageid": 19452,
                "ns": 0,
                "title": "May 11"
            },
            {
                "pageid": 19530,
                "ns": 0,
                "title": "March 11"
            },
            {
                "pageid": 20347,
                "ns": 0,
                "title": "Meaning of life"
            },
            {
                "pageid": 22530,
                "ns": 0,
                "title": "October 12"
            },
            {
                "pageid": 24145,
                "ns": 0,
                "title": "Pun"
            },
            {
                "pageid": 24936,
                "ns": 0,
                "title": "Pneumatic tube"
            },
            {
                "pageid": 25228,
                "ns": 0,
                "title": "Q.E.D."
            },
            {
                "pageid": 25867,
                "ns": 0,
                "title": "Richard Dawkins"
            },
            {
                "pageid": 26093,
                "ns": 1,
                "title": "Talk:Rape/Archive 5"
            },
            {
                "pageid": 26110,
                "ns": 0,
                "title": "List of fictional robots and androids"
            },
            {
                "pageid": 27485,
                "ns": 0,
                "title": "Slartibartfast"
            },
            {
                "pageid": 31347,
                "ns": 0,
                "title": "Trilogy"
            },
            {
                "pageid": 31353,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 33139,
                "ns": 0,
                "title": "World Wide Web"
            },
            {
                "pageid": 33822,
                "ns": 0,
                "title": "Westwood Studios"
            },
            {
                "pageid": 34419,
                "ns": 0,
                "title": "Zork"
            },
            {
                "pageid": 34505,
                "ns": 0,
                "title": "Z-machine"
            },
            {
                "pageid": 34551,
                "ns": 0,
                "title": "2001"
            },
            {
                "pageid": 34575,
                "ns": 0,
                "title": "1952"
            },
            {
                "pageid": 34753,
                "ns": 0,
                "title": "1978"
            },
            {
                "pageid": 36995,
                "ns": 0,
                "title": "Cambridge"
            },
            {
                "pageid": 37589,
                "ns": 0,
                "title": "Dorset"
            },
            {
                "pageid": 38299,
                "ns": 0,
                "title": "Activision"
            },
            {
                "pageid": 40594,
                "ns": 0,
                "title": "Pseudonym"
            },
            {
                "pageid": 42515,
                "ns": 0,
                "title": "Infinite monkey theorem"
            },
            {
                "pageid": 45061,
                "ns": 0,
                "title": "From Hell"
            },
            {
                "pageid": 47761,
                "ns": 0,
                "title": "Hitchhiking"
            },
            {
                "pageid": 48713,
                "ns": 0,
                "title": "St John's College, Cambridge"
            },
            {
                "pageid": 49626,
                "ns": 0,
                "title": "Suspended (video game)"
            },
            {
                "pageid": 50223,
                "ns": 0,
                "title": "Dirk Gently's Holistic Detective Agency"
            },
            {
                "pageid": 50377,
                "ns": 1,
                "title": "Talk:Finnish language"
            },
            {
                "pageid": 51800,
                "ns": 0,
                "title": "Terry Jones"
            },
            {
                "pageid": 53606,
                "ns": 0,
                "title": "List of science-fiction authors"
            },
            {
                "pageid": 53878,
                "ns": 0,
                "title": "Betelgeuse"
            },
            {
                "pageid": 54633,
                "ns": 0,
                "title": "Thursday"
            },
            {
                "pageid": 56282,
                "ns": 0,
                "title": "The Salmon of Doubt"
            },
            {
                "pageid": 60133,
                "ns": 0,
                "title": "Foundation series"
            },
            {
                "pageid": 60364,
                "ns": 0,
                "title": "Mostly Harmless"
            },
            {
                "pageid": 63401,
                "ns": 0,
                "title": "Stephen Fry"
            },
            {
                "pageid": 65308,
                "ns": 0,
                "title": "Apocalyptic and post-apocalyptic fiction"
            },
            {
                "pageid": 65616,
                "ns": 0,
                "title": "List of British comedians"
            },
            {
                "pageid": 66042,
                "ns": 0,
                "title": "List of science fiction sitcoms"
            },
            {
                "pageid": 66047,
                "ns": 0,
                "title": "Comic science fiction"
            },
            {
                "pageid": 66939,
                "ns": 0,
                "title": "List of fantasy authors"
            },
            {
                "pageid": 69111,
                "ns": 0,
                "title": "So Long, and Thanks for All the Fish"
            },
            {
                "pageid": 70188,
                "ns": 0,
                "title": "Highgate Cemetery"
            },
            {
                "pageid": 75912,
                "ns": 0,
                "title": "Time Lord"
            },
            {
                "pageid": 77783,
                "ns": 0,
                "title": "Guildford"
            },
            {
                "pageid": 78548,
                "ns": 1,
                "title": "Talk:Douglas Adams"
            },
            {
                "pageid": 78936,
                "ns": 2,
                "title": "User:ChrispyH"
            },
            {
                "pageid": 78975,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy: The Original Radio Scripts"
            },
            {
                "pageid": 79904,
                "ns": 0,
                "title": "Ford Prefect (character)"
            },
            {
                "pageid": 79907,
                "ns": 0,
                "title": "The Meaning of Liff"
            },
            {
                "pageid": 82998,
                "ns": 0,
                "title": "Sniglet"
            },
            {
                "pageid": 84636,
                "ns": 0,
                "title": "OK Computer"
            },
            {
                "pageid": 87916,
                "ns": 0,
                "title": "Planets in science fiction"
            },
            {
                "pageid": 88468,
                "ns": 0,
                "title": "The Pirate Planet"
            },
            {
                "pageid": 88470,
                "ns": 0,
                "title": "Shada (Doctor Who)"
            },
            {
                "pageid": 88472,
                "ns": 0,
                "title": "City of Death"
            },
            {
                "pageid": 89074,
                "ns": 0,
                "title": "Kakapo"
            },
            {
                "pageid": 89388,
                "ns": 0,
                "title": "Trillian (software)"
            },
            {
                "pageid": 89603,
                "ns": 0,
                "title": "Joanna Lumley"
            },
            {
                "pageid": 91431,
                "ns": 3,
                "title": "User talk:Jbrave"
            },
            {
                "pageid": 92321,
                "ns": 0,
                "title": "Nonsense verse"
            },
            {
                "pageid": 92896,
                "ns": 0,
                "title": "Romana (Doctor Who)"
            },
            {
                "pageid": 93792,
                "ns": 0,
                "title": "Christopher Moore (author)"
            },
            {
                "pageid": 94097,
                "ns": 0,
                "title": "Highgate"
            },
            {
                "pageid": 94105,
                "ns": 0,
                "title": "Holloway, London"
            },
            {
                "pageid": 94222,
                "ns": 0,
                "title": "Penge"
            },
            {
                "pageid": 95855,
                "ns": 0,
                "title": "Islington"
            },
            {
                "pageid": 101888,
                "ns": 0,
                "title": "List of fictional computers"
            },
            {
                "pageid": 108137,
                "ns": 0,
                "title": "Montecito, California"
            },
            {
                "pageid": 140193,
                "ns": 0,
                "title": "Sheridan, Wyoming"
            },
            {
                "pageid": 140648,
                "ns": 0,
                "title": "The Long Dark Tea-Time of the Soul"
            },
            {
                "pageid": 141949,
                "ns": 0,
                "title": "Gretna Green"
            },
            {
                "pageid": 142580,
                "ns": 0,
                "title": "Misotheism"
            },
            {
                "pageid": 143372,
                "ns": 3,
                "title": "User talk:Lezek"
            },
            {
                "pageid": 143385,
                "ns": 1,
                "title": "Talk:Gin and tonic"
            },
            {
                "pageid": 143994,
                "ns": 0,
                "title": "Zaphod Beeblebrox"
            },
            {
                "pageid": 145128,
                "ns": 0,
                "title": "Algorithmic efficiency"
            },
            {
                "pageid": 148264,
                "ns": 0,
                "title": "The Digital Village"
            },
            {
                "pageid": 153103,
                "ns": 0,
                "title": "Jane Horrocks"
            },
            {
                "pageid": 158111,
                "ns": 0,
                "title": "Zebra crossing"
            },
            {
                "pageid": 159943,
                "ns": 0,
                "title": "Starship Titanic"
            },
            {
                "pageid": 159973,
                "ns": 0,
                "title": "Marvin the Paranoid Android"
            },
            {
                "pageid": 159979,
                "ns": 0,
                "title": "Arthur Dent"
            },
            {
                "pageid": 161366,
                "ns": 0,
                "title": "Tom Baker"
            },
            {
                "pageid": 165320,
                "ns": 0,
                "title": "Jodrell Bank Observatory"
            },
            {
                "pageid": 167583,
                "ns": 0,
                "title": "BBC Radio"
            },
            {
                "pageid": 168977,
                "ns": 0,
                "title": "Trillian (character)"
            },
            {
                "pageid": 169104,
                "ns": 1,
                "title": "Talk:Infocom"
            },
            {
                "pageid": 169201,
                "ns": 0,
                "title": "Neil Innes"
            },
            {
                "pageid": 169363,
                "ns": 0,
                "title": "Doctor Snuggles"
            },
            {
                "pageid": 169367,
                "ns": 0,
                "title": "John Lloyd (producer)"
            },
            {
                "pageid": 173560,
                "ns": 0,
                "title": "English novel"
            },
            {
                "pageid": 174653,
                "ns": 0,
                "title": "Parallel universes in fiction"
            },
            {
                "pageid": 175570,
                "ns": 0,
                "title": "Bloom County"
            },
            {
                "pageid": 175946,
                "ns": 0,
                "title": "David Gilmour"
            },
            {
                "pageid": 182263,
                "ns": 1,
                "title": "Talk:John Logie Baird"
            },
            {
                "pageid": 188472,
                "ns": 0,
                "title": "Level 42"
            },
            {
                "pageid": 190173,
                "ns": 0,
                "title": "List of years in literature"
            },
            {
                "pageid": 190185,
                "ns": 0,
                "title": "2001 in literature"
            },
            {
                "pageid": 190210,
                "ns": 0,
                "title": "1990 in literature"
            },
            {
                "pageid": 190213,
                "ns": 0,
                "title": "1987 in literature"
            },
            {
                "pageid": 190227,
                "ns": 0,
                "title": "1980 in literature"
            },
            {
                "pageid": 190228,
                "ns": 0,
                "title": "1979 in literature"
            },
            {
                "pageid": 190428,
                "ns": 0,
                "title": "1978 in literature"
            },
            {
                "pageid": 190921,
                "ns": 0,
                "title": "1952 in literature"
            },
            {
                "pageid": 191067,
                "ns": 0,
                "title": "1977 in literature"
            },
            {
                "pageid": 191173,
                "ns": 0,
                "title": "Life, the Universe and Everything"
            },
            {
                "pageid": 191178,
                "ns": 0,
                "title": "42 (number)"
            },
            {
                "pageid": 193278,
                "ns": 0,
                "title": "List of songs that retell a work of literature"
            },
            {
                "pageid": 195642,
                "ns": 0,
                "title": "List of works published posthumously"
            },
            {
                "pageid": 197730,
                "ns": 0,
                "title": "Alternate reality game"
            },
            {
                "pageid": 202349,
                "ns": 0,
                "title": "The Restaurant at the End of the Universe"
            },
            {
                "pageid": 202358,
                "ns": 0,
                "title": "Vogon"
            },
            {
                "pageid": 202380,
                "ns": 0,
                "title": "Dirk Gently"
            },
            {
                "pageid": 203621,
                "ns": 0,
                "title": "Cranleigh"
            },
            {
                "pageid": 204504,
                "ns": 0,
                "title": "Millennium"
            },
            {
                "pageid": 205512,
                "ns": 0,
                "title": "Monty Python's The Meaning of Life"
            },
            {
                "pageid": 206019,
                "ns": 0,
                "title": "Robert Sheckley"
            },
            {
                "pageid": 208439,
                "ns": 0,
                "title": "Not the Nine O'Clock News"
            },
            {
                "pageid": 210085,
                "ns": 0,
                "title": "Genre fiction"
            },
            {
                "pageid": 220066,
                "ns": 0,
                "title": "Encyclopedia Galactica"
            },
            {
                "pageid": 222453,
                "ns": 0,
                "title": "Geoffrey Perkins"
            },
            {
                "pageid": 222734,
                "ns": 1,
                "title": "Talk:Knights Who Say Ni"
            },
            {
                "pageid": 226741,
                "ns": 0,
                "title": "Earth in science fiction"
            },
            {
                "pageid": 226759,
                "ns": 1,
                "title": "Talk:Cardinal direction"
            },
            {
                "pageid": 230265,
                "ns": 0,
                "title": "Deaths in 2001"
            },
            {
                "pageid": 230698,
                "ns": 0,
                "title": "Helen Mirren"
            },
            {
                "pageid": 236707,
                "ns": 0,
                "title": "List of English novelists"
            },
            {
                "pageid": 236962,
                "ns": 0,
                "title": "Steve Meretzky"
            },
            {
                "pageid": 237992,
                "ns": 0,
                "title": "Griff Rhys Jones"
            },
            {
                "pageid": 240602,
                "ns": 0,
                "title": "Taunton"
            },
            {
                "pageid": 240698,
                "ns": 0,
                "title": "Return to Zork"
            },
            {
                "pageid": 246726,
                "ns": 2,
                "title": "User:Oliver Pereira/stuff"
            },
            {
                "pageid": 247619,
                "ns": 2,
                "title": "User:Fantasy/Films and Books"
            },
            {
                "pageid": 248723,
                "ns": 0,
                "title": "Online encyclopedia"
            },
            {
                "pageid": 255451,
                "ns": 0,
                "title": "List of science fiction novels"
            },
            {
                "pageid": 255938,
                "ns": 2,
                "title": "User:Arteitle"
            },
            {
                "pageid": 256799,
                "ns": 0,
                "title": "Aphorism"
            },
            {
                "pageid": 260914,
                "ns": 0,
                "title": "Orders of magnitude (numbers)"
            },
            {
                "pageid": 265408,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy (video game)"
            },
            {
                "pageid": 266356,
                "ns": 0,
                "title": "List of minor The Hitchhiker's Guide to the Galaxy characters"
            },
            {
                "pageid": 267247,
                "ns": 0,
                "title": "River dolphin"
            },
            {
                "pageid": 269742,
                "ns": 0,
                "title": "Eoin Colfer"
            },
            {
                "pageid": 270906,
                "ns": 0,
                "title": "Three-letter acronym"
            },
            {
                "pageid": 272687,
                "ns": 0,
                "title": "Stalbridge"
            },
            {
                "pageid": 275009,
                "ns": 0,
                "title": "Culture of the United Kingdom"
            },
            {
                "pageid": 275154,
                "ns": 0,
                "title": "Blackmore Vale"
            },
            {
                "pageid": 277135,
                "ns": 0,
                "title": "Person from Porlock"
            },
            {
                "pageid": 284515,
                "ns": 0,
                "title": "Timeline of hypertext technology"
            },
            {
                "pageid": 287801,
                "ns": 0,
                "title": "Hypermedia"
            },
            {
                "pageid": 292910,
                "ns": 0,
                "title": "Metafiction"
            },
            {
                "pageid": 294628,
                "ns": 0,
                "title": "2005 in film"
            },
            {
                "pageid": 295712,
                "ns": 0,
                "title": "Young Zaphod Plays It Safe"
            },
            {
                "pageid": 296550,
                "ns": 0,
                "title": "British literature"
            },
            {
                "pageid": 297098,
                "ns": 0,
                "title": "Creatures (video game series)"
            },
            {
                "pageid": 299530,
                "ns": 0,
                "title": "Brentwood School, Essex"
            },
            {
                "pageid": 299646,
                "ns": 0,
                "title": "Places in The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 300228,
                "ns": 0,
                "title": "Charlie Bean"
            },
            {
                "pageid": 310029,
                "ns": 0,
                "title": "Layered Image File Format"
            },
            {
                "pageid": 310619,
                "ns": 0,
                "title": "Achewood"
            },
            {
                "pageid": 313242,
                "ns": 0,
                "title": "BSFA Award"
            },
            {
                "pageid": 313675,
                "ns": 0,
                "title": "SF Masterworks"
            },
            {
                "pageid": 323782,
                "ns": 0,
                "title": "Lalla Ward"
            },
            {
                "pageid": 324415,
                "ns": 0,
                "title": "The Ballad of Halo Jones"
            },
            {
                "pageid": 338183,
                "ns": 0,
                "title": "The Sirens of Titan"
            },
            {
                "pageid": 338984,
                "ns": 2,
                "title": "User:Midom"
            },
            {
                "pageid": 340620,
                "ns": 0,
                "title": "Didcot"
            },
            {
                "pageid": 343210,
                "ns": 0,
                "title": "Princess (car)"
            },
            {
                "pageid": 349853,
                "ns": 1,
                "title": "Talk:List of minor The Hitchhiker's Guide to the Galaxy characters"
            },
            {
                "pageid": 354536,
                "ns": 0,
                "title": "Son of Dracula (1974 film)"
            },
            {
                "pageid": 357020,
                "ns": 0,
                "title": "LucasArts adventure games"
            },
            {
                "pageid": 357820,
                "ns": 0,
                "title": "The Division Bell"
            },
            {
                "pageid": 361302,
                "ns": 0,
                "title": "Fenchurch Street railway station"
            },
            {
                "pageid": 364509,
                "ns": 0,
                "title": "The South Bank Show"
            },
            {
                "pageid": 366389,
                "ns": 0,
                "title": "The Mighty Boosh"
            },
            {
                "pageid": 367649,
                "ns": 1,
                "title": "Talk:Layered Image File Format"
            },
            {
                "pageid": 368834,
                "ns": 0,
                "title": "Pierre Menard, Author of the Quixote"
            },
            {
                "pageid": 371215,
                "ns": 0,
                "title": "Babel Fish (website)"
            },
            {
                "pageid": 376078,
                "ns": 0,
                "title": "List of environmental organizations"
            },
            {
                "pageid": 381007,
                "ns": 0,
                "title": "Professor Chronotis"
            },
            {
                "pageid": 381340,
                "ns": 0,
                "title": "St. Cedd's College, Cambridge"
            },
            {
                "pageid": 384096,
                "ns": 0,
                "title": "Where no man has gone before"
            },
            {
                "pageid": 386967,
                "ns": 0,
                "title": "Bureaucracy (video game)"
            },
            {
                "pageid": 387403,
                "ns": 0,
                "title": "Nonsense"
            },
            {
                "pageid": 395894,
                "ns": 0,
                "title": "Legend Entertainment"
            },
            {
                "pageid": 401906,
                "ns": 0,
                "title": "Don't Panic: The Official Hitchhiker's Guide to the Galaxy Companion"
            },
            {
                "pageid": 404289,
                "ns": 0,
                "title": "Menippean satire"
            },
            {
                "pageid": 405493,
                "ns": 0,
                "title": "Digital physics"
            },
            {
                "pageid": 407332,
                "ns": 0,
                "title": "Rickmansworth"
            },
            {
                "pageid": 408094,
                "ns": 0,
                "title": "Startopia"
            },
            {
                "pageid": 409282,
                "ns": 0,
                "title": "List of authors by name: A"
            },
            {
                "pageid": 414643,
                "ns": 2,
                "title": "User:Znode/About (old)"
            },
            {
                "pageid": 416095,
                "ns": 0,
                "title": "Psychic detective"
            },
            {
                "pageid": 418570,
                "ns": 0,
                "title": "Hugo Award for Best Dramatic Presentation"
            },
            {
                "pageid": 421613,
                "ns": 0,
                "title": "Douglas Noël Adams",
                "redirect": true
            },
            {
                "pageid": 423303,
                "ns": 1,
                "title": "Talk:John Titor/Archive-1"
            },
            {
                "pageid": 431695,
                "ns": 0,
                "title": "Paranoid Android"
            },
            {
                "pageid": 435076,
                "ns": 0,
                "title": "Mark Wing-Davey"
            },
            {
                "pageid": 442167,
                "ns": 0,
                "title": "Douglas Adams Biography",
                "redirect": true
            },
            {
                "pageid": 442720,
                "ns": 0,
                "title": "A Mind Forever Voyaging"
            },
            {
                "pageid": 443327,
                "ns": 3,
                "title": "User talk:Barbara Shack"
            },
            {
                "pageid": 455258,
                "ns": 0,
                "title": "List of Have I Got News for You episodes"
            },
            {
                "pageid": 455776,
                "ns": 2,
                "title": "User:Sunja"
            },
            {
                "pageid": 457118,
                "ns": 0,
                "title": "The Gathering (LAN party)"
            },
            {
                "pageid": 462395,
                "ns": 0,
                "title": "Week Ending"
            },
            {
                "pageid": 466470,
                "ns": 0,
                "title": "The Eyre Affair"
            },
            {
                "pageid": 471205,
                "ns": 0,
                "title": "Hipgnosis"
            },
            {
                "pageid": 475298,
                "ns": 0,
                "title": "Lost in a Good Book"
            },
            {
                "pageid": 478421,
                "ns": 2,
                "title": "User:Xyzzyva"
            },
            {
                "pageid": 478921,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy (novel)"
            },
            {
                "pageid": 484730,
                "ns": 0,
                "title": "Santa Cruz Operation"
            },
            {
                "pageid": 485270,
                "ns": 1,
                "title": "Talk:March 8"
            },
            {
                "pageid": 486569,
                "ns": 4,
                "title": "Wikipedia:Selected anniversaries/March"
            },
            {
                "pageid": 490358,
                "ns": 0,
                "title": "Grammy Award for Best Spoken Word Album"
            },
            {
                "pageid": 492356,
                "ns": 4,
                "title": "Wikipedia:Selected anniversaries/March 8"
            },
            {
                "pageid": 497016,
                "ns": 0,
                "title": "List of BBC Radio 4 programmes"
            },
            {
                "pageid": 507760,
                "ns": 4,
                "title": "Wikipedia:Selected anniversaries/All"
            },
            {
                "pageid": 508263,
                "ns": 0,
                "title": "Andrew Marshall (screenwriter)"
            },
            {
                "pageid": 510257,
                "ns": 0,
                "title": "Last Chance to See"
            },
            {
                "pageid": 510303,
                "ns": 1,
                "title": "Talk:DNA/Archive 6"
            },
            {
                "pageid": 511626,
                "ns": 0,
                "title": "Cultured meat"
            },
            {
                "pageid": 515856,
                "ns": 2,
                "title": "User:Wolf530"
            },
            {
                "pageid": 516802,
                "ns": 0,
                "title": "Dave Lebling"
            },
            {
                "pageid": 519769,
                "ns": 0,
                "title": "Bartleby, the Scrivener"
            },
            {
                "pageid": 529967,
                "ns": 0,
                "title": "List of fictional Cambridge colleges"
            },
            {
                "pageid": 530260,
                "ns": 2,
                "title": "User:Shyamal"
            },
            {
                "pageid": 538317,
                "ns": 2,
                "title": "User:Geeoharee"
            },
            {
                "pageid": 545919,
                "ns": 0,
                "title": "69,105"
            },
            {
                "pageid": 547679,
                "ns": 0,
                "title": "Wetwang"
            },
            {
                "pageid": 550719,
                "ns": 0,
                "title": "Brian Blessed"
            },
            {
                "pageid": 555606,
                "ns": 0,
                "title": "Douglas Noel Adams",
                "redirect": true
            },
            {
                "pageid": 561505,
                "ns": 1,
                "title": "Talk:Joris-Karl Huysmans"
            },
            {
                "pageid": 563943,
                "ns": 0,
                "title": "List of prostitutes and courtesans"
            },
            {
                "pageid": 564881,
                "ns": 2,
                "title": "User:Dunk"
            },
            {
                "pageid": 572317,
                "ns": 0,
                "title": "Blowin' in the Wind"
            },
            {
                "pageid": 573880,
                "ns": 0,
                "title": "Fine-tuned Universe"
            },
            {
                "pageid": 575803,
                "ns": 0,
                "title": "The Big Read"
            },
            {
                "pageid": 577249,
                "ns": 0,
                "title": "Grue (monster)"
            },
            {
                "pageid": 581509,
                "ns": 0,
                "title": "List of fictional diseases"
            },
            {
                "pageid": 581632,
                "ns": 0,
                "title": "Mountain gorilla"
            },
            {
                "pageid": 589105,
                "ns": 0,
                "title": "David Agnew"
            },
            {
                "pageid": 592368,
                "ns": 0,
                "title": "Towel Day"
            },
            {
                "pageid": 597408,
                "ns": 0,
                "title": "The Adventure Game"
            },
            {
                "pageid": 615224,
                "ns": 0,
                "title": "Leather Goddesses of Phobos"
            },
            {
                "pageid": 620267,
                "ns": 0,
                "title": "List of text-based computer games"
            },
            {
                "pageid": 623143,
                "ns": 0,
                "title": "18610 Arthurdent"
            },
            {
                "pageid": 623209,
                "ns": 0,
                "title": "List of minor planets named after people"
            },
            {
                "pageid": 626608,
                "ns": 0,
                "title": "Christopher Priest (novelist)"
            },
            {
                "pageid": 631711,
                "ns": 0,
                "title": "Comic novel"
            },
            {
                "pageid": 634686,
                "ns": 0,
                "title": "Greg Rucka"
            },
            {
                "pageid": 638514,
                "ns": 0,
                "title": "BBC Online"
            },
            {
                "pageid": 640911,
                "ns": 0,
                "title": "List of satirists and satires"
            },
            {
                "pageid": 646205,
                "ns": 0,
                "title": "Tyler Labine"
            },
            {
                "pageid": 647158,
                "ns": 0,
                "title": "List of fictional books"
            },
            {
                "pageid": 649005,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/How to Fly"
            },
            {
                "pageid": 654925,
                "ns": 0,
                "title": "Forbidden Planet (bookstore)"
            },
            {
                "pageid": 671958,
                "ns": 0,
                "title": "List of fictional Prime Ministers of the United Kingdom"
            },
            {
                "pageid": 675682,
                "ns": 2,
                "title": "User:HansWobbe"
            },
            {
                "pageid": 681311,
                "ns": 2,
                "title": "User:Edward/books"
            },
            {
                "pageid": 692345,
                "ns": 0,
                "title": "Fictional currency"
            },
            {
                "pageid": 697699,
                "ns": 0,
                "title": "Bop Ad",
                "redirect": true
            },
            {
                "pageid": 711878,
                "ns": 0,
                "title": "Radio Academy"
            },
            {
                "pageid": 712000,
                "ns": 2,
                "title": "User:Tormaroe"
            },
            {
                "pageid": 713873,
                "ns": 0,
                "title": "List of detective fiction authors"
            },
            {
                "pageid": 722670,
                "ns": 0,
                "title": "Tor Books"
            },
            {
                "pageid": 730146,
                "ns": 0,
                "title": "Simon Jones (actor)"
            },
            {
                "pageid": 731738,
                "ns": 1,
                "title": "Talk:Earth/Archive 1"
            },
            {
                "pageid": 732330,
                "ns": 0,
                "title": "Brian Moriarty"
            },
            {
                "pageid": 740817,
                "ns": 0,
                "title": "Mathematical coincidence"
            },
            {
                "pageid": 742979,
                "ns": 0,
                "title": "Adams, Douglas",
                "redirect": true
            },
            {
                "pageid": 753557,
                "ns": 0,
                "title": "Triumph of the Nerds"
            },
            {
                "pageid": 762801,
                "ns": 0,
                "title": "The Burkiss Way"
            },
            {
                "pageid": 763822,
                "ns": 0,
                "title": "Wishbringer"
            },
            {
                "pageid": 766489,
                "ns": 2,
                "title": "User:JoshG"
            },
            {
                "pageid": 797949,
                "ns": 2,
                "title": "User:Brandalone"
            },
            {
                "pageid": 799056,
                "ns": 0,
                "title": "Adams, Douglas Noel",
                "redirect": true
            },
            {
                "pageid": 804250,
                "ns": 0,
                "title": "Doctor Who spin-offs"
            },
            {
                "pageid": 814696,
                "ns": 2,
                "title": "User:Ben Lewis"
            },
            {
                "pageid": 822749,
                "ns": 0,
                "title": "So Long and Thanks for All the Shoes"
            },
            {
                "pageid": 823354,
                "ns": 0,
                "title": "Clun"
            },
            {
                "pageid": 825679,
                "ns": 2,
                "title": "User:Guybrush"
            },
            {
                "pageid": 839439,
                "ns": 1,
                "title": "Talk:Kakapo"
            },
            {
                "pageid": 843158,
                "ns": 0,
                "title": "San Diego Comic-Con"
            },
            {
                "pageid": 849869,
                "ns": 0,
                "title": "Rice pudding"
            },
            {
                "pageid": 852368,
                "ns": 0,
                "title": "Planetfall"
            },
            {
                "pageid": 855755,
                "ns": 4,
                "title": "Wikipedia:Reference desk archive/July 2004"
            },
            {
                "pageid": 856679,
                "ns": 0,
                "title": "Bernice Summerfield"
            },
            {
                "pageid": 859443,
                "ns": 0,
                "title": "Cornerstone (software)"
            },
            {
                "pageid": 861370,
                "ns": 0,
                "title": "The Lost Treasures of Infocom"
            },
            {
                "pageid": 864968,
                "ns": 2,
                "title": "User:Average Earthman"
            },
            {
                "pageid": 865381,
                "ns": 0,
                "title": "Deep Thought (chess computer)"
            },
            {
                "pageid": 867545,
                "ns": 0,
                "title": "The Five Doctors"
            },
            {
                "pageid": 869769,
                "ns": 0,
                "title": "Life on Other Planets"
            },
            {
                "pageid": 873352,
                "ns": 0,
                "title": "A113"
            },
            {
                "pageid": 875467,
                "ns": 0,
                "title": "Zork: Grand Inquisitor"
            },
            {
                "pageid": 878281,
                "ns": 1,
                "title": "Talk:Goulash"
            },
            {
                "pageid": 884156,
                "ns": 0,
                "title": "List of kakapo"
            },
            {
                "pageid": 897135,
                "ns": 1,
                "title": "Talk:Norse mythology/Archive 2"
            },
            {
                "pageid": 905614,
                "ns": 0,
                "title": "Tim Anderson (programmer)"
            },
            {
                "pageid": 908185,
                "ns": 0,
                "title": "List of races and species in The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 911959,
                "ns": 0,
                "title": "Douglas adams",
                "redirect": true
            },
            {
                "pageid": 915262,
                "ns": 1,
                "title": "Talk:Googleplex"
            },
            {
                "pageid": 918635,
                "ns": 0,
                "title": "Anton Zeilinger"
            },
            {
                "pageid": 920676,
                "ns": 10,
                "title": "Template:The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 920901,
                "ns": 0,
                "title": "Software versioning"
            },
            {
                "pageid": 930311,
                "ns": 0,
                "title": "Target Books"
            },
            {
                "pageid": 934494,
                "ns": 4,
                "title": "Wikipedia:Featured article candidates/Archived nominations/Index/August 2004"
            },
            {
                "pageid": 936829,
                "ns": 0,
                "title": "Zooey Deschanel"
            },
            {
                "pageid": 937210,
                "ns": 0,
                "title": "Fable (2004 video game)"
            },
            {
                "pageid": 944266,
                "ns": 0,
                "title": "Douglass adams",
                "redirect": true
            },
            {
                "pageid": 952380,
                "ns": 4,
                "title": "Wikipedia:Featured article candidates/Featured log/September 2004"
            },
            {
                "pageid": 955001,
                "ns": 0,
                "title": "Starcross (video game)"
            },
            {
                "pageid": 959741,
                "ns": 0,
                "title": "History of Doctor Who"
            },
            {
                "pageid": 982874,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy (film)"
            },
            {
                "pageid": 983931,
                "ns": 0,
                "title": "Enchanter (video game)"
            },
            {
                "pageid": 988730,
                "ns": 4,
                "title": "Wikipedia:People by year/Reports/All"
            },
            {
                "pageid": 990779,
                "ns": 2,
                "title": "User:Greyweather"
            },
            {
                "pageid": 996056,
                "ns": 0,
                "title": "The Utterly Utterly Merry Comic Relief Christmas Book"
            },
            {
                "pageid": 999864,
                "ns": 0,
                "title": "Trinity (video game)"
            },
            {
                "pageid": 1007332,
                "ns": 11,
                "title": "Template talk:IMDb/Archive 1"
            },
            {
                "pageid": 1012235,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/List of terms associated with the color..."
            },
            {
                "pageid": 1031386,
                "ns": 0,
                "title": "One of These Nights"
            },
            {
                "pageid": 1048304,
                "ns": 0,
                "title": "Zork Nemesis"
            },
            {
                "pageid": 1052343,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/Alt.fan.douglas-adams"
            },
            {
                "pageid": 1055432,
                "ns": 2,
                "title": "User:Fmobus"
            },
            {
                "pageid": 1060486,
                "ns": 0,
                "title": "ŽVPL"
            },
            {
                "pageid": 1063385,
                "ns": 0,
                "title": "Phrases from The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 1075187,
                "ns": 0,
                "title": "Beyond Zork"
            },
            {
                "pageid": 1082023,
                "ns": 0,
                "title": "Mouseland"
            },
            {
                "pageid": 1088352,
                "ns": 0,
                "title": "Starstruck (comics)"
            },
            {
                "pageid": 1092923,
                "ns": 0,
                "title": "Google"
            },
            {
                "pageid": 1096189,
                "ns": 1,
                "title": "Talk:Doctor Who spin-offs"
            },
            {
                "pageid": 1104882,
                "ns": 0,
                "title": "List of University of Cambridge people"
            },
            {
                "pageid": 1105048,
                "ns": 2,
                "title": "User:Danarchy"
            },
            {
                "pageid": 1108523,
                "ns": 0,
                "title": "BayCon"
            },
            {
                "pageid": 1120443,
                "ns": 2,
                "title": "User:Jongarrettuk/Better writing guide (current draft)"
            },
            {
                "pageid": 1125164,
                "ns": 0,
                "title": "Bluebottle (character)"
            },
            {
                "pageid": 1133130,
                "ns": 1,
                "title": "Talk:The Hunting of the Snark"
            },
            {
                "pageid": 1137976,
                "ns": 0,
                "title": "Tredegar"
            },
            {
                "pageid": 1150156,
                "ns": 0,
                "title": "The Lurking Horror"
            },
            {
                "pageid": 1154339,
                "ns": 0,
                "title": "InvisiClues"
            },
            {
                "pageid": 1158276,
                "ns": 1,
                "title": "Talk:Kenny Kramer"
            },
            {
                "pageid": 1160425,
                "ns": 2,
                "title": "User:Akchizar"
            },
            {
                "pageid": 1167171,
                "ns": 0,
                "title": "Douglas Adams (disambiguation)"
            },
            {
                "pageid": 1167603,
                "ns": 5,
                "title": "Wikipedia talk:Manual of Style (dates and numbers)/Archive 9"
            },
            {
                "pageid": 1169469,
                "ns": 0,
                "title": "AC adapter"
            },
            {
                "pageid": 1172515,
                "ns": 0,
                "title": "Computronium"
            },
            {
                "pageid": 1186248,
                "ns": 3,
                "title": "User talk:ClockworkTroll/Name the Admin Candidate"
            },
            {
                "pageid": 1189187,
                "ns": 4,
                "title": "Wikipedia:Writing better articles"
            },
            {
                "pageid": 1196859,
                "ns": 1,
                "title": "Talk:Hysterical realism"
            },
            {
                "pageid": 1204144,
                "ns": 4,
                "title": "Wikipedia:Wikifun/Answers Round 3"
            },
            {
                "pageid": 1205556,
                "ns": 3,
                "title": "User talk:Supersexyspacemonkey"
            },
            {
                "pageid": 1207282,
                "ns": 4,
                "title": "Wikipedia:Today's featured article/August 2005"
            },
            {
                "pageid": 1207602,
                "ns": 4,
                "title": "Wikipedia:Today's featured article/August 15, 2005"
            },
            {
                "pageid": 1222851,
                "ns": 1,
                "title": "Talk:St. Albans School (Washington, D.C.)"
            },
            {
                "pageid": 1233835,
                "ns": 0,
                "title": "Geoffrey McGivern"
            },
            {
                "pageid": 1234601,
                "ns": 0,
                "title": "List of Monty Python's Flying Circus episodes"
            },
            {
                "pageid": 1271199,
                "ns": 0,
                "title": "Gweek"
            },
            {
                "pageid": 1292809,
                "ns": 0,
                "title": "Doctor in the House (franchise)"
            },
            {
                "pageid": 1330622,
                "ns": 4,
                "title": "Wikipedia:Featured article candidates/Infinite monkey theorem"
            },
            {
                "pageid": 1336807,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/Thrupp"
            },
            {
                "pageid": 1343174,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/Log/2004 December 28"
            },
            {
                "pageid": 1350858,
                "ns": 0,
                "title": "Charles Thomson (artist)"
            },
            {
                "pageid": 1364362,
                "ns": 0,
                "title": "Ghost Light (Doctor Who)"
            },
            {
                "pageid": 1422125,
                "ns": 1,
                "title": "Talk:Cesar Chavez"
            },
            {
                "pageid": 1428664,
                "ns": 2,
                "title": "User:DanP"
            },
            {
                "pageid": 1436404,
                "ns": 0,
                "title": "25924 Douglasadams"
            },
            {
                "pageid": 1442444,
                "ns": 2,
                "title": "User:Binabik80"
            },
            {
                "pageid": 1448618,
                "ns": 2,
                "title": "User:Dupont Circle"
            },
            {
                "pageid": 1454245,
                "ns": 0,
                "title": "Arthur: The Quest for Excalibur"
            },
            {
                "pageid": 1483318,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/Log/2005 February 9"
            },
            {
                "pageid": 1486610,
                "ns": 4,
                "title": "Wikipedia:Articles for deletion/Stupid Day"
            },
            {
                "pageid": 1486637,
                "ns": 0,
                "title": "Dirk Maggs"
            },
            {
                "pageid": 1523660,
                "ns": 2,
                "title": "User:Cross-eyedmary"
            },
            {
                "pageid": 1526800,
                "ns": 2,
                "title": "User:Stevensweet"
            },
            {
                "pageid": 1528843,
                "ns": 0,
                "title": "Quote... Unquote"
            },
            {
                "pageid": 1545056,
                "ns": 0,
                "title": "Mavis Enderby"
            },
            {
                "pageid": 1549047,
                "ns": 1,
                "title": "Talk:Places in The Hitchhiker's Guide to the Galaxy"
            },
            {
                "pageid": 1551800,
                "ns": 0,
                "title": "Mark Carwardine"
            },
            {
                "pageid": 1562000,
                "ns": 0,
                "title": "Dark Night of the Soul"
            },
            {
                "pageid": 1567800,
                "ns": 0,
                "title": "Publius Enigma"
            },
            {
                "pageid": 1571009,
                "ns": 0,
                "title": "Meanings of minor planet names: 25001–26000"
            },
            {
                "pageid": 1592412,
                "ns": 4,
                "title": "Wikipedia:Peer review/Surreal humour/archive1"
            },
            {
                "pageid": 1620397,
                "ns": 0,
                "title": "List of Doctor Who audio plays by Big Finish"
            },
            {
                "pageid": 1657443,
                "ns": 0,
                "title": "List of acronyms: D"
            },
            {
                "pageid": 1658024,
                "ns": 10,
                "title": "Template:Infocom games"
            },
            {
                "pageid": 1660306,
                "ns": 2,
                "title": "User:(et)t~enwiki"
            },
            {
                "pageid": 1660367,
                "ns": 1,
                "title": "Talk:Charlotte Corday"
            },
            {
                "pageid": 1666929,
                "ns": 0,
                "title": "Zork Zero"
            },
            {
                "pageid": 1667025,
                "ns": 0,
                "title": "Sorcerer (video game)"
            },
            {
                "pageid": 1667026,
                "ns": 0,
                "title": "Spellbreaker"
            },
            {
                "pageid": 1674691,
                "ns": 0,
                "title": "Deadline (video game)"
            },
            {
                "pageid": 1675049,
                "ns": 0,
                "title": "Zork: The Undiscovered Underground"
            },
            {
                "pageid": 1676028,
                "ns": 0,
                "title": "Infidel (video game)"
            },
            {
                "pageid": 1679146,
                "ns": 0,
                "title": "List of avian humanoids"
            },
            {
                "pageid": 1679361,
                "ns": 4,
                "title": "Wikipedia:Peer review/April 2005"
            },
            {
                "pageid": 1680819,
                "ns": 0,
                "title": "List of Google Easter eggs"
            },
            {
                "pageid": 1681535,
                "ns": 0,
                "title": "List of Doctor Who audio releases"
            },
            {
                "pageid": 1690791,
                "ns": 4,
                "title": "Wikipedia:Wikipedia Signpost/2005-04-11/DVD releases"
            },
            {
                "pageid": 1701285,
                "ns": 4,
                "title": "Wikipedia:WikiProject Doctor Who"
            },
            {
                "pageid": 1706444,
                "ns": 0,
                "title": "List of Doctor Who planets"
            },
            {
                "pageid": 1715687,
                "ns": 2,
                "title": "User:Joo"
            },
            {
                "pageid": 1723459,
                "ns": 4,
                "title": "Wikipedia:Wikipedia Signpost/2005-04-18/In the news"
            },
            {
                "pageid": 1728996,
                "ns": 0,
                "title": "The Witness (1983 video game)"
            },
            {
                "pageid": 1729657,
                "ns": 0,
                "title": "Cutthroats (video game)"
            },
            {
                "pageid": 1739819,
                "ns": 0,
                "title": "Seastalker"
            },
            {
                "pageid": 1740324,
                "ns": 0,
                "title": "Suspect (video game)"
            },
            {
                "pageid": 1740508,
                "ns": 0,
                "title": "The Key to Time"
            },
            {
                "pageid": 1740520,
                "ns": 0,
                "title": "Ballyhoo (video game)"
            },
            {
                "pageid": 1740765,
                "ns": 0,
                "title": "Hollywood Hijinx"
            },
            {
                "pageid": 1741077,
                "ns": 0,
                "title": "Graham Williams (television producer)"
            },
            {
                "pageid": 1744498,
                "ns": 0,
                "title": "Stationfall"
            },
            {
                "pageid": 1751154,
                "ns": 0,
                "title": "Moonmist"
            },
            {
                "pageid": 1754624,
                "ns": 0,
                "title": "Border Zone (video game)"
            },
            {
                "pageid": 1759092,
                "ns": 0,
                "title": "Nord and Bert Couldn't Make Head or Tail of It"
            },
            {
                "pageid": 1762140,
                "ns": 0,
                "title": "MTropolis"
            },
            {
                "pageid": 1764629,
                "ns": 0,
                "title": "Sherlock: The Riddle of the Crown Jewels"
            },
            {
                "pageid": 1769920,
                "ns": 0,
                "title": "Plundered Hearts"
            },
            {
                "pageid": 1775512,
                "ns": 0,
                "title": "James Clavell's Shōgun"
            },
            {
                "pageid": 1776754,
                "ns": 0,
                "title": "Sandra Dickinson"
            },
            {
                "pageid": 1777937,
                "ns": 0,
                "title": "Vancouver Public Library"
            },
            {
                "pageid": 1780174,
                "ns": 0,
                "title": "Journey (1989 video game)"
            },
            {
                "pageid": 1785518,
                "ns": 0,
                "title": "The Armageddon Factor"
            },
            {
                "pageid": 1788002,
                "ns": 1,
                "title": "Talk:The Library of Babel"
            },
            {
                "pageid": 1795840,
                "ns": 4,
                "title": "Wikipedia:Wikipedia Signpost/2005-05-02/In the news"
            },
            {
                "pageid": 1814888,
                "ns": 0,
                "title": "Matt Jones (writer)"
            },
            {
                "pageid": 1814949,
                "ns": 0,
                "title": "Christopher H. Bidmead"
            },
            {
                "pageid": 1816950,
                "ns": 0,
                "title": "The Space Museum"
            },
            {
                "pageid": 1830464,
                "ns": 0,
                "title": "Fooblitzky"
            },
            {
                "pageid": 1830629,
                "ns": 0,
                "title": "Leather Goddesses of Phobos 2: Gas Pump Girls Meet the Pulsating Inconvenience from Planet X!"
            },
            {
                "pageid": 1830993,
                "ns": 0,
                "title": "Goosnargh"
            },
            {
                "pageid": 1834162,
                "ns": 0,
                "title": "High Offley"
            },
            {
                "pageid": 1834408,
                "ns": 0,
                "title": "List of religious ideas in science fiction"
            },
            {
                "pageid": 1834899,
                "ns": 0,
                "title": "Zork I"
            },
            {
                "pageid": 1835612,
                "ns": 0,
                "title": "Circuit's Edge"
            },
            {
                "pageid": 1835691,
                "ns": 15,
                "title": "Category talk:Positional numeral systems"
            },
            {
                "pageid": 1843594,
                "ns": 1,
                "title": "Talk:Nonce word"
            },
            {
                "pageid": 1847772,
                "ns": 2,
                "title": "User:Zoso~enwiki"
            },
            {
                "pageid": 1854364,
                "ns": 100,
                "title": "Portal:Doctor Who/Did you know"
            },
            {
                "pageid": 1854829,
                "ns": 2,
                "title": "User:Linuxbeak/Desk"
            },
            {
                "pageid": 1854892,
                "ns": 101,
                "title": "Portal talk:Doctor Who"
            },
            {
                "pageid": 1859446,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy (radio series)"
            },
            {
                "pageid": 1867336,
                "ns": 2,
                "title": "User:Digital Watches"
            },
            {
                "pageid": 1869065,
                "ns": 2,
                "title": "User:JollyJeanGiant"
            },
            {
                "pageid": 1871192,
                "ns": 2,
                "title": "User:Arthur Holland"
            },
            {
                "pageid": 1879923,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy (TV series)"
            },
            {
                "pageid": 1886171,
                "ns": 0,
                "title": "Hitch-hiker's Guide to Europe"
            },
            {
                "pageid": 1886253,
                "ns": 2,
                "title": "User:Nick R/books"
            },
            {
                "pageid": 1892526,
                "ns": 0,
                "title": "Duck test"
            },
            {
                "pageid": 1895842,
                "ns": 0,
                "title": "Above the Title Productions"
            },
            {
                "pageid": 1897437,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy Primary and Secondary Phases"
            },
            {
                "pageid": 1897462,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Galaxy Tertiary to Hexagonal Phases"
            },
            {
                "pageid": 1902368,
                "ns": 0,
                "title": "Destiny of the Daleks"
            },
            {
                "pageid": 1910757,
                "ns": 101,
                "title": "Portal talk:Biography"
            },
            {
                "pageid": 1916697,
                "ns": 1,
                "title": "Talk:Śākaṭāyana"
            },
            {
                "pageid": 1922349,
                "ns": 0,
                "title": "To a Mouse"
            },
            {
                "pageid": 1926357,
                "ns": 6,
                "title": "File:Deeper Meaning of Liff front cover.jpg"
            },
            {
                "pageid": 1934413,
                "ns": 0,
                "title": "Upper Street"
            },
            {
                "pageid": 1935815,
                "ns": 6,
                "title": "File:Hitchhiker's Guide (book cover).jpg"
            },
            {
                "pageid": 1936415,
                "ns": 2,
                "title": "User:Bennity"
            },
            {
                "pageid": 1954022,
                "ns": 0,
                "title": "Wish You Were Here"
            },
            {
                "pageid": 1954684,
                "ns": 6,
                "title": "File:Ultimate Hitchhikers Guide front.jpg"
            },
            {
                "pageid": 1960616,
                "ns": 0,
                "title": "Douglas Adams at the BBC"
            },
            {
                "pageid": 1960792,
                "ns": 0,
                "title": "The Hitchhiker's Guide to the Future"
            },
            {
                "pageid": 1964193,
                "ns": 6,
                "title": "File:The Salmon of Doubt Macmillan front.jpg"
            },
            {
                "pageid": 1964229,
                "ns": 6,
                "title": "File:Last Chance to See Harmony front.jpg"
            },
            {
                "pageid": 1964254,
                "ns": 6,
                "title": "File:Last Chance to See Voyager front.jpg"
            },
            {
                "pageid": 1964312,
                "ns": 6,
                "title": "File:Mostly Harmless Harmony front.jpg"
            },
            {
                "pageid": 1965715,
                "ns": 6,
                "title": "File:H2G2 first comic front cover.jpg"
            },
            {
                "pageid": 1969973,
                "ns": 0,
                "title": "Out of the Trees"
            },
            {
                "pageid": 1970255,
                "ns": 0,
                "title": "Douglas Q. Adams"
            },
            {
                "pageid": 1971166,
                "ns": 0,
                "title": "Real Time (Doctor Who)"
            },
            {
                "pageid": 1979611,
                "ns": 0,
                "title": "Toby Longworth"
            },
            {
                "pageid": 1984591,
                "ns": 2,
                "title": "User:Captmondo"
            },
            {
                "pageid": 1988147,
                "ns": 0,
                "title": "Past Doctor Adventures"
            },
            {
                "pageid": 1989697,
                "ns": 2,
                "title": "User:Zocky/Sandbox 2"
            },
            {
                "pageid": 2013148,
                "ns": 0,
                "title": "January 1981"
            },
            {
                "pageid": 2017499,
                "ns": 2,
                "title": "User:ForteTwo"
            },
            {
                "pageid": 2028922,
                "ns": 4,
                "title": "Wikipedia:Former featured articles"
            },
            {
                "pageid": 2050785,
                "ns": 3,
                "title": "User talk:Boddah"
            },
            {
                "pageid": 2060880,
                "ns": 2,
                "title": "User:Trisapeace"
            }
        ]
    }
}
"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

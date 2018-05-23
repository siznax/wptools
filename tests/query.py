# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&exintro&formatversion=2&inprop=url|watchers&list=random&pithumbsize=240&pllimit=500&ppprop=disambiguation|wikibase_item&prop=extracts|info|links|pageassessments|pageimages|pageprops|pageterms|redirects&redirects&rdlimit=500&rnlimit=1&rnnamespace=0&titles=Douglas%20Adams'

response = r"""
{
    "batchcomplete": true,
    "continue": {
        "rncontinue": "0.767230557530|0.767230621808|8539703|0",
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
                "extract": "<p><b>Douglas Noel Adams</b> (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humorist, satirist and dramatist.</p>\n<p>Adams was author of <i>The Hitchhiker's Guide to the Galaxy</i>, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.</p>\n<p>Adams also wrote <i>Dirk Gently's Holistic Detective Agency</i> (1987) and <i>The Long Dark Tea-Time of the Soul</i> (1988), and co-wrote <i>The Meaning of Liff</i> (1983), <i>The Deeper Meaning of Liff</i> (1990), <i>Last Chance to See</i> (1990), and three stories for the television series <i>Doctor Who</i>; he also served as script editor for the show's seventeenth season in 1979. A posthumous collection of his works, including an unfinished novel, was published as <i>The Salmon of Doubt</i> in 2002.</p>\n<p>Adams was an advocate for environmentalism and conservation, a lover of fast cars, technological innovation and the Apple Macintosh, and a radical atheist.</p>\n<p></p>",
                "contentmodel": "wikitext",
                "pagelanguage": "en",
                "pagelanguagehtmlcode": "en",
                "pagelanguagedir": "ltr",
                "touched": "2018-05-22T17:21:30Z",
                "lastrevid": 841482403,
                "length": 62123,
                "watchers": 460,
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
                        "title": "A Mind Forever Voyaging"
                    },
                    {
                        "ns": 0,
                        "title": "Academic conference"
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
                        "title": "Atheism"
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
                        "title": "Comedy"
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
                        "title": "Innovation"
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
                        "title": "Justin, Charles & Co."
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
                        "title": "Keith Topping"
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
                        "title": "Macintosh"
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
                        "title": "Martin Day"
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
                        "title": "Paul Cornell"
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
                        "title": "Santa Catarina (state)"
                    },
                    {
                        "ns": 0,
                        "title": "Satire"
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
                        "title": "Science fiction"
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
                        "title": "São José, Santa Catarina"
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
                        "title": "The Discontinuity Guide"
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
                        "title": "The Independent"
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
                        "title": "Upper Street"
                    },
                    {
                        "ns": 0,
                        "title": "Virgin Books"
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
                        "title": "Category:Use dmy dates from May 2018"
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
                "id": 7614573,
                "ns": 0,
                "title": "Aidenbachstraße (Munich U-Bahn)"
            }
        ]
    }
}
"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

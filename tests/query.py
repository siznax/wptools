# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&exintro&format=json&formatversion=2&inprop=displaytitle|url&list=random&pithumbsize=240&ppprop=wikibase_item&prop=extracts|images|info|pageimages|pageprops|pageterms&redirects&rnlimit=1&rnnamespace=0&titles=Douglas_Adams'

response = r'''
{
  "continue": {
    "rncontinue": "0.650501181948|0.650501197613|15741865|0",
    "imcontinue": "8091|Portal-puzzle.svg",
    "continue": "||extracts|info|pageimages|pageprops|pageterms"
  },
  "query": {
    "normalized": [
      {
        "fromencoded": false,
        "from": "Douglas_Adams",
        "to": "Douglas Adams"
      }
    ],
    "pages": [
      {
        "pageid": 8091,
        "ns": 0,
        "title": "Douglas Adams",
        "extract": "<p><b>Douglas Noel Adams</b> (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humourist, satirist and dramatist.</p>\n<p>Adams is best known as the author of <i>The Hitchhiker's Guide to the Galaxy</i>, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.</p>\n<p>Adams also wrote <i>Dirk Gently's Holistic Detective Agency</i> (1987) and <i>The Long Dark Tea-Time of the Soul</i> (1988), and co-wrote <i>The Meaning of Liff</i> (1983), <i>The Deeper Meaning of Liff</i> (1990), <i>Last Chance to See</i> (1990), and three stories for the television series <i>Doctor Who</i>; he also served as script editor for the show's seventeenth season in 1979. A posthumous collection of his works, including an unfinished novel, was published as <i>The Salmon of Doubt</i> in 2002.</p>\n<p>Adams was known as an advocate for environmentalism and conservation, as a lover of fast cars, cameras, technological innovation and the Apple Macintosh, and as a \"devout atheist\".</p>\n<p></p>",
        "images": [
          {
            "ns": 6,
            "title": "File:Commons-logo.svg"
          },
          {
            "ns": 6,
            "title": "File:DNA in Monty Python.jpg"
          },
          {
            "ns": 6,
            "title": "File:Dirk Gently's Holistic Detective Agency.svg"
          },
          {
            "ns": 6,
            "title": "File:Douglas Adams Part 1.ogg"
          },
          {
            "ns": 6,
            "title": "File:Douglas Adams Part 2.ogg"
          },
          {
            "ns": 6,
            "title": "File:Douglas Adams San Francisco.jpg"
          },
          {
            "ns": 6,
            "title": "File:Douglas adams portrait cropped.jpg"
          },
          {
            "ns": 6,
            "title": "File:Folder Hexagonal Icon.svg"
          },
          {
            "ns": 6,
            "title": "File:Highgate Cemetery - East - Douglas Adams 01.jpg"
          },
          {
            "ns": 6,
            "title": "File:Paw (Animal Rights symbol).svg"
          }
        ],
        "contentmodel": "wikitext",
        "pagelanguage": "en",
        "pagelanguagehtmlcode": "en",
        "pagelanguagedir": "ltr",
        "touched": "2016-11-05T11:00:14Z",
        "lastrevid": 747823957,
        "length": 65951,
        "fullurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
        "editurl": "https://en.wikipedia.org/w/index.php?title=Douglas_Adams&action=edit",
        "canonicalurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
        "displaytitle": "Douglas Adams",
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
            "Douglas Noël Adams",
            "Douglas Noel Adams"
          ],
          "description": [
            "English writer and humorist",
            "English writer and humorist"
          ],
          "label": [
            "Douglas Adams",
            "Douglas Adams"
          ]
        }
      }
    ],
    "random": [
      {
        "id": 39432363,
        "ns": 0,
        "title": "John Waguespack"
      }
    ]
  }
}
'''

cache = {'query': query, 'response': response}

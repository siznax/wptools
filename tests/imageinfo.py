# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&iiprop=size|url|timestamp&prop=imageinfo&titles=File%3ADouglas%20adams%20portrait%20cropped.jpg'

response = r'''
{
  "continue": {
    "iistart": "2010-04-16T22:53:21Z",
    "continue": "||"
  },
  "query": {
    "pages": [
      {
        "ns": 6,
        "title": "File:Douglas adams portrait cropped.jpg",
        "missing": true,
        "known": true,
        "imagerepository": "shared",
        "imageinfo": [
          {
            "timestamp": "2010-04-16T22:54:28Z",
            "size": 32915,
            "width": 333,
            "height": 386,
            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg",
            "descriptionurl": "https://commons.wikimedia.org/wiki/File:Douglas_adams_portrait_cropped.jpg",
            "descriptionshorturl": "https://commons.wikimedia.org/w/index.php?curid=10031710"
          }
        ]
      }
    ]
  }
}
'''

cache = {'query': query, 'response': response}

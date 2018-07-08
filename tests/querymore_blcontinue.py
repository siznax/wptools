# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&bltitle=Douglas%20Adams&bllimit=500&formatversion=2&list=backlinks'

response = r"""
{
    "batchcomplete": true,
    "continue": {
        "blcontinue": "0|2062757",
        "continue": "-||"
    },
    "query": {
        "pages": [
            {
                "pageid": 8091,
                "ns": 0,
                "title": "Douglas Adams"
            }
        ],
        "random": [
            {
                "id": 30520069,
                "ns": 0,
                "title": "Island South Divisional Secretariat"
            }
        ],
        "backlinks": [
            {
                "pageid": 1132,
                "ns": 0,
                "title": "The Ashes"
            }
        ]
    }
}
"""

cache = {'query': query,
         'response': response,
         'info': {'content-type': 'TEST', 'status': 200}}

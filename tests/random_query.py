# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&formatversion=2&list=random&rnlimit=1&rnnamespace=0'

response = r"""{
    "batchcomplete": true,
    "continue": {
        "rncontinue": "0.409283800887|0.409283961861|13478206|0",
        "continue": "-||"
    },
    "query": {
        "random": [
            {
                "id": 123456789,
                "ns": 0,
                "title": "RANDOM TEST TITLE"
            }
        ]
    }
}
"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&formatversion=2&list=categorymembers&cmlimit=500&cmtitle=Category%3ABAFTA%20winners%20%28people%29'

response = r"""{
    "batchcomplete": true,
    "continue": {
        "cmcontinue": "page|412745372f4907044b352f2f41273d03424b352f2f412704412745372f490121018f7f8f7f8f808f09|42525291",
        "continue": "-||"
    },
    "query": {
        "categorymembers": [
            {
                "pageid": 22167530,
                "ns": 0,
                "title": "Allison Abbate"
            }
        ]
    }
}"""

cache = {'query': query,
         'response': response,
         'info': {'content-type': 'TEST', 'status': 200}}

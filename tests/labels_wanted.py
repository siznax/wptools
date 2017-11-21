# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&formatversion=2&languages=en&props=labels&redirects=yes&ids=P31|Q5'

response = r"""{
    "entities": {
        "P31": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P31",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "instance of"
                }
            }
        },
        "Q5": {
            "type": "item",
            "id": "Q5",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "human"
                }
            }
        }
    },
    "success": 1
}"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

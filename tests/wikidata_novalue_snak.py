# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&formatversion=2&ids=Q483718&languages=en&props=info|claims|descriptions|labels|sitelinks&redirects=yes&sites=&titles='

response = r"""{
    "entities": {
        "Q483718": {
            "pageid": 455294,
            "ns": 0,
            "title": "Q483718",
            "lastrevid": 610328494,
            "modified": "2017-12-17T18:21:13Z",
            "type": "item",
            "id": "Q483718",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Foo Fighters"
                }
            },
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "American rock band, formed in Seattle in 1994"
                }
            },
            "claims": {
                "P576": [
                    {
                        "mainsnak": {
                            "snaktype": "novalue",
                            "property": "P576",
                            "hash": "6a18d40010201ff9031e85a3fe98f1f0dc1d7cc4",
                            "datatype": "time"
                        },
                        "type": "statement",
                        "id": "Q483718$9da5583a-45e8-4268-2770-41d999bd53da",
                        "rank": "normal"
                    }
                ],
                "P373": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P373",
                            "hash": "4d08e8ef6597a712d926b71c1c3b52d51d99a1a9",
                            "datavalue": {
                                "value": "Foo Fighters",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "q483718$6CA37AA3-178A-41CF-B219-46F9BA68CC03",
                        "rank": "normal"
                    }
                ]
            },
            "sitelinks": {}
        }
    },
    "success": 1
}"""

cache = {'query': query, 'response': response}

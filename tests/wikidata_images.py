# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&formatversion=2&ids=Q857243&languages=en&props=info|claims|descriptions|labels|sitelinks&redirects=yes&sites=&titles='

response = r"""
{
    "entities": {
        "Q857243": {
            "claims": {
                "P18": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P18",
                            "datavalue": {
                                "value": "Gujo Gifu Japan.jpg",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "id": "q857243$50FA69EA-DC47-4C86-8748-FA11095C8A4F",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P18",
                            "datavalue": {
                                "value": "Gujo in Gifu Prefecture.png",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "id": "q857243$8C06CEEB-F4D0-471F-95E9-90662320897A",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P18",
                            "datavalue": {
                                "value": "Flag of Gujo Gifu.JPG",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "id": "q857243$510BBCCE-C86A-4E0D-99F6-36ACEC1B39FC",
                        "rank": "normal"
                    }
                ]
            }
        }
    },
    "success": 1
}
"""

cache = {'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&formatversion=2&languages=en&props=labels&redirects=yes&ids=Q24925|Q14623683|P535|Q6625963|P2387|P434|Q1860|P3762|Q159288|Q4961791|P1273|P2469|P1375|P136|Q145|P1284|Q214917|Q19688263|Q351735|Q7066|P2168|P1411|P910|P1412|P1415|P1417|Q8935487|Q25169|Q40831|P1303|P2963|P1263|P998|P1266|Q463035|P1207|P1816|P950|P1015|Q2576795|Q721|P2605|P2604|P2607|P1315|P214|Q187655|Q14623678|P1953|Q14623675'

response = r"""{
    "entities": {
        "Q24925": {
            "type": "item",
            "id": "Q24925",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "science fiction"
                }
            }
        },
        "Q14623683": {
            "type": "item",
            "id": "Q14623683",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Polly Jane Rocket Adams"
                }
            }
        },
        "P535": {
            "type": "property",
            "datatype": "external-id",
            "id": "P535",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Find a Grave grave ID"
                }
            }
        },
        "Q6625963": {
            "type": "item",
            "id": "Q6625963",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "novelist"
                }
            }
        },
        "P2387": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2387",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Elonet person ID"
                }
            }
        },
        "P434": {
            "type": "property",
            "datatype": "external-id",
            "id": "P434",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "MusicBrainz artist ID"
                }
            }
        },
        "Q1860": {
            "type": "item",
            "id": "Q1860",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "English"
                }
            }
        },
        "P3762": {
            "type": "property",
            "datatype": "external-id",
            "id": "P3762",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "openMLOL author ID"
                }
            }
        },
        "Q159288": {
            "type": "item",
            "id": "Q159288",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Santa Barbara"
                }
            }
        },
        "Q4961791": {
            "type": "item",
            "id": "Q4961791",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Brentwood School"
                }
            }
        },
        "P1273": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1273",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "CANTIC-ID"
                }
            }
        },
        "P2469": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2469",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Theatricalia person ID"
                }
            }
        },
        "P1375": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1375",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "NSK ID"
                }
            }
        },
        "P136": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P136",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "genre"
                }
            }
        },
        "Q145": {
            "type": "item",
            "id": "Q145",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "United Kingdom"
                }
            }
        },
        "P1284": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1284",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Munzinger IBA"
                }
            }
        },
        "Q214917": {
            "type": "item",
            "id": "Q214917",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "playwright"
                }
            }
        },
        "Q19688263": {
            "type": "item",
            "id": "Q19688263",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Noël"
                }
            }
        },
        "Q351735": {
            "type": "item",
            "id": "Q351735",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Adams"
                }
            }
        },
        "Q7066": {
            "type": "item",
            "id": "Q7066",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "atheism"
                }
            }
        },
        "P2168": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2168",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "SFDb person ID"
                }
            }
        },
        "P1411": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P1411",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "nominated for"
                }
            }
        },
        "P910": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P910",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "topic's main category"
                }
            }
        },
        "P1412": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P1412",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "languages spoken, written or signed"
                }
            }
        },
        "P1415": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1415",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Oxford Biography Index Number"
                }
            }
        },
        "P1417": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1417",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Encyclopædia Britannica Online ID"
                }
            }
        },
        "Q8935487": {
            "type": "item",
            "id": "Q8935487",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Category:Douglas Adams"
                }
            }
        },
        "Q25169": {
            "type": "item",
            "id": "Q25169",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "The Hitchhiker's Guide to the Galaxy pentalogy"
                }
            }
        },
        "Q40831": {
            "type": "item",
            "id": "Q40831",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "comedy"
                }
            }
        },
        "P1303": {
            "type": "property",
            "datatype": "wikibase-item",
            "id": "P1303",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "instrument"
                }
            }
        },
        "P2963": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2963",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Goodreads author ID"
                }
            }
        },
        "P1263": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1263",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "NNDB people ID"
                }
            }
        },
        "P998": {
            "type": "property",
            "datatype": "external-id",
            "id": "P998",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "DMOZ ID"
                }
            }
        },
        "P1266": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1266",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "AlloCiné person ID"
                }
            }
        },
        "Q463035": {
            "type": "item",
            "id": "Q463035",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Douglas"
                }
            }
        },
        "P1207": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1207",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "NUKAT (WarsawU) authorities"
                }
            }
        },
        "P1816": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1816",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "National Portrait Gallery (London) person ID"
                }
            }
        },
        "P950": {
            "type": "property",
            "datatype": "external-id",
            "id": "P950",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "BNE ID"
                }
            }
        },
        "P1015": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1015",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "BIBSYS ID"
                }
            }
        },
        "Q2576795": {
            "type": "item",
            "id": "Q2576795",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Locus Award for Best Science Fiction Novel"
                }
            }
        },
        "Q721": {
            "type": "item",
            "id": "Q721",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Life, the Universe and Everything"
                }
            }
        },
        "P2605": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2605",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "ČSFD person ID"
                }
            }
        },
        "P2604": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2604",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Kinopoisk person ID"
                }
            }
        },
        "P2607": {
            "type": "property",
            "datatype": "external-id",
            "id": "P2607",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "BookBrainz creator ID"
                }
            }
        },
        "P1315": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1315",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "People Australia ID"
                }
            }
        },
        "P214": {
            "type": "property",
            "datatype": "external-id",
            "id": "P214",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "VIAF ID"
                }
            }
        },
        "Q187655": {
            "type": "item",
            "id": "Q187655",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Mostly Harmless"
                }
            }
        },
        "Q14623678": {
            "type": "item",
            "id": "Q14623678",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Janet Adams"
                }
            }
        },
        "P1953": {
            "type": "property",
            "datatype": "external-id",
            "id": "P1953",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Discogs artist ID"
                }
            }
        },
        "Q14623675": {
            "type": "item",
            "id": "Q14623675",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Christopher Douglas Adams"
                }
            }
        }
    },
    "success": 1
}"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

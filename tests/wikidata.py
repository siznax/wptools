# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&formatversion=2&ids=Q42&languages=en&props=info|claims|descriptions|labels|sitelinks&redirects=yes&sites=&titles='

response = r"""{
    "entities": {
        "Q42": {
            "pageid": 138,
            "ns": 0,
            "title": "Q42",
            "lastrevid": 595492361,
            "modified": "2017-11-18T10:46:38Z",
            "type": "item",
            "id": "Q42",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Douglas Adams"
                }
            },
            "descriptions": {
                "en": {
                    "language": "en",
                    "value": "English writer and humorist"
                }
            },
            "aliases": {
                "en": [
                    {
                        "language": "en",
                        "value": "Douglas Noël Adams"
                    },
                    {
                        "language": "en",
                        "value": "Douglas Noel Adams"
                    },
                    {
                        "language": "en",
                        "value": "Douglas N. Adams"
                    },
                    {
                        "language": "en",
                        "value": "DNA"
                    }
                ]
            },
            "claims": {
                "P31": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "hash": "ad7d38a03cdd40cdc373de0dc4e7b7fcbccb31d9",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 5,
                                    "id": "Q5"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$F078E5B3-F9A8-480E-B7AC-D97778CBBEF9",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2b369d0a4f1d4b801e734fe84a0b217e13dd2930",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P214": [
                                        {
                                            "snaktype": "value",
                                            "property": "P214",
                                            "hash": "20e5c69fbf37b8b0402a52948a04f481028e819c",
                                            "datavalue": {
                                                "value": "113230702",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P214",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "55d23126bca9913374faf69ba8fbd21474a74421",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "da30562523b94bc9c043e8ecdf983c520d76fa31",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 20666306,
                                                    "id": "Q20666306"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d6162a1716489623c6e595e448b17f8dca4fb2e8",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-10-10T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "c2533c0aa0d8cbc5c781f5649e9fca5b633d2954",
                                            "datavalue": {
                                                "value": "http://data.bnf.fr/ark:/12148/cb11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813",
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P21": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P21",
                            "hash": "85ad4b1c7348f7a5aac521135040d74e91fb5939",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 6581097,
                                    "id": "Q6581097"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$39F4DE4F-C277-449C-9F99-512350971B5B",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2b369d0a4f1d4b801e734fe84a0b217e13dd2930",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P214": [
                                        {
                                            "snaktype": "value",
                                            "property": "P214",
                                            "hash": "20e5c69fbf37b8b0402a52948a04f481028e819c",
                                            "datavalue": {
                                                "value": "113230702",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P214",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "55d23126bca9913374faf69ba8fbd21474a74421",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "da30562523b94bc9c043e8ecdf983c520d76fa31",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 20666306,
                                                    "id": "Q20666306"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d6162a1716489623c6e595e448b17f8dca4fb2e8",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-10-10T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "c2533c0aa0d8cbc5c781f5649e9fca5b633d2954",
                                            "datavalue": {
                                                "value": "http://data.bnf.fr/ark:/12148/cb11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813",
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P106": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "1ecddfdb184ec1e8540abf98fb07f825697cfab5",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 214917,
                                    "id": "Q214917"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$e0f736bd-4711-c43b-9277-af1e9b2fb85f",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "8c403faaa2be823ac66d54a4e5e1c37ddbf96da0",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 28389,
                                    "id": "Q28389"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$E13E619F-63EF-4B72-99D9-7A45C7C6AD34",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "f67142030dd221e1441a10a7438323ad44f35be8",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "52af760ff9ceb914251924abe88e53af182b0f92",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 193563,
                                                    "id": "Q193563"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P268": [
                                        {
                                            "snaktype": "value",
                                            "property": "P268",
                                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                                            "datavalue": {
                                                "value": "11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P268",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "0fed87b3320338e0ed0587df9b43e47cfcf5b69f",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "d679e707f58412628d39fb85af3e5393e7935e69",
                                            "datavalue": {
                                                "value": "http://www.jinni.com/tv/the-hitchhikers-guide-to-the-galaxy/cast-crew/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "7992d2aec094f84d664106049d9a4955d096082f",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 6625963,
                                    "id": "Q6625963"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$D6E21D67-05D6-4A0B-8458-0744FCEED13D",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "05de1894dc52a056fa732acf7078c4f194b036d5",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4853732,
                                    "id": "Q4853732"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$7eb8aaef-4ddf-8b87-bd02-406f91a296bd",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "468425a7d5990169ca1caa25413280f78cb985f8",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 18844224,
                                    "id": "Q18844224"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$CBDC4890-D5A2-469C-AEBB-EFB682B891E7",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "f67142030dd221e1441a10a7438323ad44f35be8",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "52af760ff9ceb914251924abe88e53af182b0f92",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 193563,
                                                    "id": "Q193563"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P268": [
                                        {
                                            "snaktype": "value",
                                            "property": "P268",
                                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                                            "datavalue": {
                                                "value": "11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P268",
                                    "P813"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P106",
                            "hash": "cb6956acd8af4f54927985ab67fb99c443340c03",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 245068,
                                    "id": "Q245068"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$58F0D772-9CE4-46AC-BF0D-FBBBAFA09603",
                        "rank": "normal"
                    }
                ],
                "P800": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "12e1c410170de1e9247f6517a0da31885e9d1d62",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 25169,
                                    "id": "Q25169"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P136": [
                                {
                                    "snaktype": "value",
                                    "property": "P136",
                                    "hash": "010718c36d933cb00795903712d779d5b3cc62d0",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 761469,
                                            "id": "Q761469"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P136"
                        ],
                        "id": "Q42$FA73986E-3D1D-4CAB-B358-424B58544620",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "19aec4ad94f8f793baf97eff96428a7868c3ae1a",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 902712,
                                    "id": "Q902712"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$61ce65a9-454a-5b97-e014-496299c1c03a",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "2f2742d0598fbc9673d3ef91ff5dbe88188276c2",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 7758404,
                                    "id": "Q7758404"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$1c92fbe2-4743-0b27-e4ac-16320efe7864",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "b58323a2e4f5967c72329d490c2e12a239650abb",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 578895,
                                    "id": "Q578895"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$e4b3a5e3-422e-593a-5b7c-3b12b5a4a0bb",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "25fb237a83b453c0406675e5a78e93611b0d5ea8",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 721,
                                    "id": "Q721"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$f338abf5-43cb-f5eb-1d32-9cdb73c084b9",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "1dbd4866665f07859d17e2e17d553f29a3351912",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 1042294,
                                    "id": "Q1042294"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$a7ebf426-476d-5cd9-b489-d849c8e0a82d",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P800",
                            "hash": "8f53ca9ce292d556286e3029f4fa69eb0f3e1411",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 187655,
                                    "id": "Q187655"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$586d443e-43ef-fdc2-223f-c4ff6c2b6531",
                        "rank": "normal"
                    }
                ],
                "P569": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P569",
                            "hash": "27f538a50ad110d1e6716c972f5f0ac24ca17430",
                            "datavalue": {
                                "value": {
                                    "time": "+1952-03-11T00:00:00Z",
                                    "timezone": 0,
                                    "before": 0,
                                    "after": 0,
                                    "precision": 11,
                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                },
                                "type": "time"
                            },
                            "datatype": "time"
                        },
                        "type": "statement",
                        "id": "q42$D8404CDA-25E4-4334-AF13-A3290BCD9C0F",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2f26d70b1e8b8cb53882b83197d1859e226da12d",
                                "snaks": {
                                    "P268": [
                                        {
                                            "snaktype": "value",
                                            "property": "P268",
                                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                                            "datavalue": {
                                                "value": "11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d257e42604861810e838f211e8259afd949dd449",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 15222191,
                                                    "id": "Q15222191"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P268",
                                    "P248",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            },
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "55d23126bca9913374faf69ba8fbd21474a74421",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "da30562523b94bc9c043e8ecdf983c520d76fa31",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 20666306,
                                                    "id": "Q20666306"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d6162a1716489623c6e595e448b17f8dca4fb2e8",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-10-10T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "c2533c0aa0d8cbc5c781f5649e9fca5b633d2954",
                                            "datavalue": {
                                                "value": "http://data.bnf.fr/ark:/12148/cb11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813",
                                    "P854"
                                ]
                            },
                            {
                                "hash": "3bc90af5225a0b1248b3362e911577073e904e20",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "dbd2f3b8b11eb0da5209a6ea4a74ce0df88c749b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1139587,
                                                    "id": "Q1139587"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P2168": [
                                        {
                                            "snaktype": "value",
                                            "property": "P2168",
                                            "hash": "5b535a453c0f88c11cb592ae35510abe93d2eec5",
                                            "datavalue": {
                                                "value": "271209",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "b468ee5535c44e76e52a8ad71217a0f5c5077d19",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2016-01-11T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P2168",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "b460d7e5cae668698a5dfe74198df6632fe7231d",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "f98ec89708e8eab9511c049702ef59df0721d652",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 29861311,
                                                    "id": "Q29861311"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P3430": [
                                        {
                                            "snaktype": "value",
                                            "property": "P3430",
                                            "hash": "1e9a0d6461bed3d3b3f7ed1956b151058982cd6e",
                                            "datavalue": {
                                                "value": "w65h7md1",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P1810": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1810",
                                            "hash": "03773f9c659ee8c03a232bce2522c8bb1b66402c",
                                            "datavalue": {
                                                "value": "Douglas Adams",
                                                "type": "string"
                                            },
                                            "datatype": "string"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "e5f60ab0b03700bb883efce38f8022d023bc49fb",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2017-10-09T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P3430",
                                    "P1810",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P19": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P19",
                            "hash": "779e8852aac9ba2014a9434016cba24b1890a9da",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 350,
                                    "id": "Q350"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$3D284234-52BC-4DA3-83A3-7C39F84BA518",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            },
                            {
                                "hash": "3f4d26cf841e20630c969afc0e48e5e3ef0c5a49",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "a99756c83f320398a58edbbdccd46eb682e68267",
                                            "datavalue": {
                                                "value": "http://www.theguardian.com/news/2001/may/15/guardianobituaries.books",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "27c7402a696628d2a0e5abbf443995be8b895503",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-15T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1433": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1433",
                                            "hash": "5c3e5ddc26dbc4ebdea58b53cc7f40811ef9e2ec",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 11148,
                                                    "id": "Q11148"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P50": [
                                        {
                                            "snaktype": "value",
                                            "property": "P50",
                                            "hash": "0c09ca36156b084dd45e1b836575dc7382d4a16e",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 18145749,
                                                    "id": "Q18145749"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "0730f27f8dcabe7b3d74ea981c7a9c15ea162685",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Obituary: Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P577",
                                    "P813",
                                    "P1433",
                                    "P50",
                                    "P1476",
                                    "P407"
                                ]
                            },
                            {
                                "hash": "51a934797fd7f7d3ee91d4d541356d4c5974075b",
                                "snaks": {
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "608a4db5259bcc914081457a65a62291c0d60fba",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Hitch Hiker's Guide author Douglas Adams dies aged 49",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "9a430275f318d708678f048d2fcc2f4e1336fccf",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-13T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "104d5e67002108464e8ba616831c50d82c4d25a3",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 192621,
                                                    "id": "Q192621"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "f58a3ab6374660155a7a316dc8e0fb3e2a30263b",
                                            "datavalue": {
                                                "value": "http://www.telegraph.co.uk/news/uknews/1330072/Hitch-Hikers-Guide-author-Douglas-Adams-dies-aged-49.html",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "0af3fa4e868fcf34f10f64051305ed69118d9254",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-01-03T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P1476",
                                    "P577",
                                    "P123",
                                    "P407",
                                    "P854",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P570": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P570",
                            "hash": "ccf97856f19fb921cadad798dea5abfcbfc0e6b8",
                            "datavalue": {
                                "value": {
                                    "time": "+2001-05-11T00:00:00Z",
                                    "timezone": 0,
                                    "before": 0,
                                    "after": 0,
                                    "precision": 11,
                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                },
                                "type": "time"
                            },
                            "datatype": "time"
                        },
                        "type": "statement",
                        "id": "q42$65EA9C32-B26C-469B-84FE-FC612B71D159",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2f26d70b1e8b8cb53882b83197d1859e226da12d",
                                "snaks": {
                                    "P268": [
                                        {
                                            "snaktype": "value",
                                            "property": "P268",
                                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                                            "datavalue": {
                                                "value": "11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d257e42604861810e838f211e8259afd949dd449",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 15222191,
                                                    "id": "Q15222191"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P268",
                                    "P248",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            },
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "55d23126bca9913374faf69ba8fbd21474a74421",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "da30562523b94bc9c043e8ecdf983c520d76fa31",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 20666306,
                                                    "id": "Q20666306"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d6162a1716489623c6e595e448b17f8dca4fb2e8",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-10-10T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "c2533c0aa0d8cbc5c781f5649e9fca5b633d2954",
                                            "datavalue": {
                                                "value": "http://data.bnf.fr/ark:/12148/cb11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813",
                                    "P854"
                                ]
                            },
                            {
                                "hash": "3a2f66aa7504902a2fa5189eb8a4aba3e0447e76",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "fb806ab9d533f93ee49c47680c403030f49d154f",
                                            "datavalue": {
                                                "value": "http://www.imdb.com/name/nm0010930/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "0068a6ea23b0337bd9b652f998d0030ac8ed7235",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-12-28T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "3bc90af5225a0b1248b3362e911577073e904e20",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "dbd2f3b8b11eb0da5209a6ea4a74ce0df88c749b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1139587,
                                                    "id": "Q1139587"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P2168": [
                                        {
                                            "snaktype": "value",
                                            "property": "P2168",
                                            "hash": "5b535a453c0f88c11cb592ae35510abe93d2eec5",
                                            "datavalue": {
                                                "value": "271209",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "b468ee5535c44e76e52a8ad71217a0f5c5077d19",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2016-01-11T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P2168",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "b460d7e5cae668698a5dfe74198df6632fe7231d",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "f98ec89708e8eab9511c049702ef59df0721d652",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 29861311,
                                                    "id": "Q29861311"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P3430": [
                                        {
                                            "snaktype": "value",
                                            "property": "P3430",
                                            "hash": "1e9a0d6461bed3d3b3f7ed1956b151058982cd6e",
                                            "datavalue": {
                                                "value": "w65h7md1",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P1810": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1810",
                                            "hash": "03773f9c659ee8c03a232bce2522c8bb1b66402c",
                                            "datavalue": {
                                                "value": "Douglas Adams",
                                                "type": "string"
                                            },
                                            "datatype": "string"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "e5f60ab0b03700bb883efce38f8022d023bc49fb",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2017-10-09T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P3430",
                                    "P1810",
                                    "P813"
                                ]
                            },
                            {
                                "hash": "e9a6c72ac1c0c2bc336ff672ddaf89ecd17fff68",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "473ac6b52f2c348ee11cff8601894a2e9a3cf838",
                                            "datavalue": {
                                                "value": "https://www.theguardian.com/uk/2001/may/13/books.booksnews",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "53b72c0a5e7ac57b3d64967a96bf920db6313b87",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2017-10-28T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P1196": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1196",
                            "hash": "95c96aff195f7cfc9cd0c684f46ebed97ae1c5f4",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 3739104,
                                    "id": "Q3739104"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$2CF6704F-527F-46F7-9A89-41FC0C9DF492",
                        "rank": "normal"
                    }
                ],
                "P509": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P509",
                            "hash": "7c9686796c28e0d6dbb7a35cf2975c1bba3f2291",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 12152,
                                    "id": "Q12152"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$E651BD8A-EA3E-478A-8558-C956EE60B29F",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "61039b96706750437e9bfd3a6beaeb0bd1d16ef1",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "29658ead4a7640c28bb3c1176b16bc05c1165352",
                                            "datavalue": {
                                                "value": "http://www.historyorb.com/people/douglas-adams",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "cc52dc102ff9f4aab357824867ced3126a88d76a",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 15290366,
                                                    "id": "Q15290366"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "1e70ab6477d30a1f61497e41162394447f226c6b",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Famous People - Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            },
                            {
                                "hash": "8ff79d35ac039707be382250be2789f2e21ee59f",
                                "snaks": {
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "0730f27f8dcabe7b3d74ea981c7a9c15ea162685",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Obituary: Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "7cc99d0eec7b745edccf680f3347956e14188d2a",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 11148,
                                                    "id": "Q11148"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "27c7402a696628d2a0e5abbf443995be8b895503",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-15T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "a99756c83f320398a58edbbdccd46eb682e68267",
                                            "datavalue": {
                                                "value": "http://www.theguardian.com/news/2001/may/15/guardianobituaries.books",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d81043f19518b0726f361bea2dd5eb2caa8cb454",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2014-01-03T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P50": [
                                        {
                                            "snaktype": "value",
                                            "property": "P50",
                                            "hash": "0c09ca36156b084dd45e1b836575dc7382d4a16e",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 18145749,
                                                    "id": "Q18145749"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P1476",
                                    "P123",
                                    "P577",
                                    "P407",
                                    "P854",
                                    "P813",
                                    "P50"
                                ]
                            },
                            {
                                "hash": "a51c458cb5e6abe7176b570b062bd8989bae0821",
                                "snaks": {
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "608a4db5259bcc914081457a65a62291c0d60fba",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Hitch Hiker's Guide author Douglas Adams dies aged 49",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "104d5e67002108464e8ba616831c50d82c4d25a3",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 192621,
                                                    "id": "Q192621"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "9a430275f318d708678f048d2fcc2f4e1336fccf",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-13T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "f58a3ab6374660155a7a316dc8e0fb3e2a30263b",
                                            "datavalue": {
                                                "value": "http://www.telegraph.co.uk/news/uknews/1330072/Hitch-Hikers-Guide-author-Douglas-Adams-dies-aged-49.html",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d81043f19518b0726f361bea2dd5eb2caa8cb454",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2014-01-03T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P1476",
                                    "P123",
                                    "P577",
                                    "P407",
                                    "P854",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P20": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P20",
                            "hash": "83bea4973abdd248ba04a3149ce7ce6952b4c9b0",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 159288,
                                    "id": "Q159288"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$C0DE2013-54C0-48F9-AD90-8A235248D8C7",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            },
                            {
                                "hash": "defb9736023b969ef081bca13cc69d80c1e11f46",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "f11da58783cfeb447930ec66140c9c809464411f",
                                            "datavalue": {
                                                "value": "http://www.nytimes.com/books/01/05/13/daily/adams-obit.html",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "9e597a1ff0ca651f1af353078d5399eed329d6ce",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-12T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "2714993a93f86610bb90b55161a935eab4be05fc",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 9684,
                                                    "id": "Q9684"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P50": [
                                        {
                                            "snaktype": "value",
                                            "property": "P50",
                                            "hash": "419ce2e3b0574f6aa77d16d971681078a27337c6",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 26724169,
                                                    "id": "Q26724169"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "f7562124f8f0eedb06fd945242d8c7789ad10e74",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams, Author of 'Hitchhiker's Guide to the Galaxy,' Dies at 49",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P577",
                                    "P123",
                                    "P50",
                                    "P407",
                                    "P1476"
                                ]
                            },
                            {
                                "hash": "de76f366926e923ef61d60535280c65570d26cc2",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "effd2a5d8045dbb30aa66c3be3755e84165f5369",
                                            "datavalue": {
                                                "value": "http://www.eskimo.com/~rkj/weekly/aa051701a.htm",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            },
                            {
                                "hash": "027c2e3272694f0292b8ed6efa7d26e4b27fa458",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "4ff990b07c7dab21f6354e0022ce8240d74220ea",
                                            "datavalue": {
                                                "value": "http://www.waymarking.com/waymarks/WMH912_Douglas_Adams_Highgate_East_Cemetery_London_UK",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P119": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P119",
                            "hash": "f22d367759fe126d0723a18e59399e4206b8f37d",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 533697,
                                    "id": "Q533697"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$881F40DC-0AFE-4FEB-B882-79600D234273",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "8a052e1954b77ac5a7a865617768d7526599f913",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "e9255857dc130ffd8c712ebbe7ab0f6981ebe238",
                                            "datavalue": {
                                                "value": "http://highgatecemetery.org/visit/who",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "81bbb971630c0e2dcb97f07d2fc77742a4bead4e",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 533697,
                                                    "id": "Q533697"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "ff1f7fd05dc971bfb5e56d485c37d091bcc3d06f",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Who’s here",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P1442": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1442",
                            "hash": "fb7cd07a669a425f896132e0b8cfdb97254b1650",
                            "datavalue": {
                                "value": "Douglas Adams' gravestone.jpg",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "id": "Q42$db1ba2ba-47b9-3650-e6c4-db683abf788c",
                        "rank": "normal"
                    }
                ],
                "P1015": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1015",
                            "hash": "33cb2c4a2227c950c19177a4c85fc4e38cacf526",
                            "datavalue": {
                                "value": "90196888",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$6583fdb7-4ffa-9fe1-4288-1a1cbb2950d0",
                        "rank": "normal"
                    }
                ],
                "P735": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P735",
                            "hash": "bc69fedf2b7ca78a342409c262e30f07008590cd",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 463035,
                                    "id": "Q463035"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$1d7d0ea9-412f-8b5b-ba8d-405ab9ecf026",
                        "rank": "preferred",
                        "references": [
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P735",
                            "hash": "d5521b1edbeae4d9c264dda7f7c783b287125768",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 19688263,
                                    "id": "Q19688263"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$1e106952-4b58-6067-c831-8593ce3d70f5",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P734": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P734",
                            "hash": "b421edc57d660e9be8eb719ee6f927f848281fcc",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 351735,
                                    "id": "Q351735"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$24df999a-4629-c679-e1f0-199bcefabbf3",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "a02f3a77ddd343e6b88be25696b055f5131c3d64",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "019a50b7de741e0068bde41c9d9955b22a5de47b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 36578,
                                                    "id": "Q36578"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P227": [
                                        {
                                            "snaktype": "value",
                                            "property": "P227",
                                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                                            "datavalue": {
                                                "value": "119033364",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "c1b3a8484d531e0eac6b9835b63e74b1412ccdb0",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P227",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P1559": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1559",
                            "hash": "95644e72f595a3bc535e0eb316325ee88d9466f8",
                            "datavalue": {
                                "value": {
                                    "text": "Douglas Adams",
                                    "language": "en"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q42$88CB3380-ADFB-427B-87E5-C8D537545FE8",
                        "rank": "normal"
                    }
                ],
                "P18": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P18",
                            "hash": "5e0f24b66c3761cfc054ea25a92c5a7fb73ab703",
                            "datavalue": {
                                "value": "Douglas adams portrait cropped.jpg",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P2096": [
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "8406a17fdbde124e88aef130bef59ce9178d1e75",
                                    "datavalue": {
                                        "value": {
                                            "text": "Portræt af Douglas Adams",
                                            "language": "da"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "5220766c2a4c803feb845e3dd3dbe3a8893a2789",
                                    "datavalue": {
                                        "value": {
                                            "text": "A portrait photo of Douglas Adams",
                                            "language": "en"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "3e61ddc5db06441ca450d9df1b27401afe9c2718",
                                    "datavalue": {
                                        "value": {
                                            "text": "Portrait de Douglas Adams.",
                                            "language": "fr"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "daa551e283c4d6c7637beeb49174ca8666b78fae",
                                    "datavalue": {
                                        "value": {
                                            "text": "Douglas Adams' Porträt.",
                                            "language": "de"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "c67416544467f9ab404b4b01323fc59a901257ec",
                                    "datavalue": {
                                        "value": {
                                            "text": "Portrét Douglase Adamse",
                                            "language": "cs"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "143d7b420be9b46cd82cdefb13f8388f69204978",
                                    "datavalue": {
                                        "value": {
                                            "text": "דיוקנו של דאגלס אדמס.",
                                            "language": "he"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "71352d2e108d8928e04f35ccc499f3dd5a1d324c",
                                    "datavalue": {
                                        "value": {
                                            "text": "Портрет Дугласа Адамса",
                                            "language": "ru"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "d6a97c29af0840ae5a26ca57c116a0dbfc2cf8fa",
                                    "datavalue": {
                                        "value": {
                                            "text": "Retrato de Douglas Adams.",
                                            "language": "es"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "34d5b0907828496ae7c902f5df236ef00ec04a10",
                                    "datavalue": {
                                        "value": {
                                            "text": "Douglas Adamsen erretratua.",
                                            "language": "eu"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                },
                                {
                                    "snaktype": "value",
                                    "property": "P2096",
                                    "hash": "079948a024785a3bfa2605c7119705c4777900e6",
                                    "datavalue": {
                                        "value": {
                                            "text": "portrét Douglase Adamse",
                                            "language": "cs"
                                        },
                                        "type": "monolingualtext"
                                    },
                                    "datatype": "monolingualtext"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P2096"
                        ],
                        "id": "Q42$44889d0f-474c-4fb9-1961-9a3366cbbb9e",
                        "rank": "normal"
                    }
                ],
                "P27": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P27",
                            "hash": "2de1ec1c14395359e1936021bcfb525b4daa9a76",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 145,
                                    "id": "Q145"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$DE2A0C89-6199-44D0-B727-D7A4BE031A2B",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2b369d0a4f1d4b801e734fe84a0b217e13dd2930",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P214": [
                                        {
                                            "snaktype": "value",
                                            "property": "P214",
                                            "hash": "20e5c69fbf37b8b0402a52948a04f481028e819c",
                                            "datavalue": {
                                                "value": "113230702",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P214",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P551": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P551",
                            "hash": "13883b9303b6163e00106585ddebcdfe487b8e83",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 159288,
                                    "id": "Q159288"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P582": [
                                {
                                    "snaktype": "value",
                                    "property": "P582",
                                    "hash": "8798597f326000b4ffd9948d42771308bdb23133",
                                    "datavalue": {
                                        "value": {
                                            "time": "+2001-05-11T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 11,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P582"
                        ],
                        "id": "Q42$E88EA363-419C-4FEA-BC63-F32669255382",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P551",
                            "hash": "4f1ebc8d1eeffa38fca7d811242ed71f4c5bed0f",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 84,
                                    "id": "Q84"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$9D3B2F23-36F4-4212-983B-DC15D47FC01E",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P551",
                            "hash": "9603fd343c189883b34772a21404dc1f8fb021f8",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 909993,
                                    "id": "Q909993"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P580": [
                                {
                                    "snaktype": "value",
                                    "property": "P580",
                                    "hash": "c786a8b39f62b37eb45745acf99302b5409f2e26",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1957-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P580"
                        ],
                        "id": "Q42$21492F88-0043-439D-B733-C7211D2283F7",
                        "rank": "normal"
                    }
                ],
                "P103": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P103",
                            "hash": "94131f8f22ef0e6c2fe4b312ea8927de20e28296",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 1860,
                                    "id": "Q1860"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$D9E6DEFB-472B-44F6-A8E2-E2B90700C74A",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "f67142030dd221e1441a10a7438323ad44f35be8",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "52af760ff9ceb914251924abe88e53af182b0f92",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 193563,
                                                    "id": "Q193563"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P268": [
                                        {
                                            "snaktype": "value",
                                            "property": "P268",
                                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                                            "datavalue": {
                                                "value": "11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P268",
                                    "P813"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P103",
                            "hash": "cf46b882e332cf9f4436ef2aea7c9516774881ba",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 7979,
                                    "id": "Q7979"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$b7526300-4ac5-a529-3a91-c8a0120673be",
                        "rank": "normal"
                    }
                ],
                "P1477": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1477",
                            "hash": "0f62a3d9d4a4e0ea07ccc5cefab5d5730cdf1b32",
                            "datavalue": {
                                "value": {
                                    "text": "Douglas Noel Adams",
                                    "language": "en-gb"
                                },
                                "type": "monolingualtext"
                            },
                            "datatype": "monolingualtext"
                        },
                        "type": "statement",
                        "id": "Q42$45220d20-40d2-299e-f4cc-f6cce89f2f42",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "67b9be98c538c1186a117125edcb254f4f351812",
                                "snaks": {
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "0730f27f8dcabe7b3d74ea981c7a9c15ea162685",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Obituary: Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "7cc99d0eec7b745edccf680f3347956e14188d2a",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 11148,
                                                    "id": "Q11148"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "27c7402a696628d2a0e5abbf443995be8b895503",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-05-15T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "a99756c83f320398a58edbbdccd46eb682e68267",
                                            "datavalue": {
                                                "value": "http://www.theguardian.com/news/2001/may/15/guardianobituaries.books",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P50": [
                                        {
                                            "snaktype": "value",
                                            "property": "P50",
                                            "hash": "0c09ca36156b084dd45e1b836575dc7382d4a16e",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 18145749,
                                                    "id": "Q18145749"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P1476",
                                    "P123",
                                    "P577",
                                    "P407",
                                    "P854",
                                    "P813",
                                    "P50"
                                ]
                            }
                        ]
                    }
                ],
                "P1368": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1368",
                            "hash": "a724070c64f13db757c53d1f769083a74d47ac67",
                            "datavalue": {
                                "value": "000057405",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$11725e9f-4f81-e0fd-b00a-b885fe7a75ac",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P244": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P244",
                            "hash": "5308b152b94274513309d2ad5cee9b9286fff0bd",
                            "datavalue": {
                                "value": "n80076765",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$2D472379-EC67-4C71-9700-0F9D551BF5E6",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "14d2400e3b1d36332748dc330276f099eeaa8800",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "39224a9c2e8ce5424defbd16603d25771956c7fc",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1551807,
                                                    "id": "Q1551807"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P947": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P947",
                            "hash": "b4a90e2f8841117a6add1d92098d457a0b615831",
                            "datavalue": {
                                "value": "000002833",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$cf5f61ec-440d-60d4-7847-e95f75171f2f",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "e13240e63b2eb76c57e8e26db9d04e0065d1d336",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "e75f69c99737f47627612a57905a3e5988ef44e2",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1048694,
                                                    "id": "Q1048694"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P214": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P214",
                            "hash": "20e5c69fbf37b8b0402a52948a04f481028e819c",
                            "datavalue": {
                                "value": "113230702",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$488251B2-6732-4D49-85B0-6101803C97AB",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "14d2400e3b1d36332748dc330276f099eeaa8800",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "39224a9c2e8ce5424defbd16603d25771956c7fc",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1551807,
                                                    "id": "Q1551807"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P345": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P345",
                            "hash": "c5e0f8f8e24ac2a6721b316e2a3a73820e61bc11",
                            "datavalue": {
                                "value": "nm0010930",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$231549F5-0296-4D87-993D-6CBE3F24C0D2",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 48183,
                                                    "id": "Q48183"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P373": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P373",
                            "hash": "cd5ccca2ccdf15c9c1894d1ce7f01df9a1c17fbd",
                            "datavalue": {
                                "value": "Douglas Adams",
                                "type": "string"
                            },
                            "datatype": "string"
                        },
                        "type": "statement",
                        "id": "q42$7EC4631F-FB22-4768-9B75-61875CD6C854",
                        "rank": "normal"
                    }
                ],
                "P349": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P349",
                            "hash": "a544d8f45670d2b702abc65104e158b700efa63f",
                            "datavalue": {
                                "value": "00430962",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$31B1BC2A-D09F-4151-AD2B-5CEA229B9058",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 48183,
                                                    "id": "Q48183"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P213": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P213",
                            "hash": "ed6b11a980013ea8e084b8e634cfcac37d2eba8a",
                            "datavalue": {
                                "value": "0000 0000 8045 6315",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$1CF5840B-A274-402B-9556-F202C2F9B831",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P434": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P434",
                            "hash": "8d03e96243cf77d4c123e929081cc16940e25412",
                            "datavalue": {
                                "value": "e9ed318d-8cc5-4cf8-ab77-505e39ab6ea4",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$fc61f952-4071-7cc1-c20a-dc7a90ad6515",
                        "rank": "normal"
                    }
                ],
                "P269": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P269",
                            "hash": "adb558674eda6bfe9b17c3fed9be99c3d55f0cc3",
                            "datavalue": {
                                "value": "026677636",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$D0E17F5E-4302-43F8-926B-5FE7AA8A4380",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P268": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P268",
                            "hash": "8721e8944f95e9ce185c270dd1e12b81d13f7e9b",
                            "datavalue": {
                                "value": "11888092r",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$BB4B67FE-FECA-4469-9DEE-3E8F03AC9F1D",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "d4bd87b862b12d99d26e86472d44f26858dee639",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "f30cbd35620c4ea6d0633aaf0210a8916130469b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 8447,
                                                    "id": "Q8447"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P227": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P227",
                            "hash": "2a20755d12051fc95152d6107bd8a34e7fbc63c4",
                            "datavalue": {
                                "value": "119033364",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$8AA8CCC1-86CE-4C66-88FC-267621A81EA0",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "14d2400e3b1d36332748dc330276f099eeaa8800",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "39224a9c2e8ce5424defbd16603d25771956c7fc",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1551807,
                                                    "id": "Q1551807"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            },
                            {
                                "hash": "dd3ff7346d2dbe78013c48629bb46c53fdb951b2",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "255300f97841c9c773c9ee6e82a75095e356ee13",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1419226,
                                                    "id": "Q1419226"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P535": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P535",
                            "hash": "ce3fb403e96b3b004b1b480734c941819c442c01",
                            "datavalue": {
                                "value": "22814",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$0DD4F039-6CDC-40C9-871B-63CDE4A47032",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "7dfe2e0d2d86c960cf4b365dd64fe9934fcf9ffe",
                                "snaks": {
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "4e8717be05f94ef9d94844fa9ac448eb1b6fd56d",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Noel Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "d9b949b67c334103af825045cc198dec267df1eb",
                                            "datavalue": {
                                                "value": "http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid=22814",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "ee18a449a5b0b58a2ac2a1eb537367b5f78ff139",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 63056,
                                                    "id": "Q63056"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "7b4e3b6251283293572bb344027f6108800ce722",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2001-06-25T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P1476",
                                    "P854",
                                    "P123",
                                    "P577",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P691": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P691",
                            "hash": "bc9fdc5daaa2387d2d7bc5749239552a696adb78",
                            "datavalue": {
                                "value": "jn19990000029",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$704392C4-6E77-4E25-855F-7CF2D198DD6A",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P140": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P140",
                            "hash": "62a2f67bc4780266b21d302c5114355254aaa72d",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 7066,
                                    "id": "Q7066"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$8419C20C-8EF8-4EC0-80D6-AF1CA55E7557",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "ba8b8e4808de217c0a0d4a1276a78297b01b1ea1",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "866d4429816b741d092732473f76b9a1a680e8e0",
                                            "datavalue": {
                                                "value": "http://www.douglasadams.eu/douglas-adams-and-god-portrait-of-a-radical-atheist/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3fe8509e2f9b2cd0b97fdfe55a492027cda1e9a0",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams and God. Portrait of a radical atheist",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P813",
                                    "P1476",
                                    "P407"
                                ]
                            },
                            {
                                "hash": "6f594ed7391250cb94bc94aaa94d855184a7bdf5",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "68e98d6a655164d7048d812549d0fb1a84c63c74",
                                            "datavalue": {
                                                "value": "http://www.nichirenbuddhist.org/Religion/Atheists/DouglasAdams/Interview-American-Atheists.html",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "904f90350bb00d18384278d4c1dedf0c213cd0cf",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 15290435,
                                                    "id": "Q15290435"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "0b72628f400aac7659e7cc94a55382c45c1d0661",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2002-01-01T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 9,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "374e0650068f668869e7f7b0b7a8230af4dc6146",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams' Interview with American Atheists",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P123",
                                    "P577",
                                    "P813",
                                    "P1476",
                                    "P407"
                                ]
                            }
                        ]
                    }
                ],
                "P22": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P22",
                            "hash": "f4768d2f7e81044a59e2a6b793ae305a85fe9337",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 14623675,
                                    "id": "Q14623675"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$9ac7fb72-4402-8d72-f588-a170ca5e715c",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P25": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P25",
                            "hash": "890caf7af7d2bd93029730fcbf981c4389c867bb",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 14623678,
                                    "id": "Q14623678"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$cf4cccbe-470e-e627-86a3-70ef115f601c",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P26": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P26",
                            "hash": "e41afff05ff2364b903d9cbc117e5730a99f8cfb",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 14623681,
                                    "id": "Q14623681"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P580": [
                                {
                                    "snaktype": "value",
                                    "property": "P580",
                                    "hash": "cccb5ca124ec4121900c8beb41b777148829fa49",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1991-11-25T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 11,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ],
                            "P582": [
                                {
                                    "snaktype": "value",
                                    "property": "P582",
                                    "hash": "8798597f326000b4ffd9948d42771308bdb23133",
                                    "datavalue": {
                                        "value": {
                                            "time": "+2001-05-11T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 11,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P580",
                            "P582"
                        ],
                        "id": "q42$b88670f8-456b-3ecb-cf3d-2bca2cf7371e",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P40": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P40",
                            "hash": "3f5ef5e39468c6f0459f5039c92c5840004eba83",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 14623683,
                                    "id": "Q14623683"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "q42$70b600fa-4c0a-b3e6-9e19-1486e71c99fb",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P409": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P409",
                            "hash": "ee67cbff3db03abd0756291848d8351fb35833dd",
                            "datavalue": {
                                "value": "35163268",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "q42$506fc7c8-439d-b77f-5041-8ca85659ad57",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P906": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P906",
                            "hash": "0fe37e1d5b93dd5c01d2b265272f541ae3dbe467",
                            "datavalue": {
                                "value": "230807",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$D92DF8AE-786C-4C3E-8A33-BABD8CB06D31",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "3582332eaefe93a65e8d64b0f15f33e1094455c3",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "149851a61fcc9e546ea127e93180ce3e86972ad3",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1798125,
                                                    "id": "Q1798125"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P950": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P950",
                            "hash": "fd89c3e8114dce50507d5dce01124aa51da46ee6",
                            "datavalue": {
                                "value": "XX1149955",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$856BE41B-546B-4381-B671-07DC17E1F677",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P1006": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1006",
                            "hash": "3e97ad82f26830173fb5c332b6ccd2db3df6624e",
                            "datavalue": {
                                "value": "068744307",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$B7643D02-6EF0-4932-A36A-3A2D4DA3F578",
                        "rank": "normal"
                    }
                ],
                "P1005": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1005",
                            "hash": "37f6dc2b15256fe80a31628333c20d4a550cf5c4",
                            "datavalue": {
                                "value": "68537",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$35342507-3E6E-4F3C-9BB6-F05C9F7DBD95",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P949": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P949",
                            "hash": "e6c5d85d4dbc36b3a63a7f0042a25506b667609e",
                            "datavalue": {
                                "value": "000163846",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$2D50AE02-2BD8-4F82-9DFD-B3166DEFDEC1",
                        "rank": "normal"
                    }
                ],
                "P396": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P396",
                            "hash": "7f6dc5a9ab2508b0ceee1d0676915fbba722fbbb",
                            "datavalue": {
                                "value": "IT\\ICCU\\RAVV\\034417",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$b4c088b8-4bd9-c037-6b4e-7a0be3730947",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P646": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P646",
                            "hash": "119ce5ea11d825b41f7a763700a530f1fd602531",
                            "datavalue": {
                                "value": "/m/0282x",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$48D9C731-BDA8-45D6-B593-437CD10A51B4",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 15241312,
                                                    "id": "Q15241312"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-10-28T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P577"
                                ]
                            }
                        ]
                    }
                ],
                "P69": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P69",
                            "hash": "7c26b753f767dd296d3323721c0f9e018e2fae90",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 691283,
                                    "id": "Q691283"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P582": [
                                {
                                    "snaktype": "value",
                                    "property": "P582",
                                    "hash": "cf63122733bae275108bbf5d043d46669f782697",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1974-01-01T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ],
                            "P812": [
                                {
                                    "snaktype": "value",
                                    "property": "P812",
                                    "hash": "e03f82fd83e940fdf0020ded271f0edf11977d72",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 186579,
                                            "id": "Q186579"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ],
                            "P512": [
                                {
                                    "snaktype": "value",
                                    "property": "P512",
                                    "hash": "e1bbba02ae21a15bcef937d017c8142e5cf73a88",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 1765120,
                                            "id": "Q1765120"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ],
                            "P580": [
                                {
                                    "snaktype": "value",
                                    "property": "P580",
                                    "hash": "847c4c912d3781dc83eabd7135d6403c473c0daf",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1971-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P582",
                            "P812",
                            "P512",
                            "P580"
                        ],
                        "id": "q42$0E9C4724-C954-4698-84A7-5CE0D296A6F2",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "355b56329b78db22be549dec34f2570ca61ca056",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "d1d1b10a05a8f3fc5d26bb4aeb6849617ad81fc7",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 5375741,
                                                    "id": "Q5375741"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            },
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P69",
                            "hash": "24e9c420759c3934fdb089994d6c07f9e96989cd",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4961791,
                                    "id": "Q4961791"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P582": [
                                {
                                    "snaktype": "value",
                                    "property": "P582",
                                    "hash": "5c5b90187b61a0af83711c9495e5529940747577",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1970-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ],
                            "P580": [
                                {
                                    "snaktype": "value",
                                    "property": "P580",
                                    "hash": "923f84fcbf398253e1ef1a8a13f1da430b87d7bb",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1959-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P582",
                            "P580"
                        ],
                        "id": "Q42$32490F12-D9B5-498A-91A8-839F9149F600",
                        "rank": "normal"
                    }
                ],
                "P1273": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1273",
                            "hash": "0c743c083410c1a7181a4e385097bdc26355f6b8",
                            "datavalue": {
                                "value": "a10667040",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$4A2873C0-D848-4F3D-8066-38204E50414C",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "cbd294ba99228d76563dacad5326342b7cbcd81c",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "79c7aecc389a0463fd6c991d3481a375c9610987",
                                            "datavalue": {
                                                "value": "https://viaf.org/viaf/113230702/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P1415": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1415",
                            "hash": "46fc3ad846c890a1848fc4c59b7cef72b8054334",
                            "datavalue": {
                                "value": "101075853",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$F4EC4761-2DCC-4106-8156-D5D36B5FA29A",
                        "rank": "normal"
                    }
                ],
                "P108": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P108",
                            "hash": "399e6e94b953e4305e2c0d4d6f752cedfd5576a9",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 9531,
                                    "id": "Q9531"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$853B16C8-1AB3-489A-831E-AEAD7E94AB87",
                        "rank": "normal"
                    }
                ],
                "P998": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "e436a6c335c51397267b0c244a54801fa88ba1c6",
                            "datavalue": {
                                "value": "Arts/Literature/Authors/A/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 1860,
                                            "id": "Q1860"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$BE724F6B-6981-4DE9-B90C-338768A4BFC4",
                        "rank": "preferred"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "f07d223888dcbdf328dc74fd6a28fbe85bba1f02",
                            "datavalue": {
                                "value": "World/Dansk/Kultur/Litteratur/Forfattere/A/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "4a90e9ca00d0eae667dbbdeb5d575498ec041124",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 9035,
                                            "id": "Q9035"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$5776B538-2441-4B9E-9C39-4E6289396763",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "f67566d0a20a24e29f665d06f2e391b45d556699",
                            "datavalue": {
                                "value": "World/Français/Arts/Littérature/Genres/Science-fiction_et_fantastique/Auteurs/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "d197d0a5efa4b4c23a302a829dd3ef43684fe002",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 150,
                                            "id": "Q150"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$B60CF952-9C65-4875-A4BA-6B8516C81E99",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "46e31918e9a49a4625ac129bcd6fe307881148e4",
                            "datavalue": {
                                "value": "World/Deutsch/Kultur/Literatur/Autoren_und_Autorinnen/A/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "46bfd327b830f66f7061ea92d1be430c135fa91f",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 188,
                                            "id": "Q188"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$A0B48E74-C934-42B9-A583-FB3EAE4BC9BA",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "db656ead856cf3bfa451ba355e21363730a8d465",
                            "datavalue": {
                                "value": "World/Italiano/Arte/Letteratura/Autori/A/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "2ab2e485ce235a18142330fa1873a5bba7115d23",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 652,
                                            "id": "Q652"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$F2632AC4-6F24-49E4-9E4E-B008F26BA8CE",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P998",
                            "hash": "1ae5f83e9a27b3099283feee56595d8aa05a8585",
                            "datavalue": {
                                "value": "World/Svenska/Kultur/Litteratur/Genre/Science_fiction_och_fantasy/Författare/Adams,_Douglas/",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "e41efcf0acaa18ea8fca63b87e2e0c24618f5664",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 9027,
                                            "id": "Q9027"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$84B82B5A-8F33-4229-B988-BF960E676875",
                        "rank": "normal"
                    }
                ],
                "P1233": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1233",
                            "hash": "b601606b4bce3131ed7b591bb3acbcaeaa8f7a6e",
                            "datavalue": {
                                "value": "122",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$9F55FA72-F9E5-41E4-A771-041EB1D59C28",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 48183,
                                                    "id": "Q48183"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P1207": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1207",
                            "hash": "fb8c444b252a36a9690abf99924481f76209d617",
                            "datavalue": {
                                "value": "n94004172",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$00ddd8cf-48fa-609f-dd4e-977e9672c96f",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P1375": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1375",
                            "hash": "74f3cc3776b62c99ac1e7eaff7cdc7c9558cd12c",
                            "datavalue": {
                                "value": "000010283",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$97db6877-4c06-88ce-2db5-aaba53383fd2",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P1670": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1670",
                            "hash": "d61de0b70e9a69753fdd2e33499c67efb1140823",
                            "datavalue": {
                                "value": "0052C2705",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$2370b5b3-487b-89dd-ad93-b023a2a86ac4",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "759b2a264fff886006b6f49c3ef2f1acbfd1cef0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "b14f8dad3de12f83b158a718b20772dc6c65fa0d",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P1284": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1284",
                            "hash": "2f5c2e65a1d9fca309615b885bf62f3e5260874e",
                            "datavalue": {
                                "value": "00000020676",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$2EE16C9C-B74B-4322-9542-4A132555B363",
                        "rank": "normal"
                    }
                ],
                "P866": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P866",
                            "hash": "37d031cbb7d33f06c43ad0a1faafac8071b4c3e1",
                            "datavalue": {
                                "value": "douglas-adams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$A29644ED-0377-4F88-8BA6-FAAB7DE8C7BA",
                        "rank": "normal"
                    }
                ],
                "P1695": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1695",
                            "hash": "5b3ec159aae2cbcee8689e36af4bda9a5497e72f",
                            "datavalue": {
                                "value": "A11573065",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$9B5EED2E-C3F5-4634-8B85-4D4CC6F15C93",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "26c14416670af4da8614d9db92859f07401e3b88",
                                "snaks": {
                                    "P214": [
                                        {
                                            "snaktype": "value",
                                            "property": "P214",
                                            "hash": "20e5c69fbf37b8b0402a52948a04f481028e819c",
                                            "datavalue": {
                                                "value": "113230702",
                                                "type": "string"
                                            },
                                            "datatype": "external-id"
                                        }
                                    ],
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 54919,
                                                    "id": "Q54919"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "ab1e45f4e59b97ef39387dbd419722745e6cff99",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-03-07T00:00:00Z",
                                                    "timezone": 60,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P214",
                                    "P248",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P1816": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1816",
                            "hash": "b19c490642f7a5d5c71bf612ec4089c74dbdfaf5",
                            "datavalue": {
                                "value": "mp60152",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$A70EF87C-33F4-4366-B0A7-000C5A3A43E5",
                        "rank": "normal"
                    }
                ],
                "P1263": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1263",
                            "hash": "536c401a39def76dfbb2b0e1c332d3707a6aef95",
                            "datavalue": {
                                "value": "731/000023662",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$9B26C69E-7B9E-43EB-9B20-AD1305D1EE6B",
                        "rank": "normal"
                    }
                ],
                "P1412": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1412",
                            "hash": "7056615ebf0fbde82a3ca3bb9b2c481669a46eb1",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 1860,
                                    "id": "Q1860"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$6fbc7ed0-41be-713c-2c7c-ac9dad2db936",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "55d23126bca9913374faf69ba8fbd21474a74421",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "da30562523b94bc9c043e8ecdf983c520d76fa31",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 20666306,
                                                    "id": "Q20666306"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "d6162a1716489623c6e595e448b17f8dca4fb2e8",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-10-10T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "c2533c0aa0d8cbc5c781f5649e9fca5b633d2954",
                                            "datavalue": {
                                                "value": "http://data.bnf.fr/ark:/12148/cb11888092r",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813",
                                    "P854"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1412",
                            "hash": "3ccfcedff2284b4d79985c968d00ead896a31459",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 7979,
                                    "id": "Q7979"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$E6ACC163-F1F7-4790-9D90-30DC699068EE",
                        "rank": "normal"
                    }
                ],
                "P271": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P271",
                            "hash": "4427f3fc3ca4aa75b84c93e90043707031b24a72",
                            "datavalue": {
                                "value": "DA07517784",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$f69cd1df-4655-d1fa-5978-e3454415e57e",
                        "rank": "normal"
                    }
                ],
                "P856": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P856",
                            "hash": "8e7a6ef0b1b4ed806d226b6fc64975f00ada8000",
                            "datavalue": {
                                "value": "http://www.douglasadams.com/",
                                "type": "string"
                            },
                            "datatype": "url"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P407": [
                                {
                                    "snaktype": "value",
                                    "property": "P407",
                                    "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 1860,
                                            "id": "Q1860"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P407"
                        ],
                        "id": "Q42$D32EFF42-C5E2-482A-AE97-2159D6A99524",
                        "rank": "normal"
                    }
                ],
                "P1411": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1411",
                            "hash": "99f1efe2922c2a67bb499cdee14b487adfe564ee",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 3414212,
                                    "id": "Q3414212"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P1686": [
                                {
                                    "snaktype": "value",
                                    "property": "P1686",
                                    "hash": "6976dd054773df55af13d08387ac072427e71cb6",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 3521267,
                                            "id": "Q3521267"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ],
                            "P585": [
                                {
                                    "snaktype": "value",
                                    "property": "P585",
                                    "hash": "21ce2394cef40d7e380a249ee1911d6efa38d1af",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1979-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P1686",
                            "P585"
                        ],
                        "id": "Q42$1B3C484C-643E-45D0-B01C-F6DAD3D1F88E",
                        "rank": "normal"
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1411",
                            "hash": "79aef316494aa8d5e3f72352a5315ecdea123e04",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 2576795,
                                    "id": "Q2576795"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P585": [
                                {
                                    "snaktype": "value",
                                    "property": "P585",
                                    "hash": "1f4575b36bd16a12b6ce37bd18576d2809be2317",
                                    "datavalue": {
                                        "value": {
                                            "time": "+1983-00-00T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 9,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ],
                            "P1686": [
                                {
                                    "snaktype": "value",
                                    "property": "P1686",
                                    "hash": "e7bb7e6e72fbe3cab6b40bc12cd86966ff4f9175",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 721,
                                            "id": "Q721"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P585",
                            "P1686"
                        ],
                        "id": "Q42$285E0C13-9674-4131-9556-51B316A57AEE",
                        "rank": "normal"
                    }
                ],
                "P1953": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1953",
                            "hash": "62213f70dc895a9605d36aeeda01e3a6ab73e74f",
                            "datavalue": {
                                "value": "134923",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$6C466225-DCB1-47B9-B868-C285F016E216",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "b2e93db8744c6c00360db0868706706c3d951d92",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "623cc8f0e2f65afe4d66b91962d354a2f3aa9a27",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 14005,
                                                    "id": "Q14005"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "795072cd4393cd80747d64449b3a561fef5aa380",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2015-07-27T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248",
                                    "P813"
                                ]
                            }
                        ]
                    }
                ],
                "P648": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P648",
                            "hash": "54001f8cc18087fa51c188b474a3abf2a5db19a0",
                            "datavalue": {
                                "value": "OL272947A",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$0BC410B8-8A0F-4658-90B0-BB2AE1D6AA3F",
                        "rank": "normal"
                    }
                ],
                "P1258": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1258",
                            "hash": "8c80814f0a15ebe01dc19766129dbfe4276ad77a",
                            "datavalue": {
                                "value": "celebrity/douglas_adams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$4bc2af98-4182-3b11-0df3-80aac8e24081",
                        "rank": "normal"
                    }
                ],
                "P172": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P172",
                            "hash": "3105dc237695c09c9a74a306455c363927e3c75b",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 42406,
                                    "id": "Q42406"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$32e3f411-4934-9c3b-6be0-c53bff07b544",
                        "rank": "normal"
                    }
                ],
                "P2191": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2191",
                            "hash": "aa304e7e2d774630d7b8d8d673b0e4b586ed4e59",
                            "datavalue": {
                                "value": "NILF10014",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$2DB4179B-D385-495D-B248-9D0A53041DD4",
                        "rank": "normal"
                    }
                ],
                "P1266": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1266",
                            "hash": "bdbb98c7c753fb88584e387119e1c174ffadb411",
                            "datavalue": {
                                "value": "97049",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$788bd2c1-46a0-9898-6410-5339ecf90a8b",
                        "rank": "normal"
                    }
                ],
                "P2019": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2019",
                            "hash": "6dffad6e477d1b2e84322dcde7a5f67ea5414bfe",
                            "datavalue": {
                                "value": "p279442",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$b0322bc3-497a-8ef4-8eed-e4927b805d87",
                        "rank": "normal"
                    }
                ],
                "P2188": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2188",
                            "hash": "241f004ee4042a5226417b8570251268a77d7982",
                            "datavalue": {
                                "value": "45993",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$5215183d-42ec-a3e5-1745-0abd519d026a",
                        "rank": "normal"
                    }
                ],
                "P2168": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2168",
                            "hash": "5b535a453c0f88c11cb592ae35510abe93d2eec5",
                            "datavalue": {
                                "value": "271209",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$77b4aae6-473c-f860-1918-9ca573cdfb2e",
                        "rank": "normal"
                    }
                ],
                "P1315": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1315",
                            "hash": "26738bb6b795b709bab76e844b45c507e06cf04a",
                            "datavalue": {
                                "value": "847711",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$809C95C5-ED69-432B-91D8-FF7C8C9965A2",
                        "rank": "normal"
                    }
                ],
                "P2163": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2163",
                            "hash": "a727f412894f1378687c860124872df50221304a",
                            "datavalue": {
                                "value": "56544",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$7424C174-D7A8-4D60-89E3-416156EAC76D",
                        "rank": "normal"
                    }
                ],
                "P1417": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1417",
                            "hash": "6ea6871c416e9475ac71ca2f65128b3bf4202f79",
                            "datavalue": {
                                "value": "biography/Douglas-Adams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$2B2DC742-3BC1-4DAA-BECF-C81A33453B57",
                        "rank": "normal"
                    }
                ],
                "P2611": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2611",
                            "hash": "0631354d6f7ce9e874e9d561a8c77602d14c7661",
                            "datavalue": {
                                "value": "douglas_adams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$3169835D-BBAB-48C0-B197-7428BDBAC28E",
                        "rank": "normal"
                    }
                ],
                "P1003": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1003",
                            "hash": "553be73a1bcf4674349453e9eb396810a2b67e13",
                            "datavalue": {
                                "value": "RUNLRAUTH770139180",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$5644B49C-B3EA-4540-B2EB-78F3AC3B89BB",
                        "rank": "normal"
                    }
                ],
                "P2435": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2435",
                            "hash": "c38967daaf99993bbc91b468fc81a82e3bb9dad3",
                            "datavalue": {
                                "value": "208947",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$daf51782-49c8-1e46-7738-e923dba42cb0",
                        "rank": "normal"
                    }
                ],
                "P2604": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2604",
                            "hash": "421122162eba6332387f5e8cd004d4de354a64b8",
                            "datavalue": {
                                "value": "246164",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$ca83a88a-470c-b93a-2393-35a1de0a9c60",
                        "rank": "normal"
                    }
                ],
                "P2387": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2387",
                            "hash": "d61c15b28b800e74f0c307c30d1caf14acd7fb0a",
                            "datavalue": {
                                "value": "1289170",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$29c1b057-497d-7d15-864e-3d889a76c750",
                        "rank": "normal"
                    }
                ],
                "P2626": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2626",
                            "hash": "9d2f07ecfb40cd02ff993b45b55462b133d32779",
                            "datavalue": {
                                "value": "159696",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$5a41f776-4135-80b1-e3fe-43156047ecb8",
                        "rank": "normal"
                    }
                ],
                "P2605": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2605",
                            "hash": "cb22a19dc73066bcc1cddfd57ab8d26248180bfe",
                            "datavalue": {
                                "value": "39534",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$7398157a-409e-7d35-7d89-7351426cb36c",
                        "rank": "normal"
                    }
                ],
                "P2963": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2963",
                            "hash": "4221e8296d6a925d42a4df043b063108546097b5",
                            "datavalue": {
                                "value": "4",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$eb0d02d3-4b1d-0e19-cb86-78a0a5439144",
                        "rank": "normal"
                    }
                ],
                "P910": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P910",
                            "hash": "66af9938438374fa44164b5c655fd4902e65345a",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 8935487,
                                    "id": "Q8935487"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$3B111597-2138-4517-85AD-FD0056D3DEB0",
                        "rank": "normal"
                    }
                ],
                "P3106": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3106",
                            "hash": "80d1fadf05f08f13eda14529506bd5a48390a367",
                            "datavalue": {
                                "value": "books/douglasadams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$d8ebbd62-4229-1e3b-6494-ca96246286e3",
                        "rank": "normal"
                    }
                ],
                "P1303": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1303",
                            "hash": "32ba5bbd0bb5778c1097444f80b17d3de3b3cdab",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 6607,
                                    "id": "Q6607"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$67547850-C3A0-4C99-AFE4-3C18956CB19A",
                        "rank": "normal"
                    }
                ],
                "P2469": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2469",
                            "hash": "8182569fbc34cb375d652c1108c4895160df700d",
                            "datavalue": {
                                "value": "238p",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$32DACDAA-0C29-489B-B587-7CB5D374EEE5",
                        "rank": "normal"
                    }
                ],
                "P3373": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3373",
                            "hash": "5e84b11b53fecf61d0ceff89b8f4d7beff79bd4a",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 14623673,
                                    "id": "Q14623673"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P1039": [
                                {
                                    "snaktype": "value",
                                    "property": "P1039",
                                    "hash": "5b3f59b1f0d729762738dd6fef802583269d88e5",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 595094,
                                            "id": "Q595094"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P1039"
                        ],
                        "id": "Q42$A3B1288B-67A9-4491-A3AA-20F881C292B9",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "9177d75c6061e9e1ab149c0aa01bee5a90e07415",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "db25e2819537870d0ef893d382ef7c400f4ec4d3",
                                            "datavalue": {
                                                "value": "http://www.nndb.com/people/731/000023662/",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P407": [
                                        {
                                            "snaktype": "value",
                                            "property": "P407",
                                            "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1860,
                                                    "id": "Q1860"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "201f20dc608f8134f4b320df3cc273babfbb2284",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 1373513,
                                                    "id": "Q1373513"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P813": [
                                        {
                                            "snaktype": "value",
                                            "property": "P813",
                                            "hash": "6b8fcfa6afb3911fecec93ae1dff2b6b6cde5659",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-12-07T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "3efff2f94d96938bcfa1c19a34a4fa41de7be644",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P407",
                                    "P123",
                                    "P813",
                                    "P1476"
                                ]
                            }
                        ]
                    }
                ],
                "P3417": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3417",
                            "hash": "db4aa0e21094eecf0c47e3826a988cf886d67fe0",
                            "datavalue": {
                                "value": "Douglas-Adams-4",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$edea25d2-4736-b539-ec8d-d3f82e1f7100",
                        "rank": "normal"
                    }
                ],
                "P3430": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3430",
                            "hash": "1e9a0d6461bed3d3b3f7ed1956b151058982cd6e",
                            "datavalue": {
                                "value": "w65h7md1",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$76AD35E4-F222-418A-A3AC-CF6472790811",
                        "rank": "normal"
                    }
                ],
                "P1617": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1617",
                            "hash": "aeab2cca07e2851f3be2739cb17cd7fc7fdcf255",
                            "datavalue": {
                                "value": "aa075cb6-75bf-46d8-b0bf-9751d6c04c93",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$545d5c9a-4bde-ee8b-089f-1a11ba699301",
                        "rank": "normal"
                    }
                ],
                "P3762": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3762",
                            "hash": "6700459c02f26575f0d773d2c98ef75a8802cc07",
                            "datavalue": {
                                "value": "140290",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$6BC778E7-7176-4F20-A450-A9A0FC3B3209",
                        "rank": "normal"
                    }
                ],
                "P2048": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2048",
                            "hash": "bb30f6a415dca2ba16fc59f4fa2b5b32df39cd7d",
                            "datavalue": {
                                "value": {
                                    "amount": "+1.96",
                                    "unit": "http://www.wikidata.org/entity/Q11573"
                                },
                                "type": "quantity"
                            },
                            "datatype": "quantity"
                        },
                        "type": "statement",
                        "id": "Q42$b0bf3caf-481c-356b-03a2-e61174b8e6da",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "6cafde5d9b86c476c4c839a172776bf58ca2e920",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "hash": "9806f7100381f841399dc049ab07b12cc358e880",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 52,
                                                    "id": "Q52"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P3222": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P3222",
                            "hash": "24ce0b270b00ea4d2dcc082d647f8eb542070bbd",
                            "datavalue": {
                                "value": "douglas-adams",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$D41D834D-0BD4-411C-A671-2B7BE6053EB5",
                        "rank": "normal"
                    }
                ],
                "P109": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P109",
                            "hash": "8328c1fb86022aa9e55f6338bbdf98512c50c2e6",
                            "datavalue": {
                                "value": "Douglas Adams Unterschrift.jpg",
                                "type": "string"
                            },
                            "datatype": "commonsMedia"
                        },
                        "type": "statement",
                        "id": "Q42$e5b8e5d5-4243-43e3-3476-c8f1572f14fa",
                        "rank": "normal"
                    }
                ],
                "P4193": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P4193",
                            "hash": "f1fe4a6c587c168332f92c0bd2a995bd9570b99a",
                            "datavalue": {
                                "value": "Douglas_Noel_Adams_(1952-2001)",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$769463b3-4b83-cf93-d5ef-0b4e98e1cf33",
                        "rank": "normal"
                    }
                ],
                "P136": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P136",
                            "hash": "202d8227cb86026ec9956eea1628a52cd8d3cdfb",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 24925,
                                    "id": "Q24925"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$0ff4aeeb-4fdb-56cf-5fe9-916e1bbbbc73",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2f8e9f13763cdad3dcd7bc1cde454c244907cda2",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "b3784f20fdd968a0a3c739174983521c82d178fd",
                                            "datavalue": {
                                                "value": "https://www.theguardian.com/books/2013/mar/11/douglas-adams-king-comic-science-fiction",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "cc070d30c037a656be8479b9ecec12ae4d125596",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams is still the king of comic science fiction",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "7cc99d0eec7b745edccf680f3347956e14188d2a",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 11148,
                                                    "id": "Q11148"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "8c7cfd920adb380546ec2444b506d6d00fce49e6",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-03-11T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P1476",
                                    "P123",
                                    "P577"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P136",
                            "hash": "61ab43a3146565344895c746d35e7d3cf1917cc3",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 40831,
                                    "id": "Q40831"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$2ac90f53-4dc5-2ecc-d595-70f7c43f2fda",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2f8e9f13763cdad3dcd7bc1cde454c244907cda2",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "b3784f20fdd968a0a3c739174983521c82d178fd",
                                            "datavalue": {
                                                "value": "https://www.theguardian.com/books/2013/mar/11/douglas-adams-king-comic-science-fiction",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ],
                                    "P1476": [
                                        {
                                            "snaktype": "value",
                                            "property": "P1476",
                                            "hash": "cc070d30c037a656be8479b9ecec12ae4d125596",
                                            "datavalue": {
                                                "value": {
                                                    "text": "Douglas Adams is still the king of comic science fiction",
                                                    "language": "en"
                                                },
                                                "type": "monolingualtext"
                                            },
                                            "datatype": "monolingualtext"
                                        }
                                    ],
                                    "P123": [
                                        {
                                            "snaktype": "value",
                                            "property": "P123",
                                            "hash": "7cc99d0eec7b745edccf680f3347956e14188d2a",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 11148,
                                                    "id": "Q11148"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ],
                                    "P577": [
                                        {
                                            "snaktype": "value",
                                            "property": "P577",
                                            "hash": "8c7cfd920adb380546ec2444b506d6d00fce49e6",
                                            "datavalue": {
                                                "value": {
                                                    "time": "+2013-03-11T00:00:00Z",
                                                    "timezone": 0,
                                                    "before": 0,
                                                    "after": 0,
                                                    "precision": 11,
                                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                                },
                                                "type": "time"
                                            },
                                            "datatype": "time"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854",
                                    "P1476",
                                    "P123",
                                    "P577"
                                ]
                            }
                        ]
                    },
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P136",
                            "hash": "98c2629a70e699b536d71d16e03b20fbbad7b8d5",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 128758,
                                    "id": "Q128758"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        },
                        "type": "statement",
                        "id": "Q42$43f046bb-47a4-00aa-5174-aa7ca343396b",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "fb6300cf6bc0ce72d3d960d4d671fd772125d3ee",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "889fba69e20a1dfca93abe793e0c3cc6218472cd",
                                            "datavalue": {
                                                "value": "https://www.theguardian.com/commentisfree/2015/aug/07/hitchhikers-guide-galaxy-book-changed-me-vogons-economics",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P4431": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P4431",
                            "hash": "1faf29b616aacd94361ec05e63b2faabef5aadcd",
                            "datavalue": {
                                "value": "douglas-adams-61st-birthday",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "qualifiers": {
                            "P585": [
                                {
                                    "snaktype": "value",
                                    "property": "P585",
                                    "hash": "52ee0260174795772f9cfbfa8ec3b7561ef4e7bc",
                                    "datavalue": {
                                        "value": {
                                            "time": "+2013-03-11T00:00:00Z",
                                            "timezone": 0,
                                            "before": 0,
                                            "after": 0,
                                            "precision": 11,
                                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                        },
                                        "type": "time"
                                    },
                                    "datatype": "time"
                                }
                            ]
                        },
                        "qualifiers-order": [
                            "P585"
                        ],
                        "id": "Q42$520b13d1-47df-2d1c-f56d-7106f383a3b6",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "a403d90550be4608a47c62ec6d9fd69e0c707d1c",
                                "snaks": {
                                    "P854": [
                                        {
                                            "snaktype": "value",
                                            "property": "P854",
                                            "hash": "40acb7d11e3e8b2c54e00f0ac12e49b3d909fa72",
                                            "datavalue": {
                                                "value": "http://www.google.com/doodles/douglas-adams-61st-birthday",
                                                "type": "string"
                                            },
                                            "datatype": "url"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P854"
                                ]
                            }
                        ]
                    }
                ],
                "P2607": [
                    {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2607",
                            "hash": "39e9c24ade56182f9826a6cdeb65b741c59f7349",
                            "datavalue": {
                                "value": "307812da-da11-4ee5-a906-31e5ce9694bb",
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "id": "Q42$52EA4A30-C798-4ED3-AEA0-A2FEB4B0FB95",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "706208b3024200fd0a39ad499808dd0d98d74065",
                                "snaks": {
                                    "P248": [
                                        {
                                            "snaktype": "value",
                                            "property": "P248",
                                            "hash": "623cc8f0e2f65afe4d66b91962d354a2f3aa9a27",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 14005,
                                                    "id": "Q14005"
                                                },
                                                "type": "wikibase-entityid"
                                            },
                                            "datatype": "wikibase-item"
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P248"
                                ]
                            }
                        ]
                    }
                ]
            },
            "sitelinks": {
                "arwiki": {
                    "site": "arwiki",
                    "title": "دوغلاس آدمز",
                    "badges": []
                },
                "arzwiki": {
                    "site": "arzwiki",
                    "title": "دوجلاس ادامز",
                    "badges": []
                },
                "astwiki": {
                    "site": "astwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "azbwiki": {
                    "site": "azbwiki",
                    "title": "داقلاس آدامز",
                    "badges": []
                },
                "azwiki": {
                    "site": "azwiki",
                    "title": "Duqlas Adams",
                    "badges": []
                },
                "azwikiquote": {
                    "site": "azwikiquote",
                    "title": "Duqlas Noel Adams",
                    "badges": []
                },
                "barwiki": {
                    "site": "barwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "be_x_oldwiki": {
                    "site": "be_x_oldwiki",
                    "title": "Дуглас Адамз",
                    "badges": []
                },
                "bewiki": {
                    "site": "bewiki",
                    "title": "Дуглас Адамс",
                    "badges": []
                },
                "bgwiki": {
                    "site": "bgwiki",
                    "title": "Дъглас Адамс",
                    "badges": []
                },
                "bgwikiquote": {
                    "site": "bgwikiquote",
                    "title": "Дъглас Адамс",
                    "badges": []
                },
                "bnwiki": {
                    "site": "bnwiki",
                    "title": "ডগলাস অ্যাডামস",
                    "badges": []
                },
                "bswiki": {
                    "site": "bswiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "bswikiquote": {
                    "site": "bswikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "cawiki": {
                    "site": "cawiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "cswiki": {
                    "site": "cswiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "cswikiquote": {
                    "site": "cswikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "cywiki": {
                    "site": "cywiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "dawiki": {
                    "site": "dawiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "dewiki": {
                    "site": "dewiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "dewikiquote": {
                    "site": "dewikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "elwiki": {
                    "site": "elwiki",
                    "title": "Ντάγκλας Άνταμς",
                    "badges": []
                },
                "elwikiquote": {
                    "site": "elwikiquote",
                    "title": "Ντάγκλας Άνταμς",
                    "badges": []
                },
                "enwiki": {
                    "site": "enwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "enwikiquote": {
                    "site": "enwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "eowiki": {
                    "site": "eowiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "eowikiquote": {
                    "site": "eowikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "eswiki": {
                    "site": "eswiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "eswikiquote": {
                    "site": "eswikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "etwiki": {
                    "site": "etwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "etwikiquote": {
                    "site": "etwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "euwiki": {
                    "site": "euwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "fawiki": {
                    "site": "fawiki",
                    "title": "داگلاس آدامز",
                    "badges": []
                },
                "fawikiquote": {
                    "site": "fawikiquote",
                    "title": "داگلاس آدامز",
                    "badges": []
                },
                "fiwiki": {
                    "site": "fiwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "fiwikiquote": {
                    "site": "fiwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "frwiki": {
                    "site": "frwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "frwikiquote": {
                    "site": "frwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "gawiki": {
                    "site": "gawiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "glwiki": {
                    "site": "glwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "glwikiquote": {
                    "site": "glwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "hewiki": {
                    "site": "hewiki",
                    "title": "דאגלס אדמס",
                    "badges": []
                },
                "hewikiquote": {
                    "site": "hewikiquote",
                    "title": "דאגלס אדמס",
                    "badges": []
                },
                "hrwiki": {
                    "site": "hrwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "huwiki": {
                    "site": "huwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "huwikiquote": {
                    "site": "huwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "hywiki": {
                    "site": "hywiki",
                    "title": "Դուգլաս Ադամս",
                    "badges": []
                },
                "hywikiquote": {
                    "site": "hywikiquote",
                    "title": "Դուգլաս Ադամս",
                    "badges": []
                },
                "idwiki": {
                    "site": "idwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "iowiki": {
                    "site": "iowiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "iswiki": {
                    "site": "iswiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "itwiki": {
                    "site": "itwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "itwikiquote": {
                    "site": "itwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "jawiki": {
                    "site": "jawiki",
                    "title": "ダグラス・アダムズ",
                    "badges": []
                },
                "jvwiki": {
                    "site": "jvwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "kawiki": {
                    "site": "kawiki",
                    "title": "დაგლას ადამსი",
                    "badges": []
                },
                "kowiki": {
                    "site": "kowiki",
                    "title": "더글러스 애덤스",
                    "badges": []
                },
                "lawiki": {
                    "site": "lawiki",
                    "title": "Duglassius Adams",
                    "badges": []
                },
                "liwikiquote": {
                    "site": "liwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ltwikiquote": {
                    "site": "ltwikiquote",
                    "title": "Douglas Adamsas",
                    "badges": []
                },
                "lvwiki": {
                    "site": "lvwiki",
                    "title": "Duglass Adamss",
                    "badges": []
                },
                "mgwiki": {
                    "site": "mgwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "mkwiki": {
                    "site": "mkwiki",
                    "title": "Даглас Адамс",
                    "badges": []
                },
                "mlwiki": {
                    "site": "mlwiki",
                    "title": "ഡഗ്ലസ് ആഡംസ്",
                    "badges": []
                },
                "mrjwiki": {
                    "site": "mrjwiki",
                    "title": "Адамс, Дуглас",
                    "badges": []
                },
                "mrwiki": {
                    "site": "mrwiki",
                    "title": "डग्लस अ‍ॅडम्स",
                    "badges": []
                },
                "nlwiki": {
                    "site": "nlwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "nlwikiquote": {
                    "site": "nlwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "nnwiki": {
                    "site": "nnwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "nowiki": {
                    "site": "nowiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ocwiki": {
                    "site": "ocwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "plwiki": {
                    "site": "plwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "plwikiquote": {
                    "site": "plwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ptwiki": {
                    "site": "ptwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ptwikiquote": {
                    "site": "ptwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "rowiki": {
                    "site": "rowiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ruwiki": {
                    "site": "ruwiki",
                    "title": "Адамс, Дуглас",
                    "badges": []
                },
                "ruwikiquote": {
                    "site": "ruwikiquote",
                    "title": "Дуглас Ноэль Адамс",
                    "badges": []
                },
                "scowiki": {
                    "site": "scowiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "scwiki": {
                    "site": "scwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "shwiki": {
                    "site": "shwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "simplewiki": {
                    "site": "simplewiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "simplewikiquote": {
                    "site": "simplewikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "skwiki": {
                    "site": "skwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "skwikiquote": {
                    "site": "skwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "slwiki": {
                    "site": "slwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "sqwiki": {
                    "site": "sqwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "srwiki": {
                    "site": "srwiki",
                    "title": "Даглас Адамс",
                    "badges": []
                },
                "svwiki": {
                    "site": "svwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "svwikiquote": {
                    "site": "svwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "tawiki": {
                    "site": "tawiki",
                    "title": "டக்ளஸ் ஆடம்ஸ்",
                    "badges": []
                },
                "thwikiquote": {
                    "site": "thwikiquote",
                    "title": "ดั๊กลาส อดัมส์",
                    "badges": []
                },
                "trwiki": {
                    "site": "trwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "trwikiquote": {
                    "site": "trwikiquote",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "ukwiki": {
                    "site": "ukwiki",
                    "title": "Дуглас Адамс",
                    "badges": []
                },
                "urwiki": {
                    "site": "urwiki",
                    "title": "ڈگلس ایڈمس",
                    "badges": []
                },
                "vepwiki": {
                    "site": "vepwiki",
                    "title": "Adams Duglas",
                    "badges": []
                },
                "viwiki": {
                    "site": "viwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "warwiki": {
                    "site": "warwiki",
                    "title": "Douglas Adams",
                    "badges": []
                },
                "zhwiki": {
                    "site": "zhwiki",
                    "title": "道格拉斯·亚当斯",
                    "badges": []
                },
                "zhwikiquote": {
                    "site": "zhwikiquote",
                    "title": "道格拉斯·亞當斯",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}"""

cache = {'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&formatversion=2&ids=Q42&languages=en&props=info|claims|descriptions|labels|sitelinks&redirects=yes&sites=&titles='

response = r"""
{
  "entities": {
    "Q42": {
      "pageid": 138,
      "ns": 0,
      "title": "Q42",
      "lastrevid": 401457326,
      "modified": "2016-11-05T10:59:45Z",
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
      "claims": {
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
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
                "hash": "050ec907ff2d96e82eddea6ecfc54f12503b9f4c",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "84bf485417f064cf273f05ecbda447612eec7314",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "050ec907ff2d96e82eddea6ecfc54f12503b9f4c",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "84bf485417f064cf273f05ecbda447612eec7314",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 36180,
                  "id": "Q36180"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q42$FE0848B4-34A7-4FC6-9752-BBC736600BB5",
            "rank": "preferred"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P106",
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
            "rank": "preferred"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P106",
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
            "rank": "preferred",
            "references": [
              {
                "hash": "43fc2b2664b154de4cfd68b6a5e1239e1b1d9951",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "1de77c1ae655ffd6b8e48650a16f96a6ae491289",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "43fc2b2664b154de4cfd68b6a5e1239e1b1d9951",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P106",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 482980,
                  "id": "Q482980"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q42$7F1E6FDB-2A8D-4968-A7E3-0168396EB5E4",
            "rank": "normal",
            "references": [
              {
                "hash": "833613d891b97db66d2f3113840bef8a4f354d3b",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/tv/753/000049606/",
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
        "P800": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P800",
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
            "id": "Q42$FA73986E-3D1D-4CAB-B358-424B58544620",
            "rank": "normal",
            "references": [
              {
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "6f6a14880df1a77b2ca9f6093bad8f68386f0d0c",
                "snaks": {
                  "P268": [
                    {
                      "snaktype": "value",
                      "property": "P268",
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
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "84bf485417f064cf273f05ecbda447612eec7314",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "e497b5f7fccf9399077f421e6ce76d3650d312e1",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "38c92f205da0d56c107a6e0854cf483428e38db6",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              }
            ]
          }
        ],
        "P19": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P19",
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
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "cc8e207a81b62f7eb17b07d44dfcf8e52a3dc080",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "7e6f5106921a912c63f4ce557693502e11b83998",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "6f6a14880df1a77b2ca9f6093bad8f68386f0d0c",
                "snaks": {
                  "P268": [
                    {
                      "snaktype": "value",
                      "property": "P268",
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
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "84bf485417f064cf273f05ecbda447612eec7314",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "e497b5f7fccf9399077f421e6ce76d3650d312e1",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "38c92f205da0d56c107a6e0854cf483428e38db6",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              }
            ]
          }
        ],
        "P1196": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1196",
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
                "hash": "095945968d9abac7b03e3507fd1336448949cb99",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                  "P535": [
                    {
                      "snaktype": "value",
                      "property": "P535",
                      "datavalue": {
                        "value": "22814",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
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
                  "P535",
                  "P813"
                ]
              },
              {
                "hash": "1a6c2030885a0ef22b79ee3102bf84621432d96a",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.historyorb.com/people/douglas-adams",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
                  "P123",
                  "P813",
                  "P1476"
                ]
              },
              {
                "hash": "923566d714cc30be3821ab8383fb973624027a2d",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
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
                "hash": "aff958dcf62e41999ba4e69b26ccd400ddadf6ec",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
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
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "e38dadec9d6b784aab71b64e334557250d40c256",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              },
              {
                "hash": "a1761a3d8247edeb27b08f081c04fd69e8a5459a",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "a1aad4b004875b6a7eed733ef980392f383b6ca9",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "f276fb7ae6dfb473b76fe98ffb5afcd8b9bf0743",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "095945968d9abac7b03e3507fd1336448949cb99",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                  "P535": [
                    {
                      "snaktype": "value",
                      "property": "P535",
                      "datavalue": {
                        "value": "22814",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
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
                  "P535",
                  "P813"
                ]
              },
              {
                "hash": "be3d7896f24c7ae3495cb50bb6791718b78e9103",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://highgatecemetery.org/visit/who",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 261113,
                  "id": "Q261113"
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "59a0cc6905ecaa37b00aaef0b23034fbe25b4429",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              "datavalue": {
                "value": "Douglas adams portrait cropped.jpg",
                "type": "string"
              },
              "datatype": "commonsMedia"
            },
            "type": "statement",
            "id": "q42$43D37345-54ED-4FF2-A226-EC26A356E38D",
            "rank": "normal"
          }
        ],
        "P27": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P27",
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
                "hash": "050ec907ff2d96e82eddea6ecfc54f12503b9f4c",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                  "hash": "79d42f9dcfeab031b16f712d728f6a8225329bc6",
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
                  "hash": "519a514583acf9313ab83bf9edaa6be2b3f1e8d1",
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
                "hash": "43fc2b2664b154de4cfd68b6a5e1239e1b1d9951",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              "datavalue": {
                "value": {
                  "text": "Douglas Noël Adams",
                  "language": "en"
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
                "hash": "f6c671a38daa2881f1c4c901c1de5eeb76c11978",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
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
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "3e9859118d01bc62b5dbe8939be812333eb7c594",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "980624fa9331261f9383f286b4056619228b626f",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "3e9859118d01bc62b5dbe8939be812333eb7c594",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "004ec6fbee857649acdbdbad4f97b2c8571df97b",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "004ec6fbee857649acdbdbad4f97b2c8571df97b",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "f70116eac7f49194478b3025330bfd8dcffa3c69",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "3e9859118d01bc62b5dbe8939be812333eb7c594",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "9f454a27f5efb737e03ba11bd3e85a1ea1c08a7d",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "57a1934b7460d09727f7ad27f181f8b0da396975",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "23fa16418189eaee574c252fa6c2d4b433e2f9fa",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.douglasadams.eu/en_adams_athee.php",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
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
                "hash": "3fb7315a05ace04ecc4bda533fdb612a94b2daca",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
                  "P123",
                  "P813",
                  "P1476"
                ]
              }
            ]
          }
        ],
        "P9": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P9",
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
            "id": "q42$76d70dc8-4646-cc84-b66c-be9ed1c469e2",
            "rank": "normal",
            "references": [
              {
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                  "hash": "b42b4077a100e1a8cb55586caec525bcee1ed7dd",
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
                  "hash": "79d42f9dcfeab031b16f712d728f6a8225329bc6",
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
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "6db5f234c81ddf3171f0971c57e1ac2c834b2796",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
              "datavalue": {
                "value": "068744307",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q42$B7643D02-6EF0-4932-A36A-3A2D4DA3F578",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1006",
              "datavalue": {
                "value": "339433876",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q42$C16FB948-39C8-4CFD-AD10-16C0355187D7",
            "rank": "normal",
            "references": [
              {
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
        "P1005": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1005",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "af38848ab5d9d9325cffd93a5ec656cc6ca889ed",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                  "hash": "9c9aa1050b05acfe16f0334bee307c20965ecaf6",
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
                  "hash": "81b44430e63da20d9bffc9bad4b244a1a6d30e93",
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
                  "hash": "158d7693369e716aaae6bef281ee0921a2fc5bb2",
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
                  "hash": "6f71f82b9ab85d3cb8b99e86b497d2f6fbf587fc",
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
                "hash": "8f8bb308b61e4e0cff924b9eb7d783d003fc3ce7",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
                "hash": "c75cea5df57da844ab4708013996bf1501def461",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "datavalue": {
                        "value": "http://www.nndb.com/people/731/000023662/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P364": [
                    {
                      "snaktype": "value",
                      "property": "P364",
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
                  "P364",
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
                  "hash": "9fea35a52abaeb843b452f70accef06c16a5104f",
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
                  "hash": "21e8668f87f42e777ce8a418c7d3d1fb05e915e0",
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
                "hash": "1fe0761d4c6964bd0083fc8af5f2a4d18d707aa6",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
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
                  "hash": "17da29e56d69809fde8793aaa4864de2e6bb5780",
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
                  "hash": "eed80ca4e1ffc12b82c55116042dabdb873707ad",
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
                  "hash": "3be4fb23771c9decf6c908552444e6753215dcf4",
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
                  "hash": "bfab56097f2ee29b68110953c09618468db6871b",
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
                  "hash": "a77ef6d322e3915085c305de616027d3f709c807",
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
                  "hash": "feef8b68d719a5caffb99cd28280ed8133f04965",
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
                "hash": "004ec6fbee857649acdbdbad4f97b2c8571df97b",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "a51d6594fee36c7452eaed2db35a4833613a7078",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
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
                "hash": "74459442f89f27373d1716e217c113727fd9201a",
                "snaks": {
                  "P214": [
                    {
                      "snaktype": "value",
                      "property": "P214",
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
                "hash": "84bf485417f064cf273f05ecbda447612eec7314",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
        "P136": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 761469,
                  "id": "Q761469"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q42$dfa28763-47c1-d41f-c173-cbc5a1de7973",
            "rank": "normal"
          }
        ],
        "P271": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P271",
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
              "datavalue": {
                "value": "http://www.douglasadams.com/",
                "type": "string"
              },
              "datatype": "url"
            },
            "type": "statement",
            "id": "Q42$D32EFF42-C5E2-482A-AE97-2159D6A99524",
            "rank": "normal"
          }
        ],
        "P1411": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1411",
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
                  "hash": "79c8bb02c550645c283dd1baee5cf315243d7d3c",
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
                  "hash": "ac483417a74de01c924dc2bed70e8c6bf19c75e0",
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
                  "hash": "afb6bd8b4658a2ac655589561485cbd17095f04e",
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
                  "hash": "cb0556d944f9ec7a10a3235068cc12449530dc3c",
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
                "hash": "a2c6ab3ed8c552ce15bb30298534670d73a55534",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
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
              "datavalue": {
                "value": "4.Douglas_Adams",
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
}
"""

cache = {'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&exintro&formatversion=2&inprop=url|watchers&list=random&pithumbsize=240&pllimit=500&ppprop=disambiguation|wikibase_item&prop=extracts|info|links|pageimages|pageprops|pageterms&redirects&rnlimit=1&rnnamespace=0&titles=Douglas%20Adams%20%28disambiguation%29'

response = r"""
{
    "batchcomplete": true,
    "continue": {
        "rncontinue": "0.841264018333|0.841264104557|48635964|0",
        "continue": "-||extracts|info|links|pageimages|pageprops|pageterms"
    },
    "query": {
        "pages": [
            {
                "pageid": 1167171,
                "ns": 0,
                "title": "Douglas Adams (disambiguation)",
                "extract": "<p><b>Douglas Adams</b> was an English writer and dramatist.</p>\n<p><b>Douglas</b> or <b>Doug Adams</b> may also refer to:</p>\n<ul><li>Douglas Adams (engineer), American engineer</li>\n<li>Douglas Q. Adams, Indo-Europeanist professor of English</li>\n<li>Doug Adams (American football) (1949–1997), American football player</li>\n<li>Doug Adams (baseball) (born 1943), MLB player</li>\n<li>Doug Adams (music journalist), music journalist and author</li>\n<li>Doug Adams (television producer), American television producer</li>\n<li>Douglas Adams, CEO of Adams Cable</li>\n<li>Douglas Adams (cricketer) (1876–1931), American cricketer</li>\n</ul>",
                "contentmodel": "wikitext",
                "pagelanguage": "en",
                "pagelanguagehtmlcode": "en",
                "pagelanguagedir": "ltr",
                "touched": "2017-10-18T01:46:38Z",
                "lastrevid": 805854377,
                "length": 671,
                "fullurl": "https://en.wikipedia.org/wiki/Douglas_Adams_(disambiguation)",
                "editurl": "https://en.wikipedia.org/w/index.php?title=Douglas_Adams_(disambiguation)&action=edit",
                "canonicalurl": "https://en.wikipedia.org/wiki/Douglas_Adams_(disambiguation)",
                "links": [
                    {
                        "ns": 0,
                        "title": "Adams Cable"
                    },
                    {
                        "ns": 0,
                        "title": "Doug Adam"
                    },
                    {
                        "ns": 0,
                        "title": "Doug Adams (American football)"
                    },
                    {
                        "ns": 0,
                        "title": "Doug Adams (baseball)"
                    },
                    {
                        "ns": 0,
                        "title": "Doug Adams (music journalist)"
                    },
                    {
                        "ns": 0,
                        "title": "Doug Adams (television producer)"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams (cricketer)"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Adams (engineer)"
                    },
                    {
                        "ns": 0,
                        "title": "Douglas Q. Adams"
                    },
                    {
                        "ns": 1,
                        "title": "Talk:Douglas Adams (disambiguation)"
                    },
                    {
                        "ns": 12,
                        "title": "Help:Disambiguation"
                    }
                ],
                "pageprops": {
                    "disambiguation": "",
                    "wikibase_item": "Q5301194"
                },
                "terms": {
                    "description": [
                        "Wikipedia disambiguation page"
                    ],
                    "label": [
                        "Douglas Adams"
                    ]
                }
            }
        ],
        "random": [
            {
                "id": 50798021,
                "ns": 0,
                "title": "Morchella arbutiphila"
            }
        ]
    }
}
"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&formatversion=2&pllimit=500&prop=links&list=random&titles=List_of_programming_languages'

response = r"""
{
    "continue": {
        "plcontinue": "144146|0|Perl_Data_Language",
        "continue": "||"
    },
    "query": {
        "pages": [
            {
                "pageid": 144146,
                "ns": 0,
                "title": "List of programming languages",
                "links": [
                    {
                        "ns": 0,
                        "title": "A++"
                    }
                ]
            }
        ],
        "random": [
            {
                "id": 123,
                "ns": 0,
                "title": "RANDOM"
            }
        ]
    }
}
"""

cache = {'query': query,
         'response': response,
         'info': {'content-type': 'TEST', 'status': 200}}

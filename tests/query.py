# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&cllimit=500&clshow=!hidden&exintro&formatversion=2&imlimit=500&inprop=url|watchers&list=random&lllimit=500&pithumbsize=240&ppprop=wikibase_item&prop=categories|extracts|images|info|langlinks|pageimages|pageprops|pageterms&redirects&rnlimit=1&rnnamespace=0&titles=Douglas Adams'

response = r"""
{
    "batchcomplete": true,
    "continue": {
        "rncontinue": "0.173099126376|0.173099136868|39852235|0",
        "continue": "-||categories|extracts|images|info|langlinks|pageimages|pageprops|pageterms"
    },
    "query": {
        "pages": [
            {
                "pageid": 8091,
                "ns": 0,
                "title": "Douglas Adams",
                "categories": [
                    {
                        "ns": 14,
                        "title": "Category:1952 births"
                    },
                    {
                        "ns": 14,
                        "title": "Category:2001 deaths"
                    },
                    {
                        "ns": 14,
                        "title": "Category:20th-century English novelists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:20th-century atheists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:21st-century British novelists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:21st-century atheists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Alumni of St John's College, Cambridge"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Audio book narrators"
                    },
                    {
                        "ns": 14,
                        "title": "Category:BBC radio producers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:British atheism activists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:British child writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Burials at Highgate Cemetery"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Critics of religions"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Douglas Adams"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English atheists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English comedy writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English humanists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English humorists"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English radio writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English science fiction writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English social commentators"
                    },
                    {
                        "ns": 14,
                        "title": "Category:English television writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Infocom"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Interactive fiction writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Monty Python"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Non-fiction environmental writers"
                    },
                    {
                        "ns": 14,
                        "title": "Category:People educated at Brentwood School (Essex)"
                    },
                    {
                        "ns": 14,
                        "title": "Category:People from Cambridge"
                    },
                    {
                        "ns": 14,
                        "title": "Category:Usenet people"
                    }
                ],
                "extract": "<p><b>Douglas Noel Adams</b> (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humorist, satirist and dramatist.</p>\n<p>Adams is best known as the author of <i>The Hitchhiker's Guide to the Galaxy</i>, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.</p>\n<p>Adams also wrote <i>Dirk Gently's Holistic Detective Agency</i> (1987) and <i>The Long Dark Tea-Time of the Soul</i> (1988), and co-wrote <i>The Meaning of Liff</i> (1983), <i>The Deeper Meaning of Liff</i> (1990), <i>Last Chance to See</i> (1990), and three stories for the television series <i>Doctor Who</i>; he also served as script editor for the show's seventeenth season in 1979. A posthumous collection of his works, including an unfinished novel, was published as <i>The Salmon of Doubt</i> in 2002.</p>\n<p>Adams was known as an advocate for environmentalism and conservation, as a lover of fast cars, cameras, technological innovation and the Apple Macintosh, and as a \"devout atheist\".</p>\n<p></p>\n\n<p></p>\n",
                "images": [
                    {
                        "ns": 6,
                        "title": "File:Blue pencil.svg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Commons-logo.svg"
                    },
                    {
                        "ns": 6,
                        "title": "File:DNA in Monty Python.jpg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Dirk Gently's Holistic Detective Agency.svg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Douglas Adams Part 1.ogg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Douglas Adams Part 2.ogg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Douglas Adams San Francisco.jpg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Douglas adams portrait cropped.jpg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Grave of Douglas Adams, Highgate.jpg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Sound-icon.svg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Towelday-Innsbruck.jpg"
                    },
                    {
                        "ns": 6,
                        "title": "File:Wikiquote-logo.svg"
                    }
                ],
                "contentmodel": "wikitext",
                "pagelanguage": "en",
                "pagelanguagehtmlcode": "en",
                "pagelanguagedir": "ltr",
                "touched": "2017-08-18T03:52:51Z",
                "lastrevid": 793736590,
                "length": 60069,
                "watchers": 447,
                "fullurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
                "editurl": "https://en.wikipedia.org/w/index.php?title=Douglas_Adams&action=edit",
                "canonicalurl": "https://en.wikipedia.org/wiki/Douglas_Adams",
                "langlinks": [
                    {
                        "lang": "ar",
                        "title": "دوغلاس آدمز"
                    },
                    {
                        "lang": "arz",
                        "title": "دوجلاس ادامز"
                    },
                    {
                        "lang": "ast",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "az",
                        "title": "Duqlas Adams"
                    },
                    {
                        "lang": "bar",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "be",
                        "title": "Дуглас Адамс"
                    },
                    {
                        "lang": "be-x-old",
                        "title": "Дуглас Адамз"
                    },
                    {
                        "lang": "bg",
                        "title": "Дъглас Адамс"
                    },
                    {
                        "lang": "bn",
                        "title": "ডগলাস অ্যাডামস"
                    },
                    {
                        "lang": "bs",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ca",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "cs",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "cy",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "da",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "de",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "el",
                        "title": "Ντάγκλας Άνταμς"
                    },
                    {
                        "lang": "eo",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "es",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "et",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "eu",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "fa",
                        "title": "داگلاس آدامز"
                    },
                    {
                        "lang": "fi",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "fr",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ga",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "gl",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "he",
                        "title": "דאגלס אדמס"
                    },
                    {
                        "lang": "hr",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "hu",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "hy",
                        "title": "Դուգլաս Ադամս"
                    },
                    {
                        "lang": "id",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "io",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "is",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "it",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ja",
                        "title": "ダグラス・アダムズ"
                    },
                    {
                        "lang": "jv",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ka",
                        "title": "დაგლას ადამსი"
                    },
                    {
                        "lang": "ko",
                        "title": "더글러스 애덤스"
                    },
                    {
                        "lang": "la",
                        "title": "Duglassius Adams"
                    },
                    {
                        "lang": "lv",
                        "title": "Duglass Adamss"
                    },
                    {
                        "lang": "mg",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "mk",
                        "title": "Даглас Адамс"
                    },
                    {
                        "lang": "ml",
                        "title": "ഡഗ്ലസ് ആഡംസ്"
                    },
                    {
                        "lang": "mr",
                        "title": "डग्लस अ‍ॅडम्स"
                    },
                    {
                        "lang": "mrj",
                        "title": "Адамс, Дуглас"
                    },
                    {
                        "lang": "nl",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "nn",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "no",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "oc",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "pl",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "pt",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ro",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ru",
                        "title": "Адамс, Дуглас"
                    },
                    {
                        "lang": "sc",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sco",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sh",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "simple",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sk",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sl",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sq",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "sr",
                        "title": "Даглас Адамс"
                    },
                    {
                        "lang": "sv",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "ta",
                        "title": "டக்ளஸ் ஆடம்ஸ்"
                    },
                    {
                        "lang": "tr",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "uk",
                        "title": "Дуглас Адамс"
                    },
                    {
                        "lang": "ur",
                        "title": "ڈگلس ایڈمس"
                    },
                    {
                        "lang": "vep",
                        "title": "Adams Duglas"
                    },
                    {
                        "lang": "vi",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "war",
                        "title": "Douglas Adams"
                    },
                    {
                        "lang": "zh",
                        "title": "道格拉斯·亚当斯"
                    }
                ],
                "thumbnail": {
                    "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Douglas_adams_portrait_cropped.jpg/207px-Douglas_adams_portrait_cropped.jpg",
                    "width": 207,
                    "height": 240
                },
                "pageimage": "Douglas_adams_portrait_cropped.jpg",
                "pageprops": {
                    "wikibase_item": "Q42"
                },
                "terms": {
                    "description": [
                        "English writer and humorist"
                    ],
                    "label": [
                        "Douglas Adams"
                    ],
                    "alias": [
                        "Douglas Noël Adams",
                        "Douglas Noel Adams",
                        "Douglas N. Adams",
                        "DNA"
                    ]
                }
            }
        ],
        "random": [
            {
                "id": 37542590,
                "ns": 0,
                "title": "1996–97 FIBA EuroLeague"
            }
        ]
    }
}
"""

cache = {'query': query, 'response': response}

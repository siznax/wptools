# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&formatversion=2&iiprop=size|url|timestamp|extmetadata&prop=imageinfo&titles=File%3ADouglas%20adams%20portrait%20cropped.jpg'

response = r'''
{
    "continue": {
        "iistart": "2010-04-16T22:53:21Z",
        "continue": "||"
    },
    "query": {
        "pages": [
            {
                "ns": 6,
                "title": "File:Douglas adams portrait cropped.jpg",
                "missing": true,
                "known": true,
                "imagerepository": "shared",
                "imageinfo": [
                    {
                        "timestamp": "2010-04-16T22:54:28Z",
                        "size": 32915,
                        "width": 333,
                        "height": 386,
                        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg",
                        "descriptionurl": "https://commons.wikimedia.org/wiki/File:Douglas_adams_portrait_cropped.jpg",
                        "descriptionshorturl": "https://commons.wikimedia.org/w/index.php?curid=10031710",
                        "extmetadata": {
                            "DateTime": {
                                "value": "2010-04-16 22:54:28",
                                "source": "mediawiki-metadata",
                                "hidden": ""
                            },
                            "ObjectName": {
                                "value": "Douglas adams portrait cropped",
                                "source": "mediawiki-metadata",
                                "hidden": ""
                            },
                            "CommonsMetadataExtension": {
                                "value": 1.2,
                                "source": "extension",
                                "hidden": ""
                            },
                            "Categories": {
                                "value": "Douglas Adams|Portrait photographs of men|Self-published work|Uploaded with derivativeFX",
                                "source": "commons-categories",
                                "hidden": ""
                            },
                            "Assessments": {
                                "value": "",
                                "source": "commons-categories",
                                "hidden": ""
                            },
                            "ImageDescription": {
                                "value": "douglas adams inspired \"Hitch hikers guide to the galaxy\" H2G2 <a rel=\"nofollow\" class=\"external text\" href=\"http://www.hughes-photography.eu\">www.hughes-photography.eu</a>",
                                "source": "commons-desc-page"
                            },
                            "DateTimeOriginal": {
                                "value": "",
                                "source": "commons-desc-page"
                            },
                            "Credit": {
                                "value": "<ul>\n<li><a href=\"//commons.wikimedia.org/wiki/File:Douglas_adams_portrait.jpg\" title=\"File:Douglas adams portrait.jpg\">Douglas_adams_portrait.jpg</a></li>\n</ul>",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "Artist": {
                                "value": "<ul>\n<li>\n<a href=\"//commons.wikimedia.org/wiki/File:Douglas_adams_portrait.jpg\" title=\"File:Douglas adams portrait.jpg\">Douglas_adams_portrait.jpg</a>: <a rel=\"nofollow\" class=\"external text\" href=\"https://www.flickr.com/people/79664273@N00\">michael hughes</a> from berlin, germany</li>\n<li>derivative work: <a href=\"//commons.wikimedia.org/wiki/User:Beao\" title=\"User:Beao\">Bea</a><b><a href=\"//commons.wikimedia.org/wiki/User_talk:Beao\" title=\"User talk:Beao\">o</a></b>\n</li>\n</ul>",
                                "source": "commons-desc-page"
                            },
                            "LicenseShortName": {
                                "value": "CC BY-SA 2.0",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "UsageTerms": {
                                "value": "Creative Commons Attribution-Share Alike 2.0",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "AttributionRequired": {
                                "value": "true",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "LicenseUrl": {
                                "value": "https://creativecommons.org/licenses/by-sa/2.0",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "Copyrighted": {
                                "value": "True",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "Restrictions": {
                                "value": "",
                                "source": "commons-desc-page",
                                "hidden": ""
                            },
                            "License": {
                                "value": "cc-by-sa-2.0",
                                "source": "commons-templates",
                                "hidden": ""
                            }
                        }
                    }
                ]
            }
        ]
    }
}
'''

cache = {'query': query, 'response': response}

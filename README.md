### Wikipedia Tools

Some random tools for to fetch articles and whatnot. Import into your
python env or run from the command line. See ``pydoc <module>`` or
``<module.py> -h`` for more info.


**wp_article** - Wikipedia article(s) from title(s) via MediaWiki API

```shell
$ wp_article.py aardvark abba accordion | jsonlint | grep \"title
query: http://en.wikipedia.org/w/api.php?titles=aardvark|abba|accordion&format=json&formatversion=2&action=query&prop=revisions&rvprop=content&redirects&continue=
request headers: {'User-Agent': 'python-requests/2.7.0'}
status code: 200
        "title": "Aardvark",
        "title": "ABBA",
        "title": "Accordion",
```


**wp_infobox** - Infobox wiki-text from titles (via API) or file

```shell
$ wp_infobox.py aardvark
Title: Aardvark {{speciesbox
| genus = Orycteropus
| species = afer
| name = Aardvark
| fossil_range = {{Fossil range|5|0}}<small>Early [[Pliocene]] – Recent</small>
| status = LC
| status_system = iucn3.1
| status_ref = <ref name="iucn">{{harvnb|Lindsey|Cilliers|Griffin|Taylor|2008}}</ref>
| trend = unknown
| image = Porc formiguer.JPG
| image_caption =
| display_parents = 4
| greatgrandparent_authority = [[Thomas Henry Huxley|Huxley]], 1872
| grandparent_authority = [[John Edward Gray|Gray]], 1821
| parent_authority = [[Georges Cuvier|G. Cuvier]], 1798
| binomial_authority = ([[Peter Simon Pallas|Pallas]], 1766)
| range_map = Aardvark area.png
| range_map_caption = Aardvark range
| subdivision_ranks = [[Subspecies]]
| subdivision = See Text
}}```

from python:

```python
>>> import wp_infobox
>>> d = wp_infobox.from_api(['aardvark', 'abba', 'accordion'], 'dict')
query: http://en.wikipedia.org/w/api.php?titles=aardvark%7Cabba%7Caccordion&format=json&formatversion=2&action=query&prop=revisions&rvprop=content&redirects&continue=
request headers: {'User-Agent': 'python-requests/2.7.0'}
status code: 200
>>> [x['title'] for x in d]
[u'Aardvark',
 u'ABBA',
 u'Accordion']
>>> [x['image'] for x in d]
[u'Porc formiguer.JPG',
 u'ABBA - TopPop 1974 5.png',
 u'A convertor free-bass piano-accordion and a Russian bayan.jpg']
>>>
```

from shell (with list of titles):

```shell
$ wp_infobox.py aardvark abba accordion -format json | jsonlint | grep title
    "title": "Aardvark"
    "title": "ABBA"
    "title": "Accordion"
```


**wp_file** - URL and HTTP status from Wikipedia File/Image name

```shell
$ wp_file.py "Porc formiguer.JPG"
https://upload.wikimedia.org/wikipedia/commons/8/8a/Porc_formiguer.JPG
200```


**wp_vae** - Extract Wikipedia Vital Articles Extended

```shell
$ wp_vae.py WP_VAE.html '//div[@id="mw-content-text"]//li//@href'
    ...
/wiki/Amount_of_substance
/wiki/Mole_(unit)
/wiki/Byte
/wiki/Bit
/wiki/Atmosphere_(unit)
found (10359) links
    #: 417
    /: 9942
8.088 seconds
```


@siznax
## Wikipedia Tools

Some fun and helpful python tools you can also run from the cmdline.
See ``pydoc <module>`` or ``<module.py> -h`` for more info. 


### wp_dump

Get article from Wikipedia <a href="https://en.wikipedia.org/wiki/Wikipedia:Database_download">XML Dump</a> in streaming fashion

*This expects to operate on the (currently ~12GB) latest/enwiki-latest-pages-articles.xml.bz2*

```shell
$ wp_dump.py enwiki-latest-pages-articles.xml.bz2 -t Aardvark
<page>
    <title>Aardvark</title>
    <ns>0</ns>
    <id>680</id>
    <revision>
      <id>677062948</id>
      <parentid>677062792</parentid>
      <timestamp>2015-08-20T21:57:54Z</timestamp>
      <contributor>
...
[[Category:Mammals of Africa]]
[[Category:Myrmecophagous mammals]]
[[Category:Living fossils]]
[[Category:Megafauna of Africa]]
[[Category:Animals described in 1766]]
[[Category:Pliocene first
appearances]]</text>
      <sha1>1gxa6ifmfibynhk22gtpdevqzc4wsew</sha1>
    </revision>
  </page>
7125314560 bytes read
0.377 seconds
```


### wp_file

Get URL and HTTP status from Wikipedia File/Image name

```shell
$ wp_file.py "ABBA - TopPop 1974 5.png"
https://upload.wikimedia.org/wikipedia/commons/c/cb/ABBA_-_TopPop_1974_5.png 200
```


### wp_get

GET Wikipedia article content from URL or filename

*This is basically an alternative path to article content outside of
the MediaWiki API, which is often quite slow. The problem is that you
don't get ``wikitext``, but you can get raw HTML or Markdown
text. It's not entirely deprecated, but ``wp_query`` and
``wp_summary`` are recommended for bulk processing.*


### wp_image

Get images from articles (just file names or expanded URLs)

```shell
$ wp_image.py "Van_Gogh" -expand
https://upload.wikimedia.org/wikipedia/commons/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_(454045).jpg
https://upload.wikimedia.org/wikipedia/commons/7/74/VincentVanGoghFoto.jpg
https://upload.wikimedia.org/wikipedia/commons/f/f6/Theo_van_Gogh_(1888).png
(+ many more...)
```


### wp_infobox

Get <a href="https://en.wikipedia.org/wiki/Help:Infobox">Infobox</a> wikitext from titles or file

```shell
$ wp_infobox.py Aardvark
= Aardvark =
{{speciesbox
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
}}
```

From python:

```python
>>> import wp_infobox
>>> d = wp_infobox.from_api(['aardvark', 'abba', 'accordion'])
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


### wp_query

Get articles via MediaWiki API given titles, format

For example, get articles as ``json``:

```shell
$ wp_query.py aardvark abba accordion | jsonlint | grep \"title
query: http://en.wikipedia.org/w/api.php?titles=aardvark|abba|accordion&format=json&formatversion=2&action=query&prop=revisions&rvprop=content&redirects&continue=
request headers: {'User-Agent': 'python-requests/2.7.0'}
status code: 200
bytes: 181931
1.881 seconds
        "title": "Aardvark",
        "title": "ABBA",
        "title": "Accordion",
```

Get articles as ``wikitext``:

```shell
$ wp_query.py aardvark abba accordion -format wikitext | grep ^=[^=]
query: http://en.wikipedia.org/w/api.php?titles=aardvark|abba|accordion&format=json&formatversion=2&action=query&prop=revisions&rvprop=content&continue=
request headers: {'User-Agent': 'python-requests/2.7.0'}
status code: 200
bytes: 76459
1.114 seconds
= Aardvark =
= Accordion =
= Abba =
```


From python:

```python
>>> import wp_query
>>> r = wp_query.data(['aardvark', 'abba', 'accordion'])
query: http://en.wikipedia.org/w/api.php?titles=aardvark|abba|accordion&format=json&formatversion=2&action=query&prop=revisions&rvprop=content&redirects&continue=
request headers: {'User-Agent': 'python-requests/2.7.0'}
status code: 200
>>> j = json.loads(r)
>>> [x['title'] for x in j['query']['pages']]
[u'Aardvark',
 u'ABBA',
 u'Accordion']
>>> j['query']['pages'][2]['title']
u'Accordion'
>>> j['query']['pages'][2]['revisions'][0]['content'][:256]
u"{{other uses}}\n{{Use dmy dates|date=July 2013}}\n{{Infobox instrument\n|name=Accordion\n|names=* [[Bosnian language|Bosnian]]: ''Harmonika''\n* [[Danish language|Danish]] ([[free-bass system|free-bass]]): ''Accordeon''\n* [[Hungarian language|Hungarian]] & [[Ic"
>>> 
```


### wp_summary

Get plain text of article's <a href="https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section">lead section</a> from titles or file

```shell
$ wp_summary.py aardvark | fold -s
= Aardvark =

The 'aardvark' ({ˈ|ɑr|d|.|v|ɑr|k|} {ARD|vark}; 'Orycteropus afer') is a
medium-sized, burrowing, nocturnal mammal native to Africa. It is the only
living species of the order Tubulidentata, although other prehistoric species
and genera of Tubulidentata are known. Unlike other insectivores, it has a long
pig-like snout, which is used to sniff out food. It roams over most of the
southern two-thirds of the African continent, avoiding mainly rocky areas. A
nocturnal feeder, it subsists on ants and termites, which it will dig out of
their hills using its sharp claws and powerful legs. It also digs to create
burrows in which to live and rear its young. It receives a "least concern"
rating from the IUCN; although its numbers seem to be decreasing.

Related terms:
 * Africa
 * IUCN
 * Tubulidentata
 * insectivore
 * nocturnal

https://en.wikipedia.org/wiki/Aardvark
```

from python:

```python
>>> import wp_summary, json
>>> j = json.loads(wp_summary.from_file('Aardvark.json', 'json'))
>>> j[0].keys()
[u'wikitext', u'title', u'related', u'summary']
```


### wp_vae

Extract <a href="https://meta.wikimedia.org/wiki/List_of_articles_every_Wikipedia_should_have/Expanded">Vital Articles Expanded</a> (10K) titles

```shell
$ curl -o WP_VAE.html https://meta.wikimedia.org/wiki/List_of_articles_every_Wikipedia_should_have/Expanded
$ wp_vae.py WP_VAE.html '//div[@id="mw-content-text"]//div//li//a' > wp_vae.txt
  found 9966 titles
  5.132 seconds

$ head wp_vae.txt
  Harold Lloyd
  Lillian Gish
  Buster Keaton
  Mary Pickford
  Gloria Swanson
  Asta Nielsen
  Fred Astaire
  Sarah Bernhardt
  Humphrey Bogart
  Marlon Brando

$ tail wp_vae.txt
  Standard deviation
  Standard error
  Statistical hypothesis testing
  Student's t-test
  Variance
  Design of experiments
  Randomized controlled trial
  Survey methodology
  Statistical population
  Sampling (statistics)
```


@siznax
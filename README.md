## Wikipedia Tools

Some fun and helpful python tools you can also run from the cmdline.
See ``pydoc <module>`` or ``<module.py> -h`` for more info. 


### [wp_file](https://github.com/siznax/wptools/blob/master/wp_file.py)

Get URL and HTTP status from Wikipedia File/Image name

```shell
$ wp_file.py "ABBA - TopPop 1974 5.png"
https://upload.wikimedia.org/wikipedia/commons/c/cb/ABBA_-_TopPop_1974_5.png 200
```


### [wp_get](https://github.com/siznax/wptools/blob/master/wp_get.py)

GET Wikipedia article content from URL or filename

*This is basically an alternative path to article content outside of
the MediaWiki API, which is often quite slow. The problem is that you
don't get ``wikitext``, but you can get raw HTML or Markdown
text. It's not entirely deprecated, but ``wp_query`` and
``wp_summary`` are recommended for bulk processing.*


### [wp_image](https://github.com/siznax/wptools/blob/master/wp_image.py)

Get images from articles (just file names or expanded URLs)

```shell
$ wp_image.py "Van_Gogh" -expand
https://upload.wikimedia.org/wikipedia/commons/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_(454045).jpg
https://upload.wikimedia.org/wikipedia/commons/7/74/VincentVanGoghFoto.jpg
https://upload.wikimedia.org/wikipedia/commons/f/f6/Theo_van_Gogh_(1888).png
(+ many more...)
```


### [wp_index](https://github.com/siznax/wptools/blob/master/wp_index.py)

Index the [Wikipedia XML
Dump](https://en.wikipedia.org/wiki/Wikipedia:Database_download)
(currently ~12GB) into alphabetical files.

```shell
$ wp_index.py -h
usage: wp_index.py [-h] [-c C] [-d D] [-m M] [-o O] [-s] [-t T] fname

Index or split Wikipedia XML Dump into alphabetical (gz) files

positional arguments:
  fname               XML Dump (bz2) filename

optional arguments:
  -h, --help          show this help message and exit
  -c C, -chunksize C  chunk size in KB (default=1)
  -d D, -dest D       write results to dest (dir)
  -m M, -maxbytes M   max bytes in MB (default=10)
  -o O, -offset O     seek to byte offset
  -s, -split          split (versus index) into files
  -t T, -titles T     flat file of titles to pull
```


It's interruptable...

```shell
$ wp_index.py data/enwiki-latest-pages-articles.xml.bz2
  ...
  Bluescreen 69966270
  British public houses 70873946
  Birds 71896368

(KeyboardInterrupt)

pages found: 2730
titles processed: 2729
first: AccessibleComputing 2911
last: Balmoral Castle 72508055
read: 72 MB
tell: 72574000
```

and restartable:

```shell
$ wp_index.py data/enwiki-latest-pages-articles.xml.bz2 -m 1 -o 72508055
pages found: 27
titles processed: 26
first: Balmoral Castle 72508055
last: B-tree 73395052
read: 1 MB
tell: 73508055
```

### [wp_infobox](https://github.com/siznax/wptools/blob/master/wp_infobox.py)

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


### [wp_pull](https://github.com/siznax/wptools/blob/master/wp_pull.py)

Pull article from Wikipedia XML Dump (bz2) or part (gz)

from XML Dump (bzip2) with index from ``wp_index``

```shell
$ wp_pull.py -i index/A Aristotle data/enwiki-latest-pages-articles.xml.bz2
      <sha1>5il233urt2yitnzdv9n2coh68ny9mom</sha1>
    </revision>
  </page>
```

from (gzip) part of XML Dump split with ``wp_index``

```shell
$ wp_pull.py Aristotle split/A
      <sha1>5il233urt2yitnzdv9n2coh68ny9mom</sha1>
    </revision>
  </page>
```


### [wp_parser](https://github.com/siznax/wptools/blob/master/wp_parser.py)

Parse a [Wikipedia XML
Dump](https://en.wikipedia.org/wiki/Wikipedia:Database_download),
naive and reckless. You'll need to override ``WPParser.process``. See
``wp_index`` for example.  

```python
class MyParser(WPParser):

    def __init__(self):
        WPParser.__init__(self)

    def process(self, elem):
        """fancy processing here"""
```


### [wp_query](https://github.com/siznax/wptools/blob/master/wp_query.py)

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


### [wp_summary](https://github.com/siznax/wptools/blob/master/wp_summary.py)

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


### [wp_vae](https://github.com/siznax/wptools/blob/master/wp_vae.py)

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
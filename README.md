### Wikipedia Tools

Some random tools for to fetch articles and whatnot. Each can be
imported into your python env or run from the command line. See
``<module.py> -h`` or ``pydoc <module>`` for more info.


**wp_article** - Dump Wikipedia article(s) via Mediawiki API

```shell
$ ./wp_article.py "Dung beetle" | jsonlint | fold | head -16
{
  "batchcomplete": true,
  "query": {
    "pages": [
      {
        "pageid": 630020,
        "ns": 0,
        "title": "Dung beetle",
        "revisions": [
          {
            "contentformat": "text/x-wiki",
            "contentmodel": "wikitext",
            "content": "{{other uses}}\n{{Taxobox\n| name = Dung beetle\n| image
 = Scarabaeus viettei 01.jpg\n| image_width = 250px\n| image_caption = ''Scaraba
eus viettei'' (syn. Madateuchus viettei, Scarabaeidae) in [[Madagascar spiny thi
ckets|dry spiny forest]] close to Mangily, western Madagascar\n| regnum = [[Anim
```


**wp_infobox** - Dump Wikipedia article(s) Infobox wiki-text

```shell
$ wp_infobox.py "Dung beetle"
{{Taxobox
| name = Dung beetle
| image = Scarabaeus viettei 01.jpg
| image_width = 250px
| image_caption = ''Scarabaeus viettei'' (syn. Madateuchus viettei, Scarabaeidae) in [[Madagascar spiny thickets|dry spiny forest]] close to Mangily, western Madagascar
| regnum = [[Animal]]ia
| phylum = [[Arthropod]]a
| classis = [[Insect]]a
| ordo = [[beetle|Coleoptera]]
| subordo = [[Polyphaga]]
| superfamilia = [[Scarabaeoidea]] (in part)
| familia = ''Scarabidae''
}}
```


**wp_file** - URL and HTTP status from Wikipedia File/Image name

```shell
$ wp_file.py "Scarabaeus viettei 01.jpg"
https://upload.wikimedia.org/wikipedia/commons/c/cc/Scarabaeus_viettei_01.jpg
200
```

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
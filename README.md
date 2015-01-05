### Wikipedia Article Tools

**wp_article** dump Wikipedia article

    $ wp_article.py "Neuromancer"
        [query] => Array
            (
                [pages] => Array
                    (
                        [21725] => Array
                            (
                                [pageid] => 21725
                                [ns] => 0
                                [title] => Neuromancer
                                [revisions] => Array
                                    (


**wp_image** find Wikipedia [File/Image](https://en.wikipedia.org/wiki/Help:Files) URL and show status

    $ wp_image.py "Image:Neuromancer (Book).jpg" --namespace en
    http://upload.wikimedia.org/wikipedia/en/4/4b/Neuromancer_(Book).jpg
    200


**wp_info** dump the [Infobox](https://en.wikipedia.org/wiki/Help:Infobox) text of a Wikipedia article

    $ wp_info.py "Neuromancer"
    {{Infobox book
    | name = Neuromancer
    | image = File:Neuromancer (Book).jpg
    | caption = First edition
    | author = [[William Gibson]]
    | cover_artist = [[James Warhola]]
    | series = [[Sprawl trilogy]]
    | genre = science fiction, [[cyberpunk]]
    | subject =
    | pub_date = July 1, 1984
    | publisher = [[Ace Books|Ace]]
    | media_type = print (paperback and hardback)
    | pages = 271
    | isbn = 0-441-56956-0
    | oclc = 10980207
    | dewey =
    | congress =
    | preceded_by = "[[Burning Chrome]]"
    | followed_by = [[Count Zero]]
    }}

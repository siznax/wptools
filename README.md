**wp_info** - get Infobox text of a Wikipedia article

    $ python wp_info.py Neuromancer
    {{Infobox book
    | name = Neuromancer
    | image = [[Image:Neuromancer (Book).jpg|300x300px]]
    | image_caption =First edition paperback cover<br />(Ace ...
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

**wp_image** - look for Wikipedia image file

    $ wp_image.py "Image:Neuromancer (Book).jpg" en
    http://upload.wikimedia.org/wikipedia/en/4/4b/Neuromancer_(Book).jpg
    200 OK

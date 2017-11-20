# -*- coding:utf-8 -*-

'''
selected titles by language for WPTools tests
'''

# animals
#     https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status
# art
#     https://en.wikipedia.org/wiki/Category:Lists_of_works_of_art
# books
#     https://en.wikipedia.org/wiki/Man_Booker_Prize
#     https://en.wikipedia.org/wiki/Man_Booker_International_Prize
#     https://en.wikipedia.org/wiki/Pulitzer_Prize_for_Fiction
# music
#     https://en.wikipedia.org/wiki/Grammy_Award_for_Album_of_the_Year
# film
#     https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films
#     https://en.wikipedia.org/wiki/List_of_films_considered_the_best
# featured
#     https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/Most_viewed
#     https://ja.wikipedia.org/wiki/Wikipedia:%E7%A7%80%E9%80%B8%E3%81%AA%E8%A8%98%E4%BA%8B
#     https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8
#     https://zh.wikipedia.org/wiki/Wikipedia:%E7%89%B9%E8%89%B2%E6%9D%A1%E7%9B%AE
# places
#     https://en.wikipedia.org/wiki/List_of_cities_proper_by_population

import random


class WPToolsTestTitles(object):
    """
    selected test titles
    - lang: en, ja, ru, zh
    - categories: animals, featured, people, places, things
    """

    def __init__(self):
        pass

    animals = {
        "en": {
            "Amur Leopard",
            "Black Rhino",
            "Bornean Orangutan",
            "Cross River Gorilla",
            "Hawksbill Turtle",
            "Javan Rhino",
            "Leatherback Turtle",
            "Mountain Gorilla",
            "Orangutan",
            "Pangolin",
            "Saola",
            "South China Tiger",
            "Sumatran Elephant",
            "Sumatran Orangutan",
            "Sumatran Rhino",
            "Sumatran Tiger",
            "Vaquita",
            "Western Lowland Gorilla",
        }
    }

    art = {
        "en": {
            "Eight Elvises",
            "Guennol Lioness",
            "Portrait of Dr. Gachet",
            "The Great Wave off Kanagawa",
            "The Scream",
            "The Sea Monster",
            "Knight, Death and the Devil",
            "Melencolia I",
        }
    }

    books = {
        "en": {
            "A Brief History of Seven Killings",
            "Bring Up the Bodies",
            "MaddAddam",
            "The Sympathizer",
            "The Vegetarian",
        }
    }

    film = {
        "en": {
            "Casablanca (film)",
            "Himala",
            "Raise the Red Lantern",
            "Seven Samurai",
            "Spotlight (film)",
        }
    }

    music = {
        "en": {
            "1989 (Taylor Swift album)",
            "Beauty Behind the Madness",
            "Giant Steps",
            "Kind of Blue",
            "To Pimp a Butterfly",
        }
    }

    # these are somewhat random, but should be high-quality articles
    featured = {
        "en": {
            "Franz Kafka",
            "Elizabeth II",
            "Barack Obama",
            "Pluto",
            "Shah Rukh Khan",
        },
        "ja": {
            "ノストラダムス",  # Nostrodamus
            "アンネ・フランク",  # Anne Frank
            "フィンセント・ファン・ゴッホ",  # Vincent van Gogh
            "アイザック・アシモフ",  # Isaac Asimov
            "チンドン屋",  # musical sandwichmen
        },
        "ru": {
            "Малер, Густав",  # Gustav Mahler
            "Сенеш, Хана",  # Hannah Szenes
            "Уильямс, Серена",  # Crime and Punishment
            "Бронте, Энн",  # Anne Bronte
            "Уолстонкрафт, Мэри",  # Mary Wollstonecraft
        },
        "zh": {
            "異特龍屬",  # allosaurus
            "兴圣教寺塔",  # Hing temple
            "玛丽·沃斯通克拉夫特",  # Mary Wollstonecraft
            "蒙山大佛",  # Monsanto Buddha
            "尼克松在中国 (歌剧)",  # Nixon in China (opera)
        },
    }

    people = {
        "en": {
            "Amelia Earhart",
            "Anne Frank",
            "Borges",
            "Eleanor of Aquitaine",
            "Elizabeth II",
            "Ella Fitzgerald",
            "Emily Dickinson",
            "Fela Kuti",
            "Flannery O'Connor",
            "Frida Kahlo",
            "Harriet Tubman",
            "Harriet Beecher Stowe",
            "Jane Goodall",
            "Jeanne d'Arc",
            "Malala Yousafzai",
            "Malcolm X",
            "Stephen Fry",
            "Simone de Beauvoir",
            "Shakespeare",
        },
        "ja": {
            "三島由紀夫",  # Yukio Mishima
            "北斎",  # Hokusai
            "穐吉敏子",  # Toshiko Akiyoshi
            "草薙素子",  # Major Motoko Kusanagi
            "紫式部",  # Murasaki Shikibu
            "村上春樹",  # Haruki Murakami
        },
        "ru": {
            "Анна Ахматова",  # Anna Akhmatova
            "Анна Павлова",  # Anna Pavlova
            "Антон Павлович Чехов",  # Anton Chekhov
            "Екатерина II",  # Catherine the Great
            "Фёдор Михайлович Достоевский",  # Fyodor Dostoyevsky
            "Валентина Владимировна Терешкова",  # Valentina Tereshkova
        },
        "zh": {
            "老子",  # Laozi
            "丹增嘉措",  # Dalai Lama 14
            "艾未未",  # Ai Weiwei
            "刘晓波",  # Liu Xiaobo
            "楊紫瓊",  # Michelle Yeoh
            "刘洋 (航天员)",  # Liu Yang (astronaut)
            "李振藩",  # Bruce Lee
        }
    }

    places = {
        "en": {
            # "Shanghai",
            "Karachi",
            # "Beijing",
            "Delhi",
            "Lagos",
            "Tianjin",
            "Istanbul",
            # "Tokyo",
        },
        "ja": {
            "広島市",  # Hiroshima
            "京都市",  # Kyoto
            "富士山",  # Mount Fuji
            "長崎市",  # Nagasaki
            "大阪市",  # Osaka
            "東京",  # Tokyo
        },
        "ru": {
            "Москва",  # Moscow
            "Красная площадь",  # Red Square
            "Собор Василия Блаженного",  # Saint Basil's Cathedral
            "Санкт-Петербург",  # Saint Petersburg
            "Зимний дворец",  # Winter Palace
        },
        "zh": {
            "北京市",  # Beijing
            "上海市",  # Shanghai
            "香港特别行政区",  # Hong Kong
            "万里长城",  # Great Wall
            "故宮博物院",  # Forbidden City
        }
    }

    things = {
        "en": {
            "A-bomb",
            "Big Bang",
            "Encyclopédie",
            "Genetics",
            "Magna Carta",
            "Quaternion",
        },
        "ja": {
            "すし",  # sushi
            "歌舞伎",  # kabuki
            "浮世絵",  # ukiyo-e
            "相撲",  # sumo
            "暗黒舞踏",  # butoh
        },
        "ru": {
            "Балалайка",  # balalaika
            "Коммунистическая партия Советского Союза",  # communist party
            "Автомат Калашникова",  # AK-47
            "пирожки",  # pirozhki
            "водка",  # vodka
        },
        "zh": {
            "功夫",  # kung fu
            "中國園林",  # Chinese garden
            "舞獅",  # lion dance
            "道",  # Daoism
            "龍",  # dragon
        },
    }


def language():
    """
    returns random language code from selections
    """
    return random.choice(list(WPToolsTestTitles.featured))


def media(lang='en'):
    """
    returns random media title
    """
    titles = set()
    titles = titles.union(WPToolsTestTitles.books[lang])
    titles = titles.union(WPToolsTestTitles.music[lang])
    titles = titles.union(WPToolsTestTitles.film[lang])
    return {'lang': lang, 'title': random.choice(list(titles))}


def title(lang=None):
    """
    returns random title from selections
    """
    if not lang:
        lang = language()

    titles = set()
    if lang == 'en':
        titles = WPToolsTestTitles.animals['en']

    titles = titles.union(WPToolsTestTitles.featured[lang])
    titles = titles.union(WPToolsTestTitles.people[lang])
    titles = titles.union(WPToolsTestTitles.places[lang])
    titles = titles.union(WPToolsTestTitles.things[lang])

    return {'lang': lang, 'title': random.choice(list(titles))}

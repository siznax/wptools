# -*- coding:utf-8 -*-

import random


class WPToolsTestTitles:
    """
    selected test titles
    - lang: en, ja, ru, zh
    - categories: animals, featured, people, places, things
    """

    animals = {  # https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status
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

    # these are somewhat random, but should be high-quality articles
    featured = {
        "en": {  # https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/Most_viewed
            "Franz Kafka",
            "Elizabeth II",
            "Barack Obama",
            "Pluto",
            "Shah Rukh Khan",
        },
        "ja": {  # https://ja.wikipedia.org/wiki/Wikipedia:%E7%A7%80%E9%80%B8%E3%81%AA%E8%A8%98%E4%BA%8B
            "ノストラダムス",  # Nostrodamus
            "アンネ・フランク",  # Anne Frank
            "フィンセント・ファン・ゴッホ",  # Vincent van Gogh
            "アイザック・アシモフ",  # Isaac Asimov
            "チンドン屋",  # musical sandwichmen
        },
        "ru": {  # https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8
            "Малер, Густав",  # Gustav Mahler
            "Сенеш, Хана",  # Hannah Szenes
            "Уильямс, Серена",  # Crime and Punishment
            "Бронте, Энн",  # Anne Bronte
            "Уолстонкрафт, Мэри",  # Mary Wollstonecraft
        },
        "zh": {  # https://zh.wikipedia.org/wiki/Wikipedia:%E7%89%B9%E8%89%B2%E6%9D%A1%E7%9B%AE
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
            "Анто́н Па́влович Че́хов",  # Anton Chekhov
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

    places = {  # https://en.wikipedia.org/wiki/List_of_cities_proper_by_population
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
            "Калашникова",  # kalash
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
    return random.choice(WPToolsTestTitles.featured.keys())


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

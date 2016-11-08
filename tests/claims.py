# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&formatversion=2&ids=Q187655|Q1042294|Q7758404|Q145|Q8935487|Q902712|Q25169|Q578895|Q761469|Q5|Q721&languages=en&props=labels&redirects=yes&sites=&titles='

response = r"""
{
  "entities": {
    "Q187655": {
      "type": "item",
      "id": "Q187655",
      "labels": {
        "en": {
          "language": "en",
          "value": "Mostly Harmless"
        }
      }
    },
    "Q1042294": {
      "type": "item",
      "id": "Q1042294",
      "labels": {
        "en": {
          "language": "en",
          "value": "So Long, and Thanks for All the Fish"
        }
      }
    },
    "Q7758404": {
      "type": "item",
      "id": "Q7758404",
      "labels": {
        "en": {
          "language": "en",
          "value": "The Private Life of Genghis Khan"
        }
      }
    },
    "Q145": {
      "type": "item",
      "id": "Q145",
      "labels": {
        "en": {
          "language": "en",
          "value": "United Kingdom"
        }
      }
    },
    "Q8935487": {
      "type": "item",
      "id": "Q8935487",
      "labels": {
        "en": {
          "language": "en",
          "value": "Category:Douglas Adams"
        }
      }
    },
    "Q902712": {
      "type": "item",
      "id": "Q902712",
      "labels": {
        "en": {
          "language": "en",
          "value": "Dirk Gently's Holistic Detective Agency"
        }
      }
    },
    "Q25169": {
      "type": "item",
      "id": "Q25169",
      "labels": {
        "en": {
          "language": "en",
          "value": "The Hitchhiker's Guide to the Galaxy pentalogy"
        }
      }
    },
    "Q578895": {
      "type": "item",
      "id": "Q578895",
      "labels": {
        "en": {
          "language": "en",
          "value": "The Restaurant at the End of the Universe"
        }
      }
    },
    "Q761469": {
      "type": "item",
      "id": "Q761469",
      "labels": {
        "en": {
          "language": "en",
          "value": "comic science fiction"
        }
      }
    },
    "Q5": {
      "type": "item",
      "id": "Q5",
      "labels": {
        "en": {
          "language": "en",
          "value": "human"
        }
      }
    },
    "Q721": {
      "type": "item",
      "id": "Q721",
      "labels": {
        "en": {
          "language": "en",
          "value": "Life, the Universe and Everything"
        }
      }
    }
  },
  "success": 1
}
"""

cache = {'query': query, 'response': response}

# -*- coding:utf-8 -*-

query = 'https://www.wikidata.org/w/api.php?action=wbgetentities&formatversion=2&languages=en&props=aliases|info|claims|descriptions|labels|sitelinks&redirects=yes&ids=Q10908976'

response = r"""{"entities":{"Q10908976":{"id":"Q10908976","missing":""}},"success":1}"""

cache = {'query': query, 'response': response}

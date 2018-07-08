# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/api/rest_v1/page/'

response = r"""{"items":["data-parsoid","graph","html","mobile-sections","mobile-sections-lead","mobile-sections-remaining","pdf","random","related","revision","segments","summary","title","wikitext"]}"""

info = {'content-type': 'TEST', 'status': 200}
cache = {'query': query, 'response': response, 'info': info}

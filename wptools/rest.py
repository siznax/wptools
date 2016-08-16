# -*- coding:utf-8 -*-

"""
WPTools RESTBase module.
"""

from __future__ import print_function

import re
import requests
import sys
import urlparse
import utils


class WPToolsREST:

    DEFAULT_WIKI = 'en.wikipedia.org'
    API_PATH = '/api/rest_v1/'
    DEBUG = True

    def __init__(self, wiki=None):
        self.wiki = wiki
        if wiki is None:
            self.wiki = self.DEFAULT_WIKI
        self.base = "https://" + self.wiki

    def rest_url(self, entrypoint, title):
        rpath = '/'.join([self.API_PATH, entrypoint, title])
        rpath = re.sub('/+', '/', rpath)
        url = urlparse.urljoin(self.base, rpath)
        self.url = url
        if self.DEBUG:
            print(url, file=sys.stderr)
        return url

    def html(self, api_json, entrypoint):
        html = []

        if entrypoint == '/page/summary/':
            html.append(api_json["extract"])

        if entrypoint == '/page/mobile-text/':
            for item in api_json["sections"][0]["items"]:
                if item["type"] != "hatnote":
                    html.append(item["text"])

        if entrypoint == '/page/mobile-sections-lead/':
            html.append(api_json["sections"][0]["text"])

        return " ".join(html)

    def pruned(self, html):
        """return pruned HTML"""
        out = utils.prune_html(html)
        out = utils.prune_html_spans(out)
        return out


def main(title, entrypoint):
    rest = WPToolsREST()
    url = rest.rest_url(entrypoint, title)
    r = requests.get(url, timeout=3)
    r_json = r.json()
    html = rest.html(r_json, entrypoint)
    return rest.pruned(html)


if __name__ == "__main__":
    print(main('Abraham Lincoln', '/page/mobile-text/'))
    # main('Abraham Lincoln', '/page/mobile-sections-lead/')
    # main('Abraham_Lincoln', '/page/summary/')

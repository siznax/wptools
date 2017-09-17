# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/w/api.php?action=query&meta=siteviews&pvismetric=uniques&pvisdays=7&formatversion=2&format=json'

response = r"""{"batchcomplete":true,"query":{"siteviews":{"2017-09-09":58280704,"2017-09-10":62551505,"2017-09-11":65442820,"2017-09-12":64589330,"2017-09-13":64394116,"2017-09-14":64349926,"2017-09-15":61951387}}}"""

cache = {'info': {'status': 200}, 'query': query, 'response': response}

# -*- coding:utf-8 -*-

"""
WPTools RESTBase module
~~~~~~~~~~~~~~~~~~~~~~~

Support for getting RESTBase page info.
"""

try:  # python2
    from urlparse import urlparse
except ImportError:  # python3
    from urllib.parse import urlparse

from . import core
from . import utils


class WPToolsRESTBase(core.WPTools):
    """
    WPtoolsRESTBase class
    """

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsRESTBase object

        Optional positional arguments:
        - [title]: <str> Mediawiki page title, file, category, etc.

        Optional keyword arguments:
        - [lang]: <str> Mediawiki language code (default='en')
        """
        super(WPToolsRESTBase, self).__init__(**kwargs)

        title = None
        if len(args) > 0:  # first positional arg is title
            title = args[0].replace(' ', '_')

        self.params.update({'lang': kwargs.get('lang') or 'en',
                            'title': title})

    def _handle_response(self):
        """
        Returns RESTBase response if appropriate
        """
        content = self.cache['rest']['info']['content']
        if content.startswith('text/html'):
            html = self.cache['rest']['response']
            if isinstance(html, bytes):
                html = html.decode('utf-8')
            self.data['html'] = html
            return

        response = self._load_response('rest')

        http_status = self.cache['rest']['info']['status']
        if http_status == 404:
            err = response.get('detail')
            if err:
                raise LookupError(err)
            else:
                raise LookupError(self.cache['rest']['query'])

        if self.params.get('endpoint') == '/page/':
            msg = "RESTBase /page/ entry points: %s" % response.get('items')
            utils.stderr(msg)
            del self.cache['rest']
            return

        return response

    def _parse_endpoint(self, endpoint):
        """
        Parse input endpoint
        """
        if not endpoint:
            return '/page/'

        parts = endpoint.split('/')
        parts = [x for x in parts if x]

        if not parts[0] == 'page':
            parts.insert(0, 'page')

        title = self.params.get('title')
        if not title and len(parts) < 3:
            raise StandardError("need a title.")

        if len(parts) == 3 and self.params.get('title'):  # check title
            if self.params['title'] != parts[2]:
                raise StandardError("titles conflict.")

        if title and len(parts) < 3:
            parts.append(title)

        if not title:
            self.params['title'] = parts[-1]

        return '/' + '/'.join(parts)

    def _query(self, action, qobj):
        """
        returns WPToolsQuery string from action
        """
        return qobj.rest(self.params['endpoint'])

    def _set_data(self, action):
        """
        Sets RESTBase response data
        """
        self._set_rest_data()

    def _set_rest_data(self):
        """
        Unpacks RESTBase response data
        """
        res = self._handle_response()
        if res is None:
            return

        self.data['description'] = res.get('description')
        self.data['pageid'] = (res.get('id') or res.get('pageid'))
        self.data['exrest'] = res.get('extract')
        self.data['exhtml'] = res.get('extract_html')

        self._unpack_images(res)

        lastmodified = res.get('lastmodified')
        if lastmodified:
            pagemod = {'page': lastmodified}
            if 'modified' in self.data:
                self.data['modified'].update(pagemod)
            else:
                self.data['modified'] = pagemod

        if res.get('sections'):
            lead = res.get('sections')[0]
            self.data['lead'] = lead.get('text')

        thumbnail = res.get('thumbnail')  # /page/summary
        if thumbnail:
            rimg = {'kind': 'rest-thumb'}
            rimg.update(thumbnail)
            if thumbnail.get('source'):
                rimg.update({'url': thumbnail.get('source')})
            self.data['image'].append(rimg)

        title = res.get('title') or res.get('normalizedtitle')
        if title:
            self.data['title'] = title.replace(' ', '_')

        wikibase = res.get('wikibase_item')
        if wikibase:
            self.data['wikibase'] = wikibase
            self.data['wikidata_url'] = utils.wikidata_url(wikibase)

        url = urlparse(self.cache['rest']['query'])
        durl = "%s://%s/wiki/%s" % (url.scheme,
                                    url.netloc,
                                    self.params['title'])
        self.data['url'] = durl
        self.data['url_raw'] = durl + '?action=raw'

    def _unpack_images(self, rdata):
        """
        Set image data from RESTBase response
        """
        image = rdata.get('image')  # /page/mobile-sections-lead
        originalimage = rdata.get('originalimage')  # /page/summary

        if image or originalimage:
            if 'image' not in self.data:
                self.data['image'] = []

        if image:
            rimg = {'kind': 'rest-image'}
            rimg.update(image)
            self.data['image'].append(rimg)

        if originalimage:
            rimg = {'kind': 'rest-image'}
            rimg.update(originalimage)
            if originalimage.get('source'):
                rimg.update({'url': originalimage.get('source')})
            self.data['image'].append(rimg)

    def get_rest(self, endpoint=None, show=True, proxy=None, timeout=0):
        """
        GET RESTBase /page/ endpoints needing only {title}
        for example:
            /page/html/{title}
            /page/summary/{title}
            /page/mobile-sections-lead/{title}

        Arguments:
        - endpoint: the RESTBase entry point

        Without arguments, lists RESTBase /page/ entry points

        Attributes affected:
        - exhtml: <str> "extract_html" from /page/summary
        - exrest: <str> "extract" from /page/summary
        - html: <str> from /page/html
        - image: <dict> {rest-image, rest-thumb}
        - lead: <str> section[0] from /page/mobile-sections-lead
        - modified (page): <str> ISO8601 date and time
        - title: <str> the article title
        - url: <str> the canonical wiki URL
        - url_raw: <str> probable raw wikitext URL
        - wikibase: <str> Wikidata item ID
        - wikidata_url: <str> Wikidata URL

        See https://en.wikipedia.org/api/rest_v1/
        """
        self.params['endpoint'] = self._parse_endpoint(endpoint)

        self._get('rest', show, proxy, timeout)

        return self

# -*- coding:utf-8 -*-

"""
WPTools RESTBase module
~~~~~~~~~~~~~~~~~~~~~~~

Support for getting RESTBase page info.
"""

from . import core


class WPToolsRESTBase(object):
    """
    WPtoolsRESTBase class
    """

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsRESTBase object
        """
        pass

    def _query(self, action, qobj):
        """
        returns WPToolsQuery string from action
        """
        return qobj.rest(self.endpoint)

    def _set_rest_data(self):
        """
        set attributes derived from RESTBase
        """
        if self.cache['rest']['info']['content'].startswith('text/html'):
            html = self.cache['rest']['response']
            if isinstance(html, bytes):
                html = html.decode('utf-8')
            self.html = html
            return

        data = self._load_response('rest')

        if self.endpoint == '/page/':
            msg = "RESTBase /page/ entry points: %s" % data.get('items')
            utils.stderr(msg)
            return

        if self.cache['rest']['info']['status'] == 404:
            raise LookupError(data.get('detail'))

        self.description = data.get('description')
        self.pageid = (data.get('id') or data.get('pageid'))
        self.exrest = data.get('extract')
        self.exhtml = data.get('extract_html')

        if data.get('image'):  # /page/mobile-sections-lead
            rimg = {'kind': 'rest-image'}
            rimg.update(data.get('image'))
            self.image.append(rimg)

        lastmodified = data.get('lastmodified')
        if lastmodified:
            self.modified['page'] = lastmodified

        originalimage = data.get('originalimage')  # /page/summary
        if originalimage:
            rimg = {'kind': 'rest-image'}
            rimg.update(originalimage)
            if originalimage.get('source'):
                rimg.update({'url': originalimage.get('source')})
            self.image.append(rimg)

        if data.get('sections'):
            lead = data.get('sections')[0]
            self.lead = lead.get('text')

        thumbnail = data.get('thumbnail')  # /page/summary
        if thumbnail:
            rimg = {'kind': 'rest-thumb'}
            rimg.update(thumbnail)
            if thumbnail.get('source'):
                rimg.update({'url': thumbnail.get('source')})
            self.image.append(rimg)

        title = (data.get('title') or data.get('normalizedtitle'))
        if title:
            self.title = title.replace(' ', '_')

        wikibase = data.get('wikibase_item')
        if wikibase:
            self.wikibase = wikibase
            self.wikidata_url = utils.wikidata_url(wikibase)

        url = urlparse(self.cache['rest']['query'])
        self.url = "%s://%s/wiki/%s" % (url.scheme, url.netloc, self.title)
        self.url_raw = self.url + '?action=raw'

    def get_rest(self, endpoint=None, show=True, proxy=None, timeout=0):
        """
        RESTBase /page endpoints needing only {title}
        for example:
            /page/html
            /page/summary
            /page/mobile-sections-lead

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
        if not self.title:
            raise LookupError("get_rest needs a title")

        if not endpoint:
            self.endpoint = '/page/'
        else:
            parts = endpoint.split('/')
            parts = [x for x in parts if x]
            if not parts[0] == 'page':
                parts.insert(0, 'page')
            parts.append(self.title)
            self.endpoint = '/' + '/'.join(parts)

        self._get('rest', show, proxy, timeout)

        return self

# -*- coding:utf-8 -*-

"""
WPTools Wikidata module
~~~~~~~~~~~~~~~~~~~~~~~

Support for getting Wikidata.

https://www.wikidata.org/wiki/Wikidata:Data_access
"""

import collections
import re

from . import core
from . import utils


class WPToolsWikidata(core.WPTools):
    """
    WPToolsWikidata class
    """

    def __init__(self, *args, **kwargs):
        """
        Returns a WPToolsWikidata object

        Optional positional {params}:
        - [title]: <str> Mediawiki page title, file, category, etc.

        Optional keyword {params}:
        - [lang]: <str> Mediawiki language code (default='en')
        - [variant]: <str> Mediawiki language variant
        - [wikibase]: <str> Wikidata database ID (e.g. 'Q1')

        Optional keyword {flags}:
        - [silent]: <bool> do not echo page data if True
        - [skip]: <list> skip actions in this list
        - [verbose]: <bool> verbose output to stderr if True
        """
        super(WPToolsWikidata, self).__init__(*args, **kwargs)

        wikibase = kwargs.get('wikibase')
        if wikibase:
            self.params.update({'wikibase': wikibase})

    def _get_entity_prop(self, entity, prop):
        """
        returns Wikidata entity property value
        """
        variant = self.params.get('variant')
        lang = self.params.get('lang')

        if entity.get(prop):
            ent = entity[prop]
            try:
                return ent[variant or lang].get('value')
            except AttributeError:
                return ent.get('value')

    def _marshal_claims(self, query_claims):
        """
        set Wikidata properties and entities from query claims
        """
        claims = self._reduce_claims(query_claims)
        # self.data['claimq'] = query_claims
        self.data['claims'] = claims
        entities = set()

        for eid in claims:
            entities.add(eid)  # P (property)
            for val in claims[eid]:
                if utils.is_text(val) and re.match(r'^Q\d+$', val):
                    entities.add(val)  # Q (item)

        self.data['entities'] = list(entities)

    def _pop_entities(self, limit=50):
        """returns up to limit entities and pops them off the list"""
        out = self.data['entities'][:limit]
        del self.data['entities'][:limit]
        return out

    def _query(self, action, qobj):
        """
        returns wikidata query string
        """
        if action == 'labels':
            return qobj.labels(self._pop_entities())
        elif action == 'wikidata':
            return qobj.wikidata(self.params.get('title'),
                                 self.params.get('wikibase'))

    def _set_data(self, action):
        """
        capture Wikidata API response data
        """
        if action == 'labels':
            self._set_labels()

        if action == 'wikidata':
            self._set_wikidata()
            self.get_labels(show=False)

    def _set_labels(self):
        """
        set property claim labels from get_claims()
        """
        data = self._load_response('labels')
        entities = data.get('entities')

        for ent in entities:
            label = self._get_entity_prop(entities[ent], 'labels')
            self.data['labels'][ent] = label

    def _set_title(self, item):
        """
        attempt to set title from wikidata
        """
        title = None
        lang = self.params['lang']
        label = self.data['label']

        if item.get('sitelinks'):
            for link in item['sitelinks']:
                if link == "%swiki" % lang:
                    title = item['sitelinks'][link]['title']
                    self.data['title'] = title.replace(' ', '_')

        if not self.data.get('title') and label:
            self.data['title'] = label.replace(' ', '_')

        if self.data.get('title') and not self.params.get('title'):
            self.params['title'] = self.data['title']

    def _set_wikidata(self):
        """
        set attributes derived from Wikidata (action=wbentities)
        """
        self.data['labels'] = {}
        self.data['wikidata'] = {}

        data = self._load_response('wikidata')
        entities = data.get('entities')
        item = entities.get(next(iter(entities)))

        self.data['pageid'] = item.get('pageid')

        aliases = item.get('aliases')
        if aliases:
            aliases = [x['value'] for x in aliases[self.params['lang']]]
            self.data['aliases'] = aliases

        modified = item.get('modified')
        try:
            self.data['modified'].update({'wikidata': modified})
        except KeyError:
            self.data['modified'] = {'wikidata': modified}

        wikibase = item.get('id')
        if wikibase:
            self.data['wikibase'] = wikibase
            self.data['wikidata_url'] = utils.wikidata_url(wikibase)

        self.data['description'] = self._get_entity_prop(item, 'descriptions')
        self.data['label'] = self._get_entity_prop(item, 'labels')

        self._marshal_claims(item.get('claims'))
        self._set_title(item)

        image = self.data['wikidata'].get('image')
        if image:
            if 'image' not in self.data:
                self.data['image'] = []
            if not isinstance(image, list):
                image = [image]
            for img in image:
                self.data['image'].append({
                    'kind': 'wikidata-image',
                    'file': img})

    def _update_what(self):
        """
        set what this thing is! "instance of (P31)"
        """
        p31 = self.data['claims']['P31'][0]
        self.data['what'] = self.data['labels'][p31]

    def _update_wikidata(self):
        """
        set wikidata from claims and labels
        """
        claims = self.data['claims']
        self.data['wikidatl'] = {}

        for ent in claims:

            claim = []
            # P (property) label
            plabel = "%s (%s)" % (self.data['labels'][ent], ent)

            for item in claims[ent]:
                if utils.is_text(item) and re.match(r'^Q\d+$', item):
                    # Q (item) label
                    ilabel = "%s (%s)" % (self.data['labels'][item], item)
                else:
                    ilabel = item

                if len(claims[ent]) == 1:
                    claim = ilabel
                else:
                    claim.append(ilabel)

            self.data['wikidata'][plabel] = claim

    def _reduce_claims(self, query_claims):
        """
        returns claims as reduced dict {P: [Q's or values]}
            P = property
            Q = item
        """
        claims = collections.defaultdict(list)

        for claim in query_claims:

            for ent in query_claims.get(claim):

                try:
                    snak = ent.get('mainsnak').get('datavalue').get('value')
                except AttributeError:
                    claims[claim] = []

                try:
                    if snak.get('id'):
                        val = snak.get('id')
                    elif snak.get('text'):
                        val = snak.get('text')
                    elif snak.get('time'):
                        val = snak.get('time')
                    else:
                        val = snak
                except AttributeError:
                    val = snak

                if not val or not [x for x in val if x]:
                    raise ValueError("%s %s" % (claim, ent))

                claims[claim].append(val)

        return dict(claims)

    def get_labels(self, show=True, proxy=None, timeout=0):
        """
        GET Wikidata:API (action=wbgetentities) for claims labels
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

        Required {data}: entities
            e.g. entities: [u'P31', u'Q5']

        Data captured:
            labels: {'P17': 'country'}
            wikidata: {'country (P17)': 'Chile (Q298)'}

        Use wikidata.get_wikidata() to populate data['entities']
        """
        if 'entities' not in self.data:
            print("No entities found.")
            return

        while self.data['entities']:
            self._get('labels', False, proxy, timeout)

        del self.data['entities']
        self._update_wikidata()
        self._update_what()

        return self

    def get_wikidata(self, show=True, proxy=None, timeout=0):
        """
        GET Wikidata:API (action=wbgetentities) wikidata
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

        Required {params}: title OR wikibase
        - title: <str> Mediawiki page title, file, category, etc.
        - wikibase: <str> Wikidata item ID

        Optional {params}:
        - [lang]: <str> Mediawiki language code (default='en')
        - [variant]: <str> Mediawiki language variant

        Optional arguments:
        - [show]: <bool> echo page data if true
        - [proxy]: <str> use this HTTP proxy
        - [timeout]: <int> timeout in seconds (0=wait forever)

        Data captured:
        - aliases: <list> list of "also known as"
        - claims: <dict> Wikidata claims (see get_labels())
        - description: <str> Wikidata description
        - image: <dict> {wikidata-image} Wikidata Property:P18
        - label: <str> Wikidata label
        - modified (wikidata): <str> ISO8601 date and time
        - pageid: <int> Wikipedia database ID
        - properties: <dict> Wikidata properties
        - title: <str> article title
        - what: <str> Wikidata Property:P31 "instance of"
        - wikibase: <str> Wikidata item ID
        - wikidata: <dict> resolved Wikidata properties
        - wikidata_url: <str> Wikidata URL
        """
        title = self.params.get('title')
        wikibase = self.params.get('wikibase')

        if not wikibase and not title:
            err = "get_wikidata needs wikibase or title"
            raise LookupError(err)

        self._get('wikidata', show, proxy, timeout)

        return self

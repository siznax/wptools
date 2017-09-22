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

    # user-defined property labels
    LABELS = {'P17': 'country',
              'P18': 'image',
              'P27': 'citizenship',
              'P30': 'continent',
              'P31': 'instance',
              'P50': 'author',
              'P57': 'director',
              'P86': 'composer',
              'P105': 'taxon rank',
              'P110': 'illustrator',
              'P123': 'publisher',
              'P135': 'movement',
              'P136': 'genre',
              'P144': 'based on',
              'P161': 'cast',
              'P170': 'creator',
              'P171': 'parent taxon',
              'P175': 'performer',
              'P186': 'material',
              'P195': 'collection',
              'P212': 'ISBN',
              'P225': 'taxon name',
              'P301': 'topic',
              'P345': 'IMDB',
              'P217': 'inventory',
              'P276': 'location',
              'P279': 'subclass',
              'P569': 'birth',
              'P570': 'death',
              'P577': 'pubdate',
              'P585': 'datetime',
              'P625': 'coordinates',
              'P655': 'translator',
              'P658': 'tracklist',
              'P800': 'work',
              'P856': 'website',
              'P910': 'category',
              'P1773': 'attribution',
              'P1779': 'creator'}

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
        properties = self._wikidata_props(query_claims)
        self.data['properties'] = properties
        self.data['claims'] = {}

        for propid in properties:
            label = self.LABELS[propid]
            for val in properties[propid]:
                if utils.is_text(val) and re.match(r'^Q\d+', val):
                    self.data['claims'][val] = label
                else:
                    self._update_wikidata(label, val)

    def _query(self, action, qobj):
        """
        returns wikidata query string
        """
        if action == 'claims':
            return qobj.claims(self.data['claims'].keys())
        elif action == 'wikidata':
            return qobj.wikidata(self.params.get('title'),
                                 self.params.get('wikibase'))

    def _set_data(self, action):
        """
        capture Wikidata API response data
        """
        if action == 'claims':
            self._set_claims_data()

        if action == 'wikidata':
            self._set_wikidata()

            if self.data.get('claims'):
                self.get_claims(show=False)

    def _set_claims_data(self):
        """
        set property claim labels from get_claims()
        """
        data = self._load_response('claims')
        entities = data.get('entities')
        for item in entities:
            attr = self.data['claims'][item]
            value = self._get_entity_prop(entities[item], 'labels')
            self._update_wikidata(attr, value)

        self.data['what'] = self.data['wikidata'].get('instance')

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

    def _update_wikidata(self, label, value):
        """
        add or update Wikidata
        """
        if self.data['wikidata'].get(label):
            try:
                self.data['wikidata'][label].append(value)
            except AttributeError:
                first = self.data['wikidata'].get(label)
                self.data['wikidata'][label] = [first]
                self.data['wikidata'][label].append(value)
        else:
            self.data['wikidata'][label] = value

    def _wikidata_props(self, query_claims):
        """
        returns dict containing selected properties from Wikidata query claims
        """
        props = collections.defaultdict(list)
        for claim in query_claims:
            for prop in query_claims.get(claim):
                try:
                    snak = prop.get('mainsnak').get('datavalue').get('value')
                except AttributeError:
                    if self.LABELS.get(claim):
                        props[claim] = []
                        continue
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
                    raise ValueError("%s %s" % (claim, prop))

                if self.LABELS.get(claim):
                    props[claim].append(val)

        return dict(props)

    def get_claims(self, show=True, proxy=None, timeout=0):
        """
        GET Wikidata:API (action=wbgetentities) claims labels
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

        Required {data}: claims
        e.g. claims: {'Q298': 'country'}

        Data captured:
        e.g. wikidata: {'country': 'Chile'}

        Use wikidata.get_wikidata() to populate data['claims']
        """
        if not self.data['claims']:
            raise LookupError("get_claims needs claims")

        self._get('claims', show, proxy, timeout)

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
        - claims: <dict> Wikidata claims (see get_claims())
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

    def update_labels(self, labels):
        """
        Update wikidata property labels to capture
        """
        self.LABELS.update(labels)

# -*- coding:utf-8 -*-

"""
WPTools Wikidata module
~~~~~~~~~~~~~~~~~~~~~~~

Support for Wikidata metadata.
"""

from . import core

class WPToolsWikidata(object):

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
        """
        self.claims = None
        self.properties = None

    def __get_entity_prop(self, entity, prop):
        """
        returns Wikidata entity property value
        """
        if entity.get(prop):
            ent = entity[prop]
            try:
                return ent[self.variant or self.lang].get('value')
            except AttributeError:
                return ent.get('value')

    def __set_title_wikidata(self, item):
        """
        attempt to set title from wikidata
        """
        if item.get('sitelinks'):
            for link in item['sitelinks']:
                if link == "%swiki" % self.lang:
                    title = item['sitelinks'][link]['title']
                    self.title = title.replace(' ', '_')

        if not self.title and self.label:
            self.title = self.label.replace(' ', '_')

    def _marshal_claims(self, query_claims):
        """
        set Wikidata properties and entities from query claims
        """
        self.props = self._wikidata_props(query_claims)

        for propid in self.props:
            label = self.wikiprops[propid]
            for val in self.props[propid]:
                if utils.is_text(val) and re.match(r'^Q\d+', val):
                    self.claims[val] = label
                else:
                    self._update_wikidata(label, val)

    def _query(self, action, qobj):
        """
        returns WPToolsQuery string
        """
        if action == 'claims':
            return qobj.claims(self.wikidata.claims.keys())
        elif action == 'wikidata':
            return qobj.wikidata(title, wikibase)

    def _set_claims_data(self):
        """
        set property claim labels from get_claims()
        """
        data = self._load_response('claims')
        entities = data.get('entities')
        for item in entities:
            attr = self.claims[item]
            value = self.__get_entity_prop(entities[item], 'labels')
            self._update_wikidata(attr, value)

        self.what = self.wikidata.get('instance')

    def _set_wikidata(self):
        """
        set attributes derived from Wikidata (action=wbentities)
        """
        data = self._load_response('wikidata')
        entities = data.get('entities')
        item = entities.get(next(iter(entities)))

        self.modified['wikidata'] = item.get('modified')
        self.wikibase = item.get('id')
        self.wikidata_url = utils.wikidata_url(self.wikibase)

        self.description = self.__get_entity_prop(item, 'descriptions')
        self.label = self.__get_entity_prop(item, 'labels')

        self._marshal_claims(item.get('claims'))
        self.__set_title_wikidata(item)

        image = self.wikidata.get('image')
        if image:
            if not isinstance(image, list):
                image = [image]
            for img in image:
                self.image.append({'kind': 'wikidata-image', 'file': img})

        if self.claims:
            self.get_claims(show=False)

    def _update_wikidata(self, label, value):
        """
        add or update Wikidata
        """
        if self.wikidata.get(label):
            try:
                self.wikidata[label].append(value)
            except AttributeError:
                first = self.wikidata.get(label)
                self.wikidata[label] = [first]
                self.wikidata[label].append(value)
        else:
            self.wikidata[label] = value

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
                    if self.wikiprops.get(claim):
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

                if self.wikiprops.get(claim):
                    props[claim].append(val)

        return dict(props)

    def get_claims(self, show=True, proxy=None, timeout=0):
        """
        Wikidata:API (action=wbgetentities) for labels of claims
        - e.g. {'Q298': 'country'} resolves to {'country': 'Chile'}
        - use get_wikidata() to populate claims
        """
        if not self.claims:
            raise LookupError("get_claims needs claims")

        self._get('claims', show, proxy, timeout)

        return self

    def get_wikidata(self, show=True, proxy=None, timeout=0):
        """
        Wikidata:API (action=wbgetentities) for:
        - claims: <dict> Wikidata claims (to be resolved)
        - description: <str> Wikidata description
        - image: <dict> {wikidata-image} Wikidata Property:P18
        - label: <str> Wikidata label
        - modified (wikidata): <str> ISO8601 date and time
        - props: <dict> Wikidata properties
        - what: <str> Wikidata Property:P31 "instance of"
        - wikibase: <str> Wikidata item ID
        - wikidata: <dict> resolved Wikidata properties
        - wikidata_url: <str> Wikidata URL
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
        """
        if not self.wikibase and (not self.lang and not self.title):
            raise LookupError("get_wikidata needs wikibase or lang and title")

        self._get('wikidata', show, proxy, timeout)

        return self

    def update_labels(self, labels):
        """
        Update wikidata property labels to capture
        """
        self.LABELS.update(labels)

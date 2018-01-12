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

        self.user_labels = None

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
        set Wikidata entities from query claims
        """
        claims = reduce_claims(query_claims)
        # self.data['claimq'] = query_claims
        self.data['claims'] = claims

        entities = set()
        for eid in claims:
            if self.user_labels:
                if eid in self.user_labels or eid == 'P31':
                    entities.add(eid)  # P (property)
                else:
                    continue  # get only wanted entities
            else:
                entities.add(eid)  # P (property)

            for val in claims[eid]:
                if utils.is_text(val) and re.match(r'^Q\d+$', val):
                    entities.add(val)  # Q (item)

        self.data['entities'] = list(entities)

    def _pop_entities(self, limit=50):
        """
        returns up to limit entities and pops them off the list
        """
        pop = self.data['entities'][:limit]
        del self.data['entities'][:limit]
        return pop

    def _post_labels_updates(self):
        """
        updates possible after getting labels
        """
        self._update_wikidata()
        self._update_images()
        self._update_what()

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
        set entity labels from get_labels()
        """
        data = self._load_response('labels')
        entities = data.get('entities') or []

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

        self.data['wikidata_pageid'] = item.get('pageid')

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

    def _update_images(self):
        """
        add images from Wikidata
        """
        wd_images = self.data['claims'].get('P18')  # image

        if wd_images:
            if not isinstance(wd_images, list):
                wd_images = [wd_images]

            if 'image' not in self.data:
                self.data['image'] = []

            for img_file in wd_images:
                self.data['image'].append({'file': img_file,
                                           'kind': 'wikidata-image'})

    def _update_what(self):
        """
        set what this thing is! "instance of (P31)"
        """
        if 'P31' not in self.data['claims']:  # missing Wikidata
            msg = ("Note: Wikidata item %s" % self.data['wikibase'],
                   "missing 'instance of' (P31)")
            utils.stderr(" ".join(msg))
            return

        instance_of = self.data['claims']['P31'][0]
        labels = self.data['labels']

        if instance_of in labels:
            self.data['what'] = labels[instance_of]

    def _update_wikidata(self):
        """
        set wikidata from claims and labels
        """
        claims = self.data['claims']

        for ent in claims:

            plabel = self.data['labels'].get(ent)  # P (property) label
            if plabel:
                plabel = "%s (%s)" % (plabel, ent)

            claim = []
            for item in claims[ent]:
                ilabel = item
                if utils.is_text(item) and re.match(r'^Q\d+$', item):
                    ilabel = self.data['labels'].get(item)  # Q (item) label
                    if ilabel:
                        ilabel = "%s (%s)" % (ilabel, item)

                if len(claims[ent]) == 1:
                    claim = ilabel
                else:
                    claim.append(ilabel)

            if plabel and ilabel:
                self.data['wikidata'][plabel] = claim

    def get_labels(self, show=False, proxy=None, timeout=0):
        """
        GET Wikidata:API (action=wbgetentities) for claims labels
        https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities

        Required {data}: entities, claims
            data['claims']: {'P17': ['Q17'], 'P910': ['Q8854938'], ...}
            data['entities']: ['P17', 'Q17', 'P910', 'Q8854938', ...]

        Data captured:
            labels: {'P17': 'country', 'Q17': 'Japan', ...}
            wikidata: {'country (P17)': 'Japan (Q17)', ...}

        Use get_wikidata() to populate data['entities']
        """
        if 'entities' not in self.data:
            utils.stderr("No entities found.")
            return

        skip_flag = False
        if 'skip' in self.flags and 'labels' in self.flags['skip']:
            skip_flag = True

        while 'entities' in self.data and self.data['entities']:
            if skip_flag:
                break
            self._get('labels', show, proxy, timeout)

        if 'entities' in self.data:
            del self.data['entities']

        self._post_labels_updates()

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
        - claims: <dict> intermediate Wikidata claims (compare to cache)
        - description: <str> Wikidata description
        - image: <dict> {wikidata-image} Wikidata Property:P18
        - label: <str> Wikidata label
        - labels: <str> list of resolved labels
        - modified (wikidata): <str> ISO8601 date and time
        - pageid: <int> Wikipedia database ID
        - requests: list of request actions made
        - title: <str> article title
        - what: <str> Wikidata Property:P31 "instance of"
        - wikibase: <str> Wikidata item ID
        - wikidata: <dict> resolved Wikidata claims
        - wikidata_url: <str> Wikidata URL
        """
        title = self.params.get('title')
        wikibase = self.params.get('wikibase')

        if not wikibase and not title:
            err = "get_wikidata needs wikibase or title"
            raise LookupError(err)

        self._get('wikidata', show, proxy, timeout)

        return self

    def wanted_labels(self, labels):
        """
        Specify only WANTED labels to minimize get_labels() requests

        Args:
        - labels: <list> of wanted labels.

        Example:
          page.wanted_labels(['P18', 'P31'])
        """
        if not isinstance(labels, list):
            raise ValueError("Input labels must be a list.")

        self.user_labels = labels


################################################################


def reduce_claims(query_claims):
    """
    returns claims as reduced dict {P: [Q's or values]}
        P = property
        Q = item
    """
    claims = collections.defaultdict(list)

    for claim, entities in query_claims.items():

        for ent in entities:

            try:
                snak = ent.get('mainsnak')
                snaktype = snak.get('snaktype')
                value = snak.get('datavalue').get('value')
            except AttributeError:
                claims[claim] = []

            try:
                if snaktype != 'value':
                    val = snaktype
                elif value.get('id'):
                    val = value.get('id')
                elif value.get('text'):
                    val = value.get('text')
                elif value.get('time'):
                    val = value.get('time')
                else:
                    val = value
            except AttributeError:
                val = value

            if not val or not [x for x in val if x]:
                raise ValueError("%s %s" % (claim, ent))

            claims[claim].append(val)

    return dict(claims)

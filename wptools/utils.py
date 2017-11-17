# -*- coding:utf-8 -*-

"""
WPTools Utilities module.
"""

from __future__ import print_function

import sys

import json

from collections import defaultdict
from itertools import chain

import lxml.etree
import lxml.html

from lxml.etree import tostring


def get_infobox(ptree):
    """
    returns infobox <type 'dict'> from get_parse:parsetreee
    """
    for item in lxml.etree.fromstring(ptree).xpath("//template"):
        if "box" in item.find('title').text:
            return template_to_dict(item)


def get_links(rlinks):
    """
    returns list of titles/urls from query/parse links response
    """
    if rlinks is None:
        return
    links = []
    for item in rlinks:
        if 'url' in item:
            links.append(item['url'])
        if 'title' in item and 'ns' in item:
            if item['ns'] == 0:  # articles only
                links.append(item['title'])
    return sorted(links) if links else None


def is_text(obj, name=None):
    """
    returns True if object is text-like
    """
    try:  # python2
        ans = isinstance(obj, basestring)
    except NameError:  # python3
        ans = isinstance(obj, str)
    if name:
        print("is_text: (%s) %s = %s" % (ans, name, obj.__class__),
              file=sys.stderr)
    return ans


def isfilename(name):
    """
    returns True if name looks like a Mediawiki filename
    """
    if name[0].isalnum() and name[-3:].isalpha():
        return True
    return False


def json_loads(data):
    """
    python-version safe json.loads
    """
    return json.loads(data, encoding='utf-8')


def pretty(data):
    """
    return pretty JSON
    """
    return json.dumps(data,
                      indent=4,
                      sort_keys=True,
                      separators=(',', ': '))


def stderr(msg, silent=False):
    """
    write msg to stderr if not silent
    """
    if not silent:
        print(msg, file=sys.stderr)


def template_to_dict(tree):
    """
    returns wikitext template as dict (one deep)
    """

    # https://en.wikipedia.org/wiki/Abraham_Lincoln?action=raw&section=0

    obj = defaultdict(str)
    errors = []
    for item in tree:
        try:
            name = item.findtext('name').strip()
            tmpl = item.find('value').find('template')
            if tmpl is not None:
                value = template_to_text(tmpl)
            else:
                value = text_with_children(item.find('value'))
            if name and value:
                obj[name] = value.strip()
        except AttributeError:
            if isinstance(item, lxml.etree.ElementBase):
                name = item.tag.strip()
                text = item.text.strip()
                if item.tag == 'title':
                    obj['infobox'] = text
                else:
                    obj[name] = text
        except:
            errors.append(lxml.etree.tostring(item))
    if errors:
        obj['errors'] = errors
    return dict(obj)


def text_with_children(node):
    """
    return text content with children (#62), sub-elements (#66)
    https://stackoverflow.com/questions/4624062/get-all-text-inside-a-tag-in-lxml
    """
    if sys.version.startswith('3'):  # py3 needs encoding=str
        parts = ([node.text] +
                 list(chain(
                     *([tostring(c, with_tail=False, encoding=str),
                        c.tail] for c in node.getchildren())))
                 + [node.tail])
    else:
        parts = ([node.text] +
                 list(chain(
                     *([tostring(c, with_tail=False),
                        c.tail] for c in node.getchildren())))
                 + [node.tail])
    return ''.join(filter(lambda x: x or isinstance(x, str), parts))


def template_to_text(tmpl):
    """
    convert parse tree template to text
    """
    text = []
    for item in tmpl.itertext():
        text.append(item)
    return "{{%s}}" % "|".join(text)


def wikidata_url(wikibase):
    """
    returns Wikidata URL from wikibase
    """
    if wikibase:
        return 'https://www.wikidata.org/wiki/' + wikibase

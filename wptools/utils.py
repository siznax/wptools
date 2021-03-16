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


def get_infobox(ptree, boxterm="box"):
    """
    Returns parse tree template with title containing <boxterm> as dict:

        <box> = {<name>: <value>, ...}

    If simple transform fails, attempts more general assembly:

        <box> = {'boxes': [{<title>: <parts>}, ...],
                 'count': <len(boxes)>}
    """
    boxes = []
    for item in lxml.etree.fromstring(ptree).xpath("//template"):

        title = item.find('title').text
        if title and boxterm in title:

            box = template_to_dict(item)
            if box:
                return box

            alt = template_to_dict_alt(item, title)
            if alt:
                boxes.append(alt)

    if boxes:
        return {'boxes': boxes, 'count': len(boxes)}


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


def template_to_dict(tree, debug=0, find=False):
    """
    returns wikitext template as dict

    debug = 1
        prints minimal debug info to stdout
    debug > 1
        compares _iter() versus _find() results
    find = True
        sets values from _find() algorithm (default _iter())
    """

    # you can compare (most) raw Infobox wikitext like this:
    # https://en.wikipedia.org/wiki/TITLE?action=raw&section=0

    obj = defaultdict(str)
    errors = []
    for item in tree:
        try:
            name = item.findtext('name').strip()

            if debug:
                template_to_dict_debug(name, item, debug)

            find_val = template_to_dict_find(item, debug)  # DEPRECATED
            iter_val = template_to_dict_iter(item, debug)

            value = iter_val
            if find:
                value = find_val

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


def template_to_dict_alt(tree, title):
    """
    Returns parse tree template as {<title>: <parts>}
    This is a more general parse tree infobox template parser.
    """
    box = []
    part = []

    for item in tree.iter():

        if item.tag == 'part':
            if part:
                box.append(part)
            part = []

        if item.tag == 'name' or item.tag == 'value':
            for attr in item.keys():
                part.append({attr: item.get(attr)})

            if item.text:
                part.append(item.text.strip())

            if item.tail:
                part.append(item.tail.strip())

    if part:
        box.append(part)

    return {title.strip(): box}


def template_to_dict_debug(name, item, debug):
    """
    Print debug statements to compare algorithms
    """
    if debug == 1:
        print("\n%s = " % name)
    elif debug > 1:
        print("\n%s" % name)
        print("=" * 64)
        print(lxml.etree.tostring(item))
        print()


def template_to_dict_find(item, debug=0):
    """
    DEPRECATED: Returns infobox parsetree value using etree.find()

    Older template_to_dict() algorithm, uses etree.xpath() to "lookup"
    or find specific elements, but fails to include tail text in the
    order it is found, and does not _exclude_ <ext> tags (references,
    etc.). Compare to template_to_dict_iter().
    """
    if debug > 1:
        print("template_to_dict_find:")

    tmpl = item.find('value').find('template')

    if tmpl is not None:
        value = template_to_text(tmpl, debug)
    else:
        value = text_with_children(item.find('value'), debug)

    if debug:
        print("  find: %s" % value)

    return value


def template_to_dict_iter(item, debug=0):
    """
    Returns infobox parsetree value using etree.iter()

    Preferred template_to_dict() algorithm, uses etree.iter() to
    iterate over elements, accumulating tail text in order, but not
    preserving `<ext>` tags (references, etc.). The advantage is that
    it picks up MORE templates and links that may be mixed in with
    `<ext>` tags, and keeps the result focused on the data. Compare to
    template_to_dict_find().
    """
    valarr = []
    found_template = False

    if debug > 1:
        print("template_to_dict_iter:")

    for elm in item.iter():

        if debug > 1:
            template_to_dict_iter_debug(elm)

        if elm.tag == 'value' and not found_template:
            valarr.append(elm.text.strip())

        if elm.tag == 'template':
            found_template = True
            valarr.append(template_to_text(elm, debug).strip())

        if elm.tail:
            valarr.append(elm.tail.strip())

    value = " ".join([x for x in valarr if x])

    if debug:
        print("  iter: %s" % value)

    return value


def template_to_dict_iter_debug(elm):
    """
    Print expanded element on stdout for debugging
    """
    if elm.text is not None:
        print("    <%s>%s</%s>" % (elm.tag, elm.text, elm.tag), end='')
        if elm.tail is not None:
            print(elm.tail)
        else:
            print()
    else:
        if elm.tail is not None:
            print("    <%s>%s" % (elm.tag, elm.tail))
        else:
            print("    <%s>" % elm.tag)


def template_to_text(tmpl, debug=0):
    """
    convert parse tree template to text
    """
    tarr = []
    for item in tmpl.itertext():
        tarr.append(item)

    text = "{{%s}}" % "|".join(tarr).strip()

    if debug > 1:
        print("+ template_to_text:")
        print("  %s" % text)

    return text


def text_with_children(node, debug=0):
    """
    DEPRECATED: return text content with children (#62), sub-elements (#66)

    Only used by deprecated template_to_dict_find(), and suffers from
    copypasta code smell.
    """

    # https://stackoverflow.com/questions/4624062/get-all-text-inside-a-tag-in-lxml

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

    value = ''.join(filter(lambda x: x or isinstance(x, str), parts)).strip()

    if debug > 1:
        print("+ text_with_children:")
        print("  %s" % value)

    return value


def wikidata_url(wikibase):
    """
    returns Wikidata URL from wikibase
    """
    if wikibase:
        return 'https://www.wikidata.org/wiki/' + wikibase

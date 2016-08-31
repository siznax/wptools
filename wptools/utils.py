# -*- coding:utf-8 -*-

"""
WPTools Utilities module.
"""

from __future__ import print_function

import hashlib
import json
import lxml.etree
import lxml.html
import re
import sys
import urllib

from collections import defaultdict


def media_url(fname, namespace='commons',
              wiki='https://upload.wikimedia.org/wikipedia'):
    """
    return Wikimedia File/Image URL from name
    """
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    try:
        digest = hashlib.md5(name).hexdigest()
        path = "/".join([digest[:1], digest[:2], name])
    except UnicodeEncodeError:
        name = name.encode('utf-8')
        digest = hashlib.md5(name).hexdigest()
        path = urllib.quote("/".join([digest[:1], digest[:2], name]))
    return "/".join([wiki, namespace, path])


def pretty(data):
    """
    return pretty JSON
    """
    return json.dumps(data,
                      indent=4,
                      sort_keys=True,
                      separators=(',', ': '))


def snip_html(text, verbose=0):
    """
    removed unwanted elements from HTML

    e.g. class=metadata, class=noexcerpt, class=reference

    verbose
        0 = silent
        1 = show replacements (stderr)
        2 = inspect descendants (stderr)
    """

    if type(text) is str:
        text = text.decode('utf-8')

    def _inspect(elem, sub=False):
        if verbose > 1:
            print("\n", file=sys.stderr)
            if sub:
                print("+ %s" % lxml.html.tostring(elem), file=sys.stderr)
            else:
                print("%s" % lxml.html.tostring(elem), file=sys.stderr)
            print("  class: %s" % elem.get('class'), file=sys.stderr)
            print("  href: %s" % elem.get('href'), file=sys.stderr)
            print("  id: %s" % elem.get('id'), file=sys.stderr)
            print("  tag: %s" % elem.tag, file=sys.stderr)
            print("  tail: %s" % elem.tail, file=sys.stderr)
            print("  text: %s" % elem.text, file=sys.stderr)

    def _note(old, new):
        old = lxml.html.tostring(old).strip()
        new = lxml.html.tostring(new).strip()
        if verbose > 0:
            print("\n%s REPLACING: %s WITH: %s"
                  % (snip_html.__name__, old, new),
                  file=sys.stderr)

    def _span(note, text):
        span = lxml.html.fromstring("<span %s>" % note)
        span.tail = text
        return span

    def _exclude(_class):
        return ('metadata' in _class
                or 'noexcerpt' in _class
                or 'noprint' in _class
                or 'reference' in _class)

    keep = lxml.html.Element("span")
    for elem in lxml.html.fromstring(text):
        _inspect(elem)

        # ignore selected elements entirely, keeping tail
        elem_class = elem.get('class')
        if elem_class:
            if _exclude(elem_class):
                span = _span('ignored', elem.tail or '')
                keep.append(span)
                _note(elem, span)
                continue

        # remove selected descendants, keeping tail
        for desc in elem.iterdescendants():
            _inspect(desc, True)
            desc_class = desc.get('class')
            if desc_class:
                if _exclude(desc_class):
                    elem.remove(desc)
                    span = _span('removed', desc.tail or '')
                    _note(desc, span)
                    elem.append(span)
                    break

        keep.append(elem)

    return text.split('<')[0] + lxml.html.tostring(keep)


def span_classes(frag):
    """
    returns list of <span> classes found in <frag>
    """
    cls = []
    for item in lxml.html.fromstring(frag).xpath('//span'):
        cls.append(item.get("class"))
    return [x for x in cls if x]


def span_ids(frag):
    """
    returns list of <span> id attributes found in <frag>
    """
    ids = []
    for item in lxml.html.fromstring(frag).xpath('//span'):
        ids.append(item.get("id"))
    return [x for x in ids if x]


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
                value = item.findtext('value')
            if name and value:
                obj[name] = value.strip()
        except AttributeError:
            if type(item) is lxml.etree._Element:
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


def template_to_text(tmpl):
    """
    convert parse tree template to text
    """
    text = []
    for item in tmpl.itertext():
        text.append(item)
    return "{{%s}}" % "|".join(text)

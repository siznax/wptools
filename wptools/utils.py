# -*- coding:utf-8 -*-

"""
WPTools Utilities module.
"""

from __future__ import print_function
try:  # python2
    from urllib import quote
except ImportError:  # python3
    from urllib.parse import quote


import re
import sys

import hashlib
import json

from collections import defaultdict

import lxml.etree
import lxml.html


def get_infobox(ptree):
    """
    returns infobox <type 'dict'> from get_parse:parsetreee
    """
    for item in lxml.etree.fromstring(ptree).xpath("//template"):
        if "box" in item.find('title').text:
            return template_to_dict(item)


def get_links(iwlinks):
    """
    returns list of interwiki links get_parse/iwlinks
    """
    links = []
    for item in iwlinks:
        links.append(item['url'])
    if len(links) == 1:
        return links[0]
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


def json_loads(data):
    """
    python-version safe json.loads
    """
    try:  # python2
        return json.loads(data)
    except TypeError:  # python3
        return json.loads(data.decode('utf-8'))


def media_url(fname, namespace='commons',
              wiki='https://upload.wikimedia.org/wikipedia'):
    """
    return Wikimedia File/Image URL from name
    """
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    name = re.sub(r'^(file|image):', '', fname).replace(' ', '_')

    try:
        digest = hashlib.md5(name).hexdigest()
    except (TypeError, UnicodeEncodeError):
        digest = hashlib.md5(name.encode('utf-8')).hexdigest()

    try:
        path = quote("/".join([digest[:1], digest[:2], name]))
    except KeyError:
        path = "/".join([digest[:1], digest[:2], name])

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
                or 'reference' in _class
                or 'haudio' in _class)

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
                    desc.getparent().remove(desc)
                    span = _span('removed', desc.tail or '')
                    _note(desc, span)
                    elem.append(span)
                    break

        keep.append(elem)

    leading_text = text.split('<')[0]
    keep_html = lxml.html.tostring(keep, encoding='unicode')

    return leading_text + keep_html


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
                value = item.findtext('value')
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

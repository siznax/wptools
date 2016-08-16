# -*- coding:utf-8 -*-

"""
WPTools Utilities module.
"""

from __future__ import print_function

import hashlib
import lxml.etree
import lxml.html
import re
import sys


def collapse(text):
    """replace newlines with pilcrows"""
    # pilcrow '\xc2\xb6'
    text = text.strip()
    text = re.sub(r"\n{1,}", " \xc2\xb6 ", text)
    if text.strip()[-2:] == '\xc2\xb6':
        text = text.strip()[:-2]
    return text


def console(msg):
    print(msg[:72].replace("\n", ""), file=sys.stderr)


def media_url(fname, namespace='commons',
              wiki='https://upload.wikimedia.org/wikipedia'):
    """return Wikimedia File/Image URL from name"""
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    digest = hashlib.md5(name).hexdigest()
    return "/".join([wiki, namespace, digest[:1], digest[:2], name])


def prune_html(frag):
    """prune select fragments by ELEMENT"""

    def exclude(item, elem):
        """returns true if element should be excluded"""
        _class = item.get("class")
        if item.tag == "sup":
            if _class and ("reference" in _class or "noprint" in _class):
                return True
            if "note" in elem.lower():
                return True
        if 'span id="coordinates"' in elem:
            return True
        if _class and "cite-error" in _class:
            return True
        if _class and "noexcerpt" in _class:
            return True
        if _class and "hatnote" in _class:
            return True
        return False

    norefs = []
    console("-" * 72)
    console("FRAG: %s" % frag)
    for item in lxml.html.fragments_fromstring(frag):
        if type(item) is str or type(item) is unicode:
            elem = item
            console("BARE: %s" % elem)
        else:
            elem = lxml.etree.tostring(item)
            console("ELEM: %s" % elem)
            if exclude(item, elem):
                a = elem
                b = elem.split('>')[-1]
                console("___A: %s" % a)
                console("___B: %s" % b)
                elem = b
        norefs.append(elem)
    return "".join(norefs)


def prune_html_spans(frag):
    """prune select spans by XPATH"""
    root = lxml.html.fromstring(frag)
    for item in root.xpath("//span"):
        if item.get("class") and "noexcerpt" in item.get("class"):
            console("-" * 72)
            console("PRUNE_SPAN: %s" % lxml.etree.tostring(item))
            item.getparent().remove(item)
    return lxml.etree.tostring(root)


def single_space(blob):
    """replace 3 or more newlines with 2"""
    return re.sub(r"\n{3,}", "\n\n", blob)


def strip_refs(blob):
    """remove [1][2][3]:456 references from text blob"""
    out = re.sub(r"\[\d+\](:\d+)?", "", blob)
    out = out.replace("[_citation needed_]", "")
    out = out.replace("[_clarification needed_]", "")
    return out

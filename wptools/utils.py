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
import urllib


def collapse(text):
    """replace newlines with pilcrows"""
    # pilcrow '\xc2\xb6'
    text = text.strip()
    text = re.sub(r"\n{1,}", " \xc2\xb6 ", text)
    if text.strip()[-2:] == '\xc2\xb6':
        text = text.strip()[:-2]
    return text


def console(msg):  # development
    return
    print(msg[:72].replace("\n", ""), file=sys.stderr)


def keep_tags(frag):
    """keep only select tags in HTML fragment"""

    # TODO: replace with Markdown or rST or something...

    from lxml.html.clean import Cleaner
    allow = ['b', 'i', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    cleaner = Cleaner(allow_tags=allow, remove_unknown_tags=False)
    text = cleaner.clean_html(frag)
    text = text.replace("<div>", "").replace("</div>", "")
    text = re.sub(r"</?b>", "**", text)
    text = re.sub(r"</?i>", "_", text)
    text = re.sub(r"<h\d>", "\n## ", text)
    text = re.sub(r"</h\d>", "\n", text)
    return text


def media_url(fname, namespace='commons',
              wiki='https://upload.wikimedia.org/wikipedia'):
    """return Wikimedia File/Image URL from name"""
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    try:
        digest = hashlib.md5(name).hexdigest()
        path = "/".join([digest[:1], digest[:2], name])
    except UnicodeEncodeError:
        name = name.encode('utf-8')
        digest = hashlib.md5(name).hexdigest()
        path = urllib.quote("/".join([digest[:1], digest[:2], name]))
    return "/".join([wiki, namespace, path])


def inner_html(elem, xpath):
    """returns full inner HTML of xpath selected element"""
    root = lxml.html.fromstring(elem)
    i = root.xpath(xpath)[0]
    try:
        return (i.text + ''.join(map(lxml.html.tostring, i))).strip()
    except:
        return (''.join(map(lxml.html.tostring, i))).strip()


def prune(frag):
    """return HTML fragment with MediaWiki cruft removed"""
    pruned = prune_html_inner(frag)
    pruned = prune_html_spans(pruned)
    return pruned


def prune_html_inner(frag):
    """returns pruned HTML fragments inside paragraphs"""
    out = []
    for par in lxml.html.fromstring(frag).xpath("//p"):
        console("-" * 72)
        console(lxml.html.tostring(par))
        inner = inner_html(lxml.html.tostring(par), "//p")
        console(inner)
        out.append(prune_html(inner))
    if out:
        return "\n".join(out)
    return frag


def prune_html(frag):
    """prune select elements from HTML fragment"""

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
    console("~" * 72)
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
    """prune select spans from HTML fragment"""
    root = lxml.html.fromstring(frag)
    for item in root.xpath("//span"):
        if item.get("class") and "noexcerpt" in item.get("class"):
            console("." * 72)
            console("SPAN: %s" % lxml.etree.tostring(item))
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


def strip_tags(frag):
    """returns HTML fragment with tags removed"""
    html = lxml.html.fromstring(frag)
    return lxml.html.tostring(html, method="text", encoding="utf-8")

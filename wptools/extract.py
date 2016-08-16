# -*- coding:utf-8 -*-

"""
WPTools Extract module.
"""

import lxml.html
import json
import re

from . import utils
from collections import defaultdict
from lxml import etree


class WPToolsExtract:

    def __init__(self):
        pass


def html_lead(frag):
    """returns lead section from page HTML fragment"""
    lead = []
    start = False
    for item in lxml.html.fromstring(frag):
        if not start and item.tag == "p":  # skip templates
            start = True
        if start:
            if html_lead_ignore(item):
                continue
            lead.append(etree.tostring(item))
    if not lead:
        return frag
    return "\n".join(lead)


def html_lead_ignore(elem):
    """returns True if element ends lead section"""
    if elem.tag == "table":
        return True
    if elem.tag == "ul" or elem.tag == "ol":
        for item in elem.getchildren():
            if item.get('id') and "cite_note" in item.get('id'):
                return True


def img_images(data):
    """returns list of images from prop=images query"""
    data = json.loads(data)
    return data["query"]["pages"][0]


def img_infobox(data):  # EXPERIMENTAL
    """returns images from infobox (data=parsetree)"""

    ibox = qry_infobox(data)
    types = ["image", "image_map", "logo"]
    data = {"fname": None, "url": None, "key": None}

    # BREAKS on Benjamin Franklin
    # consider wikitextinstead of parsetree... ?

    for item in types:
        if item in ibox and ibox[item]:
            data["key"] = item
            data["fname"] = ibox[item]
            data["source"] = utils.media_url(ibox[item])
            break
    return data


def img_pageimages(data):
    """returns images from pageimages query"""
    data = json.loads(data)
    data = data["query"]["pages"][0]
    if "pageimage" in data:
        data["source"] = utils.media_url(data["pageimage"])
    return data


def plain_text_cleanup(blob):
    """remove known extraneous items"""
    blob = re.sub(r'\s\( listen\)', "", blob, flags=re.UNICODE)
    tmp = []
    for line in blob.split("\n"):
        if not line.startswith("Cite error"):
            tmp.append(line)
    blob = "\n".join(tmp)
    return blob


def qry_html(data, lead=False):
    """returns HTML from MediaWiki query"""
    try:
        data = json.loads(data)
        doc = data["parse"]["text"]["*"]
        if lead:
            return html_lead(doc)
        return doc
    except:
        return json.dumps(data)


def qry_images(data, source):
    """returns images from selected source"""
    if source == "images":
        return img_images(data)
    if source == "pageimages":
        return img_pageimages(data)
    if source == "infobox":
        return img_infobox(data)


def qry_infobox(data):
    """returns infobox from parsetree"""
    ptree = qry_parsetree(data)
    try:
        for item in etree.fromstring(ptree).xpath("//template"):
            if "box" in item.find('title').text:
                return template_to_dict(item)
    except:
        return ptree


def qry_lead(data, text=False, compact=False):
    """returns (pruned) lead section from MediaWiki HTML query"""
    try:
         if text:
             return qry_text(data, True, compact)
         doc = json.loads(data)["parse"]["text"]["*"]
         html = html_lead(doc)
         return utils.prune(html)
    except:
        return data


def qry_parsetree(data):
    """return parsetree XML from API JSON"""
    try:
        data = json.loads(data)
        ptree = data["parse"]["parsetree"]["*"]
        return ptree
    except:
        return data


def qry_text(data, lead=False, compact=False):
    """returns plain text of article from HTML"""
    doc = qry_html(data, lead)
    doc = utils.keep_tags(doc)
    doc = utils.strip_refs(doc)
    doc = utils.single_space(doc)
    doc = plain_text_cleanup(doc)
    if compact:
        doc = utils.collapse(doc)
    return doc


def qry_wikitext(data):
    """return wikitext from wikitext query"""
    try:
        return json.loads(data)["parse"]["wikitext"]["*"]
    except:
        return data


def template_to_dict(tree):
    """returns wikitext template as dict (one deep)"""
    obj = defaultdict(str)
    for item in tree:
        try:
            name = item.findtext('name')
            tmpl = item.find('value').find('template')
            if tmpl is not None:
                value = etree.tostring(tmpl)
            else:
                value = item.findtext('value')
            if name and value:
                obj[name.strip()] = value.strip()
        except:
            obj["%s ERROR" % __name__] = etree.tostring(item)
    return dict(obj)

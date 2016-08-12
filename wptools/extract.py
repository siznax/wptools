# -*- coding:utf-8 -*-

"""
WPTools Extract module.
"""

import lxml.html
import json
import re

from . import fetch
from . import utils
from collections import defaultdict
from lxml import etree


class WPToolsExtract:

    def __init__(self):
        pass


def disambig(source, data, title):
    """return DISAMBIGUATION if found"""
    if source == 'html':
        for item in lxml.html.fromstring(data).xpath("//p[1]"):
            if "may refer to:" in etree.tostring(item):
                return "DISAMBIGUATION " + title
    if source == 'parsetree':
        for item in etree.fromstring(data).xpath("//text()"):
            if 'may refer to:' in item:
                return "DISAMBIGUATION " + title


def disambig_ptree(data):
    data = json.loads(data)
    ptree = data["parse"]["parsetree"]["*"].encode('utf-8')
    title = data["parse"]["title"].encode('utf-8')
    return disambig('parsetree', ptree, title)


def handle_redirect(red, lead):
    title = red.split("REDIRECT")[-1].strip()
    doc = qry_html(fetch.get_html(title, lead))
    try:
        return doc.decode('utf-8')
    except:
        return doc


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


def html_keep_tags(frag):
    """strip tags, except replace <b> and <i> with markdown"""
    from lxml.html.clean import Cleaner
    cleaner = Cleaner(allow_tags=['b', 'i'], remove_unknown_tags=False)
    text = cleaner.clean_html(frag)
    text = text.replace("<div>", "").replace("</div>", "")
    text = re.sub(r"</?b>", "**", text)
    text = re.sub(r"</?i>", "_", text)
    return text


def html_strip_tags(frag):
    """returns lead HTML fragment with tags removed"""
    html = lxml.html.fromstring(frag)
    return etree.tostring(html, method="text", encoding="utf-8")


def html_text(data, lead=False, compact=False):
    """returns plain text version of HTML MediaWiki query"""
    doc = qry_html(data, lead)
    doc = html_keep_tags(doc)
    doc = utils.strip_refs(doc)
    doc = utils.single_space(doc)
    doc = plain_text_cleanup(doc)
    if compact:
        doc = utils.collapse(doc)
    try:
        return doc.encode('utf-8')
    except:
        return doc


def img_images(data):
    """returns list of images from prop=images query"""
    data = json.loads(data)
    return data["query"]["pages"][0]


def img_infobox(data):  # EXPERIMENTAL
    """returns images from infobox (data=parsetree)"""

    dis = disambig_ptree(data)
    if dis:
        return dis

    ibox = qry_infobox(data, "dict")
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
    try:
        blob = blob.decode('utf-8')
    except:
        pass
    blob = re.sub(r'\s\( listen\)', "", blob, flags=re.UNICODE)
    tmp = []
    for line in blob.split("\n"):
        if not line.startswith("Cite error"):
            tmp.append(line)
    blob = "\n".join(tmp)
    return blob.encode('utf-8')


def qry_html(data, lead=False):
    """returns HTML part of action=parse MediaWiki query"""
    try:
        data = json.loads(data)
        doc = data["parse"]["text"]["*"]
        title = data["parse"]["title"]
    except:
        return "NOTFOUND"
    dis = disambig('html', doc, title)
    if dis:  # Misfits
        return dis
    red = redirect('html', doc)
    if red:  # Einstein
        doc = handle_redirect(red, lead)
    if lead:
        doc = html_lead(doc)
    try:
        return doc.encode('utf-8')
    except:
        return doc


def qry_images(data, source):
    """returns images from selected source"""
    if "missing" in data:
        return "NOTFOUND"
    if source == "images":
        return img_images(data)
    if source == "pageimages":
        return img_pageimages(data)
    if source == "infobox":
        return img_infobox(data)


def qry_infobox(data):
    """returns infobox from parsetree"""
    ptree = qry_parsetree(data)
    for item in etree.fromstring(ptree).xpath("//template"):
        if "box" in item.find('title').text:
            return template_to_dict(item)


def qry_parsetree(data):
    """return parsetree XML from API JSON"""
    try:
        data = json.loads(data)
        ptree = data["parse"]["parsetree"]["*"].encode('utf-8')
        title = data["parse"]["title"].encode('utf-8')
        dis = disambig('parsetree', ptree, title)
        if dis:
            return dis
        red = redirect('parsetree', ptree)
        if red:
            return red
        return ptree
    except:
        return json.loads(data)["error"]["info"].encode('utf-8')


def qry_text(data, lead=False, compact=False):
    """returns plain text of article from HTML"""
    return html_text(data, lead, compact)


def qry_wikitext(data):
    """return wikitext from API JSON"""
    text = json.loads(data)["parse"]["wikitext"]["*"].encode('utf-8')
    if text.startswith("#REDIRECT"):
        return text.split("\n")[0]
    return text


def redirect(source, data):
    """return #REDIRECT text from query if extant"""
    if source == 'html':
        xpath = "//div[@class=\"redirectMsg\"]//a"
        for item in lxml.html.fromstring(data).xpath(xpath):
            return "#REDIRECT %s" % item.text
    if source == 'parsetree':
        for item in etree.fromstring(data).xpath("//text()"):
            if item.startswith("#REDIRECT"):
                return item.strip()


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

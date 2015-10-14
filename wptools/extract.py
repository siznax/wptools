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


def disambig(source, data):
    """return DISAMBIGUATION if found"""
    if source == 'html':
        xpath = "//p[1]"
        for item in lxml.html.fromstring(data).xpath(xpath):
            if "may refer to" in etree.tostring(item):
                return "DISAMBIGUATION"
    if source == 'parsetree':
        txtnodes = etree.fromstring(data).xpath("//text()")
        for item in txtnodes:
            if 'may refer to:' in item:
                return "DISAMBIGUATION"


def html(data, lead=False):
    """returns HTML part of action=parse query"""
    try:
        doc = json.loads(data)["parse"]["text"]["*"]
    except:
        return "NOTFOUND"
    dis = disambig('html', doc)
    if dis:  # Misfits
        return dis
    red = redirect('html', doc)
    if red:  # Einstein
        return red
    if lead:
        doc = html_lead(doc)
    try:
        return doc.encode('utf-8')
    except:
        return doc


def html_lead(frag):
    """returns lead section from page HTML fragment"""
    lead = []
    for item in lxml.html.fromstring(frag).xpath("p"):
        # print(etree.tostring(item))
        lead.append(etree.tostring(item))
    return "\n".join(lead)


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
    doc = html(data, lead)
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


def infobox(data):
    """returns infobox dict from parsetree"""
    ptree = parsetree(data)
    try:
        for item in etree.fromstring(ptree).xpath("//template"):
            if "box" in item.find('title').text:
                return json.dumps(template_to_dict(item))
    except:
        return ptree


def parsetree(data):
    """return parsetree XML from API JSON"""
    ptree = json.loads(data)["parse"]["parsetree"]["*"].encode('utf-8')
    dis = disambig('parsetree', ptree)
    if dis:
        return dis
    red = redirect('parsetree', ptree)
    if red:
        return red
    return ptree


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


def plain_text_cleanup(blob):
    """remove known extraneous items"""
    try:
        blob = blob.decode('utf-8')
    except:
        pass
    blob = re.sub(r'\s\( listen\)', "", blob, flags=re.UNICODE)
    return blob.encode('utf-8')


def template_to_dict(tree):
    """returns wikitext template as dict (one deep)"""
    obj = defaultdict(str)
    for item in tree:
        name = item.find('name')
        if name is not None:
            value = item.find('value').text.strip()
            tmp = item.find('value').find('template')
            if tmp is not None:
                value = etree.tostring(tmp)
            obj[name.text.strip()] = value
    return dict(obj)


def text(data, lead=False, compact=False):
    """
    returns plain text of article from HTML
    :param lead: lead section only
    :param compact: collapse newlines into pilcrows
    """
    return html_text(data, lead, compact)


def wikitext(data):
    """return wikitext from API JSON"""
    text = json.loads(data)["parse"]["wikitext"]["*"].encode('utf-8')
    if text.startswith("#REDIRECT"):
        return text.split("\n")[0]
    return text


def wikitext_from_action_query(data):
    """DEPRECATED"""
    out = []
    try:
        for page in json.loads(data)["query"]["pages"]:
            content = page["revisions"][0]["content"].encode('utf-8')
            out.append({"title": page["title"], "content": content})
            return json.dumps(out)
    except:
        return data

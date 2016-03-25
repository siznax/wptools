# -*- coding:utf-8 -*-

"""
WPTools Utilities module.
"""

import hashlib
import html5lib
import json
import random
import re
import string
import sys


def images(wikitext):
    """
    return list of images from wikitext
    """

    def search(item):
        match = re.search(r"\[\[(.*)\]\]", item)
        if match:
            item = match.group(1)
        match = re.search(r"([^\|]*)|", item)
        if match:
            item = match.group(1)
        return media_url(item)

    images = []
    wikitext = wikitext.encode('utf-8')
    for line in wikitext.split("\n"):
        if re.search(r'image\d{0,} {0,}=', line):
            image = line.split("=")[1].strip()
            images.append(search(image))
    return images


def collapse(text):
    """replace newlines with pilcrows"""
    # pilcrow '\xc2\xb6'
    text = text.strip()
    text = re.sub(r"\n{1,}", " \xc2\xb6 ", text)
    if text.strip()[-2:] == '\xc2\xb6':
        text = text.strip()[:-2]
    return text


def media_url(fname, namespace='commons',
              wiki='https://upload.wikimedia.org/wikipedia'):
    """return Wikimedia File/Image URL from name"""
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    digest = hashlib.md5(name).hexdigest()
    return "/".join([wiki, namespace, digest[:1], digest[:2], name])


def parse_html(html):
    """returns etree from HTML"""
    return html5lib.parse(html,
                          treebuilder='lxml',
                          namespaceHTMLElements=False)


def safe_exit(output):
    """exit without breaking pipes."""
    try:
        sys.stdout.write(output)
        sys.stdout.flush()
    except IOError:
        pass


def sample_titles(fname, pop=100, num=10):
    """
    return list of random titles from file
    :param fname: flat file of titles
    :type fname: str
    :param pop: population size
    :type pop: int
    :param num: sample size
    :type num: int
    """
    titles = []
    count = 0
    sample = random.sample(xrange(pop), num)
    with open(fname) as fh:
        for item in fh:
            if count in sample:
                titles.append(item.strip())
                sample.remove(count)
            count += 1
    return titles


def sample_titles_alpha(fname):
    """return list of first alphabetical item found in sorted titles file"""
    sample = string.ascii_uppercase
    titles = []
    with open(fname) as fh:
        for item in fh:
            if item.startswith(sample[0]):
                titles.append(item.strip())
                sample = sample[1:]
                if not sample:
                    break
    return titles


def single_space(blob):
    """replace 3 or more newlines with 2"""
    return re.sub(r"\n{3,}", "\n\n", blob)


def strip_refs(blob):
    """remove [1][2][3]:456 references from text blob"""
    out = re.sub(r"\[\d+\](:\d+)?", "", blob)
    out = out.replace("[_citation needed_]", "")
    out = out.replace("[_clarification needed_]", "")
    return out


def wiki_path(title):
    title = title.replace(" ", "_")
    title = title[0].upper() + title[1:]
    return "/wiki/%s" % title.strip()


def wikitext_from_json(_json):
    """return wikitext from API JSON"""
    text = ""
    for page in json.loads(_json)["query"]["pages"]:
        text += "\n= %s =\n" % page["title"]
        text += page["revisions"][0]["content"]
    return text

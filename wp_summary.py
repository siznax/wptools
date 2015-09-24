#!/usr/bin/env python
"""
Get (pidgin) wikitext after templates and before first heading.

INPUT
    Wikipedia article title(s) (or filename)

OUTPUT
    Summary(es) as wiki-text, dict, or json

References
    https://en.wikipedia.org/wiki/Help:Summary
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import json
import os
import re
import time
import wp_query

from collections import defaultdict

DEBUG = False
DEFAULT = 'text'
FORMATS = ['dict', 'json', 'text']


def from_api(titles, _format=DEFAULT):
    """returns Summaries from api"""
    return _output(_parse(_articles(titles)), _format)


def from_file(fname, _format=DEFAULT):
    """returns Summaries from input file"""
    with open(fname) as fh:
        return _output(_parse(json.loads(fh.read())), _format)


def _output(summaries, _format):
    """returns Summaries as text, dict, or json"""
    if _format == 'dict':
        return _summaries_to_dict(summaries)
    if _format == 'json':
        return json.dumps(summaries)
    if _format == 'text':
        return _summaries_to_text(summaries)


def _summaries_to_dict(summaries):
    """return list of dicts from list of infosummaries"""
    for i, summary in enumerate(summaries):
        _dict = defaultdict(str)
        for line in summary['wikitext'].split("\n"):
            _dict['title'] = summary['title']
            _dict['wikitext'] = summary['wikitext']
            if '=' in line:
                terms = line.split('=')
                key = terms[0].replace(' ', '').replace('|', '')
                _dict[key] = terms[1].strip()
        summaries[i] = dict(_dict)
    return summaries


def _summaries_to_text(summaries):
    """return wikitext from list of infosummaries"""
    text = ""
    for summary in summaries:
        text += "\n= %s =\n\n" % summary['title']
        text += summary['wikitext'] + "\n"
    return text


def _rm_html(wikitext):
    """returns wikitext with HTML tags removed"""
    html = r'<[^>]*>'
    found = re.findall(html, wikitext)
    if DEBUG:
        if found:
            print("\n<html> to be removed:")
            for term in found:
                print("  %s" % term)
    return re.sub(html, '', wikitext)


def _rm_refs(wikitext):
    """returns wikitext with <ref> tags removed"""
    refs = r'<ref[^>]*>[^<]*</ref>'
    found = re.findall(refs, wikitext)
    if DEBUG:
        print("\n<refs> to be removed:")
        for term in found:
            print("  %s" % term)
    return re.sub(refs, '', wikitext)


def _pidgin_brackets(term):
    new = ""
    if "|" in term:
        match = term.split("|")
        new = "[" + match[-1].replace("]]", "]")
    else:
        new = term.replace("[[", "[").replace("]]", "]")
    if DEBUG:
        print("  '-> %s" % new)
    return new


def _pidgin_braces(term):
    new = ""
    if "|" in term:
        new = "{" + "|".join(term.split("|")[1:]).replace("}}", "}")
    else:
        new = term.replace("{{", "{").replace("}}", "}")
    if DEBUG:
        print("  '-> %s" % new)
    return new


def _replace_markup(term, wikitext):
    """replaces MediaWiki markup with pidgin markup"""
    new = term
    if term.startswith("{{"):
        new = _pidgin_braces(term)
    if term.startswith("[["):
        new = _pidgin_brackets(term)
    if new != term:
        wikitext = wikitext.replace(term, new)
    return wikitext


def _disposition(char, dispo, last):
    """returns the MediaWiki markup disposition of the current character"""
    tags = ["[", "]", "{", "}"]
    if char in tags:
        if not dispo:
            dispo = "open"
        if dispo == "enclosed":
            dispo = "close"
        if dispo == "close":
            if last == char:
                dispo = "close"
        if dispo == "open":
            if last == char:
                dispo = "open"
    if char not in tags:
        if dispo == "open":
            dispo = "enclosed"
        if dispo == "close":
            dispo = ""
    return dispo


def _clean_markup(wikitext):
    """returns wikitext without Mediawiki markup"""
    clean = ""
    markup = ""
    markup_found = []
    dispo = ""
    last_dispo = ""
    for i, char in enumerate(wikitext):
        char = char.encode('utf-8')
        dispo = _disposition(char, dispo, wikitext[i-1])
        if dispo:
            markup += char
            last_dispo = dispo
        else:
            if last_dispo and markup:
                markup_found.append(markup)
            markup = ""
        if markup:
            # clean += "_"
            clean += char
        else:
            clean += char
        # print("[%d] %s %s %s" % (i, char, dispo, markup))
    if DEBUG:
        print("markup to be cleaned:")
    for term in markup_found:
        if DEBUG:
            print("  %s" % term)
        clean = _replace_markup(term, clean)
    clean = re.sub(r"'+", "'", clean)
    return clean


def _clean(wikitext):
    """returns wikitext without MediaWiki markup, <ref> tags, or other HTML"""
    clean = _clean_markup(wikitext)
    clean = _rm_refs(clean)
    clean = _rm_html(clean)
    return clean.decode('utf-8')


def _summary(wikitext):
    """returns wikitext after templates and before first heading"""
    output = []
    temple = False
    braces = 0
    mark = " "
    lines = wikitext.split("\n")
    for line in lines:
        if line.startswith("="):
            break

        fence = re.search(r'^{{.*}}$', line)
        fence1 = re.search(r'^\[\[.*\]\]$', line)
        fence2 = re.search(r'^<!--.*-->$', line)

        braces += len(re.findall(r'{{', line))
        braces -= len(re.findall(r'}}', line))

        exited = False
        if braces > 0:
            temple = True
        if temple and braces == 0:
            temple = False
            exited = True

        mark = ">"
        if fence or fence1 or fence2:
            mark = "*"
        elif braces > 0:
            mark = str(braces)
        if exited:
            mark = "0"

        if mark == ">":
            output.append(line.lstrip())

        # print("[%s] %s" % (mark, line.encode('utf-8')))

    return "\n".join(output)


def _parse(api_json):
    """returns [{title, summary}, ...] from JSON"""
    summaries = []
    # print("pages: %d" % len(api_json["query"]['pages']), file=sys.stderr)
    for page in api_json["query"]["pages"]:
        wikitext = page["revisions"][0]["content"]
        summary = _clean(_summary(wikitext))
        if summary:
            summaries.append({'title': page["title"],
                              'wikitext': summary})
    return summaries


def _articles(titles):
    """returns JSON object from list of titles"""
    if isinstance(titles, str):
        titles = [titles]
    return json.loads(wp_query.data("|".join(titles)))


def _main(titles, _format):
    """emits Summaries from api or local file"""
    if os.path.exists(titles[0]):
        return from_file(titles[0], _format)
    else:
        return from_api(titles, _format)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Wikipedia article summaries given titles, format")
    argp.add_argument("titles", nargs='+',
                      help="article titles (optionally, local filename)")
    argp.add_argument("-format", choices={'text', 'json', 'clean'},
                      default='text',
                      help="output format (default=text)")
    args = argp.parse_args()

    start = time.time()
    print(_main(args.titles, args.format).encode('utf-8'))
    # print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

#!/usr/bin/env python
"""
Get plain text of article's lead section

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
import sys
import time
import wp_query

from collections import defaultdict

DEBUG = False
DEFAULT = 'text'
FORMATS = ['dict', 'json', 'text']
RELATED = []


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
    prefix = "https://en.wikipedia.org/wiki"
    for summary in summaries:
        text += "\n= %s =\n\n" % summary['title']
        text += summary['summary'] + "\n"
        if summary['related']:
            text += "\nRelated terms:\n"
            text += "\n".join(summary['related']) + "\n\n"
        text += "%s/%s\n" % (prefix, summary['title'].replace(" ", "_"))
    return re.sub(r'\n{3,}', "\n\n", text)


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
    term = term.replace("[[", "").replace("]]", "")
    terms = term.split("|")
    new = ""
    if len(terms) == 1:
        new = terms[0]
    if len(terms) > 1:
        new = terms[-1]
    article = terms[0].split("#")[0].decode('utf-8')
    RELATED.append(" * %s" % article)
    if DEBUG:
        print("    > %s" % new)
    return new


def _pidgin_braces(term):
    new = ""
    if term.lower().startswith("{{cit"):
        new = "ignored"
    else:
        term = term.replace("{{", "").replace("}}", "")
        if "|" in term:
            new = "{%s}" % "|".join(term.split("|")[1:])
        else:
            new = term
    if DEBUG:
        print("    + %s" % new)
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


def _ignores(line):
    """returns of list of matching patterns to ignore in summary lines"""
    ignore = [re.search(r'^\W+$', line),  # only non-word characters
              re.search(r'^{.*}$', line),  # begins/ends with braces
              re.search(r'^\[.*\]$', line),  # begins/ends with brackets
              re.search(r'^<!--.*-->$', line)]  # HTML comments
    return [x for x in ignore if x]


def _set_mark(ignores, braces, exited):
    """returns summary mark based on line processing status"""
    if exited or braces > 0:
        return str(braces)
    if ignores:
        return "*"
    return ">"


def _summary(wikitext):
    """returns wikitext AFTER templates and BEFORE first heading"""
    summary = []
    braces = 0
    template = False
    exited = False
    for line in wikitext.split("\n"):
        if line.startswith("="):
            break
        ignores = _ignores(line)
        braces += len(re.findall(r'{{', line))
        braces -= len(re.findall(r'}}', line))
        exited = False
        if braces > 0:
            template = True
        if template and braces == 0:
            template = False
            exited = True
        mark = _set_mark(ignores, braces, exited)
        if exited:
            exited = False
        if DEBUG:
            print("[%s] %s" % (mark, line.encode('utf-8')))
        if mark == ">":
            summary.append(line.lstrip())
    return "\n".join(summary)


def _parse(api_json):
    """returns [{title, summary}, ...] from JSON"""
    summaries = []
    if DEBUG:
        print("pages: %d" % len(api_json["query"]['pages']))
    for page in api_json["query"]["pages"]:
        wikitext = page["revisions"][0]["content"]
        summary = _clean(_summary(wikitext))
        if summary:
            summaries.append({'title': page["title"],
                              'wikitext': wikitext,
                              'related': sorted(RELATED),
                              'summary': summary})
    return summaries


def _articles(titles):
    """returns JSON object from list of titles"""
    if isinstance(titles, str):
        titles = [titles]
    return json.loads(wp_query.data("|".join(titles), lead=True))


def _main(titles, _format):
    """emits Summaries from api or local file"""
    if os.path.exists(titles[0]):
        return from_file(titles[0], _format)
    else:
        return from_api(titles, _format)


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="Plain text of article(s) lead section")
    argp.add_argument("titles", nargs='+',
                      help="article titles (or filename)")
    argp.add_argument("-f", "-format", choices={'text', 'json'},
                      default='text',
                      help="output format (default=text)")
    argp.add_argument("-d", "-debug", action='store_true',
                      help="emit debug messages")
    args = argp.parse_args()
    if args.d:
        DEBUG = True
    start = time.time()
    print(_main(args.titles, args.f).encode('utf-8'))
    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)

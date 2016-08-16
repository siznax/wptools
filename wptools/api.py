# -*- coding:utf-8 -*-

"""
wptools.api
~~~~~~~~~~~

This is the WPTools API.
"""

from . import extract
from . import fetch


def html(title,
         lead=False,
         test=False, verbose=False,
         wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article HTML"""
    data = fetch.get_html(title, lead, test, wiki, verbose)
    if test:
        return data
    return extract.qry_html(data, lead)


def images(title,
           source="pageimages",
           test=False, verbose=False,
           wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article images"""
    data = fetch.get_images(title, source,
                            lead=False, test=test,
                            wiki=wiki, verbose=verbose)
    if test:
        return data
    return extract.qry_images(data, source)


def infobox(title,
            test=False, verbose=False,
            wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article Infobox as dict"""
    data = fetch.get_parsetree(title, False, test, wiki, verbose)
    if test:
        return data
    return extract.qry_infobox(data)


def lead(title,
         plain=False, compact=False,
         test=False, verbose=False,
         wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article lead section (pruned) as HTML or plain text"""
    data = fetch.get_html(title, True, test, wiki, verbose)
    if test:
        return data
    return extract.qry_lead(data, plain, compact)


def parsetree(title,
              lead=False,
              test=False,
              wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article parse tree as XML"""
    data = fetch.get_parsetree(title, lead, test, wiki)
    if test:
        return data
    return extract.qry_parsetree(data)


def text(title,
         compact=False,
         lead=False,
         test=False, verbose=False,
         wiki=fetch.WPToolsFetch.ENDPOINT):
    """returns article as Markdown text"""
    data = fetch.get_html(title, lead, test, wiki, verbose)
    if test:
        return data
    return extract.qry_text(data, lead, compact)


def wikitext(title,
             lead=False,
             test=False,
             wiki=fetch.WPToolsFetch.ENDPOINT):
    """return article wikitext"""
    data = fetch.get_wikitext(title, lead, test, wiki)
    if test:
        return data
    return extract.qry_wikitext(data)

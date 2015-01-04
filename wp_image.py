#!/usr/bin/env python
"""
Compute Wikipedia File/Image URL from File/Image name and optionally
give HTTP status. Inspired by AzaToth's "wikimgrab.pl"
<https://commons.wikimedia.org/wiki/User:AzaToth/wikimgrab.pl>
"""

__author__ = "siznax"
__date__ = 2014

import argparse
import hashlib
import re
import requests

API = "http://upload.wikimedia.org/wikipedia"


def url(fname, namespace='commons'):
    """
    return Wikimedia File/Image URL from File/Image name
    """
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    digest = hashlib.md5(name).hexdigest()
    return "/".join([API, namespace, digest[:1], digest[:2], name])


def head(url):
    """
    return HTTP response code from candidate URL
    """
    r = requests.head(url)
    return r.status_code


if __name__ == "__main__":
    desc = "return Wikipedia File/Image URL from File/Image name."
    argp = argparse.ArgumentParser(description=(desc))
    argp.add_argument("filename")
    argp.add_argument("-ns", "--namespace",
                      help="try namespace (if not in commons)")
    argp.add_argument("-s", "--get_status", action="store_true",
                      help="get HTTP status.")
    args = argp.parse_args()

    if args.namespace:
        image = url(args.filename, args.namespace)
    else:
        image = url(args.filename)
    print image

    if args.get_status:
        print head(image)


# test cases TBD
#
# "File:Battery Park City 8952.JPG"
# "Image:Neuromancer (Book).jpg" (need -ns "en")

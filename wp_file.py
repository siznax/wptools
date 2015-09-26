#!/usr/bin/env python
"""
Get URL and HTTP status from Wikipedia File/Image name

Inspired by AzaToth's "wikimgrab.pl"
<https://commons.wikimedia.org/wiki/User:AzaToth/wikimgrab.pl>
"""

__author__ = "@siznax"
__version__ = "15 Sep 2015"

import argparse
import hashlib
import re
import requests

API = "https://upload.wikimedia.org/wikipedia"


def url(fname, namespace):
    """
    return Wikimedia File/Image URL from File/Image name
    """
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    digest = hashlib.md5(name).hexdigest()
    return "/".join([API, namespace, digest[:1], digest[:2], name])


def main(filename, namespace, check):
    img_url = url(filename, namespace)
    if check:
        print img_url,
        print requests.head(img_url).status_code
    else:
        print img_url


if __name__ == "__main__":
    desc = "URL and HTTP status from Wikipedia File/Image name."
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("filename")
    argp.add_argument("-n", "-namespace", choices={'commons', 'en'},
                      default='commons',
                      help="namespace (default=commons)")
    argp.add_argument("-c", "-check", action='store_true',
                      help="check HTTP status of computed URL")
    args = argp.parse_args()
    main(args.filename, args.n, args.c)


# test cases TBD
#
# "File:Battery Park City 8952.JPG"
# "Image:Neuromancer (Book).jpg" (need -ns "en")

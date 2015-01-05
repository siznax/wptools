#!/usr/bin/env python
"""
Compute Wikipedia File/Image URL from File/Image name and show HTTP
status. Inspired by AzaToth's "wikimgrab.pl"
<https://commons.wikimedia.org/wiki/User:AzaToth/wikimgrab.pl>
"""

__author__ = "siznax"
__date__ = 2014

import argparse
import hashlib
import re
import requests

API = "http://upload.wikimedia.org/wikipedia"


def url(fname, namespace):
    """
    return Wikimedia File/Image URL from File/Image name
    """
    name = re.sub(r'^(File|Image):', '', fname).replace(' ', '_')
    digest = hashlib.md5(name).hexdigest()
    return "/".join([API, namespace, digest[:1], digest[:2], name])


def main(args):
    img_url = url(args.filename, args.namespace)
    print img_url
    print requests.head(img_url).status_code


if __name__ == "__main__":
    desc = "URL and HTTP status from Wikipedia File/Image name."
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("filename")
    argp.add_argument("-ns", "--namespace", default='commons',
                      help="namespace (default=commons)")
    main(argp.parse_args())


# test cases TBD
#
# "File:Battery Park City 8952.JPG"
# "Image:Neuromancer (Book).jpg" (need -ns "en")

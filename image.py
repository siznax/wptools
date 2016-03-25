#!/usr/bin/env python
"""
Query MediaWiki API for main article image

Here, we look in the infobox instead of the API query "prop=images"
because we want to find the image that is most relevant.

References
    https://www.mediawiki.org/wiki/API:Images
    https://www.mediawiki.org/wiki/API:Main_page
"""

from __future__ import print_function

import argparse
import json
import os
import sys
import time
import wptools


def main(title, api, test, verbose, wiki):
    start = time.time()
    ptree = wptools.get_parsetree(title, lead=False,
                                  test=test, wiki=wiki,
                                  verbose=verbose)
    if test:
        print(ptree)
        sys.exit(os.EX_OK)

    ibox = wptools.infobox(ptree, "dict")
    types = ["image", "image_map", "logo"]
    image = {"fname": None, "url": None, "key": None}

    # AWWW... this breaks on Benjamin Franklin, consider wikitext
    # instead of parsetree?

    for item in types:
        if item in ibox and ibox[item]:
            image["key"] = item
            image["fname"] = ibox[item]
            image["url"] = wptools.utils.media_url(ibox[item])
            break

    if api:
        data = wptools.get_images(title, lead=False,
                                  test=test, wiki=wiki,
                                  verbose=verbose)
        print(data)
    else:
        print(json.dumps(image))

    print("%5.3f seconds" % (time.time() - start), file=sys.stderr)


if __name__ == "__main__":
    desc = "Query MediaWiki API for article image(s)"
    argp = argparse.ArgumentParser(description=desc)
    argp.add_argument("title",
                      help="article title")
    argp.add_argument("-a", "-api", action='store_true',
                      help="show images from API")
    argp.add_argument("-t", "-test", action='store_true',
                      help="show query and exit")
    argp.add_argument("-v", "-verbose", action='store_true',
                      help="HTTP status to stdout")
    argp.add_argument("-w", "-wiki",
                      default=wptools.WPToolsFetch.ENDPOINT,
                      help="wiki (%s)" % wptools.WPToolsFetch.ENDPOINT)
    args = argp.parse_args()

    main(args.title, args.a, args.t, args.v, args.w)

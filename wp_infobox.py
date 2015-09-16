#!/usr/bin/env python
"""
dump Wikipedia article Infobox text
https://en.wikipedia.org/wiki/Help:Infobox
"""

__author__ = "siznax"
__date__ = 2014

import argparse
import re
import wp_article


def infobox(wp_txt):
    """
    dump Infobox text from Mediawiki API text output
    """
    output = []
    region = False
    braces = 0
    for line in wp_txt.split("\n"):
        match = re.search(r'{{Infobox', line, flags=re.IGNORECASE)
        braces += len(re.findall(r'{{', line))
        braces -= len(re.findall(r'}}', line))
        if match:
            region = True
            line = re.sub(r'.*{{Infobox', '{{Infobox', line)
        if region:
            output.append(line.lstrip())
            if braces == 0:
                break
    return "\n".join(output)


def main(args):
    for title in args.title:
        print infobox(wp_article.dump(title))


if __name__ == "__main__":
    argp = argparse.ArgumentParser(
        description="dump Wikipedia article Infobox")
    argp.add_argument("title", nargs='+',
                      help="one or more article titles")
    args = argp.parse_args()
    main(args)


# test cases TBD
#
# Aerocar
# GitHub
# Heroku
# Stack Overflow

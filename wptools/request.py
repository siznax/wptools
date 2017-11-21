# -*- coding:utf-8 -*-

"""
WPTools Request module
~~~~~~~~~~~~~~~~~~~~~~

Makes WMF API HTTP requests.
"""

from __future__ import print_function

from io import BytesIO

import sys

import certifi
import pycurl

from . import __title__, __contact__, __version__


class WPToolsRequest(object):
    """
    WPToolsRequest class
    """

    DISABLED = False  # disable requests when testing

    info = None
    silent = False

    def __init__(self, silent=False, verbose=False, proxy=None, timeout=None):
        """
        Returns a WPToolsRequest object.

        Arguments:
        - [proxy]: <str> HTTP proxy to use
        - [silent]: <bool> silent if True
        - [timeout]: <int> connection timeout (0=wait forever)
        - [verbose]: <bool> verbose if True
        """
        self.silent = silent
        self.verbose = verbose
        self.curl_setup(proxy, timeout)

    def __del__(self):
        """
        Close HTTP request
        """
        self.cobj.close()

    def get(self, url, status):
        """
        in favor of python-requests for speed
        """

        # consistently faster than requests by 3x
        #
        # r = requests.get(url,
        #                  headers={'User-Agent': self.user_agent})
        # return r.text

        crl = self.cobj

        try:
            crl.setopt(pycurl.URL, url)
        except UnicodeEncodeError:
            crl.setopt(pycurl.URL, url.encode('utf-8'))

        if not self.silent:
            print(status, file=sys.stderr)

        if self.DISABLED:
            print("Requests DISABLED", file=sys.stderr)
        else:
            return self.curl_perform(crl)

    def curl_perform(self, crl):
        """
        performs HTTP GET and returns body of response
        """
        bfr = BytesIO()
        crl.setopt(crl.WRITEFUNCTION, bfr.write)
        crl.perform()
        info = curl_info(crl)
        if info:
            if self.verbose and not self.silent:
                for item in sorted(info):
                    print("  %s: %s" % (item, info[item]), file=sys.stderr)
            self.info = info
        body = bfr.getvalue()
        bfr.close()
        return body

    def curl_setup(self, proxy=None, timeout=0):
        """
        set curl options
        """

        crl = pycurl.Curl()
        crl.setopt(pycurl.USERAGENT, user_agent())
        crl.setopt(pycurl.FOLLOWLOCATION, True)
        crl.setopt(pycurl.CAINFO, certifi.where())

        if proxy:
            crl.setopt(pycurl.PROXY, proxy)
        if timeout:  # 0 = wait forever
            crl.setopt(pycurl.CONNECTTIMEOUT, timeout)
            crl.setopt(pycurl.TIMEOUT, timeout)
        if self.verbose and not self.silent:
            crl.setopt(pycurl.VERBOSE, True)

        self.cobj = crl


def curl_info(crl):
    """
    returns curl (response) info from Pycurl object
    """
    kbps = crl.getinfo(crl.SPEED_DOWNLOAD) / 1000.0
    url = crl.getinfo(crl.EFFECTIVE_URL)
    url = url.replace("&format=json", '').replace("&formatversion=2", '')
    return {"url": url,
            "user-agent": user_agent(),
            "content": crl.getinfo(crl.CONTENT_TYPE),
            "status": crl.getinfo(crl.RESPONSE_CODE),
            "bytes": crl.getinfo(crl.SIZE_DOWNLOAD),
            "seconds": "%5.3f" % crl.getinfo(crl.TOTAL_TIME),
            "kB/s": "%3.1f" % kbps}


def user_agent():
    """
    returns the wptools user-agent string
    """
    return "%s/%s (%s) %s" % (__title__,
                              __version__,
                              __contact__,
                              pycurl.version)

__author__ = "siznax"
__version__ = 2012
__credits__ = 'https://www.mediawiki.org/wiki/API:Main_page'

import os
import sys
import urllib
import urllib2

class wp_query:

    API="http://en.wikipedia.org/w/api.php"

    def __init__(self,title,fmt="txt"):
        '''simple Mediawiki API query'''
        self.url = "%s?"\
            "&titles=%s"\
            "&format=%s"\
            "&action=query"\
            "&prop=revisions"\
            "&rvprop=content"\
            "&redirects"\
            % (self.API,urllib.quote(title),fmt)
    
    def get(self):
        '''dump Wikipedia article'''
        user_agent = "python-urllib2/"+sys.version.split()[0]
        dl = urllib2.build_opener()
        dl.addheaders = [('User-agent', user_agent)]
        return dl.open(self.url).read()

if __name__=="__main__":
    if len(sys.argv) == 1:
        print "%s title format" % (os.path.basename(__file__))
        exit(1)
    if len(sys.argv) == 2:
        q = wp_query(sys.argv[1])
    if len(sys.argv) == 3:
        q = wp_query(sys.argv[1],sys.argv[2])
    if len(sys.argv) == 4:
        q = wp_query(sys.argv[1],sys.argv[2],sys.argv[3])
    print q.get()
    print q.url
    exit(0)

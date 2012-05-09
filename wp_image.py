#!/usr/bin/python
#
# siznax 2012
#
# https://commons.wikimedia.org/wiki/User:AzaToth/wikimgrab.pl

class wp_image:

    API="http://upload.wikimedia.org/wikipedia"

    def __init__(self):
        pass

    @staticmethod
    def url(infile='File:Battery Park City 8952.JPG',ns='commons'):
        '''return Wikimedia File/Image URL from File/Image name'''

        import re
        f = infile.replace(' ','_')
        m = re.search(r'^(File|Image):',f)
        if m:
            f = f[:m.start()] + f[m.end():]

        import hashlib
        h = hashlib.md5()
        h.update(f)
        d = h.hexdigest()

        return "%s/%s/%s/%s/%s" % (wp_image.API,ns,d[0:1],d[0:2],f)

    @staticmethod
    def head(url):
        '''return response code from HEAD of Wikimedia File/Image URL'''

        import urlparse
        u = urlparse.urlparse(url)
        print u.geturl()

        import httplib
        c = httplib.HTTPConnection(u.netloc)
        c.request("HEAD",u.path)
        r = c.getresponse()
        c.close()
        
        print r.status, r.reason

if __name__=="__main__":
    import sys,os
    if len(sys.argv) == 1:
        print "%s wp_file [namespace]" % (os.path.basename(__file__))
        exit(1)
    if len(sys.argv) == 2:
        wp_image.head(wp_image.url(sys.argv[1]))
    if len(sys.argv) == 3:
        wp_image.head(wp_image.url(sys.argv[1],sys.argv[2]))
    exit(0)

#!/usr/bin/python

# siznax 2012

class wp_query:

    # https://www.mediawiki.org/wiki/API:Main_page
    API="http://en.wikipedia.org/w/api.php"

    def __init__(self,title,fmt="txt",user_agent='wp_query/0.0'):
        '''simple Mediawiki API query'''
        import urllib
        self.url = "%s?"\
            "&titles=%s"\
            "&format=%s"\
            "&action=query"\
            "&prop=revisions"\
            "&rvprop=content"\
            "&redirect"\
            % (self.API,urllib.quote(title),fmt)
        self.user_agent = user_agent
    
    def get(self):
        '''dump Wikipedia article'''
        import urllib2
        dl = urllib2.build_opener()
        dl.addheaders = [('User-agent', self.user_agent)]
        return dl.open(self.url).read()

if __name__=="__main__":
    import sys,os
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
    exit(0)

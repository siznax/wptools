# siznax 2012

class wp_query:

    # https://www.mediawiki.org/wiki/API:Main_page
    API="http://en.wikipedia.org/w/api.php"

    def __init__(self,titles,fmt="txt"):
        '''simple Mediawiki API query'''
        import urllib
        self.url = "%s?"\
            "&titles=%s"\
            "&format=%s"\
            "&action=query"\
            "&prop=revisions"\
            "&rvprop=content"\
            "&redirect"\
            % (self.API,urllib.quote(titles),fmt)
        self.dl = self.downloader()
    
    def downloader(self,user_agent='WikipediaQuery/0.0'):
        '''setup URL opener'''
        import urllib2
        dl = urllib2.build_opener()
        dl.addheaders = [('User-agent', user_agent)]
        return dl
        
    def get(self):
        '''dump Wikipedia article'''
        return self.dl.open(self.url).read()

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            q = wp_query(sys.argv[1],sys.argv[2])
        else:
            q = wp_query(sys.argv[1])
        print q.get()
    else:
        import os
        print "%s titles format" % (os.path.basename(__file__))

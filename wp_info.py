#!/usr/bin/python

# siznax 2012

class wp_info:

    def __init__(self):
        self.info = ''

    def infobox(self,txt,DEBUG=False):
        '''leak Infobox from Mediawiki API text output'''
        infobox = False
        braces = 0
        import re
        for line in txt:
            match = re.search(r'{{Infobox',line,flags=re.IGNORECASE)
            braces += len(re.findall(r'{{',line))
            braces -= len(re.findall(r'}}',line))
            if match:
                infobox = True
                line = re.sub(r'.*{{Infobox','{{Infobox',line)
            if infobox:
                if DEBUG: print "[%d] %s" % (braces,line.lstrip())
                self.info += line.lstrip() + "\n"
                if braces == 0:
                    break

# test cases TBD
#   Aerocar
#   GitHub
#   Heroku
#   Stack Overflow 

if __name__=="__main__":
    import sys,os
    if len(sys.argv) == 1:
        print "%s title" % (os.path.basename(__file__))
        exit(1)
    if len(sys.argv) == 2:
        import wp_query
        q = wp_query.wp_query(sys.argv[1])
        i = wp_info()
        i.infobox(q.get().split("\n"))
        if not i.info:
            # try title case
            q = wp_query.wp_query(sys.argv[1].title())
            i.infobox(q.get().split("\n"))
            print i.info,
            exit(0)
        else:
            print i.info,
            exit(0)


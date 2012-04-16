#!/usr/bin/python

# siznax 2012

class wp_info:

    def __init__(self):
        pass

    @staticmethod
    def infobox(txt):
        '''extract Infobox from Mediawiki API text output'''
        # format=txt output is predictable PHP print_r() 
        start = False
        import re
        for line in txt:
            if re.search(r'{{Infobox',line):
                start = True
            if start:
                print line
                if re.search(r'}}',line) and not re.search(r'{{',line):
                    break

if __name__=="__main__":
    import sys,os
    if len(sys.argv) > 1:
        import wp_query
        q = wp_query.wp_query(sys.argv[1])
        wp_info.infobox(q.get().split("\n"))
    else:
        print "%s title" % (os.path.basename(__file__))

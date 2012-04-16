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
        ignore = 0
        import re
        for line in txt:
            if re.search(r'{{Infobox',line):
                start = True
            if start:
                print line
                if re.search(r'{{[^Infobox]',line):
                    ignore += 1
                if re.search(r'}}',line):
                    if not ignore: 
                        break
                    else:
                        ignore -= 1


if __name__=="__main__":
    import sys,os
    if len(sys.argv) == 1:
        print "%s title" % (os.path.basename(__file__))
        exit(1)
    if len(sys.argv) == 2:
        import wp_query
        q = wp_query.wp_query(sys.argv[1])
        wp_info.infobox(q.get().split("\n"))
        exit(0)

#!/usr/bin/python

# siznax 2012

class wp_info:

    def __init__(self):
        pass

    @staticmethod
    def infobox(txt,DEBUG=True):
        '''leak Infobox from Mediawiki API text output'''
        # format=txt output is predictable PHP print_r() 
        infobox = 0
        ignore = 0
        import re
        for line in txt:
            match = re.search(r'{{Infobox',line,flags=re.IGNORECASE)
            if match:
                infobox += 1
                if DEBUG: print ">>>> infobox %d" % (infobox) 
            if infobox:
                print line.lstrip()
                if re.search(r'{{',line) and not match:
                    # non-Infobox opening double-braces
                    ignore += 1
                    if DEBUG: print ">>>> ignore %d" % (ignore)
                if re.search(r'}}',line):
                    if re.search(r'{{',line):
                        # non-Infobox opening/closing double-braces
                        ignore -= 1
                        if DEBUG: print "<<<< ignore %d" % (ignore)
                    else:
                        if ignore <= 0:
                            if DEBUG: print "---- break"
                            break 
                    # non-Infobox closing double-braces
                    ignore -= 1
                    if DEBUG: print "<<<< ignore %d" % (ignore)

# test cases
# Aerocar (nested Infoboxes)
# GitHub (non-title-case redirect)
# Stack Overflow (embedded multi-line double braces)

if __name__=="__main__":
    import sys,os
    if len(sys.argv) == 1:
        print "%s title" % (os.path.basename(__file__))
        exit(1)
    if len(sys.argv) == 2:
        import wp_query
        q = wp_query.wp_query(sys.argv[1].title())
        wp_info.infobox(q.get().split("\n"))
        exit(0)

"""
parse data from huge Wikpedia XML Dump
"""

__author__ = "siznax"
__verion__ = "29 Sep 2015"


class WPParser:

    MAX_ELEM_BYTES = 1024**2
    _ebfr = ""
    _found_end = False
    _found_start = False
    _sbfr = ""
    elem = ""
    elems_found = 0
    elems_processed = 0

    def __init__(self, start="<page>", end="</page>"):
        self.start = start
        self.end = end

    def process(self, elem):
        """override this method to process elements"""
        pass

    def parse(self, chunk):
        """scan uncompressed chunk for start/end"""
        if len(self.elem) > self.MAX_ELEM_BYTES:
            print self.elem[:1024]
            raise RuntimeError("elem grew too big!")
        for char in chunk:
            self._scan(char)

    def _scan(self, char):
        if self._found_start:
            self.elem += char
            self._find_end(char)
        else:
            self._find_start(char)
        if self._found_end:
            self._found_end = False
            self.process(self.elem)
            self.elems_processed += 1
            self.elem = ""

    def _find_start(self, char):
        if len(self._sbfr) == len(self.start):
            if self._sbfr == self.start:
                if self._found_start:
                    raise RuntimeError("already found start!")
                self._found_start = True
                self.elem = self.start + "\n"
                self.elems_found += 1
                # print self._sbfr
            self._sbfr = ""
        if self._sbfr:
            self._sbfr += char
        if char == self.start[0]:
            self._sbfr = char

    def _find_end(self, char):
        if len(self._ebfr) == len(self.end):
            if self._ebfr == self.end:
                if self._found_end:
                    raise RuntimeError("already found end!")
                self._found_end = True
                self._found_start = False
                # print self._ebfr
            self._ebfr = ""
        if self._ebfr:
            self._ebfr += char
        if char == self.end[0]:
            self._ebfr = char

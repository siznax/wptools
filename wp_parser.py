"""
parse data by line (naive and reckless)
"""

__author__ = "siznax"
__verion__ = "2 Oct 2015"


class WPLineParser:

    MAX_ELEM_BYTES = 1024**2
    _found_end = False
    _found_start = False
    byte_count = 0
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
        if type(chunk) is list:
            for line in chunk:
                self._scan(line)
                self.byte_count += len(line)
        else:
            self._scan(chunk)
            self.byte_count += len(chunk)

    def _scan(self, line):
        if self._found_start:
            self.elem += line
            self._find_end(line)
        else:
            self._find_start(line)
        if self._found_end:
            self._found_end = False
            self.process(self.elem)
            self.elems_processed += 1
            self.elem = ""

    def _find_start(self, line):
        if line.strip() == self.start:
            if self._found_start:
                raise RuntimeError("already found start!")
            self._found_start = True
            self.elem = line
            self.elems_found += 1

    def _find_end(self, line):
        if line.strip() == self.end:
            if self._found_end:
                raise RuntimeError("already found end!")
            self._found_end = True
            self._found_start = False

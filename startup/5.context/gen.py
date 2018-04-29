import sys
from contextlib import contextmanager

@contextmanager
def open_file(name, method):
    f = open(name, method)
    yield f
    f.close()

with open_file(sys.argv[0], 'r') as infile:
    for line in infile:
        print(line.rstrip())

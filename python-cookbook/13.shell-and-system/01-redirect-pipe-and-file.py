#!/usr/bin/env python3

import sys, fileinput

def f1():
    with fileinput.input('/etc/passwd') as f:
        for line in f:
            print(f.filename(), f.lineno(), line, end='')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "f1":
            f1()

    else:
        print("NULL")


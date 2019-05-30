#!/usr/bin/env python3

import os, sys

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
    if len(sys.argv) > 2:
        findfile(sys.argv[1], sys.argv[2])

        raise SystemExit("done")
    else:
        print("NULL")


#!/usr/bin/env python3

import os, sys

def f1():
    sz = os.get_terminal_size()
    print("terminal size: ", sz)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "f1":
            f1()

        raise SystemExit("done")
    else:
        print("NULL")


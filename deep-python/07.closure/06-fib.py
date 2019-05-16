#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def fib(max):
    a, b = 0, 1

    while a < max:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    for n in fib(1000):
        sys.stdout.write("%s " %(n))
    print("")

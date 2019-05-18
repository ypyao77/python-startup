#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

from functools import reduce
from operator import mul

def fact1(n):
    return reduce(mul, range(1, n+1))

def fact2(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

# 使用 reduce 函数和一个匿名函数计算阶乘
if __name__ =='__main__':
    print("fact1(5): %s" %(fact1(5)))

    print("fact2(5): %s" %(fact2(5)))

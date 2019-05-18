#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
from operator import methodcaller

# 演示使用 itemgetter 排序一个元组列表
if __name__ =='__main__':
    s = 'The time has come'
    upcase = methodcaller('upper')
    print("upcase(s): %s" %(upcase(s)))

    hiphenate = methodcaller('replace', ' ', '-')
    print("hiphenate(s): %s" %(hiphenate(s)))

    print("str.upper(s): %s" %(str.upper(s)))

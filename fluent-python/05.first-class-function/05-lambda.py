#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


# 计算阶乘列表： map 和 filter 与列表推导比较
if __name__ =='__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    print("sorted(fruits, key=lambda word: word[::-1]): %s" %(sorted(fruits, key=lambda word: word[::-1])))

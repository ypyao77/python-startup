#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


def reverse(word):
    return word[::-1]
# 高阶函数
if __name__ =='__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    # 根据单词长度给一个列表排序
    print("sorted(fruits, key=len): %s" %(sorted(fruits, key=len)))

    # 根据反向拼写给一个单词列表排序
    print("reverse('testing'): %s" %(reverse('testing')))
    print("sorted(fruits, key=reverse): %s" %(sorted(fruits, key=reverse)))


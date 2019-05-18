#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

# ❶ 从 Python 3.0 起， reduce 不再是内置函数了
from functools import reduce

# ❷ 导入 add， 以免创建一个专求两数之和的函数
from operator import add


# 计算阶乘列表： map 和 filter 与列表推导比较
if __name__ =='__main__':
    # ❸ 计算 0~99 之和。
    info("reduce(add, range(100)): %s" %(reduce(add, range(100))))

    # ❹ 使用 sum 做相同的求和； 无需导入或创建求和函数
    info("sum(range(100)): %s" %(sum(range(100))))


    a = ["", 0, 1, "abc"]
    b = ["abc", 1, [1], {1}]
    c = ["", 0, [], {}]

    print("a: %s" %(a))
    print("b: %s" %(b))
    print("c: %s" %(c))

    print("any(a): %s" %(any(a)))
    print("any(b): %s" %(any(b)))
    print("any(c): %s" %(any(c)))

    print("all(a): %s" %(all(a)))
    print("all(b): %s" %(all(b)))
    print("all(c): %s" %(all(c)))

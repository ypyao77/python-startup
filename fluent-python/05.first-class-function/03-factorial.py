#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

# 计算阶乘列表： map 和 filter 与列表推导比较
if __name__ =='__main__':
    fact = factorial

    # ❶ 构建 0! 到 5! 的一个阶乘列表
    print("list(map(fact, range(6))): %s" %(list(map(fact, range(6)))))

    # ❷ 使用列表推导执行相同的操作
    print("[fact(n) for n in range(6)]: %s" %([fact(n) for n in range(6)]))

    # ❸ 使用 map 和 filter 计算直到 5! 的奇数阶乘列表
    print("list(map(factorial, filter(lambda n: n % 2, range(6)))): %s" %(list(map(factorial, filter(lambda n: n % 2, range(6))))))

    # ❹ 使用列表推导做相同的工作， 换掉 map 和 filter， 并避免了使用lambda 表达式
    print("[factorial(n) for n in range(6) if n % 2]: %s" %([factorial(n) for n in range(6) if n % 2]))


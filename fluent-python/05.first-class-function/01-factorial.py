#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

# 创建并测试一个函数， 然后读取它的 __doc__ 属性， 再检查它的类型
if __name__ =='__main__':
    info("factorial(42): %s" %(factorial(42)))

    info("type(factorial): %s" %(type(factorial)))

    # 文档
    info("factorial.__doc__: %s" %(factorial.__doc__))

    # 别名
    fact = factorial
    info("fact(5): %s" %(fact(5)))

    # 入参
    info("map(factorial, range(11)): %s" %(map(factorial, range(11))))
    info("list(map(fact, range(11))): %s" %(list(map(fact, range(11)))))

    l = range(11)
    info("map(factorial, l): %s" %(map(factorial, l)))
    info("list(map(fact, l)): %s" %(list(map(fact, l))))

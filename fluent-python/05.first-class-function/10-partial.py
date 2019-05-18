#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

from operator import mul
from functools import partial

# 使用 partial 把一个两参数函数改编成需要单参数的可调用对象
if __name__ =='__main__':
    # functools.partial 这个高阶函数用于部分应用一个函数。 部分应用
    # 是指， 基于一个函数创建一个新的可调用对象， 把原函数的某些参数固
    # 定。 使用这个函数可以把接受一个或多个参数的函数改编成需要回调的
    # API， 这样参数更少。

    # ➊ 使用 mul 创建 triple 函数， 把第一个定位参数定为 3
    triple = partial(mul, 3)

    # ➋ 测试 triple 函数
    print("triple(7): %s" %(triple(7)))

    # ➌ 在 map 中使用 triple； 在这个示例中不能使用 mul
    l = list(map(triple, range(1, 10)))
    print("l: %s" %(l))

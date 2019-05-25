#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import operator

# 计算整数 0~5 的累计异或的 3 种方式
if __name__ == "__main__":
    # ❶ 使用 for 循环和累加器变量计算聚合异或
    n = 0
    for i in range(1, 6):
        n ^= i
    print(n)

    # ❷ 使用 functools.reduce 函数， 传入匿名函数
    n = functools.reduce(lambda a, b: a^b, range(6))
    print(n)

    # ❸ 使用 functools.reduce 函数， 把 lambda 表达式换成operator.xor
    n = functools.reduce(operator.xor, range(6))
    print(n)



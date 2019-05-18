#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成第 n 个斐波纳契数， 递归方式非常耗时

import time
from clockdeco import clock

@clock
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)


if __name__=='__main__':
    print(fibonacci(6))


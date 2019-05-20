#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用缓存实现， 速度更快
import time, functools
from clockdeco import clock

# ❶ 注意， 必须像常规函数那样调用 lru_cache。 这一行中有一对括
# 号： @functools.lru_cache()。 这么做的原因是， lru_cache 可以
# 接受配置参数
@functools.lru_cache()
# ❷ 这里叠放了装饰器： @lru_cache() 应用到 @clock 返回的函数上
@clock
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)

# 这样一来， 执行时间减半了， 而且 n 的每个值只调用一次函数

# 把 @d1 和 @d2 两个装饰器按顺序应用到 f 函数上， 作用相当于 f = d1(d2(f))。

if __name__=='__main__':
    print(fibonacci(6))


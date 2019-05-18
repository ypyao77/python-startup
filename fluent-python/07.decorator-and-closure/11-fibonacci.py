#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成第 n 个斐波纳契数， 递归方式非常耗时

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

if __name__=='__main__':
    print(fibonacci(6))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def clock(func):
    # ❶ 定义内部函数 clocked， 它接受任意个定位参数
    def clocked(*args):
        t0 = time.perf_counter()

        # ❷ 这行代码可用， 是因为 clocked 的闭包中包含自由变量 func
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    
    # ❸ 返回内部函数， 取代被装饰的函数。 示例 7-16 演示了 clock 装饰器的用法
    return clocked



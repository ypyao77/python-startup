#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)


# 计算移动平均值的高阶函数
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

if __name__ == "__main__":
    avg = make_averager()

    print("avg(10): %s" %(avg(10)))
    print("avg(11): %s" %(avg(11)))
    print("avg(12): %s" %(avg(12)))

    print("avg.__code__: %s" %(avg.__code__))

    # 闭包是一种函数， 它会保留定义函数时存在的自由变量的绑定，
    # 这样调用函数时， 虽然定义作用域不可用了， 但是仍能使用那些绑定。
    # 注意， 只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中
    # 的外部变量




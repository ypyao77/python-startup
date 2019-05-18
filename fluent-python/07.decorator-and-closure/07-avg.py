#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)


# 计算移动平均值的高阶函数， 不保存所有历史值， 但有缺陷
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

if __name__ == "__main__":
    avg = make_averager()

    print("avg(10): %s" %(avg(10)))
    print("avg(11): %s" %(avg(11)))
    print("avg(12): %s" %(avg(12)))

    print("avg.__code__: %s" %(avg.__code__))

    # Python 3 引入了 nonlocal 声明。 它的作用是把变量标记为自由变量， 
    # 即使在函数中为变量赋予新值了， 也会变成自由变量。 
    # 如果为 nonlocal 声明的变量赋予新值， 闭包中保存的绑定会更新



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)


# 装饰器通常把函数替换成另一个函数
def deco(func):
    def inner():
        print("running inner()")
    
    # ❶ deco 返回 inner 函数对象
    return inner

# ❷ 使用 deco 装饰 target
@deco
def target1():
    print("running target1()")

def target2():
    print("running target2()")
target2 = deco(target2)

if __name__ == "__main__":
    # ❸ 调用被装饰的 target 其实会运行 inner
    target1()
    # ❹ 审查对象， 发现 target 现在是 inner 的引用
    print("target1: %s" %(target1))

    target2()
    print("target2: %s" %(target2))

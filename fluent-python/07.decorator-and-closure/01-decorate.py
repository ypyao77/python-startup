#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)


# 方法1
@decorate
def target1():
    print('running target1()')

# 方法2: 与方法1等价
def target2():
    print('running target2()')
target2 = decorate(target2)

if __name__ == "__main__":
    target1()

    target2()




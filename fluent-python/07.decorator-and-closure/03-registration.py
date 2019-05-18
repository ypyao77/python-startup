#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

import registration

if __name__=='__main__':
    # 函数装饰器在导入模块时立即执行， 而被装饰的
    # 函数只在明确调用时运行。 这突出了 Python 程序员所说的导入时和运
    # 行时之间的区别
    pass


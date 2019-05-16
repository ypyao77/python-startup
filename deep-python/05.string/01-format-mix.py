#!/usr/bin/env python
# -*- coding: utf-8 -*-

import humansize
import sys


if __name__ == "__main__":
    si_suffixes = humansize.SUFFIXES[1000]
    print("si_suffixes: {0}".format(si_suffixes))

    # 注意si_suffixes 是一个列表。
    # 所以{0[0]}指代 si_suffixes 的第一个元素，即'KB'。
    # 同时， {0[1]}指代该列表的第二个元素，即： 'MB'。
    # 大括号以外的内容 — 包括 1000，等号，还有空格等 — 则按原样输出。
    # 语句最后返回字符串为'1000KB = 1MB'。
    print("1000{0[0]} = 1{0[1]}".format(si_suffixes))

    #• 使用列表作为参数，并且通过下标索引来访问其元素（跟上一例类似）
    #• 使用字典作为参数，并且通过键来访问其值• 使用模块作为参数，并且通过名字来访问其变量及函数
    #• 使用类的实例作为参数，并且通过名字来访问其方法和属性
    #• 以上方法的任意组合
    print("1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}".format(sys))

    s = '''Finished files are the re‐
    sult of years of scientif‐
    ic study combined with the
    experience of years.'''
    print("s.splitlines(): {0}".format(s.splitlines()))
    print("s.lower(): {0}".format(s.lower()))
    print("s.lower().count('f'): {0}".format(s.lower().count('f')))


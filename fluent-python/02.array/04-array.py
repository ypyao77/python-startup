#!/usr/bin/env python
# -*- coding: utf-8 -*-


import array

if __name__ == "__main__":
    symbols = '$¢£¥€¤'

    # ➊ 如果生成器表达式是一个函数调用过程中的唯一参数， 那么不需要
    # 额外再用括号把它围起来。
    tpl = tuple(ord(symbol) for symbol in symbols)
    print("tpl: {0}".format(tpl))

    # ➋ array 的构造方法需要两个参数， 因此括号是必需的。 array 构造
    # 方法的第一个参数指定了数组中数字的存储方式。 2.9.1 节中有更多关
    # 于数组的详细讨论。
    arr = array.array('I', (ord(symbol) for symbol in symbols))
    print("arr: {0}".format(arr))




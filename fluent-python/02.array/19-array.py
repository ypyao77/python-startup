#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ❶ 引入 array 类型。
from array import array
from random import random

# 示例 2-20 一个浮点型数组的创建、 存入文件和从文件读取的过程
if __name__ == "__main__":
    # ❷ 利用一个可迭代对象来建立一个双精度浮点数组（类型码是 'd'） ，
    # 这里我们用的可迭代对象是一个生成器表达式。
    floats = array('d', (random() for i in range(10**7)))

    # ❸ 查看数组的最后一个元素。
    print("floats[-1]: {0}".format(floats[-1]))
    fp = open('floats.bin', 'wb')

    # ❹ 把数组存入一个二进制文件里。
    floats.tofile(fp)
    fp.close()

    # ❺ 新建一个双精度浮点空数组。
    floats2 = array('d')
    fp = open('floats.bin', 'rb')

    # ❻ 把 1000 万个浮点数从二进制文件里读取出来。
    floats2.fromfile(fp, 10**7)
    fp.close()

    # ❼ 查看新数组的最后一个元素
    print("floats[-1]: {0}".format(floats[-1]))

    # ❽ 检查两个数组的内容是不是完全一样。
    print("floats2 == floats: {0}".format(floats2 == floats))

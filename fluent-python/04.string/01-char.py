#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


if __name__ =='__main__':
    s = 'café'

    # ❶ 'café' 字符串有 4 个 Unicode 字符
    info("len(s): %s" %(len(s)))

    # ❷ 使用 UTF-8 把 str 对象编码成 bytes 对象
    b = s.encode('utf8')

    # ❸ bytes 字面量以 b 开头
    info("b: %s" %(b))

    # ❹ 字节序列 b 有 5 个字节（在 UTF-8 中， “é”的码位编码成两个字节）
    info("len(b): %s" %(len(b)))

    # ❺ 使用 UTF-8 把 bytes 对象解码成 str 对象
    info("b.decode('utf8'): %s" %(b.decode('utf8')))

    # ❶ bytes 对象可以从 str 对象使用给定的编码构建
    cafe = bytes('café', encoding='utf_8')
    info("cafe: %s" %(cafe))

    # ❷ 各个元素是 range(256) 内的整数。
    info("cafe[0]: %s" %(cafe[0]))

    # ❸ bytes 对象的切片还是 bytes 对象， 即使是只有一个字节的切片。
    info("cafe[-1]: %s" %(cafe[-1]))

    # ❹ bytearray 对象没有字面量句法， 而是以 bytearray() 和字节序列字面量参数的形式显示。
    cafe_arr = bytearray(cafe)
    info("cafe_arr: %s" %(cafe_arr))

    # ❺ bytearray 对象的切片还是 bytearray 对象
    info("cafe_arr[-1:]: %s" %(cafe_arr[-1:]))

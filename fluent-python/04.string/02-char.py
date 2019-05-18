#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
import struct

if __name__ =='__main__':
    # ❶ 结构体的格式： < 是小字节序， 3s3s 是两个 3 字节序列， HH 是两个16 位二进制整数
    fmt = '<3s3sHH'
    with open('o.gif', 'rb') as fp:
        # ❷ 使用内存中的文件内容创建一个 memoryview 对象
        img = memoryview(fp.read())

    # ❸ 然后使用它的切片再创建一个 memoryview 对象； 这里不会复制字节序列
    header = img[:10]

    # ❹ 转换成字节序列， 这只是为了显示； 这里复制了 10 字节
    info("bytes(header): %s" %(bytes(header)))

    # ❺ 拆包 memoryview 对象， 得到一个元组， 包含类型、 版本、 宽度和高度
    un = struct.unpack(fmt, header)
    info("un: %s" %(un))

    # ❻ 删除引用， 释放 memoryview 实例所占的内存
    del header
    del img

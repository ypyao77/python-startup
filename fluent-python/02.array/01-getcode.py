#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ord()函数返回一个字符的ascii值
if __name__ == "__main__":
    symbols = '$¢£¥€¤'

    # 方法1
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    print("codes: {0}".format(codes))

    # 方法2
    codes = [ord(x) for x in symbols]
    print("codes: {0}".format(codes))


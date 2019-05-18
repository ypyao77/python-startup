#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

import unicodedata, functools

# 使用 partial 构建一个便利的 Unicode 规范化函数
if __name__ =='__main__':
    nfc = functools.partial(unicodedata.normalize, 'NFC')

    s1 = 'café'
    s2 = 'cafe\u0301'
    print("s1, s2: %s, %s" %(s1, s2))

    print("s1 == s2: %s" %(s1 == s2))

    print("nfc(s1) == nfc(s2): %s" %(nfc(s1) == nfc(s2)))

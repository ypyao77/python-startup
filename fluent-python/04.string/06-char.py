#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

import unicodedata, re


# Unicode 数据库中数值字符的元数据示例（各个标号说明输出中的各列）
if __name__ =='__main__':
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

    for char in sample:
        print('U+%04x' % ord(char),                       # ➊ U+0000 格式的码位。
            char.center(6),                               # ➋ 在长度为 6 的字符串中居中显示字符
            're_dig' if re_digit.match(char) else '-',    # ➌ 如果字符匹配正则表达式 r'\d'， 显示 re_dig
            'isdig' if char.isdigit() else '-',           # ➍ 如果 char.isdigit() 返回 True， 显示 isdig
            'isnum' if char.isnumeric() else '-',         # ➎ 如果 char.isnumeric() 返回 True， 显示 isnum
            format(unicodedata.numeric(char), '5.2f'),    # ➏ 使用长度为 5、 小数点后保留 2 位的浮点数显示数值
            unicodedata.name(char),                       # ➐ Unicode 标准中字符的名称
            sep='\t')

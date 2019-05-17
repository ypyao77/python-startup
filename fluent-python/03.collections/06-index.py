#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
import re, collections

# 利用 defaultdict 实例而不是 setdefault 方法
if __name__ =='__main__':
    if len(sys.argv) > 1:
        # 创建一个从单词到其出现情况的映射
        WORD_RE = re.compile(r'\w+')

        # 把 list 构造方法作为 default_factory 来创建一个defaultdict
        index = collections.defaultdict(list)
        with open(sys.argv[1], encoding='utf-8') as fp:
            for line_no, line in enumerate(fp, 1):
                for match in WORD_RE.finditer(line):
                    word = match.group()
                    column_no = match.start()+1
                    location = (line_no, column_no)

                    # ➋ 如果 index 并没有 word 的记录， 那么 default_factory 会被调
                    # 用， 为查询不到的键创造一个值。 这个值在这里是一个空的列表， 然后
                    # 这个空列表被赋值给 index[word]， 继而被当作返回值返回， 因此.append(location) 操作总能成功
                    index[word].append(location)

        # 以字母顺序打印出结果
        for word in sorted(index, key=str.upper):
            print(word, index[word])


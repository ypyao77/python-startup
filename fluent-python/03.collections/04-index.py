#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
import re

# 这段程序从索引中获取单词出现的频率信息， 并把它们写进对应的列表里
if __name__ =='__main__':
    if len(sys.argv) > 1:
        WORD_RE = re.compile(r'\w+')
        index = {}
        with open(sys.argv[1], encoding='utf-8') as fp:
            for line_no, line in enumerate(fp, 1):
                for match in WORD_RE.finditer(line):
                    word = match.group()
                    column_no = match.start()+1
                    location = (line_no, column_no)

            # 这其实是一种很不好的实现， 这样写只是为了证明论点

            # ❶ 提取 word 出现的情况， 如果还没有它的记录， 返回 []。
            occurrences = index.get(word, [])

            # ❷ 把单词新出现的位置添加到列表的后面。
            occurrences.append(location)

            # ❸ 把新的列表放回字典中， 这又牵扯到一次查询操作。
            index[word] = occurrences
            # 以字母顺序打印出结果

        # ❹ sorted 函数的 key= 参数没有调用 str.uppper， 而是把这个方法
        # 的引用传递给 sorted 函数， 这样在排序的时候， 单词会被规范成统一格式
        for word in sorted(index, key=str.upper):
            info(word, index[word])




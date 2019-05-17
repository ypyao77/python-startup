#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
import re

# 用一行就解决了获取和更新单词的出现情况列
# 表， 当然跟示例 3-2 不一样的是， 这里用到了 dict.setdefault
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
                    # ➊ 获取单词的出现情况列表， 如果单词不存在， 把单词和一个空列表
                    # 放进映射， 然后返回这个空列表， 这样就能在不进行第二次查找的情况
                    # 下更新列表了
                    index.setdefault(word, []).append(location)

        # 以字母顺序打印出结果
        for word in sorted(index, key=str.upper):
            info(word, index[word])



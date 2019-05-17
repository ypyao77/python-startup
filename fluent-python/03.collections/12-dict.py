#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

if __name__ =='__main__':
    # 世界人口数量前10位国家的电话区号
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

    # ➊ 创建 d1 的时候， 数据元组的顺序是按照国家的人口排名来决定的。
    d1 = dict(DIAL_CODES)
    info('d1: %s' %d1.keys())

    # ➋ 创建 d2 的时候， 数据元组的顺序是按照国家的电话区号来决定的
    d2 = dict(sorted(DIAL_CODES))
    info('d2: %s' %d2.keys())

    # ➌ 创建 d3 的时候， 数据元组的顺序是按照国家名字的英文拼写来决定的
    d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
    info('d3: %s' %d3.keys())

    # ➍ 这些字典是相等的， 因为它们所包含的数据是一样的。 示例 3-18 里是上面例子的输出。
    assert(d1 == d2 and d2 == d3)

    # 往字典里添加新键可能会改变已有键的顺序


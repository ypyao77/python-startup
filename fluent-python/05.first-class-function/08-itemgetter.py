#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

from operator import itemgetter

# 演示使用 itemgetter 排序一个元组列表
if __name__ =='__main__':
    metro_data = [
                    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
                    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
                    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
                    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
                ]

    print("metro_data")
    for city in sorted(metro_data, key=itemgetter(1)):
        print("    ", city)

    print("metro_data")
    for city in sorted(metro_data, key=itemgetter(2)):
        print("    ", city)

    print("metro_data")
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print("    ", cc_name(city))


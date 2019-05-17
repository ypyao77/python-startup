#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import bisect
import random

# 示例 2-19 insort 可以保持有序序列的顺序
if __name__ == "__main__":
    SIZE=7
    random.seed(1729)
    my_list = []

    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)


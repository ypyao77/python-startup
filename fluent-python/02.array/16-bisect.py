#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        # ❶ 用特定的 bisect 函数来计算元素应该出现的位置。
        position = bisect_fn(HAYSTACK, needle)

        # ❷利用该位置来算出需要几个分隔符号。
        offset = position * ' |'

        # ❸ 把元素和其应该出现的位置打印出来。
        print(ROW_FMT.format(needle, position, offset))

# 2.8 用bisect来管理已排序的序列
if __name__ == "__main__":
    # ❹ 根据命令上最后一个参数来选用 bisect 函数。
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    # ❺ 把选定的函数在抬头打印出来。
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

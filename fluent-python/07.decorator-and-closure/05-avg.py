#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)


# 计算移动平均值的类
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


if __name__ == "__main__":
    avg = Averager()

    print("avg(10): %s" %(avg(10)))
    print("avg(11): %s" %(avg(11)))
    print("avg(12): %s" %(avg(12)))

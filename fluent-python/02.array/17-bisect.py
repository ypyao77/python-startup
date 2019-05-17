#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import bisect
import sys


def grade(score, breakpoints=[60, 70, 80, 90, 100], grades=["F", "D", "C", "B", "A", "A+"]):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


# 2-18 根据一个分数， 找到它所对应的成绩
if __name__ == "__main__":
    var = [grade(score) for score in [0, -1, 33, 99, 60, 77, 70, 89, 90, 100]]
    print(var)


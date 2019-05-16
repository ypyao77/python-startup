#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 给切片赋值
if __name__ == "__main__":
    l = list(range(10))
    print("l: {0}".format(l))

    l[2:5] = [20, 30]
    print("l: {0}".format(l))

    del l[5:7]
    print("l: {0}".format(l))

    l[3::2] = [11, 22]
    print("l: {0}".format(l))

    l[2:5] = [100]
    print("l: {0}".format(l))




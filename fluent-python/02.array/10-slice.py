#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 元祖切片
if __name__ == "__main__":
    a = (1, 2)
    b = ("a", "b")
    s = a + b

    print("s: {0}".format(s))
    print("s[2:]: {0}".format(s[2:]))

    s = 'bicycle'
    print("s: {0}".format(s))
    print("s[::-1]: {0}".format(s[::-1]))

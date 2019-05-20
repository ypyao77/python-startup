#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数可能会修改接收到的任何可变对象
def f(a, b):
    a += b
    return a


if __name__ == "__main__":
    x = 1
    y = 2
    print("x, y: {}, {}".format(x, y))

    a = [1, 2]
    b = [3, 4]
    print("f(a, b): {}".format(f(a, b)))
    print("a, b: {}, {}".format(a, b))

    t = (1, 2)
    u = (3, 4)
    print("f(t, u): {}".format(f(t, u)))
    print("t, u: {}, {}".format(t, u))

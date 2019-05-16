#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def f1():
    return (1, 'a')

def f2():
    return (1, 'a', True, [], math.pi)


if __name__ == "__main__":
    print("f1(): {0}".format(f1()))
    print("f2(): {0}".format(f2()))

    (a, b) = f1()
    print("f1(): {0} {1}".format(a, b))

    (a, b, c, d, e) = f2()
    print("f2(): {0} {1} {2} {3} {4}".format(a, b, c, d, e))

    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    print("WEDNESDAY: {0}".format(WEDNESDAY))

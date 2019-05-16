#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    a = {11, 11, 12, 12, 13, 14, 14, 14, 14}
    print("a: {0}".format(a))

    l = [1, 1, 2, 2, 3, 4, 4, 4, 4]
    b = set(l)
    print("b: {0}".format(b))

    b.update({4, 4, 6, 5, 7, 5, 6, 7})
    print("b: {0}".format(b))

    print("a.union(b): {0}".format(a.union(b)))

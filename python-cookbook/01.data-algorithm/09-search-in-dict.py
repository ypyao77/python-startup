#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）
if __name__ == "__main__":
    a = {
            'x' : 1,
            'y' : 2,
            'z' : 3
        }
    b = {
            'w' : 10,
            'x' : 11,
            'y' : 2
        }

    # Find keys in common
    print("a.keys() & b.keys(): ", a.keys() & b.keys())
    # Find keys in a that are not in b
    print("a.keys() - b.keys(): ", a.keys() - b.keys())
    # Find (key, value) pairs in common
    print("a.items() & b.items(): ", a.items() & b.items())

    c = {key:a[key] for key in a.keys() - {'z', 'w'}}
    print("c: ", c)

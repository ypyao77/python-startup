#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表排序
if __name__ == "__main__":
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print("fruits: {0}".format(fruits))

    # sorted生成新列表
    print("sorted(fruits): {0}".format(sorted(fruits)))

    print("fruits: {0}".format(fruits))

    print("sorted(fruits, reverse=True): {0}".format(sorted(fruits, reverse=True)))

    # sort()不改变列表
    fruits.sort()
    print("fruits: {0}".format(fruits))


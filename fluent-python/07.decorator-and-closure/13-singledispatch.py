#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# functools.singledispatch 是作为装饰器来使用的，他可以把整体方案拆分成多个小的模块，
# 甚至可以为你无法修改的类提供专门的函数。使用 @singledispatch 装饰的普通函
# 数会变成泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作的一组函数

from functools import singledispatch
import numbers

@singledispatch
def sort_type(obj):
    print(obj, type(obj), 'obj')

@sort_type.register(str)
def _(text):
    print(text, type(text), 'str')

@sort_type.register(numbers.Integral)
def _(n):
    print(n, type(n), 'int')


if __name__ == "__main__":
    sort_type('aaaa')
    sort_type(222222)
    sort_type(list)

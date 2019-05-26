#!/usr/bin/env python3


# 8.4 创建大量对象时节省内存方法
# 你的程序要创建大量 (可能上百万) 的对象，导致占用很大的内存。


class Date:
    # 对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存。
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day










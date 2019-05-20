#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Cheese 有个 kind 属性和标准的字符串表示形式
class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
if __name__ == "__main__":
    # ❶ stock 是 WeakValueDictionary 实例
    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

    for cheese in catalog:
        # ❷ stock 把奶酪的名称映射到 catalog 中 Cheese 实例的弱引用上
        stock[cheese.kind] = cheese

    # ❸ stock 是完整的
    print("sorted(stock.keys()): {}".format(sorted(stock.keys())))

    del catalog
    # ❹ 删除 catalog 之后， stock 中的大多数奶酪都不见了， 这是WeakValueDictionary 的预期行为。 为什么不是全部呢
    print("sorted(stock.keys()): {}".format(sorted(stock.keys())))

    del cheese
    print("sorted(stock.keys()): {}".format(sorted(stock.keys())))


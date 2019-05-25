#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 怎样实现一个键对应多个值的字典（也叫 multidict）
import heapq


if __name__ == "__main__":
    # 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
    # 就需要将这多个值放到另外的容器中，比如列表或者集合里面。比如，你可以像下面这
    # 样构造这样的字典
    d = {
        "a": [1, 2, 3],
        "b": [4, 5]
    }
    e = {
        'a' : {1, 2, 3},
        'b' : {4, 5}
    }
    print("d: ", d)
    print("e: ", e)

    # 你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
    # defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要
    # 关注添加元素操作了。
    from collections import defaultdict
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print("d: ", d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print("d: ", d)

    # 需要注意的是， defaultdict 会自动为将要访问的键（就算目前字典中并不存在
    # 这样的键）创建映射实体。如果你并不需要这样的特性，你可以在一个普通的字典上使
    # 用 setdefault() 方法来代替
    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print("d: ", d)


    # 一般来讲，创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，
    # 那么对于值的初始化可能会有点麻烦，你可能会像下面这样来实现
    pairs = [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("d", 4),
        ("e", 5),
        ("f", 6),
        ]
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)
    print("d: ", d)

    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
    print("d: ", d)



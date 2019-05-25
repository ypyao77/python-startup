#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 下面的类利用 heapq 模块实现了一个简单的优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


if __name__ == "__main__":
    class Item:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return 'Item({!r})'.format(self.name)

    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

    # 仔细观察可以发现，第一个 pop() 操作返回优先级最高的元素。另外注意到如果
    # 两个有着相同优先级的元素(foo 和 grok), pop 操作按照它们被插入到队列的顺序返回的

    # 为了阐明这些，先假定 Item 实例是不支持排序的
    a = Item('foo')
    b = Item('bar')
    try:
        print(a < b)
    except Exception as e:
        print(e)

    # 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。但是
    # 如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错
    a = (1, Item('foo'))
    b = (5, Item('bar'))
    try:
        print(a < b)
    except Exception as e:
        print(e)

    c = (1, Item('grok'))
    try:
        print(a < c)
    except Exception as e:
        print(e)

    # 通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的
    # 避免上面的错误，因为不可能有两个元素有相同的 index 值。 Python 在做元组比较时
    # 候，如果前面的比较已经可以确定结果了，后面的比较操作就不会发生了
    a = (1, 0, Item('foo'))
    b = (5, 1, Item('bar'))
    c = (1, 2, Item('grok'))
    try:
        print(a < b)
    except Exception as e:
        print(e)
    try:
        print(a < c)
    except Exception as e:
        print(e)



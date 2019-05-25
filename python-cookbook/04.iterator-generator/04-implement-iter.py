#!/usr/bin/env python3


# 4.4 实现迭代器协议
# 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。

# 目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数。在 4.2 小节中，
# 使用 Node 类来表示树形数据结构。你可能想实现一个以深度优先方式遍历树形节点的生成器。
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Python 的迭代协议要求一个 __iter__() 方法返回一个特殊的迭代器对象，这个
# 迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。但
# 是，实现这些通常会比较繁琐。下面我们演示下这种方式，如何使用一个关联迭代器类
# 重新实现 depth_first() 方法：
class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)



if __name__ == "__main__":
    print("Node()")
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print("  ", ch)

    print("Node2()")
    root = Node2(0)
    child1 = Node2(1)
    child2 = Node2(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print("  ", ch)

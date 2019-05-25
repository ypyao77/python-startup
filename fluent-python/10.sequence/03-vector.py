#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from array import array
import reprlib
import math


# 支持切片了
class Vector:
    typecode = 'd'

    def __init__(self, components):
        # ❶ self._components 是“受保护的”实例属性， 把 Vector 的分量保存在一个数组中
        self._components = array(self.typecode, components)

    def __iter__(self):
        # ❷ 为了迭代， 我们使用 self._components 构建一个迭代器
        return iter(self._components)

    def __repr__(self):
        # ❸ 使用 reprlib.repr() 函数获取 self._components 的有限长度表示形式（如 array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])）
        components = reprlib.repr(self._components)
        # ❹ 把字符串插入 Vector 的构造方法调用之前， 去掉前面的array('d' 和后面的 )
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # ❺ 直接使用 self._components 构建 bytes 对象
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # ❻ 不能使用 hypot 方法了， 因此我们先计算各分量的平方之和， 然后再使用 sqrt 方法开平方
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # ❼ 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行： 直接把 memoryview 传给构造方法， 不用像前面那样使用 * 拆包
        return cls(memv)


if __name__ == "__main__":
    print(Vector([3.1, 4.2]))
    print(Vector((3, 4, 5)))
    print(Vector(range(10)))

    v1 = Vector([3, 4, 5])
    print(v1[0], v1[-1])

    v7 = Vector(range(7))
    print(v7[1:4])


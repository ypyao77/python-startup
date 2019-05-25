#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 只在 Vector2d 类中添加了__slots__ 属性
from array import array
import math
class Vector2d:
    # 在类中定义 __slots__ 属性的目的是告诉解释器： “这个类中的所有实
    # 例属性都在这儿了！ ”这样， Python 会在各个实例中使用类似元组的结
    # 构存储实例变量， 从而避免使用消耗内存的 __dict__ 属性。 如果有数
    # 百万个实例同时活动， 这样做能节省大量内存


    # 在 10 000 000 个 Vector2d 实例中使用 __dict__ 属性时，RAM 用量高达 1.5GB；
    # 而在 Vector2d 类中定义 __slots__ 属性之后， RAM 用量降到了 655MB。

    # 在类中定义 __slots__ 属性之后， 实例不能再有__slots__ 中所列名称之外的其他属性。 这只是一个副作用， 不是
    # __slots__ 存在的真正原因。 不要使用 __slots__ 属性禁止类的用户新增实例属性。 __slots__ 是用于优化的， 不是为了约束程序员。

    # __slots__ 的问题, 有几点要注意:
    #   * 每个子类都要定义 __slots__ 属性， 因为解释器会忽略继承的__slots__ 属性。
    #   * 实例只能拥有 __slots__ 中列出的属性， 除非把 '__dict__' 加入 __slots__ 中（这样做就失去了节省内存的功效）
    #   * 如果不把 '__weakref__' 加入 __slots__， 实例就不能作为弱引用的目标
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

if __name__ == "__main__":
    # A two-dimensional vector class
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)

    x, y = v1
    print(x, y)
    print(v1)

    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)

    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))

    # Test of ``.frombytes()`` class method
    v1_clone = Vector2d.frombytes(bytes(v1))
    print(v1_clone)
    print(v1 == v1_clone)

    # Tests of ``format()`` with Cartesian coordinates
    print(format(v1))
    print(format(v1, ".2f"))
    print(format(v1, ".3e"))

    # Tests of the ``angle`` method
    print(Vector2d(0, 0).angle())
    print(Vector2d(1, 0).angle())

    epsilon = 10**-8
    print(abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon)
    print(abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon)

    # Tests of ``format()`` with polar coordinates
    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '0.5fp'))

    # Tests of `x` and `y` read-only properties:
    print(v1.x, v1.y)
    try:
        v1.x = 123
    except Exception as e:
        print(e)

    # Tests of hashing:
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))
    print(len(set([v1, v2])))


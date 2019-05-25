#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 私有属性的名称会被“改写”， 在前面加上下划线和类名
from array import array
import math
class Vector2d:
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


class A:
    _x = None

    def __init__(self, x):
        self._x = float(x)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({})'.format(class_name, self._x)


if __name__ == "__main__":
    # 名称改写是一种安全措施， 不能保证万无一失： 它的目的是避免意外访问， 不能防止故意做错事
    v1 = Vector2d(3, 4)
    print(v1.__dict__)
    print(v1._Vector2d__x)
    print(v1._Vector2d__y)

    # 只要编写 v1._Vector__x = 7 这样的代码， 就能轻松地为 Vector2d 实
    # 例的私有分量直接赋值。 如果真在生产环境中这么做了， 出问题时可别抱怨

    # 绝对不要使用两个前导下划线， 这是很烦人的自私行为。 如果担心名称冲突， 应该明确使用一种名称改写方式（如
    # _MyThing_blahblah） 。 这其实与使用双下划线一样， 不过自己定的规则比双下划线易于理解
    a = A(1)
    print(a)
    print(a._x)

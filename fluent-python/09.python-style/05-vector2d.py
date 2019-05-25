#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from array import array
import math

# 目前定义的都是特殊方法
class Vector2d:
    # ❶ typecode 是类属性， 在 Vector2d 实例和字节序列之间转换时使用。
    typecode = 'd'

    def __init__(self, x, y):
        # ❶ 使用两个前导下划线(尾部没有下划线, 或者有一个下划线), 把属性标记为私有的.
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # ❻ 需要读取 x 和 y 分量的方法可以保持不变， 通过 self.x 和 self.y
        # 读取公开特性， 而不必读取私有属性， 因此上述代码清单省略了这个类的其他代码。
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

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    # ❷ @property 装饰器把读值方法标记为特性。
    @property
    # ❸ 读值方法与公开属性同名， 都是 x
    def x(self):
        # ❹ 直接返回 self.__x
        return self.__x

    # ❺ 以同样的方式处理 y 特性
    @property
    def y(self):
        return self.__y

    # ❶ 类方法使用 classmethod 装饰器修饰
    # 我们用的 classmethod 装饰器是 Python 专用的
    @classmethod
    # ❷ 不用传入 self 参数； 相反， 要通过 cls 传入类本身
    def frombytes(cls, octets):
        # ❸ 从第一个字节中读取 typecode
        typecode = chr(octets[0])

        # ❹ 使用传入的 octets 字节序列创建一个 memoryview， 然后使用typecode 转换
        memv = memoryview(octets[1:]).cast(typecode)

        # ❺ 拆包转换后的 memoryview， 得到构造方法所需的一对参数
        return cls(*memv)


if __name__ == "__main__":
    v1 = Vector2d(3, 4)

    # ❶ Vector2d 实例的分量可以直接通过属性访问（无需调用读值方法） 。
    print(v1.x, v1.y)

    # ❷ Vector2d 实例可以拆包成变量元组。
    x, y = v1
    print(x, y)

    # ❸ repr 函数调用 Vector2d 实例， 得到的结果类似于构建实例的源码。
    print(v1)

    # ❹ 这里使用 eval 函数， 表明 repr 函数调用 Vector2d 实例得到的是对构造方法的准确表述
    v1_clone = eval(repr(v1))

    # ❺ Vector2d 实例支持使用 == 比较； 这样便于测试。
    print(v1 == v1_clone)

    # ❻ print 函数会调用 str 函数， 对 Vector2d 来说， 输出的是一个有序对。
    print(v1)

    # ❼ bytes 函数会调用 __bytes__ 方法， 生成实例的二进制表示形式。
    octets = bytes(v1)
    print(octets)

    # ❽ abs 函数会调用 __abs__ 方法， 返回 Vector2d 实例的模。
    print(abs(v1))

    # ❾ bool 函数会调用 __bool__ 方法， 如果 Vector2d 实例的模为零，返回 False， 否则返回 True。
    print(bool(v1), bool(Vector2d(0, 0)))



#!/usr/bin/env python3

# 9.8 将装饰器定义为类的一部分

# 你想在类中定义装饰器，并将其作用在其他函数或方法上。

from functools import wraps

# 在类里面定义装饰器很简单，但是你首先要确认它的使用方式。比如到底是作为一个实例方法还是类方法。
class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper



if __name__ == '__main__':
    # 下面是一使用例子
    # 仔细观察可以发现一个是实例调用，一个是类调用。

    # As an instance method
    a = A()
    @a.decorator1
    def spam():
        pass

    # As a class method
    @A.decorator2
    def grok():
        pass



#!/usr/bin/env python3

# 9.9 将装饰器定义为类

# 你想使用一个装饰器去包装函数，但是希望返回一个可调用的实例。你需要让你的装饰器可以同时工作在类定义的内部和外部。

import types
from functools import wraps

# 为了将装饰器定义成一个实例，你需要确保它实现了 __call__() 和 __get__() 方法。
# 例如，下面的代码定义了一个类，它在其他函数上放置一个简单的记录层
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

# 你可以将它当做一个普通的装饰器来使用，在类里面或外面都可以
@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)



if __name__ == '__main__':
    print("add(2, 3): ", add(2, 3))
    print("add(4, 5): ", add(4, 5))
    print("add.ncalls: ", add.ncalls)

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print("Spam.bar.ncalls: ", Spam.bar.ncalls)

    # 将装饰器定义成类通常是很简单的。但是这里还是有一些细节需要解释下，特别是当你想将它作用在实例方法上的时候。
    # 首先，使用 functools.wraps() 函数的作用跟之前还是一样，将被包装函数的元信息复制到可调用实例中去。
    # 其次，通常很容易会忽视上面的 __get__() 方法。如果你忽略它，保持其他代码不变再次运行，你会发现当你去调用被装饰实例方法时出现很奇怪的问题。
    # 出错原因是当方法函数在一个类中被查找时，它们的 __get__() 方法依据描述器协议被调用，在 8.9 小节已经讲述过描述器协议了。在这里， __get__() 的目的是创建一个绑定方法对象 (最终会给这个方法传递 self 参数)。
    s = Spam()
    def grok(self, x):
        print("grok()")

    grok.__get__(s, Spam)




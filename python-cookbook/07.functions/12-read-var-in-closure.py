#!/usr/bin/env python3


# 7.12 访问闭包中定义的变量

# 你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。

if __name__ == "__main__":
    # 通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是，你可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的。
    def sample():
        n = 0
        # Closure function
        def func():
            print('n=', n)

        # Accessor methods for n
        def get_n():
            return n

        def set_n(value):
            # 为了说明清楚它如何工作的，有两点需要解释一下。首先， nonlocal 声明可以让我们编写函数来修改内部变量的值。
            nonlocal n
            n = value

        # Attach as function attributes
        func.get_n = get_n
        func.set_n = set_n
        return func

    f = sample()
    f()

    f.set_n(10)
    f()

    print("f.get_n(): ", f.get_n())

    # 还可以进一步的扩展，让闭包模拟类的实例。你要做的仅仅是复制上面的内部函数到一个字典实例中并返回它即可。
    import sys
    class ClosureInstance:
        def __init__(self, locals=None):
            if locals is None:
                locals = sys._getframe(1).f_locals

            # Update instance dictionary with callables
            self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

        # Redirect special methods
        def __len__(self):
            return self.__dict__['__len__']()

    # Example use
    def Stack():
        items = []
        def push(item):
            items.append(item)

        def pop():
            return items.pop()

        def __len__():
            return len(items)

        return ClosureInstance()

    s = Stack()
    print("s: ", s)

    s.push(10)
    s.push(20)
    s.push('Hello')

    print("len(s): ", len(s))

    print("s.pop(): ", s.pop())
    print("s.pop(): ", s.pop())
    print("s.pop(): ", s.pop())

    # 有趣的是，这个代码运行起来会比一个普通的类定义要快很多。你可能会像下面这样测试它跟一个类的性能对比
    class Stack2:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def __len__(self):
            return len(self.items)

    # 如果这样做，你会得到类似如下的结果
    from timeit import timeit

    # Test involving closures
    s = Stack()
    print(timeit('s.push(1);s.pop()', 'from __main__ import s')) # 0.9874754269840196

    # Test involving a class
    s = Stack2()
    print(timeit('s.push(1);s.pop()', 'from __main__ import s')) # 1.0707052160287276

    # 结果显示，闭包的方案运行起来要快大概 8%，大部分原因是因为对实例变量的简化访问，闭包更快是因为不会涉及到额外的 self 变量。
    # 不过，你得考虑下是否真的需要在你代码中这样做，而且它只是真实类的一个奇怪的替换而已，例如，类的主要特性如继承、属性、描述器或类方法都是不能用的。
    # 并且你要做一些其他的工作才能让一些特殊方法生效 (比如上面 ClosureInstance 中重写过的 __len__()实现。 )




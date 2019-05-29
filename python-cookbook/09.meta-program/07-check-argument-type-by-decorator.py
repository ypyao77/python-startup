#!/usr/bin/env python3

# 9.7 利用装饰器强制函数上的类型检查

# 作为某种编程规约，你想在对函数参数进行强制类型检查。

# 使用装饰器技术来实现 @typeassert
from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))

            return func(*args, **kwargs)
        return wrapper
    return decorate

# 在演示实际代码前，先说明我们的目标：能对函数参数类型进行断言
@typeassert(int, int)
def add1(x, y):
    print("add({}, {})".format(x, y))
    return x + y

@typeassert(int, float)
def add2(x, y):
    print("add({}, {})".format(x, y))
    return x + y

# 可以看出这个装饰器非常灵活，既可以指定所有参数类型，也可以只指定部分。并且可以通过位置或关键字来指定参数类型。
@typeassert(int, z=int)
def spam(x, y, z=42):
    print("spam({}, {}, {})".format(x, y, z))


if __name__ == '__main__':
    add1(2, 3)

    try:
        add1(2, 3.0)
    except Exception as e:
        print(e)


    try:
        add2(2, 3)
    except Exception as e:
        print(e)

    add2(2, 3.0)


    spam(1, 2, 3)
    spam(1, "hello", 3)

    try:
        spam(1.0, 2, 3)
    except Exception as e:
        print(e)

    try:
        spam(1, 2, 3.0)
    except Exception as e:
        print(e)


# 这节是高级装饰器示例，引入了很多重要的概念。
# 1. 首先，装饰器只会在函数定义时被调用一次。有时候你去掉装饰器的功能，那么你只需要简单的返回被装饰函数即可。
#    下面的代码中，如果全局变量　 __debug__ 被设置成了 False(当你使用-O 或-OO 参数的优化模式执行程序时)，那么就直接返回未修改过的函数本身：
'''
def decorate(func):
    # If in optimized mode, disable type checking
    if not __debug__:
        return func
'''

# 2. 其次，这里还对被包装函数的参数签名进行了检查，我们使用了 inspect.signature() 函数。简单来讲，它运行你提取一个可调用对象的参数签名信息。
'''
from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)
sig.parameters
sig.parameters['z'].name
sig.parameters['z'].default
sig.parameters['z'].kind
'''

# 3. 最后一点是关于适用装饰器参数和函数注解之间的争论。例如，为什么不像下面这样写一个装饰器来查找函数中的注解呢？
'''
@typeassert
def spam(x:int, y, z:int = 42):
    print(x,y,z)
'''
# 一个可能的原因是如果使用了函数参数注解，那么就被限制了。如果注解被用来做类型检查就不能做其他事情了。
# 而且 @typeassert 不能再用于使用注解做其他事情的函数了。而使用上面的装饰器参数灵活性大多了，也更加通用。

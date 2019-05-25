#!/usr/bin/env python3


# 3.6 复数的数学运算

# 你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使
# 用复数空间。再或者是你仅仅需要使用复数来执行一些计算操作
if __name__ == "__main__":
    # 复数可以用使用函数 complex(real, imag) 或者是带有后缀 j 的浮点数来指定
    a = complex(2, 4)
    b = 3 - 5j
    print("a: ", a)
    print("b: ", b)

    # 对应的实部、虚部和共轭复数可以很容易的获取。
    print("a.real: ", a.real)
    print("a.imag: ", a.imag)
    print("a.conjugate(): ", a.conjugate())

    # 所有常见的数学运算都可以工作
    print("a + b: ", a + b)
    print("a * b: ", a * b)
    print("a / b: ", a / b)
    print("abs(a): ", abs(a))

    # 如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
    import cmath
    print("cmath.sin(a): ", cmath.sin(a))
    print("cmath.cos(a): ", cmath.cos(a))
    print("cmath.exp(a): ", cmath.exp(a))

    # Python 中大部分与数学相关的模块都能处理复数。比如如果你使用 numpy ，可以
    # 很容易的构造一个复数数组并在这个数组上执行各种操作
    '''
    import numpy as np
    a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
    print("a: ", a)
    print("a + 2: ", a + 2)
    print("np.sin(a): ", np.sin(a))
    '''

    # Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会出现复数返回值。
    import math
    try:
        print("math.sqrt(-1): ", math.sqrt(-1))
    except Exception as e:
        print(e)

    # 如果你想生成一个复数返回结果，你必须显示的使用 cmath 模块，或者在某个支
    # 持复数的库中声明复数类型的使用。
    import cmath
    print("cmath.sqrt(-1): ", cmath.sqrt(-1))









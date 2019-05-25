#!/usr/bin/env python3


# 3.7 无穷大与 NaN
import math
# 你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
if __name__ == "__main__":
    # Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们。
    a = float('inf')
    b = float('-inf')
    c = float('nan')

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("a == b: ", a == b)
    print("a is b: ", a is b)

    # 为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数。
    print("math.isinf(a): ", math.isinf(a))
    print("math.isinf(b): ", math.isinf(b))
    print("math.isnan(c): ", math.isnan(c))


    # 想了解更多这些特殊浮点值的信息，可以参考 IEEE 754 规范。然而，也有一些地方需要你特别注意，
    # 特别是跟比较和操作符相关的时候。无穷大数在执行数学计算的时候会传播
    a = float('inf')
    print("a + 56: ", a + 56)
    print("a * 10: ", a * 10)
    print("a / 10: ", a / 10)
    print("10 / a: ", 10 / a)


    # 但是有些操作时未定义的并会返回一个 NaN 结果。
    a = float('inf')
    print("a: ", a)
    print("a / a: ", a / a)

    b = float('-inf')
    print("b: ", b)
    print("a + b: ", a + b)

    # NaN 值会在所有操作中传播，而不会产生异常。
    c = float('nan')
    print("c + 24: ", c + 24)
    print("c / 2: ", c / 2)
    print("c * 2: ", c * 2)
    print("math.sqrt(c): ", math.sqrt(c))

    # NaN 值的一个特别的地方时它们之间的比较操作总是返回 False。
    c = float('nan')
    d = float('nan')
    print("c == d: ", c == d)
    print("c is d: ", c is d)

    # 测试一个 NaN 值得唯一安全的方法就是使用 math.isnan() ，也就是上面演示的那样。








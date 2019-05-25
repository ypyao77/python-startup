#!/usr/bin/env python3


# 3.8 分数运算
import math
# 你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。或者你可能需要写代码去计算在你的木工工厂中的测量值
if __name__ == "__main__":
    # fractions 模块可以被用来执行包含分数的数学运算。
    from fractions import Fraction

    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print("a: ", a)
    print("b: ", b)
    print("a + b: ", a + b)
    print("a * b: ", a * b)

    # Getting numerator/denominator
    c = a * b
    print("c: ", c)
    print("c.numerator: ", c.numerator)
    print("c.denominator: ", c.denominator)

    # Converting to a float
    print("float(c): ", float(c))

    # Limiting the denominator of a value
    print("c.limit_denominator(8): ", c.limit_denominator(8))

    # Converting a float to a fraction
    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print("x: ", x)
    print("y: ", y)




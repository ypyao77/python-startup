#!/usr/bin/env python3


# 7.4 返回多个值的函数

# 为了能返回多个值，函数直接 return 一个元组就行了。
def f1():
    return 1, 2, 3

def f2():
    return (1, 2, 3)


if __name__ == "__main__":
    a, b, c = f1()
    print("a, b, c: ", a, b, c)
    (a, b, c) = f1()
    print("a, b, c: ", a, b, c)
    x = f1()
    print("x: ", x)

    a, b, c = f2()
    print("a, b, c: ", a, b, c)
    (a, b, c) = f2()
    print("a, b, c: ", a, b, c)
    x = f2()
    print("x: ", x)

    # 尽管 f1() 看上去返回了多个值，实际上是先创建了一个元组然后返回的。
    # 这个语法看上去比较奇怪，实际上我们使用的是逗号来生成一个元组，而不是用括号。
    a = (1, 2)
    print("a: ", a)

    b = 1, 2
    print("b: ", b)

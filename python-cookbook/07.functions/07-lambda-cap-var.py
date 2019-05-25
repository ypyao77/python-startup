#!/usr/bin/env python3


# 7.7 匿名函数捕获变量值
# 你用 lambda 定义了一个匿名函数，

if __name__ == "__main__":
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y

    # a(10) 和 b(10) 返回的结果是什么？如果你认为结果是 20 和 30，那么你就错了
    print("a(10): ", a(10)) # 30
    print("b(10): ", b(10)) # 30

    # 其中的奥妙在于 lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不是定义时就绑定，
    # 这跟函数的默认值参数定义是不同的。因此，在调用这个 lambda 表达式的时候， x 的值是执行时的值。

    x = 15
    print("a(10): ", a(10))
    x = 3
    print("a(10): ", a(10))

    # 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y

    print("a(10): ", a(10)) # 30
    print("b(10): ", b(10)) # 30

    # 在这里列出来的问题是新手很容易犯的错误，有些新手可能会不恰当的使用lambda 表达式。
    # 比如，通过在一个循环或列表推导中创建一个 lambda 表达式列表，并期望函数能在定义时就记住每次的迭代值。
    funcs = [lambda x: x+n for n in range(5)]
    print("error()")
    for f in funcs:
        print(" ", f(0))

    # 但是实际效果是运行是 n 的值为迭代的最后一个值。现在我们用另一种方式修改一下
    funcs = [lambda x, n=n: x+n for n in range(5)]
    print("ok()")
    for f in funcs:
        print(" ", f(0))


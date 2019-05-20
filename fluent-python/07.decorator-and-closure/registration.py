#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ❶ registry 保存被 @register 装饰的函数引用
registry = []

# ❷ register 的参数是一个函数
def register(func):
    # ❸ 为了演示， 显示被装饰的函数
    print('running register(%s)' % func)

    # ❹ 把 func 存入 registry
    registry.append(func)

    # ❺ 返回 func： 必须返回函数； 这里返回的函数与通过参数传入的一样。
    return func

# ❻ f1 和 f2 被 @register 装饰
@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

# ❼ f3 没有装饰
def f3():
    print('running f3()')

# ❽ main 显示 registry， 然后调用 f1()、 f2() 和 f3()
def main():
    print('running main()')
    print('registry ->', registry)

    f1()
    f2()
    f3()


if __name__=='__main__':
    main()



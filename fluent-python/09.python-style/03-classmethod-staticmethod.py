#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 比较 classmethod 和 staticmethod 的行为
class Demo:
    @classmethod
    def klassmeth(*args):
        # ❶ klassmeth 返回全部位置参数
        return args

    @staticmethod
    def statmeth(*args):
        # ❷ statmeth 也是
        return args


if __name__ == "__main__":
    # ❸ 不管怎样调用 Demo.klassmeth， 它的第一个参数始终是 Demo 类
    print(Demo.klassmeth())
    print(Demo.klassmeth("spam"))

    # ❹ Demo.statmeth 的行为与普通的函数相似
    print(Demo.statmeth())
    print(Demo.statmeth("spam"))

    # classmethod 装饰器非常有用， 但是我从未见过不得不用staticmethod 的情况。 如果想定义不需要与类交互的函数， 那么在模块中定义就好


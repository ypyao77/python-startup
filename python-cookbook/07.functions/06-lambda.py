#!/usr/bin/env python3


# 7.6 定义匿名或内联函数

# 你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数，而是希望通过某个快捷方式以内联方式来创建这个函数

# 当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用 lambda 表达式来代替了。


if __name__ == "__main__":
    add = lambda x, y: x + y
    print("add(2, 3): ", add(2, 3))
    print("add('hello ', 'world'): ", add('hello ', 'world'))

    def add(x, y):
        return x + y
    print("add(2, 3): ", add(2, 3))
    print("add('hello ', 'world'): ", add('hello ', 'world'))


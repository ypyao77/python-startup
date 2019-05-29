#!/usr/bin/env python3


# 7.6 定义匿名或内联函数

if __name__ == "__main__":
    # 你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数，而是希望通过某个快捷方式以内联方式来创建这个函数
    add1 = lambda x, y: x + y
    print("add(2, 3): ", add1(2, 3))
    print("add('hello ', 'world'): ", add1('hello ', 'world'))

    # 当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用 lambda 表达式来代替了。
    # 这里使用的 lambda 表达式跟下面的效果是一样的
    def add2(x, y):
        return x + y

    print("add2(2, 3): ", add2(2, 3))
    print("add2('hello ', 'world'): ", add2('hello ', 'world'))

    # lambda 表达式典型的使用场景是排序或数据 reduce 等
    names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    print("sorted(names, key=lambda name: name.split()[-1].lower()): ", sorted(names, key=lambda name: name.split()[-1].lower()))

    # 尽管 lambda 表达式允许你定义简单函数，但是它的使用是有限制的。你只能指定单个表达式，它的值就是最后的返回值。
    # 也就是说不能包含其他的语言特性了，包括多个语句、条件表达式、迭代以及异常处理等等。你可以不使用 lambda 表达式
    # 就能编写大部分 python 代码。但是，当有人编写大量计算表达式值的短小函数或者需要用户提供回调函数的程序的时候，
    # 你就会看到lambda 表达式的身影了。








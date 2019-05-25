#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# from operator import avg
if __name__ == "__main__":
    def drop_first_last(grades):
        first, *middle, last = grades
        return sum(middle)

    print(drop_first_last((1, 2, 3, 4, 5, 6)))

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    print("record: ", record)
    name, email, *phone_numbers = record
    print(name)
    print(email)
    print(phone_numbers)

    # 星号表达式在迭代元素为可变长元组的序列时是很有用的。比如，下面是一个带有标签的元组序列
    records = [
                ('foo', 1, 2),
                ('bar', 'hello'),
                ('foo', 3, 4),
            ]

    def do_foo(x, y):
        print('foo', x, y)
    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    # 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ ignore）
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    print("record: ", record)
    name, *_, (*_, year) = record
    print(name)
    print(year)

    # 在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有一个列表，你可以很容易的将它分割成前后两部分
    items = [1, 10, 7, 4, 5, 9]
    print("items: ", items)
    head, *tail = items
    print("head: ", head)
    print("tail: ", tail)

    # 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法
    def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head

    print("sum(items): ", sum(items))
    print("sum([3, 4]): ", sum([3, 4]))
    print("sum([3]): ", sum([3]))
    print("sum([]): ", sum([]))

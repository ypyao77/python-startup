#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import namedtuple

# 具名元祖
if __name__ == "__main__":
    # ❶ 创建一个具名元组需要两个参数， 一个是类名， 另一个是类的各个
    # 字段的名字。 后者可以是由数个字符串组成的可迭代对象， 或者是由空
    # 格分隔开的字段名组成的字符串
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

    print("tokyo: {0}".format(tokyo))

    # ❷  存放在对应字段里的数据要以一串参数的形式传入到构造函数中
    # （注意， 元组的构造函数却只接受单一的可迭代对象）

    # ❸ 你可以通过字段名或者位置来获取一个字段的信息
    print("tokyo.population: {0}".format(tokyo.population))
    print("tokyo.coordinates: {0}".format(tokyo.coordinates))
    print("tokyo[1]: {0}".format(tokyo[1]))





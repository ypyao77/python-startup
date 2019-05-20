#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 使用另一个元组构建元组， 得到的其实是同一个元组


if __name__ == "__main__":
    t1 = (1, 2, 3)
    t2 = tuple(t1)

    # ❶ t1 和 t2 绑定到同一个对象
    print("t2 is t1: {}".format(t2 is t1))

    t3 = t1[:]
    # ❷ t3 也是
    print("t3 is t1: {}".format(t3 is t1))

    # str、 bytes 和 frozenset 实例也有这种行为。 注意， frozenset 实
    # 例不是序列， 因此不能使用 fs[:]（fs 是一个 frozenset 实例） 。 但
    # 是， fs.copy() 具有相同的效果： 它会欺骗你， 返回同一个对象的引
    # 用， 而不是创建一个副本


    # copy 方法不会复制所有对象， 这是一个善意的谎言， 为的是接口的兼容性： 这使得
    # frozenset 的兼容性比 set 强。 两个不可变对象是同一个对象还是副本， 反正对最终用户来
    # 说没有区别


    # ❶ 新建一个元组
    t1 = (1, 2, 3)
    t3 = (1, 2, 3)

    # ❷ t1 和 t3 相等， 但不是同一个对象
    print("t3 is t1: {}".format(t3 is t1))

    # ❸ 再新建一个字符串
    s1 = "ABC"
    s2 = "ABC"

    # ❹ 奇怪的事发生了， a 和 b 指代同一个字符串
    print("s2 is s1: {}".format(s2 is s1))


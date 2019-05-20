#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 弱引用是可调用的对象， 返回的是被引用的对象； 如果所指对象不存在了， 返回 None
import weakref


if __name__ == "__main__":
    a_set = {0, 1}
    print("a_set: {}".format(a_set))

    # ❶ 创建弱引用对象 wref， 下一行审查它
    wref = weakref.ref(a_set)

    print("wref: {}".format(wref))

    # ❷ 调用 wref() 返回的是被引用的对象， {0, 1}。 因为这是控制台会话， 所以 {0, 1} 会绑定给 _ 变量
    print("wref(): {}".format(wref()))

    # ❸ a_set 不再指代 {0, 1} 集合， 因此集合的引用数量减少了。 但是 _变量仍然指代它
    a_set = {2, 3, 4}
    print("a_set: {}".format(a_set))

    # ❹ 调用 wref() 依旧返回 {0, 1}
    print("wref(): {}".format(wref()))

    # ❺ 计算这个表达式时， {0, 1} 存在， 因此 wref() 不是 None。 但是，随后 _ 绑定到结果值 False。 现在 {0, 1} 没有强引用了
    print("wref() is None: {}".format(wref() is None))

    # ❻ 因为 {0, 1} 对象不存在了， 所以 wref() 返回 None
    print("wref() is None: {}".format(wref() is None))
    print("wref() is None: {}".format(wref() is None))
    print("wref() is None: {}".format(wref() is None))

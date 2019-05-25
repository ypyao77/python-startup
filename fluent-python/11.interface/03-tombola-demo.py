#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tombola import Tombola


# ❶ 把 Fake 声明为 Tombola 的子类
class Fake(Tombola):
    def pick(self):
        return 13


if __name__ == "__main__":
    # ❷ 创建了 Fake 类， 目前没有错误
    print(Fake)

    # ❸ 尝试实例化 Fake 时抛出了 TypeError。 错误消息十分明确： Python 认为 Fake 是抽象类，
    # 因为它没有实现 load 方法， 这是 Tombola 抽象基类声明的抽象方法之一
    try:
        f = Fake()
    except Exception as e:
        print(e)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from tombola import Tombola


# ❶ 明确指定 BingoCage 类扩展 Tombola 类
class BingoCage(Tombola):
    def __init__(self, items):
        # ❷ 假设我们将在线上游戏中使用这个。 random.SystemRandom 使用os.urandom(...) 函数实现 random API。 根据 os 模块的文档
        # （http://docs.python.org/3/library/os.html#os.urandom） ， os.urandom(...) 函数生成“适合用于加密”的随机字节序列。
        self._randomizer = random.SystemRandom()
        self._items = []

        # ❸ 委托 .load(...) 方法实现初始加载
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        # ❹ 没有使用 random.shuffle() 函数， 而是使用 SystemRandom 实例的 .shuffle() 方法
        self._randomizer.shuffle(self._items)

    # ❺ pick 方法的实现方式与示例 5-8 一样
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    # ❻ __call__ 也跟示例 5-8 中的一样。 它没必要满足 Tombola 接口， 添加额外的方法没有问题
    def __call__(self):
        self.pick()


if __name__ == "__main__":
    try:
        f = BingoCage([])
    except Exception as e:
        print(e)

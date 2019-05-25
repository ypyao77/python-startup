#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from tombola import Tombola


# LotteryBlower 是 Tombola 的具体子类，覆盖了继承的 inspect 和 loaded 方法
class LotteryBlower(Tombola):
    def __init__(self, iterable):
        # ❶ 初始化方法接受任何可迭代对象： 把参数构建成列表
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            # ❷ 如果范围为空， random.randrange(...) 函数抛出 ValueError，为了兼容 Tombola， 我们捕获它， 抛出 LookupError
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')

        # ❸ 否则， 从 self._balls 中取出随机选中的元素
        return self._balls.pop(position)

    # ❹ 覆盖 loaded 方法， 避免调用 inspect 方法（示例 11-9 中的Tombola.loaded 方法是这么做的） 。 我们可以直接处理self._balls 而不必构建整个有序元组， 从而提升速度
    def loaded(self):
        return bool(self._balls)

    # ❺ 使用一行代码覆盖 inspect 方法
    def inspect(self):
        return tuple(sorted(self._balls))


if __name__ == "__main__":
    try:
        f = LotteryBlower([])
    except Exception as e:
        print(e)

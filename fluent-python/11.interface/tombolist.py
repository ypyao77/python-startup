#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randrange
from tombola import Tombola


# ❶ 把 Tombolist 注册为 Tombola 的虚拟子类
@Tombola.register
# ❷ Tombolist 扩展 list
class TomboList(list):
    def pick(self):
        # ❸ Tombolist 从 list 中继承 __bool__ 方法， 列表不为空时返回True
        if self:
            position = randrange(len(self))
            # ❹ pick 调用继承自 list 的 self.pop 方法， 传入一个随机的元素索引
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

        # ❺ Tombolist.load 与 list.extend 一样
        load = list.extend

    def loaded(self):
        # ❻ loaded 方法委托 bool 函数。
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# ❼ 如果是 Python 3.3 或之前的版本， 不能把 .register 当作类装饰器使用， 必须使用标准的调用句法
# Tombola.register(TomboList)

if __name__ == "__main__":
    try:
        f = LotteryBlower([])
    except Exception as e:
        print(e)

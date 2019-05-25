#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc

# ❶ 自己定义的抽象基类要继承 abc.ABC
class Tombola(abc.ABC):
    @abc.abstractmethod
    # ❷ 抽象方法使用 @abstractmethod 装饰器标记， 而且定义体中通常只有文档字符串
    # 在抽象基类出现之前， 抽象方法使用 raise NotImplementedError 语句表明由子类负责实现。
    def load(self, iterable):
        """从可迭代对象中添加元素。 """

    @abc.abstractmethod
    # ❸ 根据文档字符串， 如果没有元素可选， 应该抛出 LookupError
    def pick(self):
        """随机删除元素， 然后将其返回。如果实例为空， 这个方法应该抛出`LookupError`。"""

    # ❹ 抽象基类可以包含具体方法
    def loaded(self):
        """如果至少有一个元素， 返回`True`， 否则返回`False`。 """
        # ❺ 抽象基类中的具体方法只能依赖抽象基类定义的接口（即只能使用抽象基类中的其他具体方法、 抽象方法或特性）
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组， 由当前元素构成。 """
        items = []
        
        # ❻ 我们不知道具体子类如何存储元素， 不过为了得到 inspect 的结果， 我们可以不断调用 .pick() 方法， 把 Tombola 清空
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        # ❼ 然后再使用 .load(...) 把所有元素放回去
        self.load(items)
        return tuple(sorted(items))





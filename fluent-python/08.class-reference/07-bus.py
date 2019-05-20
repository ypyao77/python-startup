#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 一个简单的类， 说明接受可变参数的风险
class TwilightBus:
    """让乘客销声匿迹的校车"""
    def __init__(self, passengers=None):
        if passengers is None:
            # ❶ 这里谨慎处理， 当 passengers 为 None 时， 创建一个新的空列表
            self.passengers = []
        else:
            # 然而， 这个赋值语句把 self.passengers 变成 passengers 的别
            # 名， 而后者是传给 __init__ 方法的实参（即示例 8-14 中的basketball_team） 的别名。

            # 正确方法：➊ 创建 passengers 列表的副本； 如果不是列表， 就把它转换成列表。
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        # ❸ 在 self.passengers 上调用 .remove() 和 .append() 方法其实会修改传给构造方法的那个列表
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)


# 备受幽灵乘客折磨的校车
if __name__ == "__main__":
    # ❶ basketball_team 中有 5 个学生的名字
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']

    # ❷ 使用这队学生实例化 TwilightBus
    bus = TwilightBus(basketball_team)

    # ❸ 一个学生从 bus 下车了， 接着又有一个学生下车了
    bus.drop('Tina')
    bus.drop('Pat')

    # ❹ 下车的学生从篮球队中消失了
    print("basketball_team: {}".format(basketball_team))

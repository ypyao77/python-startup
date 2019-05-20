#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 不要使用可变类型作为参数的默认值
# 一个简单的类， 说明可变默认值的危险
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    # ❶ 如果没传入 passengers 参数， 使用默认绑定的列表对象， 一开始是空列表
    # 通常使用 None 作为接收可变值的参数的默认值
    def __init__(self, passengers=[]):
        # ❷ 这个赋值语句把 self.passengers 变成 passengers 的别名， 而没有传入 passengers 参数时， 后者又是默认列表的别名
        self.passengers = passengers

    def pick(self, name):
        # ❸ 在 self.passengers 上调用 .remove() 和 .append() 方法时， 修改的其实是默认列表， 它是函数对象的一个属性
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)



# 备受幽灵乘客折磨的校车
if __name__ == "__main__":
    bus1 = HauntedBus(['Alice', 'Bill'])
    bus1.passengers
    bus1.pick('Charlie')
    bus1.drop('Alice')

    # ❶ 目前没什么问题， bus1 没有出现异常
    print("bus1: {}".format(bus1))

    # ❷ 一开始， bus2 是空的， 因此把默认的空列表赋值给self.passengers
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print("bus2: {}".format(bus2))

    # ❸ bus3 一开始也是空的， 因此还是赋值默认的列表
    bus3 = HauntedBus()

    # ❹ 但是默认列表不为空!!!
    print("bus3: {}".format(bus3))

    # ❺ 登上 bus3 的 Dave 出现在 bus2 中
    bus3.pick('Dave')
    print("bus3.pick('Dave')")
    print("bus3: {}".format(bus3))
    print("bus2: {}".format(bus2))

    # ❻ 问题是， bus2.passengers 和 bus3.passengers 指代同一个列表
    print("bus2.passengers is bus3.passengers: {}".format(bus2.passengers is bus3.passengers))

    # ❼ 但 bus1.passengers 是不同的列表
    print("bus1: {}".format(bus1))



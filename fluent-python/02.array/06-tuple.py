#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
# from math import divmod

if __name__ == "__main__":
    lax_coordinates = (33.9425, -118.408056)
    print("lax_coordinates: {0}".format(lax_coordinates))

    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    print("city, year, pop, chg, area: {0} {1} {2} {3} {4}".format(city, year, pop, chg, area))

    # failure
    # city, year, pop, chg = ('Tokyo', 2003, 32450, 0.66, 8014)
    # print("city, year, pop, chg: {0} {1} {2} {3}".format(city, year, pop, chg))

    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)

    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates # 元组拆包
    print('latitude, longitude: %s, %s' % (latitude, longitude))

    # 一个很优雅的写法当属不使用中间变量交换两个变量的值
    a, b = "a", 33
    a, b = b, a
    print("a, b: %s, %s" %(a, b))

    # 可以用 * 运算符把一个可迭代对象拆开作为函数的参数
    # print("divmod(20, 8): %s" %(divmod(20, 8)))
    # t = (20, 8)
    # print("divmod(*): %s" %(divmod(*t)))
    # quotient, remainder = divmod(*t)
    # print('quotient, remainder: %s, %s' % (quotient, remainder))

    _, filename = os.path.split('/home/base/root/luciano/.ssh/idrsa.pub')
    print("filename: %s" %(filename))

    # 在 Python 中， 函数用 *args 来获取不确定数量的参数算是一种经典写法了。
    # 于是 Python 3 里， 这个概念被扩展到了平行赋值中
    a, b, *rest = range(5)
    print("a, b, rest: %s, %s, %s" %(a, b, rest))
    a, b, *rest = range(3)
    print("a, b, rest: %s, %s, %s" %(a, b, rest))
    a, b, *rest = range(2)
    print("a, b, rest: %s, %s, %s" %(a, b, rest))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import namedtuple

# 具名元祖的属性与方法
if __name__ == "__main__":
    City = namedtuple('City', 'name country population coordinates')

    # ❶ _fields 属性是一个包含这个类所有字段名称的元组
    print("City._fields: {0}".format(City._fields))

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

    # ➋ 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例， 它
    # 的作用跟 City(*delhi_data) 是一样的。
    delhi = City._make(delhi_data)

    # ➌  _asdict() 把具名元组以 collections.OrderedDict 的形式返
    # 回， 我们可以利用它来把元组里的信息友好地呈现出来
    delhi._asdict()
    print("delhi._asdict(): {0}".format(delhi._asdict()))

    for key, value in delhi._asdict().items():
        print(key + ':', value)



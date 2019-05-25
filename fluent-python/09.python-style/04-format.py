#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
# 内置的 format() 函数和 str.format() 方法把各个类型的格式化方式
# 委托给相应的 .__format__(format_spec) 方法。 format_spec 是格
# 式说明符， 它是：
# * format(my_obj, format_spec) 的第二个参数， 或者
# * str.format() 方法的格式字符串， {} 里代换字段中冒号后面的部分

if __name__ == "__main__":
    brl = 1/2.43

    print("brl: {}".format(brl))

    # ❶ 格式说明符是 '0.4f'
    print(format(format(brl, '0.4f')))

    # ❷ 格式说明符是 '0.2f'。 代换字段中的 'rate' 子串是字段名称，
    # 与格式说明符无关， 但是它决定把 .format() 的哪个参数传给代换字段
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

    now = datetime.now()
    print("It's now {:%H:%M:%S}".format(now))

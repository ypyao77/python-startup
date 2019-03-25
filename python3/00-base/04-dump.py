#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# 位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
print('常量 PI 的值近似为 {1:.3f}。{0}.'.format("", math.pi))

p = 123456789.123456789
q = 123.123456789
print('p 的值近似为 {0:.3f}。'.format(p))
print('q 的值近似为 {0:.3f}。'.format(q))
print('p 的值近似为 {0:8.2f}。'.format(p))
print('q 的值近似为 {0:8.2f}。'.format(q))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'Google': 1, 'Run': 22, 'JD': 333}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
print('Run: {0[Run]:d}; Google: {0[Google]:d}; JD: {0[JD]:d}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能
print('Run: {Run:d}; Google: {Google:d}; JD: {JD:d}'.format(**table))



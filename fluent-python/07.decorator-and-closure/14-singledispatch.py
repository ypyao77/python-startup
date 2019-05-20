#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# functools.singledispatch 装饰器可以把整体方案
# 拆分成多个模块， 甚至可以为你无法修改的类提供专门的函数。 使用
# @singledispatch 装饰的普通函数会变成泛函数 (generic function):
# 根据第一个参数的类型， 以不同方式执行相同操作的一组函数

# singledispatch 创建一个自定义的htmlize.register 装饰器， 把多个函数绑在一起组成一个泛函数

from functools import singledispatch
from collections import abc
import numbers
import html

# ❶ @singledispatch 标记处理 object 类型的基函数。
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

# ❷ 各个专门函数使用 @«base_function».register(«type») 装饰
@htmlize.register(str)
# ❸ 专门函数的名称无关紧要； _ 是个不错的选择， 简单明了
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

# ❹ 为每个需要特殊处理的类型注册一个函数。 numbers.Integral 是int 的虚拟超类
@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

# ❺ 可以叠放多个 register 装饰器， 让同一个函数支持不同类型
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == "__main__":
    # ❶ 默认情况下， 在 <pre></pre> 中显示 HTML转义后的对象字符串表示形式
    print(htmlize({1, 2, 3}))

    print(htmlize(abs))

    # ❷ 为 str 对象显示的也是 HTML转义后的字符串表示形式， 不过放在<p></p> 中， 而且使用 <br> 表示换行
    print(htmlize('Heimlich & Co.\n- a game'))

    # ❸ int 显示为十进制和十六进制两种形式， 放在 <pre></pre> 中
    print(htmlize(42))

    # ❹ 各个列表项目根据各自的类型格式化， 整个列表则渲染成 HTML列表
    print(htmlize(['alpha', 66, {3, 2, 1}]))



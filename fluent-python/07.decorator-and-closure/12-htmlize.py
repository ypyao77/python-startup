#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成 HTML的 htmlize 函数， 调整了几种对象的输出
import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

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


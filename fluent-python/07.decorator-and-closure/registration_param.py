#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 示例 7-23 为了接受参数， 新的 register 装饰器必须作为函数调用

# ❶ registry 现在是一个 set 对象， 这样添加和删除函数的速度更快
registry = set()

# ❷ register 接受一个可选的关键字参数
def register(active=True):
    # ❸ decorate 这个内部函数是真正的装饰器; 注意， 它的参数是一个函数
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))

        # ❹ 只有 active 参数的值（从闭包中获取） 是 True 时才注册 func
        if active:
            registry.add(func)
        else:
            # ❺ 如果 active 不为真， 而且 func 在 registry 中， 那么把它删除
            registry.discard(func)

        # ❻ decorate 是装饰器， 必须返回一个函数
        return func

    # ❼ register 是装饰器工厂函数， 因此返回 decorate
    return decorate

# ❽ @register 工厂函数必须作为函数调用， 并且传入所需的参数
@register(active=False)
def f1():
    print('running f1()')

# ❾ 即使不传入参数， register 也必须作为函数调用（ @register()） ， 即要返回真正的装饰器 decorate
@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

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



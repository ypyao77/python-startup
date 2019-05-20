#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# ❶ clock 是参数化装饰器工厂函数
def clock(fmt=DEFAULT_FMT):
    # ❷ decorate 是真正的装饰器
    def decorate(func):
        # ❸ clocked 包装被装饰的函数
        def clocked(*_args):
            t0 = time.time()

            # ❹ _result 是被装饰的函数返回的真正结果
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__

            # ❺ _args 是 clocked 的参数， args 是用于显示的字符串
            args = ', '.join(repr(arg) for arg in _args)

            # ❻ result 是 _result 的字符串表示形式， 用于显示。
            result = repr(_result)

            # ❼ 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量
            print(fmt.format(**locals()))

            # ❽ clocked 会取代被装饰的函数， 因此它应该返回被装饰的函数返回的值
            return _result

        # ❾ decorate 返回 clocked
        return clocked

    # ❿ clock 返回 decorate
    return decorate

if __name__ == '__main__':
    # ⓫ 在这个模块中测试， 不传入参数调用 clock()， 因此应用的装饰器使用默认的格式 str。
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)


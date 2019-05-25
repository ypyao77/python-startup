#!/usr/bin/env python3


# 7.10 带额外状态信息的回调函数

# 你的代码中需要依赖到回调函数的使用 (比如事件处理器、等待后台任务完成后的回调等)，
# 并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。
if __name__ == "__main__":
    # 这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用——特别是跟异步处理有关的。
    # 为了演示与测试，我们先定义如下一个需要调用回调函数的函数
    def apply_async(func, args, *, callback):
        # Compute the result
        result = func(*args)

        # Invoke the callback with the result
        callback(result)

    # 实际上，这段代码可以做任何更高级的处理，包括线程、进程和定时器，但是这些都不是我们要关心的。我们仅仅只需要关注回调函数的调用。
    def print_result(result):
        print('Got:', result)

    def add1(x, y):
        return x + y

    apply_async(add1, (2, 3), callback=print_result)
    apply_async(add1, ('hello ', 'world'), callback=print_result)

    # 注意到 print_result() 函数仅仅只接受一个参数 result 。不能再传入其他信息。而当你想让回调函数访问其他变量或者特定环境的变量值的时候就会遇到麻烦。

    # 方法1, 为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数。比如，下面这个类会保存一个内部序列号，每次接收到一个 result 的时候序列号加 1
    class ResultHandler:
        def __init__(self):
            self.sequence = 0
        def handler(self, result):
            self.sequence += 1
            print('[{}] Got: {}'.format(self.sequence, result))

    # 使用这个类的时候，你先创建一个类的实例，然后用它的 handler() 绑定方法来做为回调函数
    r = ResultHandler()
    apply_async(add1, (2, 3), callback=r.handler)
    apply_async(add1, ('hello ', 'world'), callback=r.handler)

    # 方法2, 作为类的替代，可以使用一个闭包捕获状态值
    def make_handler():
        sequence = 0
        def handler(result):
            nonlocal sequence
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))
        return handler

    handler = make_handler()
    apply_async(add1, (2, 3), callback=handler)
    apply_async(add1, ('hello ', 'world'), callback=handler)

    # 方法3, 还有另外一个更高级的方法，可以使用协程来完成同样的事情
    def make_handler2():
        sequence = 0
        while True:
            result = yield
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))

    # 对于协程，你需要使用它的 send() 方法作为回调函数
    handler = make_handler2()
    next(handler) # Advance to the yield
    apply_async(add1, (2, 3), callback=handler.send)
    apply_async(add1, ('hello ', 'world'), callback=handler.send)

    # 如果你仅仅只需要给回调函数传递额外的值的话，还有一种使用 partial() 的方式也很有用。在没有使用 partial() 的时候，你可能经常看到下面这种使用 lambda 表达式的复杂代码
    ''' apply_async(add1, (2, 3), callback=lambda r: handler(r, seq)) '''



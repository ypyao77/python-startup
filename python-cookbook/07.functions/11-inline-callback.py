#!/usr/bin/env python3


# 7.11 内联回调函数

# 当你编写使用回调函数的代码的时候，担心很多小函数的扩张可能会弄乱程序控制流。
# 你希望找到某个方法来让代码看上去更像是一个普通的执行序列。
if __name__ == "__main__":
    # 通过使用生成器和协程可以使得回调函数内联在某个函数中。为了演示说明，假设你有如下所示的一个执行某种计算任务然后调用一个回调函数的函数.
    def apply_async(func, args, *, callback):
        # Compute the result
        result = func(*args)
        # Invoke the callback with the result
        callback(result)

    # 接下来让我们看一下下面的代码，它包含了一个 Async 类和一个 inlined_async装饰器
    from queue import Queue
    from functools import wraps

    class Async:
        def __init__(self, func, args):
            self.func = func
            self.args = args

    def inlined_async(func):
        @wraps(func)
        def wrapper(*args):
            f = func(*args)
            result_queue = Queue()
            result_queue.put(None)

            while True:
                result = result_queue.get()
                try:
                    a = f.send(result)
                    apply_async(a.func, a.args, callback=result_queue.put)
                except StopIteration:
                    break
        return wrapper

    def add1(x, y):
        return x + y

    @inlined_async
    def test():
        r = yield Async(add1, (2, 3))
        print(r)

        r = yield Async(add1, ('hello ', 'world'))
        print(r)

        for n in range(10):
            r = yield Async(add1, (n, n))
            print(r)

        print('Goodbye')

    # main()
    test()

    import multiprocessing

    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    # Run the test function
    test()



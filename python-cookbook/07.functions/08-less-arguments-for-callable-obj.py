#!/usr/bin/env python3


# 7.8 减少可调用对象的参数个数

# 你有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者是一个处理器，但是它的参数太多了，导致调用时出错


if __name__ == "__main__":
    # 如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。partial()函数允许
    # 你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。为了演示清楚，假设你有下面这样的函数
    def spam(a, b, c, d):
        return a, b, c, d

    from functools import partial

    s1 = partial(spam, 1) # a = 1
    print("s1(2, 3, 4): ", s1(2, 3, 4))
    print("s1(4, 5, 6): ", s1(4, 5, 6))

    s2 = partial(spam, d=42) # d = 42
    print("s2(1, 2, 3): ", s2(1, 2, 3))
    print("s2(4, 5, 5): ", s2(4, 5, 5))

    s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
    print("s3(3): ", s3(3))
    print("s3(4): ", s3(4))
    print("s3(5): ", s3(5))

    # 这里要解决的问题是让原本不兼容的代码可以一起工作。下面我会列举一系列的例子。
    points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    import math
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x2 - x1, y2 - y1)

    # 现在假设你想以某个点为基点，根据点和基点之间的距离来排序所有的这些点。列表的 sort() 方法接受一个关键字参数来自定义排序逻辑，
    # 但是它只能接受一个单个参数的函数 (distance() 很明显是不符合条件的)。现在我们可以通过使用 partial() 来解决这个问题
    pt = (3.2, 4.2)
    points.sort(key=partial(distance,pt))
    print("points: ", points)

    # 更进一步， partial() 通常被用来微调其他库函数所使用的回调函数的参数。例如，下面是一段代码，使用 multiprocessing 来异步计算一个结果值，
    # 然后这个值被传递给一个接受一个 result 值和一个可选 logging 参数的回调函数
    def output_result(result, log=None):
        if log is not None:
            log.debug('Got: %r', result)
    # A sample function
    def add1(x, y):
        return x + y

    import logging
    from multiprocessing import Pool
    from functools import partial
    
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    # 当给 apply_async() 提供回调函数时，通过使用 partial() 传递额外的 logging参数。
    # 而 multiprocessing 对这些一无所知——它仅仅只是使用单个值来调用回调函数。
    p.apply_async(add1, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

    # 作为一个类似的例子，考虑下编写网络服务器的问题， socketserver 模块让它变得很容易。下面是个简单的 echo 服务器
    from socketserver import StreamRequestHandler, TCPServer
    class EchoHandler(StreamRequestHandler):
        # 假设你想给 EchoHandler 增加一个可以接受其他配置选项的 __init__ 方法。
        def __init__(self, *args, ack, **kwargs):
            self.ack = ack
            super().__init__(*args, **kwargs)

        def handle(self):
            for line in self.rfile:
                self.wfile.write(b'GOT:' + line)

    # 初看起来好像很难修正这个错误，除了修改 socketserver 模块源代码或者使用某些奇怪的方法之外。
    # 但是，如果使用 partial() 就能很轻松的解决——给它传递 ack 参数的值来初始化即可
    from functools import partial

    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv.serve_forever()





















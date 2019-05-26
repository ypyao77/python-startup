#!/usr/bin/env python3


# 8.3 让对象支持上下文管理协议

# 你想让你的对象支持上下文管理协议 (with 语句)
# 为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法。例如，考虑如下的一个类，它能为我们创建一个网络连接

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        print("__enter__")
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        print("__exit__")
        self.sock.close()
        self.sock = None

# 还有一个细节问题就是 LazyConnection 类是否允许多个 with 语句来嵌套使用连接。
# 很显然，上面的定义中一次只能允许一个 socket 连接，如果正在使用一个 socket的时候
# 又重复使用 with 语句，就会产生一个异常了。不过你可以像下面这样修改下上面的实现来解决这个问题
class LazyConnection2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        print("__enter__")
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        print("__exit__")
        self.connections.pop().close()

if __name__ == "__main__":
    # 这个类的关键特点在于它表示了一个网络连接，但是初始化的时候并不会做任何事情 (比如它并没有建立一个连接)。连接的建立和关闭是使用 with 语句自动完成的
    from functools import partial

    conn = LazyConnection(('localhost', 15000))

    # Connection closed
    with conn as s:
        # conn.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print("resp: ", resp)
        # conn.__exit__() executes: connection closed

    # 编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。当出现 with语句的时候，
    # 对象的 __enter__() 方法被触发，它返回的值 (如果有的话) 会被赋值给as 声明的变量。
    # 然后， with 语句块里面的代码开始执行。最后， __exit__() 方法被触发进行清理工作。

    # 不管 with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是一样的。
    # 事实上， __exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息 (如果有的话)。 
    # __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个 None 值。
    # 如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生一样， with 语句后面的程序继续在正常执行


    # Example use
    conn = LazyConnection2(('localhost', 15000))

    with conn as s1:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')

        with conn as s2:
            s.send(b'GET /index.html HTTP/1.0\r\n')
            s.send(b'Host: www.python.org\r\n')
            s.send(b'\r\n')




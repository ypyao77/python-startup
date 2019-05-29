#!/usr/bin/env python3


# 11.7 在不同的 Python 解释器之间交互

# 你在不同的机器上面运行着多个 Python 解释器实例，并希望能够在这些解释器之间通过消息来交换数据。

# 通过使用 multiprocessing.connection 模块可以很容易的实现解释器之间的通信。
from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')

if __name__ == '__main__':
    from multiprocessing.connection import Client
    c = Client(('localhost', 25000), authkey=b'peekaboo')
    c.send('hello')
    print("c.recv(): ", c.recv())

    c.send(42)
    print("c.recv(): ", c.recv())

    c.send([1, 2, 3, 4, 5])
    print("c.recv(): ", c.recv())


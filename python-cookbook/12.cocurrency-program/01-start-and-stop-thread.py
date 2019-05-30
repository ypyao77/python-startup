#!/usr/bin/env python3

# 12.1 启动与停止线程

# 你要为需要并发执行的代码创建/销毁线程
import time
from threading import Thread

# threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象。你可
# 以创建一个 Thread 对象并将你要执行的对象以 target 参数的形式提供给该对象。
def countdown(_max, _min):
    while _max > _min:
        print('T-minus', _max)
        _max -= 1
        time.sleep(1)

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, _max, _min):
        while self._running and _max > 0:
            print('T-minus', _max)
            _max -= 1
            time.sleep(1)

# 如果线程执行一些像 I/O 这样的阻塞操作，那么通过轮询来终止线程将使得线程之间的协调变得非常棘手。
# 比如，如果一个线程一直阻塞在一个 I/O 操作上，它就永远无法返回，也就无法检查自己是否已经被结束了。
# 要正确处理这些问题，你需要利用超时循环来小心操作线程。
class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        # Set timeout period
        sock.settimeout(5)
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing

        # Terminated
        return

# 有时你会看到下边这种通过继承 Thread 类来实现的线程
'''
from threading import Thread

class CountdownThread(Thread):
    def __init__(self, _max, _min):
        super().__init__()
        self._max = _max
        self._min = _min

    def run(self):
        while self._max > self._min:
            print('T-minus', self._max)
            self._max -= 1
            time.sleep(1)

c = CountdownThread(10, 5)
c.start()
'''

# 尽管这样也可以工作，但这使得你的代码依赖于 threading 库，所以你的这些代
# 码只能在线程上下文中使用。上文所写的那些代码、函数都是与 threading 库无关的，
# 这样就使得这些代码可以被用在其他的上下文中，可能与线程有关，也可能与线程无
# 关。比如，你可以通过 multiprocessing 模块在一个单独的进程中执行你的代码
'''
import multiprocessing

c = CountdownTask(10, 5)
p = multiprocessing.Process(target=c.run)
p.start()
'''

# 再次重申，这段代码仅适用于 CountdownTask 类是以独立于实际的并发手段（多线程、多进程等等）实现的情况。


if __name__ == '__main__':
    # t = Thread(target=countdown, args=(10, 3))
    t = Thread(target=countdown, args=(10, 3), daemon=True)

    print("start")
    t.start()

    t.join()
    print("exit")

    c = CountdownTask()
    t = Thread(target=c.run, args=(10, 3))
    print("start")
    t.start()

    time.sleep(3)

    c.terminate() # Signal termination
    t.join() # Wait for actual termination (if needed)

    print("exit")


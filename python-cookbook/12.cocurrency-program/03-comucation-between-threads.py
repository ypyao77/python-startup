#!/usr/bin/env python3

# 12.3 线程间通信

# 你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据

import time
from queue import Queue
from threading import Thread

# 1.
# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
# 创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。

# A thread that produces data
def producer(out_q):
    data = 0

    for i in range(5):
        # Produce some data
        data = data + 1
        print("put: %s" %(data))
        out_q.put(data)
        time.sleep(1)

# A thread that consumes data
def consumer(in_q):
    for i in range(5):
        # Get some data
        data = in_q.get()
        # Process the data
        print("got: %s" %(data))


# 2.
# Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。
# 当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。
# 一个通用的解决方法是在队列中放置一个特殊的值，当消费者读到这个值的时候，终止执行。

if __name__ == '__main__':
    # Create the shared queue and launch both threads
    q = Queue()

    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()







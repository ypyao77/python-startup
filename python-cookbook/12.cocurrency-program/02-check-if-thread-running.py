#!/usr/bin/env python3

# 12.2 判断线程是否已经启动

# 你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了。
from threading import Thread, Event
import time

# 1. event
# 线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其
# 他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时线程同步问题就
# 会变得非常棘手。为了解决这些问题，我们需要使用 threading 库中的 Event 对象。
# Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初
# 始情况下， event 对象中的信号标志被设置为假。如果有线程等待一个 event 对象，而
# 这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。一个线程
# 如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的线
# 程。如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，继
# 续执行。下边的代码展示了如何使用 Event 来协调线程的启动

# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()

    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# 2. condition
# event 对象最好单次使用，就是说，你创建一个 event 对象，让某个线程等待这个
# 对象，一旦这个对象被设置为真，你就应该丢弃它。尽管可以通过 clear() 方法来重置
# event 对象，但是很难确保安全地清理 event 对象并对它重新赋值。很可能会发生错
# 过事件、死锁或者其他问题（特别是，你无法保证重置 event 对象的代码会在线程再次
# 等待这个 event 对象之前执行）。如果一个线程需要不停地重复使用 event 对象，你最
# 好使用 Condition 对象来代替。下面的代码使用 Condition 对象实现了一个周期定时
# 器，每当定时器超时的时候，其他线程都可以监测到

# 3.semaphore or condition
# event 对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程。如果你
# 只想唤醒单个线程，最好是使用信号量或者 Condition 对象来替代。


if __name__ == '__main__':
    # 当你执行这段代码，“countdown is running”总是显示在“countdown starting”之
    # 后显示。这是由于使用 event 来协调线程，使得主线程要等到 countdown() 函数输出
    # 启动信息后，才能继续执行。

    # Create the event object that will be used to signal startup
    started_evt = Event()

    # Launch the thread and pass the startup event
    print('Launching countdown')
    t = Thread(target=countdown, args=(10,started_evt), daemon=True)
    t.start()

    # Wait for the thread to start
    started_evt.wait()
    print('countdown is running')

    t.join()
    print("exit")




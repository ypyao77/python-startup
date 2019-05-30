#!/usr/bin/env python3

# 12.5 防止死锁的加锁机制

import sys
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield

    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


# 你正在写一个多线程程序，其中线程需要一次获取多个锁，此时如何避免死锁问题。

# 1. 非死锁
# 在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的。举个例子：
# 一个线程获取了第一个锁，然后在获取第二个锁的时候发生阻塞，那么这个线程就
# 可能阻塞其他线程的执行，从而导致整个程序假死。解决死锁问题的一种方案是为程序
# 中的每一个锁分配一个唯一的 id，然后只允许按照升序规则来使用多个锁，这个规则
# 使用上下文管理器是非常容易实现的
def f1():
    x_lock = threading.Lock()
    y_lock = threading.Lock()

    def thread_1():
        c = 0
        while True:
            with acquire(x_lock, y_lock):
                c = c + 1
                if c % 100 == 0:
                    print('Thread-1')

    def thread_2():
        c = 0
        while True:
            with acquire(y_lock, x_lock):
                c = c + 1
                if c % 100 == 0:
                    print('Thread-2')

    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

    t1.join()
    t2.join()


# 2. 死锁
# 如果你执行这段代码，你会发现它即使在不同的函数中以不同的顺序获取锁也没
# 有发生死锁。其关键在于，在第一段代码中，我们对这些锁进行了排序。通过排序，使
# 得不管用户以什么样的顺序来请求锁，这些锁都会按照固定的顺序被获取。如果有多个
# acquire() 操作被嵌套调用，可以通过线程本地存储（ TLS）来检测潜在的死锁问题。
def f2():
    x_lock = threading.Lock()
    y_lock = threading.Lock()

    def thread_1():
        c = 0
        while True:
            with acquire(x_lock):
                with acquire(y_lock):
                    c = c + 1
                    if c % 100 == 0:
                        print('Thread-1')

    def thread_2():
        c = 0
        while True:
            with acquire(y_lock):
                with acquire(x_lock):
                    c = c + 1
                    if c % 100 == 0:
                        print('Thread-2')

    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

    t1.join()
    t2.join()


# 3. 哲学家就餐问题
# 下面以一个关于线程死锁的经典问题：“哲学家就餐问题”，作为本节最后一个例
# 子。题目是这样的：五位哲学家围坐在一张桌子前，每个人面前有一碗饭和一只筷子。
# 在这里每个哲学家可以看做是一个独立的线程，而每只筷子可以看做是一个锁。每个哲
# 学家可以处在静坐、思考、吃饭三种状态中的一个。需要注意的是，每个哲学家吃饭是
# 需要两只筷子的，这样问题就来了：如果每个哲学家都拿起自己左边的筷子，那么他们
# 五个都只能拿着一只筷子坐在那儿，直到饿死。此时他们就进入了死锁状态。下面是一
# 个简单的使用死锁避免机制解决“哲学家就餐问题”的实现
def f3():
    # The philosopher thread
    def philosopher(left, right):
        while True:
            with acquire(left,right):
                print(threading.currentThread(), 'eating')

    # The chopsticks (represented by locks)
    NSTICKS = 5
    chopsticks = [threading.Lock() for n in range(NSTICKS)]

    # Create all of the philosophers
    for n in range(NSTICKS):
        t = threading.Thread(target=philosopher, args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
        t.start()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "f1":
            f1()

        elif sys.argv[1] == "f2":
            f2()

        elif sys.argv[1] == "f3":
            f3()

# NOTE: 最后，要特别注意到，为了避免死锁，所有的加锁操作必须使用 acquire() 函数。
# 如果代码中的某部分绕过 acquire 函数直接申请锁，那么整个死锁避免机制就不起作用了。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque

#
#
# deque 可以在多线程程序中安全地当作先进先出的栈使用， 而使用者不需要担心资源锁的问题
#
# 提供了同步（线程安全） 类 Queue、 LifoQueue 和
# PriorityQueue， 不同的线程可以利用这些数据类型来交换信息。 这三
# 个类的构造方法都有一个可选参数 maxsize， 它接收正整数作为输入
# 值， 用来限定队列的大小。 但是在满员的时候， 这些类不会扔掉旧的元
# 素来腾出位置。 相反， 如果队列满了， 它就会被锁住， 直到另外的线程
# 移除了某个元素而腾出了位置。 这一特性让这些类很适合用来控制活跃
# 线程的数量。
#

#
# multiprocessing
# 这个包实现了自己的 Queue， 它跟 queue.Queue 类似， 是设计给
# 进程间通信用的。 同时还有一个专门的multiprocessing.JoinableQueue 类型， 可以让任务管理变得更方便。
#
# asyncio
# Python 3.4 新提供的包， 里面有Queue、 LifoQueue、 PriorityQueue 和 JoinableQueue， 这些类受
# 到 queue 和 multiprocessing 模块的影响， 但是为异步编程里的任务管理提供了专门的便利。
#
# heapq
# 跟上面三个模块不同的是， heapq 没有队列类， 而是提供了
# heappush 和 heappop 方法， 让用户可以把可变序列当作堆队列或者优先队列来使用

# 示例 2-23 使用双向队列
if __name__ == "__main__":
    # ❶ maxlen 是一个可选参数， 代表这个队列可以容纳的元素的数量， 而且一旦设定， 这个属性就不能修改了。
    dq = deque(range(10), maxlen=10)
    print("dq: ", dq)

    # ❷ 队列的旋转操作接受一个参数 n， 当 n > 0 时， 队列的最右边的 n
    # 个元素会被移动到队列的左边。 当 n < 0 时， 最左边的 n 个元素会被
    # 移动到右边。
    dq.rotate(3)
    print("dq: ", dq)

    dq.rotate(-4)
    print("dq: ", dq)

    # ❸ 当试图对一个已满（len(d) == d.maxlen） 的队列做尾部添加操作
    # 的时候， 它头部的元素会被删除掉。 注意在下一行里， 元素 0 被删除了
    dq.appendleft(-1)
    print("dq: ", dq)

    # ❹ 在尾部添加 3 个元素的操作会挤掉 -1、 1 和 2。
    dq.extend([11, 22, 33])
    print("dq: ", dq)

    # ❺ extendleft(iter) 方法会把迭代器里的元素逐个添加到双向队列
    # 的左边， 因此迭代器里的元素会逆序出现在队列里。
    dq.extendleft([10, 20, 30, 40])
    print("dq: ", dq)

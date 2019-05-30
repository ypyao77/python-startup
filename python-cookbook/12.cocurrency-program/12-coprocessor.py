#!/usr/bin/env python3

# 12.12 使用生成器代替线程

import sys, time

# 你想使用生成器（协程）替代系统线程来实现并发。这个有时又被称为用户级线程或绿色线程。

# 要使用生成器实现自己的并发，你首先要对生成器函数和 yield 语句有深刻理解。
# yield 语句会让一个生成器挂起它的执行，这样就可以编写一个调度器，将生成器当做
# 某种“任务”并使用任务协作切换来替换它们的执行。要演示这种思想，考虑下面两个
# 使用简单的 yield 语句的生成器函数

# Two simple generator functions
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')

def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1

# 这些函数在内部使用 yield 语句，下面是一个实现了简单任务调度器的代码
from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        ''' Admit a newly started task to the scheduler '''
        self._task_queue.append(task)

    def run(self):
        ''' Run until there are no more tasks '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)

            except StopIteration:
                # Generator is no longer executing
                pass

def f1():
    # Example use
    sched = TaskScheduler()

    sched.new_task(countdown(10))
    sched.new_task(countdown(5))
    sched.new_task(countup(15))

    sched.run()

    for _ in range(5):
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "f1":
            f1()






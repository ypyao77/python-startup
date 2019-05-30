#!/usr/bin/env python3

# 13.13 实现一个计时器

import time

# 你想记录程序执行多个任务所花费的时间

# time 模块包含很多函数来执行跟时间有关的函数。尽管如此，通常我们会在此基础之上构造一个更高级的接口来模拟一个计时器。
class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    # Use 1: Explicit start/stop
    t = Timer()
    t.start()
    countdown(1000000)
    t.stop()
    print("t.elapsed: ", t.elapsed)

    # Use 2: As a context manager
    with t:
        countdown(1000000)
    print("t.elapsed: ", t.elapsed)

    with Timer() as t2:
        countdown(1000000)
    print("t.elapsed: ", t.elapsed)

    # 上述代码中由 Timer 类记录的时间是钟表时间，并包含了所有休眠时间。如果你
    # 只想计算该进程所花费的 CPU 时间，应该使用 time.process_time() 来代替
    t = Timer(time.process_time)
    with t:
        countdown(1000000)
    print("t.elapsed: ", t.elapsed)

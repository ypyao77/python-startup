# 纯计算的任务串行执行
import time


def task1():
    res = 1
    for i in range(1000000):
        res += i


def task2():
    res = 1
    for i in range(1000000):
        res *= i


start = time.time()
# 基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
task1()
task2()
stop = time.time()

print(stop - start)

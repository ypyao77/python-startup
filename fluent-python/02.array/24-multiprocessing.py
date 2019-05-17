#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 代码是由主进程里面的主线程从上到下执行的,
# 我们在主线程里面又创建了两个子进程，子进
# 程里面也是子线程在干活，这个子进程在主进
# 程里面

import multiprocessing
import time

def f0(a1):
    time.sleep(3)
    print(a1)

if __name__ == '__main__':#windows下必须加这句

    t = multiprocessing.Process(target=f0,args=(12,))
    t.daemon=True #将daemon设置为True，则主线程不比等待子进程，主线程结束则所有结束
    t.start()

    t2 = multiprocessing.Process(target=f0, args=(13,))
    t2.daemon = True
    t2.start()

    print('end')#默认情况下等待所有子进程结束，主进程才结束


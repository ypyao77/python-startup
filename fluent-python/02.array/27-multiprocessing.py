#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process,Pool
from multiprocessing import Manager
import time, os


def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def f1(a):
    time.sleep(a)
    print("({0}) thread({1}): foo {2}".format(gettime(), os.getpid(), a))

if __name__ =='__main__':
    pool = Pool(5)

    for i in range(5): #每次使用的时候会去进程池里面申请一个进程
        pool.apply(func=f1, args=(i,))
        print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "hello"))

    pool.close()
    pool.join()
    print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "done"))

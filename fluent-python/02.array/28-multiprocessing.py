#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process,Pool
from multiprocessing import Manager
import time, os


def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def Foo(i):
    print("({0}) thread({1}): foo {2}".format(gettime(), os.getpid(), i))
    time.sleep(10+1)
    return i+50

def Bar(arg):
    print("({0}) thread({1}): bar {2}".format(gettime(), os.getpid(), arg))


if __name__ =='__main__':
    pool = Pool(5)

    for i in range(10):
        # apply是去简单的去执行，而apply_async是执行完毕之后可以执行一
        # 个回调函数，起提示作用
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #是异步的
        print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "hello"))

    print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "wait"))

    pool.close() #不执行close会报错，因为join的源码里面有个断言会检验是否执行了该方法
    print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "close"))

    pool.join()  #等待所有子进程运行完毕，否则的话由于apply_async里面daemon是设置为True的，主进程不会等子进程，所欲函数可能会来不及执行完毕就结束了
    print("({0}) thread({1}): main {2}".format(gettime(), os.getpid(), "done"))
    # apply_async里面，等函数Foo执行完毕，它的返回结果会被当做参数传给Bar


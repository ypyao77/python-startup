#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process
from multiprocessing import Manager

import time
# 每个进程都创建一个列表，然后添加一个因素进去，
# 每个进程之间的数据是不能共享的

li = []

def f1(i):
    li.append(i)
    time.sleep(i)
    print('你好',li)

if __name__ =='__main__':#进程不能共用内存
    for i in range(10):
        p = Process(target=f1,args=(i,))
        p.start()


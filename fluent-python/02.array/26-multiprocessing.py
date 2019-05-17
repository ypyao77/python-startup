#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process
from multiprocessing import Manager

import time

def f1(i, dic):
    dic[i] = 200+i
    time.sleep(i)
    print(dic.values())

if __name__ =='__main__':#进程间默认不能共用内存
    manager = Manager()
    dic = manager.dict()#这是一个特殊的字典


    for i in range(10):
        p = Process(target=f1,args=(i, dic))
        p.start()
        p.join()


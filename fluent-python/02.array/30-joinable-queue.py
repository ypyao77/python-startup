#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 一个生产者+多个消费者
from multiprocessing import Process,JoinableQueue
import time,random

def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def consumer(name,q):
    while True:
        time.sleep(random.randint(1,2))
        res=q.get()
        print('(%s) \033[45m%s consumed %s\033[0m' %(gettime(), name,res))
        q.task_done()

def producer(seq,q):
    for item in seq:
        time.sleep(random.randrange(1,2))
        q.put(item)
        print('(%s) \033[46m produced %s\033[0m' %(gettime(), item))
    q.join()

if __name__ == '__main__':
    q=JoinableQueue()
    seq=('bag %s' %i for i in range(10))

    p1=Process(target=consumer,args=('消费者1',q,))
    p2=Process(target=consumer,args=('消费者2',q,))
    p3=Process(target=consumer,args=('消费者3',q,))

    p1.daemon=True
    p2.daemon=True
    p3.daemon=True

    p1.start()
    p2.start()
    p3.start()

    producer(seq,q)
    print('(%s) main thread' %(gettime()))



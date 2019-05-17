#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process,JoinableQueue
import time,random


def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def consumer(q):
    while True:
        time.sleep(random.randint(1,5))
        res=q.get()
        print('(%s) consumed %s' %(gettime(), res))
        q.task_done()

def producer(seq,q):
    for item in seq:
        time.sleep(random.randrange(1,2))
        q.put(item)
        print('(%s) produced %s' %(gettime(), item))
    q.join()

if __name__ == '__main__':
    q = JoinableQueue()
    seq = ('bag %s' %i for i in range(10))

    p = Process(target=consumer,args=(q,))
    p.daemon = True
    p.start()

    producer(seq,q)
    print('(%s) main thread' %(gettime()))

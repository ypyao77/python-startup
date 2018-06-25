import time


def consumer():
    '''任务1:接收数据,处理数据'''
    while True:
        x = yield


def producer():
    '''任务2:生产数据'''
    g = consumer()
    next(g)
    for i in range(5):
        g.send(i)
        time.sleep(1)


start = time.time()
producer()  # 并发执行,但是任务producer遇到io就会阻塞住,并不会切到该线程内的其他任务去执行

stop = time.time()
print(stop - start)

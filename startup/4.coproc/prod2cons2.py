import time


def consumer():
    msg_no = 0
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        msg_no += 1
        r = '200 OK: {0}'.format(msg_no)


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
        time.sleep(1)
    c.close()


c = consumer()
produce(c)

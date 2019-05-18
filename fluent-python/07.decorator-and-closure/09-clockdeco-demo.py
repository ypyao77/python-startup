#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 改进后的 clock 装饰器

import time
from clockdeco2 import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

@clock
def sum2(*arg):
    return sum(arg)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

    print("sum2(1, 2, 3): %s" %(sum2(1, 2, 3)))
    print("factorial.__name__: %s" %(factorial.__name__))

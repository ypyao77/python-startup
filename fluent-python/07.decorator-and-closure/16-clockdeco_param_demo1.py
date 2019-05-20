#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from clockdeco_param import clock

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

if __name__ == "__main__":
    for i in range(3):
        snooze(.123)

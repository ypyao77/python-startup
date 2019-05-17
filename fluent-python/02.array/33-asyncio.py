#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys
import asyncio

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

# 定义异步函数
async def hello():
    asyncio.sleep(1)
    info("hello world")

def run():
    for i in range(5):
        asyncio.get_event_loop().run_until_complete(hello())


if __name__ =='__main__':
    info("go")
    run()
    info("done")



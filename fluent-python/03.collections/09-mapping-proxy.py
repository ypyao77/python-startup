#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

from types import MappingProxyType


if __name__ =='__main__':
    d = {1:'A'}
    d_proxy = MappingProxyType(d)
    info("d_proxy: %s" %(d_proxy))
    info("d_proxy[1]: %s" %(d_proxy[1]))

    try:
        d_proxy[2] = 'x'
    except Exception as err:
        error("exception: %s" %(err))

    d[2] = 'B'
    info("d_proxy: %s" %(d_proxy))
    info("d_proxy[2]: %s" %(d_proxy[2]))


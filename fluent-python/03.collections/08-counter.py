#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

import collections


if __name__ =='__main__':
    ct = collections.Counter('abracadabra')
    info("ct: %s" %(ct))

    ct.update('aaaaazzz')
    info("ct: %s" %(ct))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error

from unicodedata import name

if __name__ =='__main__':
    s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
    info("s: %s" %(s))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
from unicodedata import normalize

if __name__ =='__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'

    print("s1: %s" %(s1))
    print("s2: %s" %(s2))

    print("len(s1): %s" %(len(s1)))
    print("len(s2): %s" %(len(s2)))

    print("s1 == s2: %s" %(s1 == s2))

    print("len(s1), len(s2): %s, %s" %(len(s1), len(s2)))
    print("len(normalize('NFC', s1)), len(normalize('NFC', s2)): %s, %s" %(len(normalize('NFC', s1)), len(normalize('NFC', s2))))
    print("len(normalize('NFD', s1)), len(normalize('NFD', s2)): %s, %s" %(len(normalize('NFD', s1)), len(normalize('NFD', s2))))

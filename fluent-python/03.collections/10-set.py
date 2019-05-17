#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


if __name__ =='__main__':
    l = ['spam', 'spam', 'eggs', 'spam']

    s = set(l)
    info("s: %s" %(s))

    l2 = list(s)
    info("l2: %s" %(l2))


    s1 = set([a for a in "abcdef"])
    s2 = set([a for a in "defgh"])

    info("s1: %s" %(s1))
    info("s2: %s" %(s2))

    # info("s1+s2: %s" %(s1+s2))
    info("s1|s2: %s" %(s1|s2))

    info("s1&s2: %s" %(s1&s2))
    info("s1-s2: %s" %(s1-s2))


    needles = [a+"@fn" for a in "aaaaaaabcdef"]
    haystack = [a+"@fn" for a in "defdefdefghghghg"]
    #
    info("set(needles) & set(haystack): %s" %(set(needles) & set(haystack)))
    # 另一种写法：
    info("set(needles).intersection(haystack): %s" %(set(needles).intersection(haystack)))

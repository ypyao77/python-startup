#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


if __name__ =='__main__':
    tt = (1, 2, (30, 40))
    info("hash(tt): {0}".format(hash(tt)))

    tl = (1, 2, [30, 40])
    try:
        info("hash(tl): {0}".format(hash(tl)))
    except Exception as err:
        warn("throw: {0}".format(err))

    tf = (1, 2, frozenset([30, 40]))
    info("hash(tf): {0}".format(hash(tf)))

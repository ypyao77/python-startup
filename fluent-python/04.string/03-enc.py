#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


if __name__ =='__main__':
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Niño'.encode(codec), sep='\t')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import random
from array import array

with open('floats-10M-lines.txt', 'w') as f:
    l = [str(random()) for i in range(10**7)]
    f.write('\n'.join(l))

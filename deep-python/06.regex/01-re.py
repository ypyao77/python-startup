#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

if __name__ == "__main__":
    s = '100 NORTH BROAD ROAD'
    print("s: {0}".format(s))
    print("s.replace('ROAD', 'RD.'): {0}".format(s.replace('ROAD', 'RD.')))
    print("re.sub('ROAD$', 'RD.', s): {0}".format(re.sub('ROAD$', 'RD.', s)))
    print("re.sub(r'\\bROAD\\b', 'RD.', s): {0}".format(re.sub(r'\bROAD\b', 'RD.', s)))
    print("")

    s = '100 BROAD ROAD APT. 3'
    print("s: {0}".format(s))
    print("s.replace('ROAD', 'RD.'): {0}".format(s.replace('ROAD', 'RD.')))
    print("re.sub('ROAD$', 'RD.', s): {0}".format(re.sub('ROAD$', 'RD.', s)))
    print("re.sub(r'\\bROAD\\b', 'RD.', s): {0}".format(re.sub(r'\bROAD\b', 'RD.', s)))
    print("")

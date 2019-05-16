#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

if __name__ == "__main__":
    # 要匹配这些电话格式
    # • 800‐555‐1212
    # • 800 555 1212
    # • 800.555.1212
    # • (800) 555‐1212
    # • 1‐800‐555‐1212
    # • 800‐555‐1212‐1234
    # • 800‐555‐1212x1234
    # • 800‐555‐1212 ext. 1234
    # • work 1‐(800) 555.1212 #1234
    phonePattern = re.compile(r'^(\d{3})‐(\d{3})‐(\d{4})$')
    phonePattern.search('800‐555‐1212').groups()
    phonePattern.search('800‐555‐1212‐1234')

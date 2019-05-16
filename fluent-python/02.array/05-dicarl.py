#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)

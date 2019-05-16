#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    symbols = '$¢£¥€¤'

    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print("beyond_ascii: {0}".format(beyond_ascii))

    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print("beyond_ascii: {0}".format(beyond_ascii))




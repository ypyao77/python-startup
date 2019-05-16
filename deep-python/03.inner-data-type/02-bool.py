#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Bool(cond):
    if cond:
        print("{0}: is true".format(cond))
    else:
        print("{0}: is false".format(cond))


if __name__ == "__main__":
    Bool(None)
    Bool("")
    Bool("abc")
    Bool([])
    Bool([1,2,3])
    Bool({})
    Bool({"a": 1, "b": 2, "c": 3})


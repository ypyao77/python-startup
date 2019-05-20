#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import wrapt

# without argument in decorator
@wrapt.decorator
def logging1(wrapped, instance, args, kwargs):  # instance is must
    print("[DEBUG]: enter {}()".format(wrapped.__name__))
    return wrapped(*args, **kwargs)

@logging1
def say(something): pass

def logging2(level):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print("[{}]: enter {}()".format(level, wrapped.__name__))
        return wrapped(*args, **kwargs)

    return wrapper

@logging2(level="INFO")
def do(work): pass

if __name__ == "__main__":
    say("hello world")

    do("hello world")

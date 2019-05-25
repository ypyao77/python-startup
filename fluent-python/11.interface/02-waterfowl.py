#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Artist:
    def draw(self): pass

class Gunslinger:
    def draw(self): pass

class Lottery:
    def draw(self): pass

class Struggle:
    def __len__(self): return 23


from collections import abc

if __name__ == "__main__":
    print(isinstance(Struggle(), abc.Sized))

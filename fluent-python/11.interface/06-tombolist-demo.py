#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tombola import Tombola
from tombolist import TomboList


if __name__ == "__main__":
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))

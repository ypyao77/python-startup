#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    p = (4, 5)
    x, y = p
    print(x)
    print(y)

    data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
    name, shares, price, date = data
    print(name)
    print(date)

    data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
    name, shares, price, (year, mon, day) = data
    print(name)
    print(year)


    s = "hello"
    a, b, c, _, _ = s
    print(a)
    print(c)

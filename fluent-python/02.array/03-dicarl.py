#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']

    tshirts = [(color, size) for color in colors for size in sizes]
    print("tshirts: {0}".format(tshirts))

    for color in colors:
        for size in sizes:
            print((color, size))

    tshirts = [(color, size) for size in sizes for color in colors]
    print("tshirts: {0}".format(tshirts))

    ranks = [x for x in "2345678910JQKA"]
    ranks = [x for x in "JQKA"]
    suits = [x for x in "♠♡♣♢"]
    cards = [(rank, suit) for suit in suits for rank in ranks]
    print("cards: {0}".format(cards))

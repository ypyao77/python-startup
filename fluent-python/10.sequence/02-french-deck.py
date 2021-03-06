#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = "♠ ♥ ♣ ♦".split() # ♤ ♡ ♧ ♢ ♠ ♥ ♣ ♦

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, position):
    return self._cards[position]


if __name__ == "__main__":
    deck = FrenchDeck()

    print("len(deck): %s" %(len(deck)))
    #print("deck[6]: %s" %(deck[6]))
    #print("deck[31]: %s" %(deck[31]))
    print(deck[1])
    print(deck[2])
    print(deck[3])
    print(deck[11])
    print(deck[21])
    print(deck[31])
    print(deck[41])
    print(deck[-1])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 为FrenchDeck 打猴子补丁， 把它变成可变的， 让random.shuffle 函数能处理
from random import shuffle
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
    l = list(range(10))
    shuffle(l)
    print(l)

    deck = FrenchDeck()
    print(deck[:5])

    try:
        shuffle(deck)
        print(deck)
    except Exception as e:
        print(e)

    # ❶ 定义一个函数， 它的参数为 deck、 position 和 card
    def set_card(deck, position, card):
        deck._cards[position] = card

    # ❷ 把那个函数赋值给 FrenchDeck 类的 __setitem__ 属性
    FrenchDeck.__setitem__ = set_card

    # ❸ 现在可以打乱 deck 了， 因为 FrenchDeck 实现了可变序列协议所需的方法
    shuffle(deck)
    print(deck[:5])


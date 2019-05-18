#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from promotions import best_promo
from collections import namedtuple

# 内省单独的 promotions 模块， 构建 promos 列表
Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # ❶ 计算折扣只需调用 self.promotion() 函数。
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


if __name__ == "__main__":
    # ❶ 与示例 6-1 一样的测试固件
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)

    cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

    # ❷ 为了把折扣策略应用到 Order 实例上， 只需把促销函数作为参数传入
    print("Order(joe, cart, FidelityPromo()): %s" %(Order(joe, cart, best_promo)))
    print("Order(ann, cart, FidelityPromo()): %s" %(Order(ann, cart, best_promo)))

    banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

    # ❶ best_promo 为顾客 joe 选择 larger_order_promo
    print("Order(joe, banana_cart, BulkItemPromo()): %s" %(Order(joe, banana_cart, best_promo)))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

    # ❷ 订购大量香蕉时， joe 使用 bulk_item_promo 提供的折扣
    print("Order(joe, long_order, LargeOrderPromo()): %s" %(Order(joe, long_order, best_promo)))
    # ❸ 在一个简单的购物车中， best_promo 为忠实顾客 ann 提供fidelity_promo 优惠的折扣
    print("Order(joe, cart, LargeOrderPromo()): %s" %( Order(joe, cart, best_promo)))

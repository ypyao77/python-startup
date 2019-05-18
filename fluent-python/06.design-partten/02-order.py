#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from abc import ABC, abstractmethod
from collections import namedtuple


# Order 类和使用函数实现的折扣策略
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

# ❷ 没有抽象类
def fidelity_promo(order): # ❸ 各个策略都是函数
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

if __name__ == "__main__":
    # ❶ 与示例 6-1 一样的测试固件
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)

    cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]

    # ❷ 为了把折扣策略应用到 Order 实例上， 只需把促销函数作为参数传入
    print("Order(joe, cart, FidelityPromo()): %s" %(Order(joe, cart, fidelity_promo)))
    print("Order(ann, cart, FidelityPromo()): %s" %(Order(ann, cart, fidelity_promo)))

    banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]

    # ❸ 这个测试和下一个测试使用不同的促销函数
    print("Order(joe, banana_cart, BulkItemPromo()): %s" %(Order(joe, banana_cart, bulk_item_promo)))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]

    print("Order(joe, long_order, LargeOrderPromo()): %s" %(Order(joe, long_order, large_order_promo)))
    print("Order(joe, cart, LargeOrderPromo()): %s" %( Order(joe, cart, large_order_promo)))

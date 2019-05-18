#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ❶ promos 列表起初是空的
promos = []

# ❷ promotion 把 promo_func 添加到 promos 列表中， 然后原封不动地将其返回。
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

# ❸ 被 @promotion 装饰的函数都会添加到 promos 列表中
@promotion
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# ❹ best_promos 无需修改， 因为它依赖 promos 列表
def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

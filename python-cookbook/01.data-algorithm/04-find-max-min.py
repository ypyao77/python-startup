#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 怎样从一个集合中获得最大或者最小的 N 个元素列表
import heapq


if __name__ == "__main__":
    # heapq 模块有两个函数： nlargest() 和 nsmallest() 可以完美解决这个问题
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

    # 两个函数都能接受一个关键字参数，用于更复杂的数据结构中
    portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print("cheap, ", cheap)
    print("expensive: ", expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print("heap: ", heap)

    # 堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很
    # 容易的通过调用 heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
    # 用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)， N 是
    # 堆大小）。比如，如果想要查找最小的 3 个元素，你可以这样做
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))



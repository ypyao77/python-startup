#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ❶ 安装 NumPy 之后， 导入它（NumPy 并不是 Python 标准库的一部分）
import numpy

# 示例 2-22 对 numpy.ndarray 的行和列进行基本操作
if __name__ == "__main__":
    # ❷ 新建一个 0~11 的整数的 numpy.ndarry， 然后把它打印出来。
    a = numpy.arange(12)
    print("a: \n", a)

    print("type(a): ", type(a))

    # ❸ 看看数组的维度， 它是一个一维的、 有 12 个元素的数组
    print("a.shape: ", a.shape)

    # ❹ 把数组变成二维的， 然后把它打印出来看看
    a.shape = 3, 4
    print("a: \n", a)

    # ❺ 打印出第 2 行
    print("a[2]: ", a[2])

    # ❻ 打印第 2 行第 1 列的元素
    print("a[2, 1]: ", a[2, 1])

    # ❼ 把第 1 列打印出来
    print("a[:, 1]: ", a[:, 1])

    # ❽ 把行和列交换， 就得到了一个新数组
    print("a.transpose(): \n", a.transpose())

    print("a: \n", a)



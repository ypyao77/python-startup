#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ❶ 安装 NumPy 之后， 导入它（NumPy 并不是 Python 标准库的一部分）
import numpy

# ❹ 导入精度和性能都比较高的计时器（Python 3.3 及更新的版本中都有这个库） 。
from time import perf_counter as pc

# NumPy 也可以对 numpy.ndarray 中的元素进行抽象的读取、 保存和其他操作
if __name__ == "__main__":
    # ❶ 从文本文件里读取 1000 万个浮点数
    floats = numpy.loadtxt('floats-10M-lines.txt')

    # ❷ 利用序列切片来读取其中的最后 3 个数
    print("floats[-3:]: ", floats[-3:])

    # ❸ 把数组里的每个数都乘以 0.5， 然后再看看最后 3 个数
    floats *= .5
    print("floats[-3:]: ", floats[-3:])

    # ❺ 把每个元素都除以 3， 可以看到处理 1000 万个浮点数所需的时间还不足 40 毫秒
    t0 = pc(); floats /= 3; pc() - t0

    # ❻ 把数组存入后缀为 .npy 的二进制文件。
    numpy.save('floats-10M', floats)

    # ❼ 将上面的数据导入到另外一个数组里， 这次 load 方法利用了一种叫
    # 作内存映射的机制， 它让我们在内存不足的情况下仍然可以对数组做切片。
    floats2 = numpy.load('floats-10M.npy', 'r+')

    # ❽ 把数组里每个数乘以 6 之后， 再检视一下数组的最后 3 个数
    floats2 *= 6
    floats2[-3:]

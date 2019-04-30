#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np 


# NumPy提供常见的数学函几种方法可以沿不同轴将数组堆叠在一起
print("-------------------------------------")
a = np.floor(10*np.random.random((2,2)))
print("a: ", a)
b = np.floor(10*np.random.random((2,2)))
print("b: ", b)

print("np.vstack((a,b)): ", np.vstack((a,b)))
print("np.hstack((a,b)): ", np.hstack((a,b)))

# 函数 column_stack 以列将一维数组合成二维数组，它等同与 vstack 对一维数组
print("-------------------------------------")
print("np.column_stack((a,b)): ", np.column_stack((a,b)))

a = np.array([4.,3.])
b = np.array([2.,8.])
print("a: ", a)
print("b: ", b)
print("a[:,np.newaxis]: ", a[:,np.newaxis])
print("b[:,np.newaxis]: ", b[:,np.newaxis])
print("np.column_stack((a[:,np.newaxis],b[:,np.newaxis])): ", np.column_stack((a[:,np.newaxis],b[:,np.newaxis])))
print("np.row_stack((a[:,np.newaxis],b[:,np.newaxis])): ", np.row_stack((a[:,np.newaxis],b[:,np.newaxis])))


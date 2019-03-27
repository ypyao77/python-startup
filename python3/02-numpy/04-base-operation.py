#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np 
import random


print("-------------------------------------")
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print("a           : ", a)
print("b           : ", b)

print("a - b       : ", a-b)
print("a * b       : ", a*b)

print("b**2        : ", b**2)
print("10*np.sin(a): ", 10*np.sin(a))
print("a < 35      : ", a<35)
print("np.sin(b)   : ", np.sin(b))

# 不像许多矩阵语言，NumPy中的乘法运算符 * 指示按元素计算，矩阵乘法可以使用 dot 函数或创建矩阵对象实现(参见教程中的矩阵章节)
print("-------------------------------------")
a = np.array([[1,1], [0,1]])
b = np.array([[2,0], [3,4]])
print("a*b: ", a*b)
print("np.dot(a, b): ", np.dot(a, b))

# 有些操作符像 += 和 *= 被用来更改已存在数组而不创建一个新的数组
print("-------------------------------------")
a = np.ones((2,3), dtype=np.int32)
b = np.random.random((2,3))
print("a: ", a)
print("b: ", b)

a *= 3
print("a: ", a)
print("b: ", b)

b += a
print("a: ", a)
print("b: ", b)

# 当运算的是不同类型的数组时，结果数组和更普遍和精确的已知(这种行为叫做upcast)
print("-------------------------------------")
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,np.pi,3)
print("a: ", a)
print("b: ", b)
print("b.dtype.name: ", b.dtype.name)
c = a+b
print("c: ", c)
print("c.dtype.name: ", c.dtype.name)
d = np.exp(c*1j)
print("d: ", d)
print("d.dtype.name: ", d.dtype.name)
a = np.random.random((2,3))
print("a: ", a)
print("a.sum(): ", a.sum())
print("a.min(): ", a.min())
print("a.max(): ", a.max())

# 这些运算默认应用到数组好像它就是一个数字组成的列表，无关数组的形状。然而，指定 axis 参数你可以吧运算应用到数组指定的轴上
print("-------------------------------------")
b = np.arange(12).reshape(3,4)
print("b: ", b)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))




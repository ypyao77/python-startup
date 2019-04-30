#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np 


# NumPy提供常见的数学函数如 sin , cos 和 exp 。在NumPy中，这些叫作“通用函数”(ufunc)。在NumPy里这些函数作用按数组的元素运算，产生一个数组作为输出
print("-------------------------------------")
b = np.arange(3)
print("b: ", b)
print("np.exp(b): ", np.exp(b))
print("np.sqrt(b): ", np.sqrt(b))

c = np.array([2., -1., 4.])
print("c: ", c)
print("np.add(b, c): ", np.add(b, c))

d = np.linspace(0, 3.14, 3)
print("d: ", d)

e = np.linspace(0,np.pi,3)
print("e: ", e)
print("np.pi: ", np.pi)

# 一维 数组可以被索引、切片和迭代
print("-------------------------------------")
a = np.arange(10)**3
print("a: ", a)
print("a[2]: ", a[2])
print("a[2:5]: ", a[2:5])
a[:6:2] = -1000
print("a: ", a)
print("a[::-1]: ", a[::-1])
print("a: ", a)

# 多维 数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出
print("-------------------------------------")
def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print("b: ", b)
print("b[2,3]: ", b[2,3])
print("b[1,0]: ", b[1,0])
print("b[0:4, 1]: ", b[0:4, 1])
print("b[0:5, 1]: ", b[0:5, 1])
print("b[ : ,1]: ", b[ : ,1])
print("b[1:3, : ]: ", b[1:3, : ])
print("b[1:4, : ]: ", b[1:4, : ])

# 当少于轴数的索引被提供时，确失的索引被认为是整个切片
print("b[-1]: ", b[-1])
for row in b:
    print("row: ", row)

for element in b.flat:
    print(element,)

# 更改数组的形状
# 一个数组的形状由它每个轴上的元素个数给出
print("-------------------------------------")
a = np.floor(10*np.random.random((3,4)))
print("a: ", a)
print("a.shape: ", a.shape)
print("a.ravel(): ", a.ravel())
a.shape = (6, 2)
print("a.transpose(): ", a.transpose())
a.shape = (4, 3)
print("a.transpose(): ", a.transpose())
a.shape = (3, 4)
print("a.transpose(): ", a.transpose())

# reshape 函数改变参数形状并返回它，而 resize 函数改变数组自身
print("-------------------------------------")
a = np.array([[ 7.,  5.],
       [ 9.,  3.],
       [ 7.,  2.],
       [ 7.,  8.],
       [ 6.,  8.],
       [ 3.,  2.]])
print("a: ", a)
a.resize((2,6))
print("a: ", a)
a.resize((3,4))
print("a: ", a)


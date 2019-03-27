#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

print(np.array([1, 2, 3]))

print(np.array([1, 2, 3, 4, 5], ndmin=2))

print(np.array([1, 2, 3], dtype=complex))

a = np.array([[1, 2], [3, 4]])
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

a = np.arange(15).reshape(3, 5)
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

a = np.zeros((3,4))
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

a = np.arange( 10, 31, 5 )
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

a = np.ones((2,3,4), dtype=np.int16)
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

print(np.arange(10000))
print(np.arange(10000).reshape(100,100))
print(np.arange(10000).reshape(2000,5))

np.set_printoptions(threshold=10000)
print(np.arange(10000).reshape(100,100))


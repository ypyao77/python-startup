#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


#
dt = np.dtype(np.int32)
print(dt)

#
dt = np.dtype('i4')
print(dt)

#
dt = np.dtype('<i4')
print(dt)

#
dt = np.dtype([('age',np.int8)])
print(dt)

#
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)

#
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])

#
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

#
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print("a = ", a)
print("a.ndim = ", a.ndim)
print("a.shape = ", a.shape)
print("a.size = ", a.size)
print("a.dtype = ", a.dtype)
print("a.itemsize = ", a.itemsize)
print("a.data = ", a.data)

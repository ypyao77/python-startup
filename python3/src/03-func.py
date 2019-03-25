#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def change_int(a):
    a = 10


b = 2
change_int(b)
print(b)  # 结果是 2


# 可写函数说明
def change_me(mylist):
    '''修改传入的列表'''
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
l = [10, 20, 30]
change_me(l)
print("函数外取值: ", l)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)


# lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


def f1():
    pass


print("f1(): ", f1())


vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print("[x*y for x in vec1 for y in vec2]: ", [x*y for x in vec1 for y in vec2])
print("[x+y for x in vec1 for y in vec2]: ", [x+y for x in vec1 for y in vec2])
print("[vec1[i]*vec2[i] for i in range(len(vec1))]: ", [vec1[i]*vec2[i] for i in range(len(vec1))])


print("[str(round(355/113, i)) for i in range(1, 10)]: ", [str(round(355/113, i)) for i in range(1, 10)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 以下实例将3X4的矩阵列表转换为4X3列表
print("[[row[i] for row in matrix] for i in range(4)]: ", [[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("transposed: ", transposed)
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("transposed: ", transposed)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, "->", v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, "->", v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


















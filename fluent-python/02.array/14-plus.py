#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 对序列使用+和*
if __name__ == "__main__":
    l = [1, 2, 3]
    print("l: {0}".format(l))

    print("l * 5: {0}".format(l * 5))
    print("5 * 'abcd': {0}".format(5 * 'abcd'))

    board = [['_'] * 3 for i in range(3)]
    print("board: {0}".format(board))

    # 错误
    board[1][2] = 'X'
    print("board: {0}".format(board))

    # 正确
    weird_board = [['_'] * 3] * 3
    print("weird_board: {0}".format(weird_board))

    # 比如， 你想用 my_list = [[]] * 3 来初始化一个
    # 由列表组成的列表， 但是你得到的列表里包含的 3 个元素其实是 3
    # 个引用， 而且这 3 个引用指向的都是同一个列表。 这可能不是你想
    # 要的效果
    weird_board[1][2] = 'O'
    print("weird_board: {0}".format(weird_board))

    # 犯的错误本质上跟下面的代码犯的错误一样
    row=['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    board[2][0] = 'X'
    print("board: {0}".format(board))

    # 正确
    board = []
    for i in range(3):
        row = ['_'] * 3 # ➊
        board.append(row)
    print("board: {0}".format(board))

    # 列表的id不变
    l = [1, 2, 3]
    print("id(l): {0}".format(id(l)))

    l *= 2
    print("id(l): {0}".format(id(l)))

    # 元组的id发生变化
    t = (1, 2, 3)
    print("id(t): {0}".format(id(t)))

    t *= 2
    print("id(t): {0}".format(id(t)))

    # 一个谜题: 即抛出TypeError异常，又确实修改了tuple的值
    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]
    except:
        pass
    print("t: {0}".format(t))




#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # 整型替换字段被当做传给 format() 方法的参数列表的位置索引. 即{0}会被第一个参数替换(在此例中即 username), {1}被第二个参数替换(password)
    username = 'mark'
    password = 'PapayaWhip'
    print("{0}'s password is {1}".format(username, password))



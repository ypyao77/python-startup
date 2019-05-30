#!/usr/bin/env python3

# 13.12 给函数库增加日志功能

import os, sys

# 你想给某个函数库增加日志功能，但是又不能影响到那些不使用日志功能的程序。

# 对于想要执行日志操作的函数库而已，你应该创建一个专属的 logger 对象，并且像下面这样初始化配置

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
    if len(sys.argv) > 2:
        findfile(sys.argv[1], sys.argv[2])

        raise SystemExit("done")
    else:
        print("NULL")


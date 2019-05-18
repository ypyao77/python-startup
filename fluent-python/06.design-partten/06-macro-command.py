#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from abc import ABC, abstractmethod

class MacroCommand:
    """一个执行一组命令的命令"""
    def __init__(self, commands):
        # ❶ 使用 commands 参数构建一个列表， 这样能确保参数是可迭代对象，
        # 还能在各个 MacroCommand 实例中保存各个命令引用的副本
        self.commands = list(commands)
        
    def __call__(self):
        # ❷ 调用 MacroCommand 实例时， self.commands 中的各个命令依序执行
        for command in self.commands:
            command()


if __name__ == "__main__":
    pass




#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
from collections import OrderedDict
import json

if __name__ == "__main__":
    # 为 了 能 控 制 一 个 字 典 中 元 素 的 顺 序， 你 可 以 使 用 collections 模 块 中 的
    # OrderedDict 类。在迭代操作的时候它会保持元素被插入时的顺序
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])

    # 当你想要构建一个将来需要序列化或编码成其他格式的映射的时候， OrderedDict是非常有用的。
    # 比如，你想精确控制以 JSON 编码后字段的顺序，你可以先使用OrderedDict 来构建这样的数据
    print("json.dumps(d): ", json.dumps(d))


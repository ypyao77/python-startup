#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error
from tagger import tag
from functools import partial

# 把 partial 应用到示例 5-10 中定义的 tag 函数上
if __name__ =='__main__':
    # ❶ 从示例 5-10 中导入 tag 函数， 查看它的 ID
    print("tag: %s" %(tag))

    # ❷ 使用 tag 创建 picture 函数， 把第一个定位参数固定为 'img'， 把cls 关键字参数固定为 'pic-frame'
    picture = partial(tag, 'img', cls='pic-frame')
    # ❸ picture 的行为符合预期
    picture(src='o.jpg')

    # ❹ partial() 返回一个 functools.partial 对象
    print("picture: %s" %(picture))

    # ❺ functools.partial 对象提供了访问原函数和固定参数的属性
    print("picture.func: %s" %(picture.func))
    print("picture.args: %s" %())
    print("picture.keywords: %s" %(picture.keywords))



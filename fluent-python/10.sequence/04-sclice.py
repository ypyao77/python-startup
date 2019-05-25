#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 了解 __getitem__ 和切片的行为
class MySeq:
    def  __getitem__(self, index):
        # ❶ 在这个示例中， __getitem__ 直接返回传给它的值
        return index

if __name__ == "__main__":
    s = MySeq()

    # ❷ 单个索引， 没什么新奇的
    print(s[1])

    # ❸ 1:4 表示法变成了 slice(1, 4, None)
    print(s[1:4])
    # ❹ slice(1, 4, 2) 的意思是从 1 开始， 到 4 结束， 步幅为 2
    print(s[1:4:2])

    # ❺ 神奇的事发生了： 如果 [] 中有逗号， 那么 __getitem__ 收到的是元组。
    print(s[1:4:2, 9])

    # ❻ 元组中甚至可以有多个切片对象
    print(s[1:4:2, 7:9])

    # ❶ slice 是内置的类型（2.4.2 节首次出现）
    print(slice)

    # ❷ 通过审查 slice， 发现它有 start、 stop 和 step 数据属性， 以及indices 方法
    print(dir(slice))

    # ❶ 'ABCDE'[:10:2] 等同于 'ABCDE'[0:5:2]
    print(slice(None, 10, 2).indices(5))

    # ❷ 'ABCDE'[-3:] 等同于 'ABCDE'[2:5:1]
    print(slice(-3, None, None).indices(5))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import array

# 示例 2-21 通过改变数组中的一个字节来更新数组里某个元素的值
if __name__ == "__main__":
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    print("numbers: ", numbers)

    # ❶ 利用含有 5 个短整型有符号整数的数组（类型码是 'h'） 创建一个memoryview。
    memv = memoryview(numbers)

    # ❷ memv 里的 5 个元素跟数组里的没有区别。
    print("len(memv): ", len(memv))
    print("memv[0]: ", memv[0])

    # ❸ 创建一个 memv_oct， 这一次是把 memv 里的内容转换成 'B' 类型，
    # 也就是无符号字符。
    memv_oct = memv.cast('B')

    # ❹ 以列表的形式查看 memv_oct 的内容。
    print("memv_oct.tolist(): ", memv_oct.tolist())

    # ❺ 把位于位置 5 的字节赋值成 4。
    memv_oct[5] = 4

    # ❻ 因为我们把占 2 个字节的整数的高位字节改成了 4， 所以这个有符号
    # 整数的值就变成了 1024。
    print("numbers: ", numbers)




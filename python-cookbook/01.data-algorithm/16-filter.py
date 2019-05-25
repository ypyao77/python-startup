#!/usr/bin/env python3


# 过滤序列元素
# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
if __name__ == "__main__":
    # 最简单的过滤序列元素的方法就是使用列表推导
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]

    m = [n for n in mylist if n > 0]
    print("M: ", m)

    n = [n for n in mylist if n < 0]
    print("N: ", n)

    pos = (n for n in mylist if n > 0)
    print("pos: ", pos)
    for x in pos:
        print(x)

    # 有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出
    # 来。比如，假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过滤
    # 代码放到一个函数中，然后使用内建的 filter() 函数
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False

    # # filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例那样使用 list() 去转换
    ivals = list(filter(is_int, values))
    print(ivals)

    # 列表推导和生成器表达式通常情况下是过滤数据最简单的方式。其实它们还能在过滤的时候转换数据。
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    import math
    s = [math.sqrt(n) for n in mylist if n > 0]
    print("s: ", s)

    # 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。比
    # 如，在一列数据中你可能不仅想找到正数，而且还想将不是正数的数替换成指定的数。
    # 通过将过滤条件放到条件表达式中去，可以很容易的解决这个问题
    clip_neg = [n if n > 0 else 0 for n in mylist]
    print("clip_neg: ", clip_neg)
    clip_pos = [n if n < 0 else 0 for n in mylist]
    print("clip_pos: ", clip_pos)

    # 另外一个值得关注的过滤工具就是 itertools.compress() ，它以一个 iterable
    # 对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中对
    # 应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候，
    # 这个函数是非常有用的。
    addresses = [
                '5412 N CLARK',
                '5148 N CLARK',
                '5800 E 58TH',
                '2122 N CLARK',
                '5645 N RAVENSWOOD',
                '1060 W ADDISON',
                '4801 N BROADWAY',
                '1039 W GRANVILLE',
                ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

    # 现在你想将那些对应 count 值大于 5 的地址全部输出
    from itertools import compress
    more5 = [n > 5 for n in counts]
    print("more5: ", more5)

    # 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。然后
    # compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
    # 和 filter() 函数类似， compress() 也是返回的一个迭代器。因此，如果你需要得
    # 到一个列表，那么你需要使用 list() 来将结果转换为列表类型。
    l = list(compress(addresses, more5))
    print("l----: ", l)





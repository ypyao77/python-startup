#!/usr/bin/env python3


# 1.19 转换并同时计算数据
# 你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ），但是首先你需要先转换或者过滤数据
if __name__ == "__main__":
    # 一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。比如，如果你想计算平方和，可以像下面这样做
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)
    print(s)

    # 更多的例子
    import os
    files = os.listdir('.')
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')
    # Output a tuple as CSV
    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))
    # Data reduction across fields of a data structure
    portfolio = [
                    {'name':'GOOG', 'shares': 50},
                    {'name':'YHOO', 'shares': 75},
                    {'name':'AOL', 'shares': 20},
                    {'name':'SCOX', 'shares': 65}
                ]
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)


    # 你并不需要多加一个括号
    # s = sum((x * x for x in nums)) # 显示的传递一个生成器表达式对象
    # s = sum(x * x for x in nums)   # 更加优雅的实现方式，省略了括号

























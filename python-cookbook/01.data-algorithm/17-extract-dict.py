#!/usr/bin/env python3


# 从字典中提取子集
# 你想构造一个字典，它是另外一个字典的子集
# 最简单的方式是使用字典推导
if __name__ == "__main__":
    prices = {
                'ACME': 45.23,
                'AAPL': 612.78,
                'IBM': 205.55,
                'HPQ': 37.20,
                'FB': 10.75
            }

    # Make a dictionary of all prices over 200
    # 字典推导方式表意更清晰，并且实际上也会运行的更快些
    p1 = {key: value for key, value in prices.items() if value > 200}
    print("p1: ", p1)
    p1 = dict((key, value) for key, value in prices.items() if value > 200)
    print("p1: ", p1)

    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print("p2: ", p2)

    # 有时候完成同一件事会有多种方式。比如，第二个例子程序也可以像这样重写
    tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
    p2 = { key:prices[key] for key in prices.keys() & tech_names }






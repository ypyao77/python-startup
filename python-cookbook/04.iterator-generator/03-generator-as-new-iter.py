#!/usr/bin/env python3


# 4.3 使用生成器创建新的迭代模式
# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。

# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。下面是一个生产某个范围内浮点数的生成器
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。跟普通函数不同的是，生成器只能用于迭代操作。
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

if __name__ == "__main__":
    # 为了使用这个函数，你可以用 for 循环迭代它或者使用其他接受一个可迭代对象的函数 (比如 sum() , list() 等)。
    for n in frange(0, 4, 0.5):
        print(n)

    print("sum(frange(0, 4, 0.5)): ", sum(frange(0, 4, 0.5)))
    print("list(frange(0, 4, 0.5)): ", list(frange(0, 4, 0.5)))

    # Create the generator, notice no output appears
    c = countdown(3)
    try:
        for _ in range(5):
            print("next(c): ", next(c))
    except Exception as e:
        print(e)

#!/usr/bin/env python3


# 3.11 随机选择
# 你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
if __name__ == "__main__":
    # random 模块有大量的函数用来产生随机数和随机选择元素。比如，要想从一个序列中随机的抽取一个元素，可以使用 random.choice()
    import random

    values = list(range(10))
    print("values: ", values)
    print("random.choice(values): ", random.choice(values))
    print("random.choice(values): ", random.choice(values))
    print("random.choice(values): ", random.choice(values))
    print("random.choice(values): ", random.choice(values))

    # 为了提取出 N 个不同元素的样本用来做进一步的操作，可以使用 random.sample()
    print("random.sample(values, 2): ", random.sample(values, 2))
    print("random.sample(values, 2): ", random.sample(values, 2))
    print("random.sample(values, 3): ", random.sample(values, 3))
    print("random.sample(values, 3): ", random.sample(values, 3))

    # 如果你仅仅只是想打乱序列中元素的顺序，可以使用 random.shuffle()
    random.shuffle(values)
    print("random.shuffle(values): ", values)
    random.shuffle(values)
    print("random.shuffle(values): ", values)

    # 生成随机整数，请使用 random.randint()
    print("random.randint(0,10): ", random.randint(0,10))
    print("random.randint(0,10): ", random.randint(0,10))
    print("random.randint(0,10): ", random.randint(0,10))
    print("random.randint(0,10): ", random.randint(0,10))
    print("random.randint(0,10): ", random.randint(0,10))

    # 为了生成 0 到 1 范围内均匀分布的浮点数，使用 random.random()
    print("random.random(): ", random.random())
    print("random.random(): ", random.random())
    print("random.random(): ", random.random())
    print("random.random(): ", random.random())
    print("random.random(): ", random.random())

    # 如果要获取 N 位随机位 (二进制) 的整数，使用 random.getrandbits()
    print("random.getrandbits(200): ", random.getrandbits(200))

    # random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算
    # 法，但是你可以通过 random.seed() 函数修改初始化种子。
    random.seed()
    random.seed(12345)
    random.seed(b"bytedata")

    # 除了上述介绍的功能， random 模块还包含基于均匀分布、高斯分布和其他分布的随机数生成函数。
    # 比如， random.uniform() 计算均匀分布随机数， random.gauss() 计算正态分布随机数。
    # 对于其他的分布情况请参考在线文档

    # 在 random 模块中的函数不应该用在和密码学相关的程序中。如果你确实需要类似的功能，
    # 可以使用 ssl 模块中相应的函数。比如， ssl.RAND_bytes() 可以用来生成一个安全的随机字节序列。


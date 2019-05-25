#!/usr/bin/env python3


# 3.5 字节到大整数的打包与解包

# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。
if __name__ == "__main__":
    # 假设你的程序需要处理一个拥有 128 位长的 16 个元素的字节字符串。
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print("data: ", data)

    # 为了将 bytes 解析为整数，使用 int.from_bytes() 方法，并像下面这样指定字节顺序
    print("len(data): ", len(data))
    print("int.from_bytes(data, 'little'): ", int.from_bytes(data, 'little'))
    print("int.from_bytes(data, 'big'): ", int.from_bytes(data, 'big'))

    # 为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法，并像下面这样指定字节数和字节顺序
    x = 94522842520747284487117727783387188
    print("x.to_bytes(16, 'big'): ", x.to_bytes(16, 'big'))
    print("x.to_bytes(16, 'little'): ", x.to_bytes(16, 'little'))

    # 大整数和字节字符串之间的转换操作并不常见。然而，在一些应用领域有时候也会出现，比如密码学或者网络。
    # 例如， IPv6 网络地址使用一个 128 位的整数表示。如果你要从一个数据记录中提取这样的值的时候，你就会面对这样的问题。
    # 作为一种替代方案，你可能想使用 6.11 小节中所介绍的 struct 模块来解压字节。这样也行得通，
    # 不过利用 struct 模块来解压对于整数的大小是有限制的。因此，你可能想解压多个字节串并将结果合并为最终的结果，就像下面这样
    print("data: ", data)

    import struct
    hi, lo = struct.unpack('>QQ', data)
    print("(hi << 64) + lo: ", (hi << 64) + lo)

    # 字节顺序规则 (little 或 big) 仅仅指定了构建整数时的字节的低位高位排列方式。我们从下面精心构造的 16 进制数的表示中可以很容易的看出来
    x = 0x01020304
    print("x.to_bytes(4, 'big'): ", x.to_bytes(4, 'big'))
    print("x.to_bytes(4, 'little'): ",  x.to_bytes(4, 'little'))

    # 如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。
    # 如果需要的话，你可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
    x = 523 ** 23
    print("x: ", x)
    try:
        print("x.to_bytes(16, 'little'): ", x.to_bytes(16, 'little'))
    except Exception as e:
        print(e)

    print("x.bit_length(): ", x.bit_length())
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1

    print("x.to_bytes(nbytes, 'little'): ",  x.to_bytes(nbytes, 'little'))


#!/usr/bin/env python3


# 3.4 二八十六进制整数
# 你需要转换或者输出使用二进制，八进制或十六进制表示的整数.
if __name__ == "__main__":
    # 为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用 bin(), oct() 或 hex() 函数
    x = 1234
    print("bin(x): ", bin(x))
    print("oct(x): ", oct(x))
    print("hex(x): ", hex(x))

    # 如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数。
    print("format(x, 'b'): ", format(x, 'b'))
    print("format(x, 'o'): ", format(x, 'o'))
    print("format(x, 'x'): ", format(x, 'x'))
    print("format(x, 'X'): ", format(x, 'X'))

    # 整数是有符号的，所以如果你在处理负数的话，输出结果会包含一个负号
    x = -1234
    print("format(x, 'b'): ", format(x, 'b'))
    print("format(x, 'o'): ", format(x, 'o'))
    print("format(x, 'x'): ", format(x, 'x'))

    # 如果你想产生一个无符号值，你需要增加一个指示最大位长度的值。比如为了显示32 位的值
    x = -1234
    print("format(2**32 + x, 'b'): ", format(2**32 + x, 'b'))
    print("format(2**32 + x, 'x'): ", format(2**32 + x, 'x'))

    # 为了以不同的进制转换整数字符串，简单的使用带有进制的 int() 函数即可
    print("int('4d2', 16): ", int('4d2', 16))
    print("int('10011010010', 2): ", int('10011010010', 2))

    # 使用八进制的程序员有一点需要注意下。 Python 指定八进制数的语法跟其他语言稍有不同。
    # 需确保八进制数的前缀是 0o ，就像下面这样
    #   os.chmod('script.py', 0o755)










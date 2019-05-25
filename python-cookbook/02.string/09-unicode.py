#!/usr/bin/env python3


# 2.9 将 Unicode 文本标准化
# 你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。
if __name__ == "__main__":
    # 在 Unicode 中，某些字符能够用多个合法的编码表示。在 Unicode 中，某些字符能够用多个合法的编码表示。
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'

    print("s1: ", s1)
    print("s2: ", s2)
    print("s1 == s2: ", s1 == s2)
    print("len(s1): ", len(s1))
    print("len(s2): ", len(s2))

    # 这里的文本” Spicy Jalapeño”使用了两种形式来表示。第一种使用整体字符” ñ”
    # (U+00F1)，第二种使用拉丁字母” n”后面跟一个” ~”的组合字符 (U+0303)。

    # 在需要比较字符串的程序中使用字符的多种表示会产生问题。为了修正这个问题，
    # 你可以使用 unicodedata 模块先将文本标准化

    # normalize() 第一个参数指定字符串标准化的方式。
    #       NFC 表示字符应该是整体组成 (比如可能的话就使用单一编码)
    #       NFD 表示字符应该分解为多个组合字符表示
    import unicodedata
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print("t1 == t2: ", t1 == t2)
    print(ascii(t1))
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print("t3 == t4: ", t3 == t4)
    print(ascii(t3))






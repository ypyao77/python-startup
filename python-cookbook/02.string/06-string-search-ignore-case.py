#!/usr/bin/env python3


import re
# 2.6 字符串忽略大小写的搜索替换
# 你需要以忽略大小写的方式搜索与替换文本字符串
if __name__ == "__main__":
    # 为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供re.IGNORECASE 标志参数。
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print("text: ", text)
    print("re.findall('python', text, flags=re.IGNORECASE): ", re.findall('python', text, flags=re.IGNORECASE))
    print("re.sub('python', 'snake', text, flags=re.IGNORECASE): ", re.sub('python', 'snake', text, flags=re.IGNORECASE))

    # 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大
    # 小写保持一致。为了修复这个，你可能需要一个辅助函数
    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word

        return replace

    print("re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE): ", re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

















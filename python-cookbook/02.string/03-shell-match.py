#!/usr/bin/env python3


# 用 Shell 通配符匹配字符串
# 你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文本字符串
if __name__ == "__main__":
    # fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配。
    from fnmatch import fnmatch, fnmatchcase

    print("fnmatch('foo.txt', '*.txt'): ", fnmatch('foo.txt', '*.txt'))
    print("fnmatch('foo.txt', '?oo.txt'): ", fnmatch('foo.txt', '?oo.txt'))
    print("fnmatch('Dat45.csv', 'Dat[0-9]*'): ", fnmatch('Dat45.csv', 'Dat[0-9]*'))

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print("names: ", names)
    print("[name for name in names if fnmatch(name, 'Dat*.csv')]: ", [name for name in names if fnmatch(name, 'Dat*.csv')])

    # fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来匹配模式。
    # On OS X (Mac)
    fnmatch('foo.txt', '*.TXT') # False
    # # On Windows
    fnmatch('foo.txt', '*.TXT') # True

    # 如果你对这个区别很在意，可以使用 fnmatchcase() 来代替。它完全使用你的模式大小写匹配。
    fnmatchcase('foo.txt', '*.TXT')

    # 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的。比如，假设你有一个街道地址的列表数据
    addresses = [
                    '5412 N CLARK ST',
                    '1060 W ADDISON ST',
                    '1039 W GRANVILLE AVE',
                    '2122 N CLARK ST',
                    '4802 N BROADWAY',
                ]
    # 你可以像这样写列表推导
    from fnmatch import fnmatchcase
    print("[addr for addr in addresses if fnmatchcase(addr, '* ST')]: ", [addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print("[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]: ", [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])








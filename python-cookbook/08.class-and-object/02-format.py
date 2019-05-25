#!/usr/bin/env python3


# 8.2 自定义字符串的格式化

# 你想通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化。
_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 为了自定义字符串的格式化，我们需要在类上面定义 __format__() 方法。
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


if __name__ == "__main__":
    d = Date(2012, 12, 21)

    # 现在 Date 类的实例可以支持格式化操作了
    print("format(d): ", format(d))
    print("format(d, 'mdy'): ", format(d, 'mdy'))
    print("'The date is {:ymd}'.format(d): ", 'The date is {:ymd}'.format(d))
    print("'The date is {:mdy}'.format(d): ", 'The date is {:mdy}'.format(d))

    # __format__() 方法给 Python 的字符串格式化功能提供了一个钩子。这里需要着
    # 重强调的是格式化代码的解析工作完全由类自己决定。因此，格式化代码可以是任何
    # 值。例如，参考下面来自 datetime 模块中的代码
    from datetime import date
    d = date(2012, 12, 21)

    print("format(d): ", format(d))
    print("format(d,'%A, %B %d, %Y'): ", format(d,'%A, %B %d, %Y'))
    print("format(d,'%Y-%m-%d'): ", format(d,'%Y-%m-%d'))
    print("'The end is {:%d %b %Y}. Goodbye'.format(d): ", 'The end is {:%d %b %Y}. Goodbye'.format(d))





#!/usr/bin/env python3


# 7.9 将单方法的类转换为函数

# 你有一个除 __init__() 方法外只定义了一个方法的类。为了简化代码，你想将它转换成一个函数。
if __name__ == "__main__":
    from urllib.request import urlopen
    class UrlTemplate:
        def __init__(self, template):
            self.template = template

        def open(self, **kwargs):
            return urlopen(self.template.format_map(kwargs))

    # Example use. Download stock data from yahoo
    yahoo = UrlTemplate('http://arch-od-tracker01.beta1.fn:7180/cmf/login?s={names}&f=,!{fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))

    # 这个类可以被一个更简单的函数来代替：
    def urltemplate(template):
        def opener(**kwargs):
            return urlopen(template.format_map(kwargs))
        return opener

    # Example use
    yahoo = urltemplate('http://arch-od-tracker01.beta1.fn:7180/cmf/login?s={names}&f=,!{fields}')
    for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))




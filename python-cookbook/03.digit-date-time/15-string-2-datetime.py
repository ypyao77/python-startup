#!/usr/bin/env python3


# 3.15 字符串转换为日期
# 你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便在上面执行非字符串操作。



# 使用 Python 的标准模块 datetime 可以很容易的解决这个问题。
from datetime import datetime


if __name__ == "__main__":
    text = '2019-04-20'
    print("text: ", text)
    y = datetime.strptime(text, '%Y-%m-%d')
    print("y: ", y)
    z = datetime.now()
    print("z: ", z)
    diff = z - y
    print("diff: ", diff)

    # 假设你的代码中生成了一个 datetime 对象，你想将它格式化为漂亮易读形式后放在自动生成的信件或者报告的顶部
    print("z: ", z)
    nice_z = datetime.strftime(z, '%A %B %d, %Y')
    print("nice_z: ", nice_z)

    # strptime() 的性能要比你想象中的差很多，因为它是使用纯 Python 实现，并且必须处理所有的系统本地设置。
    # 如果你要在代码中需要解析大量的日期并且已经知道了日期字符串的确切格式，可以自己实现一套解析方案来获取更好的性能。
    # 比如，如果你已经知道所以日期格式是 YYYY-MM-DD ，你可以像下面这样实现一个解析函数

    from datetime import datetime
    def parse_ymd(s):
        year_s, mon_s, day_s = s.split('-')
        return datetime(int(year_s), int(mon_s), int(day_s))

    print("parse_ymd('2019-05-21'): ", parse_ymd('2019-05-21'))



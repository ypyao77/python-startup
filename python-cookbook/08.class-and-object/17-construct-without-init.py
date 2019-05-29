#!/usr/bin/env python3

# 8.17 创建不调用 init 方法的实例
# 你想创建一个实例，但是希望绕过执行 __init__() 方法


# 可以通过 __new__() 方法创建一个未初始化的实例
import time
class Date:
    """ 方法一：使用类方法"""
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __repr__(self):
        return "{:04d}-{:02d}-{:02d}".format(self.year, self.month, self.day)

class NewDate(Date):
    pass


if __name__ == "__main__":
    d = Date.__new__(Date)

    # 这个 Date 实例的属性 year 还不存在，所以你需要手动初始化
    data = {'year':2012, 'month':8, 'day':29}
    for key, value in data.items():
        setattr(d, key, value)

    print("d: ", d)



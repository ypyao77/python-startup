#!/usr/bin/env python3

# 8.16 在类中定义多个构造器
# 你想实现一个类，除了使用 __init__() 方法外，还有其他方式可以初始化它。

# 为了实现多个构造器，你需要使用到类方法。
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
    a = Date(2012, 12, 21) # Primary
    b = Date.today()

    print("a: ", a)
    print("b: ", b)

    c = Date.today() # Creates an instance of Date (cls=Date)
    d = NewDate.today() # Creates an instance of NewDate (cls=NewDate)

    print("c: ", c)
    print("d: ", d)



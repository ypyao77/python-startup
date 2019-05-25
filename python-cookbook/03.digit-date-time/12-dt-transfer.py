#!/usr/bin/env python3


# 3.12 基本的日期与时间转换
# 你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换
if __name__ == "__main__":
    # 为了执行不同时间单位的转换和计算，请使用 datetime 模块。比如，为了表示一个时间段，可以创建一个 timedelta 实例，
    from datetime import timedelta

    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)

    print("c.days: ", c.days)
    print("c.seconds/3600: ", c.seconds/3600)
    print("c.total_seconds()/3600: ", c.total_seconds()/3600)

    # 如果你想表示指定的日期和时间，先创建一个 datetime 实例然后使用标准的数学运算来操作它们。
    from datetime import datetime

    a = datetime(2012, 9, 23)
    print("a: ", a)
    print("a + timedelta(days=10): ", a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print("b: ", b)
    print("d: ", d)
    print("d.days: ", d.days)

    now = datetime.today()
    print("now: ", now)
    print("now + timedelta(minutes=10): ", now + timedelta(minutes=10))

    # 在计算的时候，需要注意的是 datetime 会自动处理闰年。
    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print("a: ", a)
    print("b: ", b)

    a - b
    (a - b).days
    print("a - b: ", a - b)
    print("(a - b).days: ", (a - b).days)

    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    (c - d).days
    print("c: ", c)
    print("d: ", d)
    print("(c - d).days: ", (c - d).days)

    # 对大多数基本的日期和时间处理问题， datetime 模块已经足够了。如果你需要执行更加复杂的日期操作，
    # 比如处理时区，模糊时间范围，节假日计算等等，可以考虑使用 dateutil 模块
    a = datetime(2012, 9, 23)
    print("a: ", a)
    print("a + timedelta(months=1): ", a + timedelta(months=1))

    from dateutil.relativedelta import relativedelta
    print("a + relativedelta(months=+1): ", a + relativedelta(months=+1))
    print("a + relativedelta(months=+4): ", a + relativedelta(months=+4))

    # Time between two dates
    b = datetime(2012, 12, 21)
    print("b: ", b)
    d = b - a
    print("d: ", c)

    d = relativedelta(b, a)
    print("d.months: ", d.months)
    print("d.days: ", d.days)



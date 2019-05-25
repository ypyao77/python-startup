#!/usr/bin/env python3


# 3.14 计算当前月份的日期范围
# 你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方法。



# 在这样的日期上循环并需要事先构造一个包含所有日期的列表。你可以先计算出开始日期和结束日期，
# 然后在你步进的时候使用 datetime.timedelta 对象递增这个日期变量即可。
# 下面是一个接受任意 datetime 对象并返回一个由当前月份开始日和下个月开始日组成的元组对象。
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

if __name__ == "__main__":
    # 有了这个就可以很容易的在返回的日期范围上面做循环操作了
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day

    # 上面的代码先计算出一个对应月份第一天的日期。一个快速的方法就是使用 date或 datetime 对象的 replace() 方法简单的将 days 属性设置成 1 即可。
    # replace() 方法一个好处就是它会创建和你开始传入对象类型相同的对象。所以，如果输入参数是一个 date 实例，那么结果也是一个 date 实例。
    # 同样的，如果输入是一个 datetime 实例，那么你得到的就是一个 datetime 实例。
    for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=24)):
        print(d)

    # 这种实现之所以这么简单，还得归功于 Python 中的日期和时间能够使用标准的数学和比较操作符来进行运算。




#!/usr/bin/env python3


# 3.13 计算最后一个周五的日期
# 你需要查找星期中某一天最后出现的日期，比如星期五。你需要查找星期中某一天最后出现的日期，比如星期五。

"""
Topic: 最后的周五
Desc :
"""
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上 (星期一索引为 0)，
# 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期减去那个时间差即得到结果日期。
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7

    target_date = start_date - timedelta(days=days_ago)
    return target_date


if __name__ == "__main__":
    # Python 的 datetime 模块中有工具函数和类可以帮助你执行这样的计算。下面是对类似这样的问题的一个通用解决方案
    print("datetime.today(): ", datetime.today())
    print("get_previous_byday('Monday'): ", get_previous_byday('Monday'))
    print("get_previous_byday('Tuesday'): ", get_previous_byday('Tuesday'))
    print("get_previous_byday('Friday'): ", get_previous_byday('Friday'))

    # 可选的 start_date 参数可以由另外一个 datetime 实例来提供。
    print("get_previous_byday('Sunday', datetime(2019, 5, 18)): ", get_previous_byday('Sunday', datetime(2019, 5, 18)))

    # 如果你要像这样执行大量的日期计算的话，你最好安装第三方包 python-dateutil来代替。
    # 比如，下面是是使用 dateutil 模块中的 relativedelta() 函数执行同样的计算：
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    from dateutil.rrule import *

    d = datetime.now()
    print("d: ", d)

    # Next Friday
    print("d + relativedelta(weekday=FR): ", d + relativedelta(weekday=FR))
    # Last Friday
    print("d + relativedelta(weekday=FR(-1)): ", d + relativedelta(weekday=FR(-1)))









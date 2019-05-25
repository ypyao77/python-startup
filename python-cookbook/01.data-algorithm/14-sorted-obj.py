#!/usr/bin/env python3

# 排序不支持原生比较的对象
# 你想排序类型相同的对象，但是他们不支持原生的比较操作

# 内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给
# 它，这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序
# 这些对象。比如，如果你在应用程序里面有一个 User 实例序列，并且你希望通过他们
# 的 user_id 属性进行排序，你可以提供一个以 User 实例作为输入并输出对应 user_id
# 值的 callable 对象。

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


if __name__ == "__main__":
    sort_notcompare()

    # 另外一种方式是使用 operator.attrgetter() 来代替 lambda 函数
    from operator import attrgetter
    users = [User(23), User(3), User(99)]
    print("sorted(users, key=attrgetter('user_id')): ", sorted(users, key=attrgetter('user_id')))

    # 选择使 用 lambda 函数或者 是 attrgetter() 可能取决 于个人 喜好。但是，
    # attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。这
    # 个跟 operator.itemgetter() 函数作用于字典类型很类似
    # by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
    m = min(users, key=attrgetter('user_id'))
    n = max(users, key=attrgetter('user_id'))
    print("min: ", m)
    print("max: ", n)



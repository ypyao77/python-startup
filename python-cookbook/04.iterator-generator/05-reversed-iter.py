#!/usr/bin/env python3


# 4.5 反向迭代
# 你想反方向迭代一个序列

# 很多程序员并不知道可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代。
class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == "__main__":
    # 使用内置的 reversed() 函数
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    # 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
    # 如果两者都不符合，那你必须先将对象转换为一个列表才行
    # Print a file backwards
    f = open('/etc/passwd')
    for line in reversed(list(f)):
        print(line, end='')

    print("reversed(Countdown(5))")
    for rr in reversed(Countdown(5)):
        print(" ", rr)

    print("Countdown(5)")
    for rr in Countdown(5):
        print(" ", rr)




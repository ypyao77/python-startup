#!/usr/bin/env python3

# 8.1 改变对象的字符串显示
# 你想改变对象实例的打印或显示输出，让它们更具可读性

# 要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法。
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # format() 方法的使用看上去很有趣，格式化代码 {0.x} 对应的是第 1 个参数的 x 属性。因此，在下面的函数中， 0 实际上指的就是 self 本身
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
        # 作为这种实现的一个替代，你也可以使用 % 操作符，
        #     return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == "__main__":
    p = Pair(3, 4)
    p # __repr__() output
    print(p) # __str__() output

    # 我们在这里还演示了在格式化的时候怎样使用不同的字符串表现形式。特别来讲，!r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__() 。
    print('p is: {0!r}'.format(p))
    print('p is: {0}'.format(p))



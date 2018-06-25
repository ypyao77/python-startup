class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def _getitem_(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            return self._getitem_(n)

        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1

            a, b = 1, 1
            L = []

            for x in range(stop):
                if x >= start:
                    if step > 1:
                        if ((x - start) % step) == 0:
                            L.append(a)
                    else:
                        L.append(a)
                a, b = b, a + b
            return L


i = 0
for n in Fib():
    print(n)
    if i >= 10:
        break

f = Fib()
print("f[0] = {0}".format(f[0]))
print("f[1] = {0}".format(f[1]))
print("f[2] = {0}".format(f[2]))
print("f[3] = {0}".format(f[3]))
print("f[4] = {0}".format(f[4]))
print("f[6] = {0}".format(f[6]))

print("f[6:20] = {0}".format(f[6:20]))
print("f[6:20:1] = {0}".format(f[6:20:1]))
print("f[6:20:2] = {0}".format(f[6:20:2]))

#!/usr/bin/env python3


# 4.1 手动遍历迭代器
# 你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环

# 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
def manual_iter1():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print("  " + line, end='')
        except StopIteration:
            pass

# 通常来讲， StopIteration 用来指示迭代的结尾。然而，如果你手动使用上面演示
# 的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。
def manual_iter2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print("  " + line, end='')

# 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
if __name__ == "__main__":
    print("manual_iter1(): ", manual_iter1())
    print("manual_iter2(): ", manual_iter2())

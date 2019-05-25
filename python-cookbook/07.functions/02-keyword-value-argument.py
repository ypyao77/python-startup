#!/usr/bin/env python3


# 7.2 只接受关键字参数的函数

# 你想构造一个可接受任意数量参数的函数。
# 将强制关键字参数放到某个 * 参数或者单个 * 后面就能达到这种效果
def recv(maxsize, *, block):
    'Receives a message'
    pass

# 利用这种技术，我们还能在接受任意多个位置参数的函数中指定关键字参数
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

if __name__ == "__main__":
    try:
        # TypeError
        recv(1024, True)
    except:
        pass
    # OK
    recv(1024, block=True)

    print("minimum(1, 5, 2, -5, 10): ", minimum(1, 5, 2, -5, 10))
    print("minimum(1, 5, 2, -5, 10, clip=0): ", minimum(1, 5, 2, -5, 10, clip=0))

    # 很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性。
    ''' msg = recv(1024, False) '''

    # 如果调用者对 recv 函数并不是很熟悉，那他肯定不明白那个 False 参数到底来干嘛用的。
    # 但是，如果代码变成下面这样子的话就清楚多了
    ''' msg = recv(1024, block=False) '''

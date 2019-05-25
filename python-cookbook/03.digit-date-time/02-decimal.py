#!/usr/bin/env python3


# 3.2 执行精确的浮点数运算
# 你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
if __name__ == "__main__":
    # 浮点数的一个普遍问题是它们并不能精确的表示十进制数。并且，即使是最简单的数学运算也会产生小的误差
    a = 4.2
    b = 2.1
    print("a: ", a)
    print("b: ", b)
    print("a + b: ", a + b)
    print("(a + b) == 6.3: ", (a + b) == 6.3)

    # 这些错误是由底层 CPU 和 IEEE 754 标准通过自己的浮点单位去执行算术时的特征。
    # 由于 Python 的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。

    from decimal import Decimal
    a = Decimal('4.2')
    b = Decimal('2.1')
    print("a: ", a)
    print("b: ", b)
    print("a + b: ", a + b)
    print("Decimal(a + b) == Decimal(6.3): ", Decimal(a + b) == Decimal(6.3))

    # decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。为了这样做，你先得创建一个本地上下文并更改它的设置
    from decimal import localcontext
    a = Decimal('1.3')
    b = Decimal('1.7')
    print("a: ", a)
    print("b: ", b)
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)

        ctx.prec = 60
        print(a / b)

    # 数学家花了大量时间去研究各类算法，有些处理误差会比其他方法更好。
    # 你也得注意下减法删除以及大数和小数的加分运算所带来的影响。
    nums = [1.23e+18, 1, -1.23e+18]
    print("nums: ", nums)
    print("sum(nums): ", sum(nums))
    import math
    print("math.fsum(nums): ", math.fsum(nums))





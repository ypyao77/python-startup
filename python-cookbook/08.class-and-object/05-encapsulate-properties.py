#!/usr/bin/env python3


# 8.5 在类中封装属性名
# 你想封装类的实例上面的“私有”数据，但是 Python 语言并没有访问控制。

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    # Python 程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
    # 第一个约定是任何以单下划线 _ 开头的名字都应该是内部实现。
    def _internal_method(self):
        pass

    # 使用双下划线开始会导致访问名称变成其他形式。
    def __private_method(self):
        pass


if __name__ == "__main__":
    pass
    # 要注意的是，有时候你定义的一个变量和某个保留关键字冲突，这时候可以使用单下划线作为后缀
    lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword








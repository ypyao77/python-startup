#!/usr/bin/python
#coding=utf8

# case 1
class Hello():
    def say_hello(self, name='world'):
        print('Hello, %s.' % name)

hello = Hello()
hello.say_hello()

# case 2
def fn(self, name='world'): # 假如我们有一个函数叫fn
    print('Hello, %s.' % name)
    
Hello = type('Hello', (object,), dict(say_hello=fn))

hello = Hello()
hello.say_hello()

#case 3
# 道生一：传入type
class SayMetaClass(type):
    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_'+name] = lambda self,value,saying=name: print(saying+','+value+'!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)
 
class Hello(object, metaclass=SayMetaClass):
    pass
 
hello = Hello()
hello.say_Hello('world!')

# 日文
class Sayolala(object, metaclass=SayMetaClass):
    pass
 
s = Sayolala()
s.say_Sayolala('japan!')

#中文
class Nihao(object, metaclass=SayMetaClass):
    pass

n = Nihao()
n.say_Nihao('中华!')

#case 4
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)

class Foo(object):
  def __eq__(self, other):
    return True

foo = Foo()
print("foo = Foo()")
print("foo == None : %s" %(foo == None))
print("foo is None : %s" %(foo is None))


def add1(ele, target=[]):
    target.append(ele)
    return target

def add2(ele, target=None):
    if target is None:
        target = []

    target.append(ele)
    return target

print("add1(1) = %s" %(add1(1)))
print("add1(2) = %s" %(add1(2)))
print("add1(3) = %s" %(add1(3)))

print("add2(1) = %s" %(add2(1)))
print("add2(2) = %s" %(add2(2)))
print("add2(3) = %s" %(add2(3)))



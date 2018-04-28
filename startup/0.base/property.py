class People(object):
  __age = None

  @property
  def age(self):
    print People.__mro__
    return self.__age

  @age.setter
  def age(self, new_age):
    self.__age = new_age

p = People()
print ("p.age = {age}".format(age=p.age))
p.age = 10
print ("p.age = {age}".format(age=p.age))
p.age = 20
print ("p.age = {age}".format(age=p.age))

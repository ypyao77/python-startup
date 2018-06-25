class Student(object):
    __slots__ = ('name', 'age')

    def __str__(self):
        return "Student object (name: %s, age: %s)".format(self.name, self.age)

class GraduateStudent(Student):
    __slots__ = ('score')

    def __str__(self):
        return "GraduateStudent object (name: %s, age: %s, score: %s)".format(self.name, self.age, self.score)

s = Student()
s.name = 'Micheal'
s.age = 20
print("s = %s" %(s))

g = GraduateStudent()
g.name = "Grandual"
g.age = 24
g.score = 99
print("g = %s" %(g))


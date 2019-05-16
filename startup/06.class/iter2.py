class A(object):
    def __init__(self, num):
        self.l = num
        self.a = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a = self.a + 1
        if self.a > self.l:
            raise StopIteration()
        return self.a

for x in A(5):
    print(x)

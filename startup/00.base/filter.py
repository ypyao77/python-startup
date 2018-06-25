l = ["a:1", "b:2", "c:3", "d"]

a = map(lambda s: (s.split(':')[0], s.split(':')[1]) if ':' in s else (s, None), l)
print("a = %s" % (a))
for i in a:
    print(i)

f = filter(lambda x, y: y is not None, a)
print("f = %s" % (f))
for i in f:
    print(i)


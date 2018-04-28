l = ["a:1", "b:2", "c:3", "d"]

a = map(lambda s: (s.split(':')[0], s.split(':')[1]) if ':' in s else (s, None), l)
print("a = %s" %(a))

f = filter(lambda (x, y): not (x is None or y is None), a)
print("f = %s" %(f))

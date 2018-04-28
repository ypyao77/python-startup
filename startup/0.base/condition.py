pr = lambda x: x
do = lambda x: (x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))

print(do(1))
print(do(2))
print(do(3))
print(do(None))

d = {'a': "value_a", 'b': "value_b"}

print(d.get('a', 'default_value'))
print(d.get('b', 'default_value'))
print(d.get('c', 'default_value'))

import sys

# case 1
print('this is %d %s bird' % (1, 'dead'))
print('{0},{1} and {2}'.format('a', 'b', 'c'))
print('{name1},{0} and {name2}'.format('a', name1='b', name2='c'))

# case 2
aList = list('abcde')
print('my {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
print('first={0[0]} third={0[2]}'.format(aList))

a = [1, 2, 3, 4, 5]
b = a[:]
print("a = {0}".format(a))
print("b = {0}".format(b))

b.append(99)
print("a = {0}".format(a))
print("b = {0}".format(b))

# case 3
print('{0:10} = {1:10}'.format('abcde', 1.23456))
print('{0:<10} = {1:<10}'.format('abcde', 1.23456))
print('{0:>10} = {1:>10}'.format('abcde', 1.23456))

print('{0:e}, {1:.3e}, {2:g}'.format(3.141592, 3.141592, 3.141592))
print('{0:20e}, {1:.3e}, {2:20g}'.format(3.141592, 3.141592, 3.141592))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.141592, 3.141592, 3.141592))

print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
print(bin(255), int('11111111', 2), 0b11111111)
print('{0:f},{1:.2f},{2:06.2f}'.format(1 / 3, 1 / 3, 1 / 3))


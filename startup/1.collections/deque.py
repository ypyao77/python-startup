from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])

d = deque(range(5))
print(len(d))
d.popleft()
d.pop()
print(d)

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)

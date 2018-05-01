from collections import Counter
c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1

print("c = {0}".format(c))

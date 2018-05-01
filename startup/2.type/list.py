import functools

l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

functools.reduce(lambda x, y: x.extend(y), l)

def f(x):
    return {
        'a': 1,
        'b': 2,
        }.get(x, 9)    # 9 is default if x not found


print("f('a') = {0}".format(f('a')))
print("f('b') = {0}".format(f('b')))
print("f('c') = {0}".format(f('c')))

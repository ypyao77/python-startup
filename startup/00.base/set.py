# get duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# intersection
valid = set(['yellow', 'red', 'blue', 'green', 'black', 'yellow', 'red'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

# difference
valid = set(['yellow', 'red', 'blue', 'green', 'black', 'yellow', 'red'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))

# type set
# a_set = {'red', 'blue', 'green', 'green', 'green'}
# print(type(a_set))

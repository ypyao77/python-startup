multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x**2)

print("squared = %s" %(squared))

squared = [x**2 for x in range(10)]
print("squared = %s" %(squared))

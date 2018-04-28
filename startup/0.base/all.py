n = []
print("n = %s" %(n))
print("bool(n) = %s" %(bool(n)))

n = [1, 2, 3, 4, 5]
print("n = %s" %(n))
print("bool(n) = %s" %(bool(n)))

print("all(i > 2 for i in n) = %s" %(all(i > 2 for i in n)))
print("all(i > 0 for i in n) = %s" %(all(i > 0 for i in n)))

print("any(i > 10 for i in n) = %s" %(any(i > 10 for i in n)))
print("any(i > 3 for i in n) = %s" %(any(i > 3 for i in n)))


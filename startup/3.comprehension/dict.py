fruit = ['apple', 'banana', 'orange']  
dictresult = {}  
dictresult = {key: value for key, value in enumerate(fruit) if len(value) > 5}  
print("dictresult = %s" %(dictresult))


mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a','b']
}
print("mcase_frequency = %s" %(mcase_frequency))

mcase_frequency = {v: k for k, v in mcase_frequency.items()}
print("mcase_frequency = %s" %(mcase_frequency))

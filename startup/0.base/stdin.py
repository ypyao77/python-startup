import fileinput

print("lines are:")
for line in fileinput.input("stdin.py"):
    print(line.rstrip())

for line in fileinput.input():
    if line.rstrip() in ['quit', 'exit', 'q', 'e']:
        print("quit!")
        break

    print("line = {0}".format(line.rstrip()))




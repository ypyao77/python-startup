import sys

with open(sys.argv[0], 'r') as infile:
    for line in infile:
        print(line.rstrip())

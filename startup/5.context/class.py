import sys

class MyFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with MyFile(sys.argv[0], 'r') as infile:
    for line in infile:
        print(line.rstrip())
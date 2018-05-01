import os

print("os.environ = {0}".format(os.environ))
print("os.environ.get('PATH') = {0}".format(os.environ.get('PATH')))

print("os.path.abspath = {0}".format(os.path.abspath('.')))

print("os.path.split('/Users/michael/testdir/file.txt') = {0}".format(os.path.split('/Users/michael/testdir/file.txt')))
print("os.path.split('/Users/michael/testdir/file') = {0}".format(os.path.split('/Users/michael/testdir/file')))
print("os.path.split('/Users/michael/testdir/file/') = {0}".format(os.path.split('/Users/michael/testdir/file/')))

print("os.name = {0}".format(os.name))
print("os.uname = {0}".format(os.uname))

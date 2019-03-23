
def this_fails():
    1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


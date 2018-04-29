# case 1
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = 0
for i in fib():
    n += 1
    if n > 10:
        break

    print("fib() = %s" %i)

# case 2
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
search.send("I love coroutine instead!")



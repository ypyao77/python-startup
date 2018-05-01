import cProfile


def foo():
    print("hello, foo!")


cProfile.run('foo()')


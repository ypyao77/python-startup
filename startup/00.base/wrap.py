from functools import update_wrapper, partial, wraps

def log(func):
    @wraps(func)
    def wraper():
        print("INFO: Starting {}".format(func.__name__))
        func()
        print("INFO: Finishing {}".format(func.__name__))
    return wraper

@log
def run():
    """Docs' of run"""
    print("Running run...")

print(run.__name__)
print(run.__doc__)


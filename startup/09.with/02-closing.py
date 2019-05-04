class closing(object):
    # help doc here
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()

class ClosingDemo(object):
    def __init__(self):
        self.acquire()
    def acquire(self):
        print 'Acquire resources.'
    def free(self):
        print 'Clean up any resources acquired.'
    def close(self):
        self.free()
 
with closing(ClosingDemo()):
    print 'Using resources'


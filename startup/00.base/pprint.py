import pprint
import itertools

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in itertools.xrange(0, len(l), n):
        yield l[i:i+n]

pprint.pprint(list(chunks(range(10, 75), 10)))



my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint,pprint(my_dict)


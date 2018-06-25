import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print('id_generator() = {0}'.format(id_generator()))
print('id_generator(3, "6793YUIO") = {0}'.format(id_generator(3, "6793YUIO")))


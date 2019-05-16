#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)

    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)

    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)

    else:
        return noun + 's'


if __name__ == "__main__":
    print("plural('match'): {0}".format(plural('match')))
    print("plural('bus'): {0}".format(plural('bus')))
    print("plural('ship'): {0}".format(plural('ship')))
    print("plural('sheep'): {0}".format(plural('sheep')))
    print("plural('goat'): {0}".format(plural('goat')))
    print("plural('biz'): {0}".format(plural('biz')))
    print("plural('school'): {0}".format(plural('school')))

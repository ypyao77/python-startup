#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from registration_param import *

print(registry)

register()(f3)

print(registry)

register(active=False)(f2)

print(registry)

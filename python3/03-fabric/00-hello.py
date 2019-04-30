#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fabric.api import env, run
from fabric2 import Connection

env.host_string = "hadoop@arch-od-tracker04.beta1.fn"
run("whoami") # v1
cxn = Connection.from_v1(env)
cxn.run("whoami") # v2+

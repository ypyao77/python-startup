#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass, os
from fabric import Connection, Config

sudo_pass = getpass.getpass("input your password: ")
c = Connection(host='arch-od-tracker04.beta1.fn', user='hadoop', connect_kwargs={'password': sudo_pass}, config=Config(overrides={'sudo': {'password': sudo_pass}}))

c.put(os.path.abspath(__file__), remote='/tmp/')


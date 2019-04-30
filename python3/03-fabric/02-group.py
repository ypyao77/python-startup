#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
from fabric import Connection, Config
from fabric import SerialGroup

sudo_pass = getpass.getpass("input your password: ")
g = SerialGroup('arch-od-tracker02.beta1.fn', 'arch-od-tracker03.beta1.fn', user='hadoop', connect_kwargs={'password': sudo_pass}, forward_agent=True)

#g.sudo('whoami', hide='stderr')
g.run('hostname')


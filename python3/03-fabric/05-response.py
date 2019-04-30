#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
from fabric import Connection
from invoke import Responder 

sudo_pass = getpass.getpass("input your password: ")
c = Connection(host='arch-od-desktop01.beta1.fn', user='hadoop', connect_kwargs={'password': sudo_pass})

resp1 = Responder(pattern=r'Is this ok \[y/N\]:', response='y\n')
resp2 = Responder(pattern=r"\[sudo\] password", response='hadoop@123\n')

c.run('sudo yum install lsof', pty=True, watchers=[resp1, resp2]) 

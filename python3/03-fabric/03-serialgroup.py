#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
from fabric import SerialGroup

sudo_pass = getpass.getpass("input your password: ")

pool = SerialGroup('arch-od-tracker02.beta1.fn', 'arch-od-tracker03.beta1.fn', user='hadoop', connect_kwargs={"password": sudo_pass} )
#pool = SerialGroup('arch-od-tracker02.beta1.fn', 'arch-od-tracker03.beta1.fn', user='hadoop', connect_kwargs={"password": 'hadoop@123'} )
pool.run('hostname')


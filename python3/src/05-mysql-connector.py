#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector


mydb = mysql.connector.connect(
    host="arch-od-tracker01.beta1.fn",
    user="hadoop",
    passwd="hadoop@123"
)
print(mydb)
mc = mydb.cursor()

print("--------------------------------------------")
sql = "show databases;"
mc.execute(sql)
for x in mc:
    print(x)

print("--------------------------------------------")
sql = "desc test.nct;"
mc.execute(sql)
for x in mc:
    print(x)

print("--------------------------------------------")
sql = "show create table test.nct;"
mc.execute(sql)
for x in mc:
    print(x)


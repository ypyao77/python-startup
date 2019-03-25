#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect(
    host='arch-od-tracker01.beta1.fn',
    user='hadoop',
    passwd='hadoop@123',
    # db='database',
    charset='utf8'
)
cursor = db.cursor()

print("--------------------------------------------")
sql = "show databases"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print("row: ", row)

print("--------------------------------------------")
sql = "desc test.nct;"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print("row: ", row)

print("--------------------------------------------")
sql = "show create table test.nct;"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print("row: ", row)

db.close()

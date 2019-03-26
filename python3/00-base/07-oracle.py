#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cx_Oracle

conn = cx_Oracle.connect('hobigdata/hobigdata@hodb-rt01.inner.rt-mart.com:1521/RT10')
curs = conn.cursor()
sql = "desc hodba.items"
rr = curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row)
#row = curs.fetchone()
#print(row[0])

curs.close()
conn.close()

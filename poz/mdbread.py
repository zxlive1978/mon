#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyodbc 
import os

DBfile = os.getcwd() + "\\" + "suck.mdb"
conn = pyodbc.connect('DRIVER={AccessMS};DBQ='+DBfile)
cursor = conn.cursor()
#SQL = 'SELECT Artist, AlbumName FROM messageData ORDER BY Year;'
SQL = 'SELECT * FROM messageData;'

for row in cursor.execute(SQL): # cursors are iterable
   print row.objHeight

cursor.close()
conn.close()
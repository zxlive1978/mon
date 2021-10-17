#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import binascii
import socket
import struct
from struct import *
import sys
import dateutil.parser
import datetime
from datetime import datetime as dt, timedelta
import time
import math



def clear_well(table,coldate):
	try:
		
		#Удаление прошлых записей 10 дней
		beg_time = 24*60*60*10
		timestamp = int(time.time())+60*60*4 - beg_time
		db_name=table
		db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		cursor = db.cursor()
		sql = "DELETE FROM "+db_name+" WHERE "+ coldate + " < " + str(timestamp)
		cursor.execute(sql)
		db.commit()
		db.close()
	except:
		a=0

# #908
# #  clear_well("s908", "Vrema")
# #547
# clear_well("s110", "Vrema")
# #224
# clear_well("s224", "Vrema")
# #20Э
# clear_well("s20", "Vrema")
# #4450
# clear_well("s4450", "Vrema")
# #630
# clear_well("s630", "Vrema")
# #96
# clear_well("s89", "Vrema")
# #631
# clear_well("s631", "Vrema")
# #629
# clear_well("s629", "Vrema")
# #915
# clear_well("s915", "Vrema")
# #83
# clear_well("s83", "Vrema")
# #401
# clear_well("s401", "Vrema")
# #627
# clear_well("s627", "Vrema")
# #605
# clear_well("s610", "Vrema")
# #533
# # clear_well("s544", "Vrema")


#Inet kontora moskva 77.3
clear_well("pconnect", "date")
#ping 630
clear_well("p3729814", "date")
#ping 631
clear_well("p31173139218", "date")
#ping 
clear_well("p372978226", "date")
#ping 
clear_well("p31173139194", "date")
#ping 
clear_well("p31173139214", "date")
#ping 
clear_well("p31173139222", "date")
#ping 
clear_well("p31173187210", "date")
#ping 
clear_well("p192168146161", "date")
#ping 
clear_well("p192168146129", "date")
#ping 
clear_well("p1921681461", "date")
#ping 
clear_well("p1921681471", "date")
#ping 
clear_well("p19216814733", "date")
#ping 
clear_well("p19216814697", "date")
#ping 
clear_well("p3729899", "date") 	
#alarm
clear_well("a3729814", "data")










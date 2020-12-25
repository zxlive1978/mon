#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Не читает
import MySQLdb
import binascii
import socket
import struct
from struct import *
import sys
import dateutil.parser
import datetime
#from datetime import datetime as dt, timedelta
import time
import math
import threading

from datetime import datetime, timedelta



def datetime_fromdelphi(dvalue):
    return DELPHI_EPOCH + timedelta(days=dvalue)

def datetime_todelphi(dt):
    try:
        return (dt - DELPHI_EPOCH) / timedelta(days=1)
    except TypeError:
        # Python 2.7 / Python 3.1 or older don't support division
        delta = dt - DELPHI_EPOCH
        return delta.days + (delta.seconds + delta.microseconds / 1000000.0) / 24 / 3600

def datetime_to_float(d):
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.fromtimestamp(fl)

def read_well(host,table):
	#Неудачный прием
	suck=False
	#Параметры
	Wkp=-100.0
	Wdol=-100.0
	Mpot=-100.0
	Npot=-100.0
	Pbx=-100.0
	Qbx=-100.0
	Talblok=-100.0
	C1C5=-100.0
	C1=-100.0
	Xn1=-100.0
	Xn2=-100.0
	Potok=-100.0
	Tbix=-100.0
	V1=-100.0
	V2=-100.0
	V3=-100.0
	V4=-100.0
	Vdol=-100.0
	Vobj=-100.0
	Zaboj=-100.0
	Instr=-100.0
	Vrema=-100
	Vinstr=-100.0

	#try:
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, 255)
	sock.connect(server_address)




	# b = "2015-10-28 16:09:59"
	# d = dateutil.parser.parse(b).date()
	# print d
	# dta = datetime_to_float(datetime.datetime(2017,8,30,11))
	# dts=42979.4235194792
	# dta=dta +2208988800
	# myfile1 = open('otvet_geoscape', 'w')
	# myfile2 = open('sprv_geoscape', 'w')
	
	dodelphi = float(43266.4236111111) #datetime_todelphi(float_to_datetime(float("1528937597")))
	values = ('D')
	#packer = struct.Struct('s')
	packed_data = struct.pack('sd',values,dodelphi)


	sock.sendall(packed_data)
	time.sleep(1)
	sprav = sock.recv(1024)
	#dodelphi = datetime_todelphi(float_to_datetime(float("1528937597")))
	
	print (str(dodelphi))

	values = ('D')
	#packer = struct.Struct('s')
	packed_data = struct.pack('sd',values,dodelphi)

	sock.sendall(packed_data)
	time.sleep(0)
	data = sock.recv(1024)

	print len(sprav),sprav
	#print len(data)

	#print (U"Ответ:",data,"\n")
	# if (len(data)<4):
		# values = ('D')
		# packer = struct.Struct('s')
		# packed_data = packer.pack(*values)
		# sock.sendall(packed_data)
		# time.sleep(1)
		# sprav = sock.recv(1024)
		# values = ('D')
		# packer = struct.Struct('s')
		# packed_data = packer.pack(*values)
		
		# sock.sendall(packed_data)
		# time.sleep(1)
		# data = sock.recv(1024)
		# print U"НОвый Ответ:",data,"\n"


	# print len(data)
	sock.close()	
	# myfile2.write(sprav)
	# myfile1.write(data)


	i=3
	j=3
	spr_format="H"
	data_format="d"

	while i<len(sprav):

		#print i, sprav[i:i+2]
		
		numb1=unpack(spr_format,sprav[i:i+2])
		val1=unpack(data_format,data[j:j+8])
		#print numb1,val1
		i=i+2
		j=j+8
		if (numb1[0]==200): Wkp=round(val1[0],2)
		if (numb1[0]==202): Wdol=round(val1[0],2)
		if (numb1[0]==1300): Mpot=round(val1[0],2)
		if (numb1[0]==1200): Npot=round(val1[0],2)
		if (numb1[0]==300): Pbx=round(val1[0],2)
		if (numb1[0]==1001): Qbx=round(val1[0],2)
		if (numb1[0]==103): Talblok=round(val1[0],2)
		if (numb1[0]==1600): C1C5=round(val1[0],2)
		if (numb1[0]==1601): C1=round(val1[0],2)
		if (numb1[0]==50): Xn1=round(val1[0],2)
		if (numb1[0]==51): Xn2=round(val1[0],2)
		if (numb1[0]==1003): Potok=round(val1[0],2)
		if (numb1[0]==900): Tbix=round(val1[0],2)
		if (numb1[0]==711): V1=round(val1[0],2)
		if (numb1[0]==712): V2=round(val1[0],2)
		if (numb1[0]==713): V3=round(val1[0],2)
		if (numb1[0]==716): V4=round(val1[0],2)
		if (numb1[0]==715): Vdol=round(val1[0],2)
		if (numb1[0]==720): Vobj=round(val1[0],2)
		if (numb1[0]==101): Zaboj=round(val1[0],2)
		if (numb1[0]==115): Instr=round(val1[0],2)
		if (numb1[0]==104): Vinstr=round(val1[0],2)
	data_time=unpack(data_format,data[3:11])
	dt =round((data_time[0] - 25569) * 86400) - 14400
	Vrema=dt
	#dt=42984.67354604166*10000

	print Vrema,float_to_datetime(Vrema)
	if len(data)>len(sprav):
		suck=True
	else:
		suck=False
		

	suck = False
	if (suck==True):
		db_name=table
		db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		cursor = db.cursor()
		sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+")"
		cursor.execute(sql)
		db.commit()
		db.close()



# A delphi datetime value is the (fractional) number of days since the epoch
# e.g. 42 minutes past the the UNIX epoch is 25569.029166666667 in Delphi terms.
DELPHI_EPOCH = datetime(1899, 12, 30)		
#Потоки
#547
threading.Thread(target=read_well, args=["192.168.146.130","s908"]).start()
#read_well("192.168.146.98","s908")
#110
#read_well("192.168.146.50","s110")
#3ГФ
threading.Thread(target=read_well, args=["192.168.146.66","s224"]).start()
#read_well("192.168.146.66","s224")
#20Э
threading.Thread(target=read_well, args=["192.168.146.162","s20"]).start()
#read_well("192.168.146.162","s20")
			
# #96		
threading.Thread(target=read_well, args=["192.168.146.50","s89"]).start()
# read_well("192.168.146.50","s110")
# #224		
# read_well("192.168.146.66","s224")
# #928	
read_well("192.168.146.98","s631")
# #411		
# read_well("192.168.146.130","s411")
# #89		
# read_well("192.168.146.162","s89")
#print suck, Vrema, Zaboj, Talblok
#print time.mktime(datetime.datetime.now().timetuple())


# if (len(data)>4):
	# print U"Справочник:",(len(sprav)-3)/2,sprav,"\n"
	# print U"Ответ:",data,"\n"
# else:
#print mytext[2]
#ves =mytext[11:19]
#vesdouble=struct.unpack('d', ves)
#print str(vesdouble)

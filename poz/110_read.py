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
import threading



def datetime_to_float(d):
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)

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
	Dmk=-100.0
	Vbur=-100.0
	Xn3=-100.0
	V5=-100.0
	V6=-100.0
	C2=-100.0
	C3=-100.0
	C4=-100.0
	C5=-100.0
	Kalcid=-100.0
	Dolomit=-100.0
	C1sh=-100.0
	C2sh=-100.0
	C3sh=-100.0
	C4sh=-100.0
	C5sh=-100.0
	C1C5sh=-100.0
	Minbx=-100.0
	Minbix=-100.0


	try:
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

		values = ('D')
		packer = struct.Struct('s')
		packed_data = packer.pack(*values)


		sock.sendall(packed_data)
		time.sleep(1)
		sprav = sock.recv(1024)
		values = ('D')
		packer = struct.Struct('s')
		packed_data = packer.pack(*values)

		sock.sendall(packed_data)
		time.sleep(0)
		data = sock.recv(1024)
		# print len(sprav)
		# print len(data)

		# print U"Ответ:",data,"\n"
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
			if (numb1[0]==107): Dmk=round(val1[0],2)
			if (numb1[0]==106): Vbur=round(val1[0],2)
			if (numb1[0]==52): Xn3=round(val1[0],2)
			if (numb1[0]==717): V5=round(val1[0],2)
			if (numb1[0]==718): V6=round(val1[0],2)
			if (numb1[0]==1602): C2=round(val1[0],2)
			if (numb1[0]==1603): C3=round(val1[0],2)
			if (numb1[0]==1604): C4=round(val1[0],2)
			if (numb1[0]==1605): C5=round(val1[0],2)
			####
			Kalcid=-100.0
			Dolomit=-100.0
			C1sh=-100.0
			C2sh=-100.0
			C3sh=-100.0
			C4sh=-100.0
			C5sh=-100.0
			C1C5sh=-100.0
			Minbx=-100.0
			Minbix=-100.0
		data_time=unpack(data_format,data[3:11])
		dt =round((data_time[0] - 25569) * 86400) - 14400
		Vrema=dt
		#dt=42984.67354604166*10000

		# print Vrema,float_to_datetime(Vrema)
		if len(data)>len(sprav):
			suck=True
		else:
			suck=False
	except:
		suck=False
	if (suck==True):
		db_name=table
		db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		cursor = db.cursor()
		# sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+")"
		sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr, Dmk, Vbur, Xn3, V5, V6, C2, C3, C4, C5, Kalcid, Dolomit, C1sh, C2sh, C3sh, C4sh, C5sh, C1C5sh, Minbx, Minbix) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+","+str(Dmk)+","+str(Vbur)+","+str(Xn3)+","+str(V5)+","+str(V6)+","+str(C2)+","+str(C3)+","+str(C4)+","+str(C5)+","+str(Kalcid)+","+str(Dolomit)+","+str(C1sh)+","+str(C2sh)+","+str(C3sh)+","+str(C4sh)+","+str(C5sh)+","+str(C1C5sh)+","+str(Minbx)+","+str(Minbix)+")"	
		cursor.execute(sql)
		db.commit()
		db.close()

#Потоки
#605
threading.Thread(target=read_well, args=["192.168.146.98","s908"]).start()
#read_well("192.168.146.98","s908")
#99
threading.Thread(target=read_well, args=["192.168.147.66","s110"]).start()
#read_well("192.168.146.50","s110")
#604
threading.Thread(target=read_well, args=["192.168.146.66","s224"]).start()
#read_well("192.168.146.66","s224")
#73
threading.Thread(target=read_well, args=["192.168.146.162","s20"]).start()
#read_well("192.168.146.162","s20")
#106
threading.Thread(target=read_well, args=["192.168.146.130","s83"]).start()

			
# #96		
threading.Thread(target=read_well, args=["192.168.146.50","s89"]).start()

# #627		
threading.Thread(target=read_well, args=["192.168.147.34","s627"]).start()
# read_well("192.168.146.50","s110")
# #224		
# read_well("192.168.146.66","s224")
# #928	
#read_well("192.168.146.98","s631")
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

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
from multiprocessing import Process


def datetime_to_float(d):
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
# type_par='f'
# cur_type='f'
# value = -2147480000.0
# result = -2147480000.0
# size_par =	
def calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head):
	if type_par=='f':
		cur_type='f'
		cur_size=size_par
	if type_par=='i':
		cur_type='h'
		cur_size=size_par
	if type_par=='c':
		cur_type='s'
		cur_size=size_par
	if type_par=='l':
		cur_type='l'
		cur_size=size_par
	
	value = unpack(cur_type, data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
	if type_par=='f':
		result=round(value[0],2)
	else: result= value[0]
	return result

def read_well(host,table):
	# try:
		
		
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
	
	#Текущее значение времянки
	values = ('T CUR')
	#packer = struct.Struct('s')
	#packed_data = packer.pack(*values)
	#1545728147 UTC без часового пояса
	datareciever= str(1545728147 + 18000 + 14400 - 3600)
	values = (datareciever)


	sock.sendall(values)
	time.sleep(1)
	'''
	sprav = sock.recv(1024)
	values = ('D')
	packer = struct.Struct('s')
	packed_data = packer.pack(*values)
	
	sock.sendall(packed_data)
	time.sleep(0)
	'''
	data = sock.recv(8192)
	sock.close()
	if len(data)==1:
		print ("SUCK")
	else: 
		#print len(data), data
		time_head_format="=lHHBB"
		time_numb_rec,numb_well,len_rec,numb_key_param,numbs_params = unpack(time_head_format, data[0:10])

		#print len_rec,numbs_params
		
		sprv =[['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4]
		,['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['l' ,4],['l' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['l' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['i' ,2],['f' ,4],['l' ,4],['f' ,4],['f' ,4],['i' ,2],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['c' ,12],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f',4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['i' ,2],['f' ,4],['f' ,4],['f' ,4],['i' ,2],['i' ,2],['i' ,2],['i' ,2],['i' ,2],
		['i' ,2],['i' ,2],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['c' ,32],
		['c' ,9],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['i' ,2],['i' ,2],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['c' ,31],['f' ,4],['i' ,2],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['i' ,2],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['i' ,2],['l' ,4],['l' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['c' ,10],['l' ,4],['l' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f',4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],['f' ,4],
		['f' ,4],['f' ,4],['c' ,20]]
		#print sprv[1][0]
		i=0
		#начало подзаголовка данных без главного заголовка
		subhead_data_adr = 10
		next_sub_head = 0
		
		print time_numb_rec






		numb_pa=unpack('B', data[i+next_sub_head+10:i+next_sub_head+11])
		#print numb_pa

		numb_pa=unpack('f', data[i+next_sub_head+12:i+next_sub_head+16])
		#print numb_pa

		Wkp,Wdol,Mpot,Npot,Pbx,Qbx,Talblok,C1C5,C1,Xn1,Xn2,Potok,Tbix,V1,V2,V3,V4,Vdol,Vobj,Zaboj,Instr,Vinstr,Vrema = -2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000
		Vremanach = -2147480000
		#print Wkp
		cur_type=''
		cur_size=0
		while i<numbs_params:
			#ID параметра
			numb_par = unpack('B', data[subhead_data_adr+next_sub_head+1:subhead_data_adr+next_sub_head+2])
			#Тип параметра
			type_par =sprv[numb_par[0]][0]
			#Размер параметра
			size_par =sprv[numb_par[0]][1]
			#print numb_par, type_par,size_par
			if numb_par[0]==0:
				#calc_type()
				Wkp = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==1:
				Wdol = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==5:
				
				Mpot = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==4:
				
				Npot = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==2:
				
				Pbx = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==31:
				
				Qbx = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==12:
				
				Talblok = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==152:
				
				C1C5 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==16:
				
				C1 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==13:
				
				Xn1 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==14:
				
				Xn2 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==15:
				
				Potok = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==9:
				
				Tbix = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==44:
				
				V1 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==45:
				
				V2 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==46:
				
				V3 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==47:
				
				V4 = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==49:
				
				Vdol = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==51:
				
				Vobj = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==53:
				
				Zaboj = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==54:
				
				Instr = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==191:
				
				Vinstr = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			if numb_par[0]==52:
					if type_par=='f':
						cur_type='=f'
						cur_size=size_par
					if type_par=='i':
						cur_type='=h'
						cur_size=size_par
					if type_par=='c':
						cur_type='=s'
						cur_size=size_par
					if type_par=='l':
						cur_type='=l'
						cur_size=size_par
					print cur_type, cur_size, numb_par ,type_par
					
					value = unpack(cur_type, data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					#Vrema = result #- 18000 - 14400 + 3600
					arra = data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size]
					print arra
					Vrema = bytes_to_int(arra)
			
			if numb_par[0]==75:
					if type_par=='f':
						cur_type='=f'
						cur_size=size_par
					if type_par=='i':
						cur_type='=h'
						cur_size=size_par
					if type_par=='c':
						cur_type='=s'
						cur_size=size_par
					if type_par=='l':
						cur_type='=l'
						cur_size=size_par
					print cur_type, cur_size, numb_par ,type_par
					
					value = unpack(cur_type, data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Vremanach = result - 18000 - 14400 + 3600
					#value = calc_type(type_par,cur_type,size_par,data,subhead_data_adr,next_sub_head)
			next_sub_head = next_sub_head + sprv[numb_par[0]][1]+2
			i=i+1
		#Просмотр
	print Vrema,   time_numb_rec #, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr
	print "============="
# except:
		# print ("Нет связи")
	#База 
	
	# db_name=table
	# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	# cursor = db.cursor()
	# sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+")"
	# cursor.execute(sql)
	# db.commit()
	# db.close()
		
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

	
# myfile2.write(sprav)
# myfile1.write(data)


#except:
#	a=0

#1.102
# i=0
# while i>20:
	# i=i+1
	# read_well("192.168.146.35","s908")
	# threading.Thread(target=read_well, args=["192.168.146.195","s908"]).start()
	# time.sleep(5)
	
# threading.Thread(target=read_well, args=["192.168.146.3","s908"]).start()
threading.Thread(target=read_well, args=["192.168.147.131","s401"]).start()
	
#Потоки
#547
#threading.Thread(target=read_well, args=["192.168.146.130","s908"]).start()
#read_well("192.168.146.98","s908")
#110
#read_well("192.168.146.50","s110")
#3ГФ
#threading.Thread(target=read_well, args=["192.168.146.66","s224"]).start()
#read_well("192.168.146.66","s224")
#20Э
#threading.Thread(target=read_well, args=["192.168.146.162","s20"]).start()
#read_well("192.168.146.162","s20")
			
# #96		
#threading.Thread(target=read_well, args=["192.168.146.50","s89"]).start()
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

#104
#threading.Thread(target=read_well, args=["192.168.146.3","s110"]).start()
# t110 = Process(target=read_well, args=["192.168.146.3","s110"])
# t110.start()
# t110.join(10)
# if t110.is_alive(): t110.terminate()

#630
#threading.Thread(target=read_well, args=["192.168.146.3","s110"]).start()
# t630 = Process(target=read_well, args=["192.168.146.195","s630"])
# t630.start()
# t630.join(10)
# if t630.is_alive(): t630.terminate()

# if (len(data)>4):
	# print U"Справочник:",(len(sprav)-3)/2,sprav,"\n"
	# print U"Ответ:",data,"\n"
# else:
#print mytext[2]
#ves =mytext[11:19]
#vesdouble=struct.unpack('d', ves)
#print str(vesdouble)

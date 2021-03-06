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

def calc_type():
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

def read_well(host,table):
	try:
		'''
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
		'''
		
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

			print len_rec,numbs_params
			
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






			numb_pa=unpack('B', data[i+next_sub_head+10:i+next_sub_head+11])
			#print numb_pa

			numb_pa=unpack('f', data[i+next_sub_head+12:i+next_sub_head+16])
			#print numb_pa

			Wkp,Wdol,Mpot,Npot,Pbx,Qbx,Talblok,C1C5,C1,Xn1,Xn2,Potok,Tbix,V1,V2,V3,V4,Vdol,Vobj,Zaboj,Instr,Vinstr,Vrema = -2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000
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
					calc_type()
					Wkp = result
				if numb_par[0]==1:
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
					Wdol = result
				if numb_par[0]==5:
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
					Mpot = result
				if numb_par[0]==4:
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
					Npot = result
				if numb_par[0]==2:
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
					Pbx = result
				if numb_par[0]==31:
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
					Qbx = result
				if numb_par[0]==12:
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
					Talblok = result
				if numb_par[0]==152:
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
					C1C5 = result
				if numb_par[0]==16:
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
					C1 = result
				if numb_par[0]==13:
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
					Xn1 = result
				if numb_par[0]==14:
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
					Xn2 = result
				if numb_par[0]==15:
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
					Potok = result
				if numb_par[0]==9:
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
					Tbix = result
				if numb_par[0]==44:
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
					V1 = result
				if numb_par[0]==45:
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
					V2 = result
				if numb_par[0]==46:
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
					V3 = result
				if numb_par[0]==47:
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
					V4 = result
				if numb_par[0]==49:
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
					Vdol = result
				if numb_par[0]==51:
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
					Vobj = result
				if numb_par[0]==53:
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
					Zaboj = result
				if numb_par[0]==54:
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
					Instr = result
				if numb_par[0]==191:
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
					Vinstr = result
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
					
					value = unpack(cur_type, data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Vrema = result - 18000 - 14400 + 3600
					
				next_sub_head = next_sub_head + sprv[numb_par[0]][1]+2
				i=i+1
			#Просмотр
			print Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr
	except:
			print ("Нет связи")
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

	'''
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
	sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+")"
	cursor.execute(sql)
	db.commit()
	db.close()
'''
#except:
#	a=0

#1.102

threading.Thread(target=read_well, args=["192.168.1.102","s908"]).start()
	
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

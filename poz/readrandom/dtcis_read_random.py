#!/usr/bin/env python
# coding: utf-8

from os.path import join, getsize
import os
import sys
import fnmatch
from struct import *
import math
import MySQLdb
import threading

import time
from multiprocessing import Process
import shutil

def read_well(nametime, table, start, stop):
	#print os.listdir(sbor)
	# try:
		# db_name=table
		# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		# cursor = db.cursor()
		# sql = "TRUNCATE "+db_name
		# cursor.execute(sql)
		# db.commit()
		# db.close()

		file_ext='*.dep'
		cur_time=nametime
		path_to_work = os.getcwd()
		sbor = path_to_work
		# for root, dirs, files in os.walk(sbor, topdown=False):
		# 	for name in files:
		# 		SizeFile = getsize(join(root, name))
		# 		if fnmatch.fnmatch(name, file_ext):
		# 		  cur_time=name
		#cur_time=''		 
		#print name
		cur_lst=cur_time.replace('.dep','.lst')
		cur_lst_size=getsize(join(path_to_work, cur_lst))
		cur_time_size=getsize(join(path_to_work, cur_time))

		# try:
		# 	shutil.copy(sbor+'/'+cur_time, path_to_work+"/"+table+".dep")
		# except IOError, e:
		# 	print "Unable to copy file. %s"% e
		
		
		
		# try:
		# 	shutil.copy(sbor+'/'+cur_lst, path_to_work+"/"+table+".lst")
		# except IOError, e:
		# 	print "Unable to copy file. %s"% e

		cur_time=path_to_work+'/'+nametime
		# print (cur_time,cur_lst)
		cur_lst=cur_time.replace('.dep','.lst')
		
		cur_lst_size=getsize(join(path_to_work, cur_lst))
		cur_time_size=getsize(join(path_to_work, cur_time))
		
		# print (cur_lst, cur_lst_size, cur_time,cur_time_size)
		
		ii=0
		cur_lst_disp=-21
		cur_rec=0

		db_name=table
		db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		cursor = db.cursor()

		while ii < (cur_lst_size/21):
			
			cur_rec=ii
			# print cur_rec
			cur_lst_disp =cur_lst_disp+21
			# print cur_lst_disp

			#чтение последней lst записи 21 байт
			full_path_lst=cur_lst
			lst_data=''
			# try:
			f1_lst=open(full_path_lst,'rb')
			f1_lst.seek(cur_lst_disp)
			lst_data=f1_lst.read(21)
			lst_format="=lflllc"
			cur_lst_disp_addr,cur_key_value,time_dos,numb_rec,true_numb_rec,flag = unpack(lst_format, lst_data)
			# print len(lst_data)
			# except:
			# 	a=0
			# finally:
			# 	a=0
				# f1_lst.close()
			

			# print cur_lst_disp_addr,numb_rec

			#чтение заголовка dep записи 10 байт в time
			full_path_time=cur_time
			time_head_data=''
			# try:
			f1_time=open(full_path_time,'rb')
			f1_time.seek(cur_lst_disp_addr)
			time_head_data=f1_time.read(10)
			# print time_head_data
			time_head_format="=lHHBB"
			time_numb_rec,numb_well,len_rec,numb_key_param,numbs_params = unpack(time_head_format, time_head_data)
			
			# except:
			# 	f1_time.close()
			# finally:
			# 	a=0

			
			# try:
				
			# finally:
			# 	a=0
			#print len_rec,numbs_params

			#чтение  dep записи len_rec байт в time
			full_path_time=cur_time
			time_data=''
			try:
				f1_time=open(full_path_time,'rb')
				f1_time.seek(cur_lst_disp_addr)
				time_data=f1_time.read(len_rec)
			finally:
				f1_time.close()

			# time_head_format="lHHBB"
			# time_numb_rec,numb_well,len_rec,numb_key_param,numbs_params = unpack(time_head_format, time_data)


			# print len(time_data),len_rec


			#print numbs_params



			# Типы данных и номера в справочнике
			# c 0 по 34 f длина 4 байта
			# c 35 по 36 l длина 4 байта
			# c 38 по 51 f длина 4 байта
			# 52 l длина 4 байта Время сбора
			# c 53 по 72 f длина 4 байта
			# 73 i длина 2 байта Номер рейса
			# 74 f 4 длина байта
			# 75 l 4 длина байта
			# c 76 по 77 f длина 4 байта
			# 78 i длина 2 байта
			# c 79 по 85 f длина 4 байта
			# 86 S длина 12 байта
			# c 87 по 102 f длина 4 байта
			# 103 i длина 2 байта
			# c 104 по 106 f длина 4 байта
			# c 107 по 113 i длина 2 байта
			# c 114 по 124 f длина 4 байта
			# 125 S длина 32 байта
			# 126 S длина 9 байта
			# c 127 по 130 f длина 4 байта
			# c 131 по 132 i длина 2 байта
			# c 133 по 147 f длина 4 байта
			# 148 S длина 31 байта
			# 149 f длина 4 байта
			# 150 i длина 2 байта
			# c 151 по 189 f длина 4 байта
			# 190 i длина 2 байта
			# c 191 по 211 f длина 4 байта
			# 212 i длина 2 байта
			# c 213 по 214 l длина 4 байта
			# c 215 по 231 f длина 4 байта
			# c 215 по 231 f длина 4 байта
			# 232 S длина 10 байта
			# 233 l длина 4 байта
			# 234 l длина 4 байта
			# 235 d длина 8 байта Время сбора Windows
			# c 236 по 254 f длина 4 байта

			# sprv =[['f',4],
			# ['d',32]]
			#Чтение справочника
			# cur_lst_disp_addr=0
			# f1_sprav=open('Parsys01.sup','rb')
			# f1_sprav.seek(cur_lst_disp_addr)
			# time_head_data=f1_sprav.read()
			# a=''
			# while i<255:
				# numb_par=unpack('h', time_head_data[i*41+4:i*41+6])
				# size_par=unpack('h', time_head_data[i*41+6:i*41+8])
				# type_par=unpack('B', time_head_data[i*41+8:i*41+9])
				# i=i+1
				# a = a + str('[\''+chr(int(type_par[0]))+'\' ,'+str(size_par[0])+'],')
				
			# print a
			# f1_sprav.close()
			# try:
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




			# print time_data

			numb_pa=unpack('B', time_data[i+next_sub_head+10:i+next_sub_head+11])
			#print numb_pa

			numb_pa=unpack('f', time_data[i+next_sub_head+12:i+next_sub_head+16])
			#print numb_pa

			Wkp,Wdol,Mpot,Npot,Pbx,Qbx,Talblok,C1C5,C1,Xn1,Xn2,Potok,Tbix,V1,V2,V3,V4,Vdol,Vobj,Zaboj,Instr,Vinstr,Vrema,Dmk,Vbur,Xn3,V5,V6,C2,C3,C4,C5,Kalcid,Dolomit,C1sh,C2sh,C3sh,C4sh,C5sh,C1C5sh,Minbx,Minbix = -2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000,-2147480000
			#print Wkp
			cur_type=''
			cur_size=0
			while i<numbs_params:
				#ID параметра
				numb_par = unpack('B', time_data[subhead_data_adr+next_sub_head+1:subhead_data_adr+next_sub_head+2])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Vinstr = result
# # # # # # # 
				if numb_par[0]==23:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Dmk = result

				if numb_par[0]==22:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Vbur = result

				if numb_par[0]==135:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Xn3 = result

				if numb_par[0]==48:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					V5 = result

				if numb_par[0]==236:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					V6 = result

				if numb_par[0]==17:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C2 = result

				if numb_par[0]==18:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C3 = result

				if numb_par[0]==20:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C4 = result

				if numb_par[0]==21:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C5 = result

				if numb_par[0]==176:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Kalcid = result

				if numb_par[0]==196:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Dolomit = result

				if numb_par[0]==216:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C1sh = result

				if numb_par[0]==217:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C2sh = result

				if numb_par[0]==218:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C3sh = result

				if numb_par[0]==219:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C4sh = result

				if numb_par[0]==220:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C5sh = result

				if numb_par[0]==222:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					C1C5sh = result

				if numb_par[0]==155:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Minbx = result

				if numb_par[0]==156:
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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Minbix = result


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
					
					value = unpack(cur_type, time_data[subhead_data_adr+next_sub_head+2:subhead_data_adr+next_sub_head+2+cur_size])
					if type_par=='f':
						result=round(value[0],2)
					else: result= value[0]
					Vrema = result - 18000 - 10800-3600 #3600 1 час
					
					



				next_sub_head = next_sub_head + sprv[numb_par[0]][1]+2
				i=i+1
			print Vrema
			print start
			if (int(Vrema))>start:
				
			# print (str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+","+str(Dmk)+","+str(Vbur)+","+str(Xn3)+","+str(V5)+","+str(V6)+","+str(C2)+","+str(C3)+","+str(C4)+","+str(C5)+","+str(Kalcid)+","+str(Dolomit)+","+str(C1sh)+","+str(C2sh)+","+str(C3sh)+","+str(C4sh)+","+str(C5sh)+","+str(C1C5sh)+","+str(Minbx)+","+str(Minbix))
				sql = "INSERT INTO "+db_name+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr, Dmk, Vbur, Xn3, V5, V6, C2, C3, C4, C5, Kalcid, Dolomit, C1sh, C2sh, C3sh, C4sh, C5sh, C1C5sh, Minbx, Minbix) VALUE ("+str(Vrema)+","+str(Wkp)+","+str(Wdol)+","+str(Mpot)+","+str(Npot)+","+str(Pbx)+","+str(Qbx)+","+str(Talblok)+","+str(C1C5)+","+str(C1)+","+str(Xn1)+","+str(Xn2)+","+str(Potok)+","+str(Tbix)+","+str(V1)+","+str(V2)+","+str(V3)+","+str(V4)+","+str(Vdol)+","+str(Vobj)+","+str(Zaboj)+","+str(Instr)+","+str(Vinstr)+","+str(Dmk)+","+str(Vbur)+","+str(Xn3)+","+str(V5)+","+str(V6)+","+str(C2)+","+str(C3)+","+str(C4)+","+str(C5)+","+str(Kalcid)+","+str(Dolomit)+","+str(C1sh)+","+str(C2sh)+","+str(C3sh)+","+str(C4sh)+","+str(C5sh)+","+str(C1C5sh)+","+str(Minbx)+","+str(Minbix)+")"	
				cursor.execute(sql)
				db.commit()
			ii=ii+1
		
			# except:
			# 	a=0
			# finally:
			# 	a=0
			
		db.close()
		
		# db_name=table
		# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		# cursor = db.cursor()

		# # RENAME TABLE t1 TO tmp_table,
    	# # t2 TO t1,
    	# # tmp_table TO t2;

		# sql = "RENAME TABLE "+db_name+ " TO tmp_table, " +db_name+"_all TO "+ db_name+ ", tmp_table TO "+db_name+"_all;"
		# cursor.execute(sql)
		# db.commit()
		# db.close()

		# db_name=table
		# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
		# cursor = db.cursor()
		# sql = "TRUNCATE "+db_name
		# cursor.execute(sql)
		# db.commit()
		# db.close()
		# cursor = db.cursor()
		

		# # i will assume the below scenario ,

		# # 1- you need to insert in table1 all data from table 2 use this one

		# # INSERT INTO TABLE1 (Col1, Col2)
		# # SELECT Col1, COl2  FROM  Table2

		# sql = "INSERT INTO "+db_name+"_all  "+"(Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr) SELECT Vrema, Wkp, Wdol, Mpot, Npot, Pbx, Qbx, Talblok, C1C5, C1, Xn1, Xn2, Potok, Tbix, V1, V2, V3, V4, Vdol, Vobj, Zaboj, Instr, Vinstr FROM "+db_name
		# cursor.execute(sql)

		# # INSERT INTO Employee.tbl_TestMerge 
		# # (EmpNumber,EmpName)
		# # VALUES (2,'LKM')
		# # ON DUPLICATE KEY UPDATE 
		# # EmpNumber=VALUES(EmpNumber),EmpName=VALUES(EmpName);


		# db.commit()


		# db.close()
		# #print db_name
	# except:
	# 	return
	
	
# #threading.TIMEOUT_MAX=5
# #Потоки
# #406
# #read_well("/mnt/104","s110")
# t110 = Process(target=read_well, args=["/mnt/104","s401"])
# t110.start()
# t110.join(30)
# if t110.is_alive(): t110.terminate()

# # #449 406
# # #read_well("/mnt/104","s110")
# t110 = Process(target=read_well, args=["/mnt/104","s401depth", sys.argv[1], sys.argv[2]])
# t110.start()
# t110.join(300)
# if t110.is_alive(): t110.terminate()


# #544
# t544 = Process(target=read_well, args=["/mnt/544","s544depth"])
# t544.start()
# t544.join(300)
# if t544.is_alive(): t544.terminate()

# #9917
# t630 = Process(target=read_well, args=["/mnt/630","s630depth"])
# t630.start()
# t630.join(300)
# if t630.is_alive(): t630.terminate()

# #632
# t631 = Process(target=read_well, args=["/mnt/631","s629depth"])
# t631.start()
# t631.join(300)
# if t631.is_alive(): t631.terminate()


# #71
# t4450 = Process(target=read_well, args=["/mnt/4450","s4450depth"])
# t4450.start()
# t4450.join(300)
# if t4450.is_alive(): t4450.terminate()


# #938 (Обработчик)
# t4450 = Process(target=read_well, args=["/mnt/20","s20depth"])
# t4450.start()
# t4450.join(300)
# if t4450.is_alive(): t4450.terminate()


#Саратов (Обработчик)
t4450 = Process(target=read_well, args=[sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4]])
t4450.start()
t4450.join(300)
if t4450.is_alive(): t4450.terminate()




# #542
# #read_well("/mnt/915","s915")
# t915 = Process(target=read_well, args=["/mnt/915","s915depth"])
# t915.start()
# t915.join(300)
# if t915.is_alive(): t915.terminate()

# # #threading.Thread(target=read_well, args=["/mnt/631","s631"]).join(5)
# # #read_well("/mnt/631","s631")

# # #610
# # #read_well("/mnt/104","s110")
# # t610 = Process(target=read_well, args=["/mnt/610","s610"])
# # t610.start()
# # t610.join(30)
# # if t610.is_alive(): t610.terminate()

# 	#print Wkp,Wdol,Mpot,Npot,Pbx,Qbx,Talblok,C1C5,C1,Xn1,Xn2,Potok,Tbix,V1,V2,V3,V4,Vdol,Vobj,Zaboj,Instr,Vinstr,Vrema
		
# 	#  	0; 'Вес на крюке' Wkp
# 	#	1; 'Нагрузка на долото' Wdol
# 	#	5; 'Момент на роторе' Mpot
# 	#	4; 'Обороты ротора' Npot
# 	#	2; 'Давление на входе' Pbx
# 	#	31; 'Расход на входе' Qbx
# 	#	12; 'Положение крюка' Talblok
# 	#	152; 'Сумма С1...С6' C1C5
# 	#	16; 'С1'  			  C1
# 	#	13; 'Ходов насоса 1' Xn1
# 	#	14; 'Ходов насоса 2' Xn2
# 	#	15; 'Расход на выходе' Potok
# 	#	9; 'Температура на выход' Tbix
# 	#	44; 'Объем емкости 1'  V1
# 	#	45; 'Объем емкости 1'  V2
# 	#	46; 'Объем емкости 1'  V3
# 	#	47; 'Объем емкости 1'  V4
# 	#	49; 'Объем емк.Долива' Vdol
# 	#	51; 'Объем всех емкостей' Vobj
# 	#	53; 'Глубина Забоя'  Zaboj
# 	#	54; 'Глубина долота'  Instr
# 	#	191; 'Мех.скорость'	Vinstr
# 	#	52; 'Время сбора данных' Vrema	

# # 23; 'ДМК' Dmk
# # 22; 'Скорость бурения' Vbur
# # 135; 'Ходов насоса 3' Xn3
# # 48; 'Объем емкости 5' V5
# # 236; 'Объем емкости 6' V6
# # 17; 'С2' C2
# # 18; 'С3' C3
# # 20; 'С4' C4
# # 21; 'С5' C5
# # 176; 'Кальцит' Kalcid
# # 196; 'Доломит' Dolomit
# # 216; 'С1 по шламу' C1sh
# # 217; 'С2 по шламу' C2sh
# # 218; 'С3 по шламу' C3sh
# # 219; 'С4 по шламу' C4sh
# # 220; 'С5 по шламу' C5sh
# # 222; 'Сумма шламу С1...С6' C1C5sh
# # 155; 'Минерализация на вх' Minbx
# # 156; 'Минерализация на вых' Minbix

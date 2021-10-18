#!/usr/bin/env python
# coding: utf-8

from os.path import join, getsize
import os
import fnmatch
from struct import *
import math
import MySQLdb
import threading
import string




import time
from multiprocessing import Process

import codecs
import io
import shutil
import subprocess


import dateutil.parser
import datetime
from datetime import datetime as dt, timedelta
import math
from math import *

def datetime_to_float(d):
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)

def read_well(sbor,table):
	#print os.listdir(sbor)
	try:
		file_ext='*.skf'
		cur_time=''
		for root, dirs, files in os.walk(sbor):
			for name in files:
				SizeFile = getsize(join(root, name))
				if fnmatch.fnmatch(name, file_ext):
					cur_time=name
					print cur_time
					#break
				 

		
					cur_time_size=getsize(join(root, cur_time))
					
					full_path_skf=sbor+'/'+cur_time
					#копирование файла
					shutil.copy(full_path_skf, "/var/www/html/mon/poz/"+table)
					#delphi dfm to txt
					subprocess.call("wineconsole --backend=curses /var/www/html/mon/poz/convert.exe " +str(table)+ "  "+str(table), shell=True)
					with open(str(table)+'.txt') as f:
						my_lines = f.readlines()
						
					#print my_lines
					#Delphi эпоха 01.01.1900 - целая часть и дробная часть 300 долей секунды
					#Unix эпоха 1970-01-01 00:00:00
					index = 0
					for line in my_lines:
						comment_line = line.find('TCommentSeries')
						if (comment_line!=-1):
							value =my_lines[index+12].split()
							cur_delphi_day, cur_delphi_sec = value[2].split('.')
							#-25568
							# - 29221
							cur_unix_time = int(cur_delphi_day)*86400 - 25568*86400 - 100795 +floor(0.864*float(cur_delphi_sec[0:4]))*10
							epoch = datetime.datetime.utcfromtimestamp(0)
							#print  cur_delphi_day,cur_delphi_sec,value[2], float_to_datetime(float(value[2])) , float_to_datetime(cur_unix_time)
							comment_txt = my_lines[index+13][16:len(my_lines[index+13])-2].split('#')
							#try:
							align_txt1 = my_lines[index+14].find('Align')
							align_txt2 = my_lines[index+15].find('Align')
							align_txt3 = my_lines[index+16].find('Align')
							align_txt4 = my_lines[index+17].find('Align')
							align_txt5 = my_lines[index+18].find('Align')
							if (align_txt1==-1):
								comment_txt = my_lines[index+14][8:len(my_lines[index+14])].split('#')
								if (align_txt2==-1):
									comment_txt = comment_txt[:len(comment_txt)-3] + my_lines[index+15][8:len(my_lines[index+15])].split('#')
									if (align_txt3==-1):
										comment_txt = comment_txt[:len(comment_txt)-3] + my_lines[index+16][8:len(my_lines[index+16])].split('#')
										if (align_txt4==-1):
											comment_txt = comment_txt[:len(comment_txt)-3] + my_lines[index+17][8:len(my_lines[index+17])].split('#')
											if (align_txt5==-1):
												comment_txt = comment_txt[:len(comment_txt)-3] + my_lines[index+18][8:len(my_lines[index+18])].split('#')
							#except:
								#a=0
							#print align_txt
							#left right
							left_txt = my_lines[index+1].split()[2]
							#print left_txt
							right_txt = my_lines[index+2].split()[2]
							#print right_txt
							
							#comment_txt.split
							finish_comment=''
							for sub_comment in comment_txt:
								sub_comment = sub_comment.split("'")
								

								for sub_txt in sub_comment:
									if (len(sub_txt)>0):
										#1103 #1040
										try:
											a=int(sub_txt)
											if (len(sub_txt)==4 and sub_txt[0:3].isdigit and int(sub_txt)>=1040 and int(sub_txt)<=1105):
												#finish_comment += sub_txt
												subsub_txt =unichr(int(sub_txt))
												finish_comment +=subsub_txt
											else:
												finish_comment += sub_txt
										except:
											finish_comment += sub_txt
										#print sub_txt
							

							#Поиск
							db_name=table
							db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
							cursor = db.cursor()
							sql = "SELECT Vrema, Comment FROM "+db_name+" WHERE Vrema = "+str(cur_unix_time)+ " AND Comment =" + "'"+finish_comment.encode('utf-8')+"'"
							#sql = "SELECT Vrema, Comment FROM "+db_name+" WHERE Vrema = "+str(cur_unix_time)
							cursor.execute(sql)
							data =  cursor.fetchall()
							#print data
							if len(data) == 0:
								#Вставка
								db_name=table
								db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
								cursor = db.cursor()
								sql = "INSERT INTO "+db_name+"(Vrema, Comment, left_txt) VALUE ( "+str(cur_unix_time)+", "+"'"+finish_comment.encode('utf-8')+"'"+", "+str(left_txt)+" )"
								cursor.execute(sql)
								db.commit()				
						index+=1
					
					db.close()
			#break
	except:
		return
	
	
#Комментарии Geoscape
#Потоки
#104
#read_well("/mnt/104","s110")

#201 938 20Э
t20 = Process(target=read_well, args=["/mnt/20o","s20kr"])
t20.start()
t20.join(10)
if t20.is_alive(): t20.terminate()

#928
t928 = Process(target=read_well, args=["/mnt/928","s631kr"])
t928.start()
t928.join(10)
if t928.is_alive(): t928.terminate()

#Саратов 908 
# t547 = Process(target=read_well, args=["/mnt/908o","s908kr"])
# t547.start()
# t547.join(10)
# if t547.is_alive(): t547.terminate()

#84
t3 = Process(target=read_well, args=["/mnt/3","s224kr"])
t3.start()
t3.join(10)
if t3.is_alive(): t3.terminate()

#99
t96 = Process(target=read_well, args=["/mnt/96","s110kr"])
t96.start()
t96.join(10)
if t96.is_alive(): t96.terminate()

#83
t96 = Process(target=read_well, args=["/mnt/83","s83kr"])
t96.start()
t96.join(10)
if t96.is_alive(): t96.terminate()

#627
t627 = Process(target=read_well, args=["/mnt/627o","s627kr"])
t627.start()
t627.join(10)
if t627.is_alive(): t627.terminate()

"""
#4450
#read_well("/mnt/4450","s4450")
t4450 = Process(target=read_well, args=["/mnt/4450","s4450"])
t4450.start()
t4450.join(10)
if t4450.is_alive(): t4450.terminate()
#630
#read_well("/mnt/630","s630")
t630 = Process(target=read_well, args=["/mnt/630","s630"])
t630.start()
t630.join(10)
if t630.is_alive(): t630.terminate()
#read_well("/mnt/630","s630")
#631
#threading.Thread(target=read_well, args=["/mnt/631","s631"]).join(5)
#read_well("/mnt/631","s631")

"""
	#print Wkp,Wdol,Mpot,Npot,Pbx,Qbx,Talblok,C1C5,C1,Xn1,Xn2,Potok,Tbix,V1,V2,V3,V4,Vdol,Vobj,Zaboj,Instr,Vinstr,Vrema
		
	#  	0; 'Вес на крюке' Wkp
	#	1; 'Нагрузка на долото' Wdol
	#	5; 'Момент на роторе' Mpot
	#	4; 'Обороты ротора' Npot
	#	2; 'Давление на входе' Pbx
	#	31; 'Расход на входе' Qbx
	#	12; 'Положение крюка' Talblok
	#	152; 'Сумма С1...С6' C1C5
	#	16; 'С1'  			  C1
	#	13; 'Ходов насоса 1' Xn1
	#	14; 'Ходов насоса 2' Xn2
	#	15; 'Расход на выходе' Potok
	#	9; 'Температура на выход' Tbix
	#	44; 'Объем емкости 1'  V1
	#	45; 'Объем емкости 1'  V2
	#	46; 'Объем емкости 1'  V3
	#	47; 'Объем емкости 1'  V4
	#	49; 'Объем емк.Долива' Vdol
	#	51; 'Объем всех емкостей' Vobj
	#	53; 'Глубина Забоя'  Zaboj
	#	54; 'Глубина долота'  Instr
	#	191; 'Мех.скорость'	Vinstr
	#	52; 'Время сбора данных' Vrema	

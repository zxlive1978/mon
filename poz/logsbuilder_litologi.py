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

import sys
import re
import struct

from time import mktime
from datetime import datetime

def datetime_to_float(d):
    epoch = datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def float_to_datetime(fl):
    return datetime.fromtimestamp(fl)

def read_well(sbor,table):
	path_to_work ="/var/www/html/mon/poz/"
	#print os.listdir(sbor)
	#try:
	# file='WELLSITEDB.gz'
				
	# full_path_skf=sbor+'/WELLSITEDB.gz'
	# #копирование файла с обработчика с папки c:\Program files\Common files\Ps Shared\WELLSITEDB.zip
	# #который заархивирован с помощью Reciever на той стороне
	# # Внимание! Не забыть раскомментировать, когда отключится шифрование XceedZip.dll.
	
	# try:
	# 	shutil.copy(full_path_skf, path_to_work)
	# except IOError, e:
	# 	print "Unable to copy file. %s" % e
			
			
	# #if (cur_time_size==getsize(""+path_to_work+"WELLSITEDB.gz")):
	# subprocess.call("gzip -d -k -f "+path_to_work+"WELLSITEDB.gz > "+path_to_work+"WELLSITEDB", shell=True)
	# print "Распаковано"
	# #mdb файл в csv! только комментарии
	# #if (cur_time_size==getsize(path_to_work+"WELLSITEDB")):
		
	# subprocess.call("mdb-export -H -d '%%%' -R '$$$' '"+path_to_work+"WELLSITEDB' 'geologyInterval2lithology' > "+path_to_work+"WELLSITEDBlitologi.csv ", shell=True)
    subprocess.call("mdb-export "+path_to_work+"'WELLSITEDB' 'geologyInterval2lithology' > "+path_to_work+"WELLSITEDBlitologi.csv ", shell=True)
	print "Скопировано"
	
	
	curSizecsv=getsize(""+path_to_work+"WELLSITEDBlitologi.csv")

	print (curSizecsv)
	
	f1_lst=open(path_to_work+"WELLSITEDBlitologi.csv",'rb')
	f1_lst.seek(0)
	lst_data=f1_lst.read(curSizecsv)
	f1_lst.close()
	records_data = lst_data.split("$$$")
	data =records_data[:(len(records_data)-1)]
	print records_data
	# i=0
	# #f = open('out.txt', 'w')
	# #sys.stdout = f
	# for cur_rec in data:
	# 	cur_rec=cur_rec.split('%%%')
	# 	cur_par =cur_rec[15].split('""')#.split('\x00/\x00>\x00<\x00T\x00e\x00x\x00t\x00>')
		
	# 	#Текущее время комментария
	# 	time_cur=str(cur_rec[6])
	# 	print "dbid="+str(cur_rec[0]),"uidObjMessage="+str(cur_rec[5]),"dTimLastChange"+str(cur_rec[4]),"dTim="+str(cur_rec[6]), "objImage=","objPosition="+str(cur_rec[18])
	# 	#test_time ="01/28/18 02:55:00"
	# 	#print len(cur_par)
	# 	time_tuple = time.strptime(time_cur[1:17], "%m/%d/%y %H:%M:%S")
	# 	dtt = datetime.fromtimestamp(mktime(time_tuple))
	# 	cur_unix_time = datetime_to_float(dtt)
	# 	#Сдвиг
	# 	shift_hours= 14400
	# 	cur_unix_time-=shift_hours
	# 	# Комментарии с текущей даты
	# 	begin_time = 1528269694 # 6 June 2018 г., 07:21:34
	# 	#begin_time = 1496733694 # 6 June 2017 г., 07:21:34
	# 	#Типы По времени 2, По глубине, Геолог
	# 	type_cmt_time=int(str(cur_rec[5]))
	# 	if (cur_unix_time >= begin_time and len(cur_par)>= 30):
		
	# 		#cur_txt_comment = (cur_rec[15]).decode("utf-8").split(u"Text")
	# 		#cur_txt_comment = str(cur_rec[15]).split("</Text>")
	# 		#comment_line = cur_rec[15].decode('cp866')
	# 		#deltxt=cur_par[30][17:(len(cur_par))].split(u'</')
	# 		deltxt=cur_par[30][17:]
	# 		#deltxt ="gjjkjklj/jkjks/Tklk;"
			
	# 		#deltxt = re.split(r'/T', deltxt)
			
	# 		#print unichr(struct.unpack('>i',chr(deltxt[0][2:4].encode("hex"))))
	# 		#Длина комментария 2 byte символ
	# 		cmt_txt_len=abs(len(deltxt)/2)*2
	# 		#cmt_txt_len=8
	# 		#Финальный текст комментария
	# 		finish_comment='';
	# 		#print abs(cmt_txt_len /2)*2
	# 		j=0
	# 		while j<cmt_txt_len:
	# 			codchr = deltxt[j:j+2]
	# 			finish_comment+=unichr(int(struct.unpack("<H", codchr)[0]))
	# 			j+=2
	# 		'''
	# 		codchr = deltxt[0][0:2]
	# 		print deltxt[0].encode("hex"), codchr.encode("hex"),unichr(int(struct.unpack("<H", codchr)[0]))
	# 		codchr = deltxt[0][2:4]
	# 		print deltxt[0].encode("hex"), codchr.encode("hex"),unichr(int(struct.unpack("<H", codchr)[0]))
	# 		'''
	# 		#print int(struct.unpack("h", codchr[0]))
	# 		#codchr=struct.pack('>H',deltxt[0][0:2])
			
			
	# 		#print deltxt[0][0:2].encode("hex") #,int(deltxt[0][0:2].encode("hex")), len (deltxt[0])
	# 		#print deltxt[0][2:4].encode("hex")
			
			
	# 		#print unicode(deltxt[0])
	# 		finish_comment = re.split(r"</T", finish_comment)
	# 		#print finish_comment[0]#, deltxt.encode("hex")#deltxt[0].encode("hex"), cur_par[30].encode("hex")
	# 		#print "dbid="+str(cur_rec[0]),"uidObjMessage="+str(cur_rec[5]),"dTimLastChange"+str(cur_rec[4]),"dTim="+str(cur_rec[6]), "objImage=","objPosition="+str(int(round(float(cur_rec[18])*100)))
	# 	#Если зашифровано
	# 	else:
	# 			finish_comment = "Encrypted"
	# 	# left =int(round(float(cur_rec[18])*100))
	# 	# #Поиск
	# 	# db_name=table
	# 	# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	# 	# cursor = db.cursor()
	# 	# sql = "SELECT Vrema, Comment FROM "+db_name+" WHERE Vrema = "+str(cur_unix_time)+ " AND Comment =" + "'"+finish_comment.encode('utf-8')+"'"
	# 	# #sql = "SELECT Vrema, Comment FROM "+db_name+" WHERE Vrema = "+str(cur_unix_time)
	# 	# cursor.execute(sql)
	# 	# data =  cursor.fetchall()
	# 	# #print data
		
        
    #     #выгрузка в базу
    #     # if len(data) == 0:
	# 	# 	#Вставка
	# 	# 	db_name=table
	# 	# 	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	# 	# 	cursor = db.cursor()
	# 	# 	sql = "INSERT INTO "+db_name+"(Vrema, Comment, left_txt) VALUE ( "+str(cur_unix_time)+", "+"'"+finish_comment.encode('utf-8')+"'"+", "+str(left)+" )"
	# 	# 	cursor.execute(sql)
	# 	# 	db.commit()
	# 	# i+=1
	# 	# db.close()
	
	


#Комментарии Logsbuilder


#544
t629 = Process(target=read_well, args=["/mnt/544o/Archive","s544kr"])
t629.start()
t629.join(360)
if t629.is_alive(): t629.terminate()


# #71
# t4450 = Process(target=read_well, args=["/mnt/4450o/Archive","s4450kr"])
# t4450.start()
# t4450.join(10)
# if t4450.is_alive(): t4450.terminate()

# #610
# t41450 = Process(target=read_well, args=["/mnt/610o/Archive","s610kr"])
# t41450.start()
# t41450.join(10)
# if t44150.is_alive(): t44150.terminate()

# #9917
# t11450 = Process(target=read_well, args=["/mnt/630o/Archive","s630kr"])
# t11450.start()
# t11450.join(10)
# if t14150.is_alive(): t14150.terminate()


# #938
# t21450 = Process(target=read_well, args=["/mnt/20o/Archive","s20kr"])
# t21450.start()
# t21450.join(10)
# if t24150.is_alive(): t24150.terminate()



# #632
# t31450 = Process(target=read_well, args=["/mnt/629o/Archive","s629kr"])
# t31450.start()
# t31450.join(10)
# if t23150.is_alive(): t23150.terminate()

# # #104
# # t20 = Process(target=read_well, args=["/mnt/104o/Archive","s110kr"])
# # t20.start()
# # t20.join(360)
# # if t20.is_alive(): t20.terminate()

# # #629
# # t629 = Process(target=read_well, args=["/mnt/631o/Archive","s629kr"])
# # t629.start()
# # t629.join(360)
# # if t629.is_alive(): t629.terminate()

# '''
# #928
# t928 = Process(target=read_well, args=["/mnt/928","s631kr"])
# t928.start()
# t928.join(10)
# if t928.is_alive(): t928.terminate()

# #547
# t547 = Process(target=read_well, args=["/mnt/547","s908kr"])
# t547.start()
# t547.join(10)
# if t547.is_alive(): t547.terminate()

# #3ГФ
# t3 = Process(target=read_well, args=["/mnt/3","s224kr"])
# t3.start()
# t3.join(10)
# if t3.is_alive(): t3.terminate()

# #96
# t96 = Process(target=read_well, args=["/mnt/96","s89kr"])
# t96.start()
# t96.join(10)
# if t96.is_alive(): t96.terminate()

# """
# #4450
# #read_well("/mnt/4450","s4450")
# t4450 = Process(target=read_well, args=["/mnt/4450","s4450"])
# t4450.start()
# t4450.join(10)
# if t4450.is_alive(): t4450.terminate()
# #630
# #read_well("/mnt/630","s630")
# t630 = Process(target=read_well, args=["/mnt/630","s630"])
# t630.start()
# t630.join(10)
# if t630.is_alive(): t630.terminate()
# #read_well("/mnt/630","s630")
# #631
# #threading.Thread(target=read_well, args=["/mnt/631","s631"]).join(5)
# #read_well("/mnt/631","s631")

# """
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
# '''
#!/usr/bin/env python
# -*- coding: utf-8  -*-
import MySQLdb
import string
import random
import time
from datetime import datetime
import subprocess
#import pyping
import sys
import threading
from multiprocessing import Process
import os
from ping3 import do_one, verbose_ping
# import ping3 
import pyping

import gmail_post
import telegram_post
#import whatsapp_post
import struct
#import megamultiping


def fullchr(n):
    return struct.pack('<I', n).decode('utf-32le')


def check_trouble (poz_type, name_well,ip_well,ip_poz,ip_obrab,name_base,ippoz_modem,ip_signal,ip_dvr, ip_cam1, ip_cam2, ip_cam3, ip_cam4, ip_ub1, ip_ub2, ip_sbor, analogdvr, ip_gbox):
	
	# #Текущее время
	timestamp = int(time.time())+60*60*4
	#Контора
	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8mb4')
	cursor = db.cursor()
	#Поиск последних трех записей
	sql = "SELECT * FROM pconnect ORDER BY `date` DESC LIMIT 1"
	cursor.execute(sql)
	konrecords = cursor.fetchall()
	
	#Скважины
	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8mb4')
	cursor = db.cursor()
	#Поиск последних трех записей
	sql = "SELECT * FROM "+db_name+" ORDER BY `date` DESC LIMIT 3"
	cursor.execute(sql)
	treerecords = cursor.fetchall()
	#print "=====",datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),name_well, ip_well
	
	message = "UP"
	bigmessage = ""
	#print treerecords[0][24],treerecords[0][25]
	#Проверки Три последних записи и до конторы VPN работает
	# print (treerecords)
	if len(treerecords) == 3: # and konrecords[0][4]>0:
		# print ("сячся")
		#Время начала события
		timestamp =int(treerecords[0][0])
		#Luch на Зухеле
		# if poz_type == False:
			#   if luch == True:
			# 	if treerecords[1][25]==treerecords[2][25]:
			# 				message = "DOWN"
			# 				bigmessage =(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Луч не передает данные со скважины "+name_well+"\n"
			# 	else:                            
			# 				message = "UP"
			# 				bigmessage =(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Луч не передает данные со скважины "+name_well+"\n"
        #Завис MLCache на Зухеле
		# if poz_type == False and name_well!="235":
		# 		if treerecords[0][22]<=0.01:
		# 			if treerecords[1][22]<=0.01:
		# 				if treerecords[2][22]<=0.01:
		# 					message = "DOWN"
		# 					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " MLCache не передает данные с Обработчика: "+ip_obrab+"\n"
        #Проверка прочего
		# if  message != "DOWN":
		# 	bigmessage=""
		# 	#Mlcache
		# 	if treerecords[0][4] <0 and name_well!="235":
		# 		if treerecords[1][4] <0:
		# 			if treerecords[2][4] <0:
		# 				message = "DOWN"
		# 				bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+" Выключен Mlcache на Обработчике: "+ip_obrab+"\n"
		#Видеорегистратор
		if treerecords[0][8] <0:
			if treerecords[1][8] <0:
				if treerecords[2][8] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Выключен Видеорегистратор: "+ip_dvr+"\n"
		
		#Ubi1
		if analogdvr == False:
			if treerecords[0][13] <0:
				if treerecords[1][13] <0:
					if treerecords[2][13] <0:
						message = "DOWN"
						bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+" Сломалась Ubi1_Ap: "+ip_ub1+"\n"
						
		#Ubi2
		if analogdvr == False:
			if treerecords[0][14] <0:
				if treerecords[1][14] <0:
					if treerecords[2][14] <0:
						message = "DOWN"
						bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+" Сломалась Ubi2_Client: "+ip_ub2+"\n"
		
		#Камера 1
		if treerecords[0][9] <0:
			if treerecords[1][9] <0:
				if treerecords[2][9] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Сломалась CAM1: "+ip_cam1+"\n"
		#Камера 2
		if treerecords[0][10] <0:
			if treerecords[1][10] <0:
				if treerecords[2][10] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Сломалась CAM2: "+ip_cam2+"\n"
		#Камера 3
		if treerecords[0][11] <0:
			if treerecords[1][11] <0:
				if treerecords[2][11] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Сломалась CAM3: "+ip_cam3+"\n"
		#Камера 4
		if treerecords[0][12] <0:
			if treerecords[1][12] <0:
				if treerecords[2][12] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Сломалась CAM4: "+ip_cam4+"\n"
		#Сборщик
		if treerecords[0][13] <0:
			if treerecords[1][13] <0:
				if treerecords[2][13] <0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Выключен Сборщик: "+ip_sbor+"\n"
		#Выключен Обработчик
		if treerecords[0][24]<0:
			if treerecords[1][24]<0:
				if treerecords[2][24]<0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Выключен Обработчик: "+ip_obrab+"\n"
		#Выключен Gbox
		if treerecords[0][25]<0:
			if treerecords[1][25]<0:
				if treerecords[2][25]<0:
					message = "DOWN"
					bigmessage +=(fullchr(random.randrange(0x1F680,0x1F6A4))).encode("utf-8")+ " Выключен Gbox: "+ip_gbox+"\n"
		

		#Проверка пинга white ip
		if treerecords[0][1] <0:
			if treerecords[1][1] <0:
				if treerecords[2][1] <0:
					message = "DOWN"
					bigmessage =" Отвалился Мегафон: "+ip_well+"\n"				
		#Если все работает			
		if  message != "DOWN":
			bigmessage = "Все работает \xF0\x9F\x91\x8D"
	# print (bigmessage)
	#Поиск последнего события дл\xF0\x9F\x91\x8Dя текущей скважины	
	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8mb4')
	cursor = db.cursor()
	sql = "SELECT * FROM alarm WHERE nwell="+name_well+" ORDER BY `date` DESC LIMIT 1"
	cursor.execute(sql)
	alarmnwell =cursor.fetchall()
	#print cursor.fetchall(), len(alarmnwell)
	#Если событий еще никаких не было то добавим событие 1
	if len(alarmnwell)==0:
		db_name=name_base
		db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8mb4')
		cursor = db.cursor()
		sql = "INSERT INTO alarm(date, nwell, mess, bigmess) VALUES ("+str(timestamp)+",'"+str(name_well)+"','"+str(message)+"','"+str(bigmessage)+"')"
		cursor.execute(sql)
		mailtmp=unicode(" "+
		""+datetime.utcfromtimestamp(timestamp).strftime('%H:%M')+" Скв."+str(name_well)+
		"\n\n"+bigmessage, "utf8")
		#print alarmnwell[0][2],message,mailtmp
		#gmail_post.post(mailtmp,"Скважина: "+str(name_well))
		telegram_post.post(mailtmp,"-576447110")
	#Если событие было
	if len(alarmnwell)!=0:
		# print (alarmnwell)
		# print (message)
		
		#И оно было другое, то запись в базу и посылка почты
		if alarmnwell[0][2]!=message:
			print (alarmnwell)
			db_name=name_base
			db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8mb4')
			cursor = db.cursor()
			sql = "INSERT INTO alarm(date, nwell, mess, bigmess) VALUES ("+str(timestamp)+",'"+str(name_well)+"','"+str(message)+"','"+unicode(bigmessage, "utf-8")+"')"
			cursor.execute(sql)
			mailtmp=unicode(" "+
			""+datetime.utcfromtimestamp(timestamp).strftime('%H:%M')+" Скв."+str(name_well)+
			"\n\n"+bigmessage, "utf8")
			# print (message, mailtmp)
			#gmail_post.post(mailtmp,"Скважина: "+str(name_well))
			telegram_post.post(mailtmp,"-576447110")
			#whatsapp_post.post(mailtmp,"79272857676-1490802779")
			
			
		
		#date, average,rx,tx,ml,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor, ub1amc, ub1amq, ub1signal, ub2amc, ub2amq, ub2signal = -1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-100.0,-1.0,-1.0,-100.0,-1.0,-1.0
	# print average
	db.commit()
	db.close()
	#Поиск трех последних записей
	#SELECT * FROM `p192168146161` ORDER BY `date` DESC LIMIT 3 
	#Проверка сломалось ли что-то, в поле три значения меньше 0
	#Чтение последнего сообщения(состояния), если отличное от текущего то записываем в алярм и  посылаем почту
	#ip_well
	# average,ml,rx,tx,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor, ub1amc, ub1amq, ub1signal, ub2amc, ub2amq, ub2signal=-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-100.0,-1.0,-1.0,-100.0,-1.0,-1.0
	
	# average8888,average62220,average8084,average773,average3117=-1,-1,-1,-1,-1
	# #pools={ip_well,ip_dvr,ip_ub1,ip_ub2,ip_sbor,ip_cam1,ip_cam2,ip_cam3,ip_cam4}
	# #Mlcache
	# out1=mlcache.mlcacheOn(ip_obrab)
	# if (len(out1)==1):
		# ml=2
	# else:
		# ml=-1
	# if (len(out1)==5):
		# ml=1.8
	# average=-1
	
	# if (poz_type):
		# #Speed poz_br0
		# rx,tx= tellnet.speed(ip_poz,"5188",int(c))
	# else:
		# #Speed zyxel
		# tx,rx=zyxel.speed_zyxel(ip_poz,"5188",int(c))
	
	# #Speed poz_modem
	# mrx, mtx = pozmodem.speed(ippoz_modem,"5188",int(c))
	
	# #Signal level
	# signal = pozmodemsignal.signal(ip_signal,"5188",int(c))
	
	
	# #Signal Ubi1 ubisignal how connect!
	# ub1signal, ub1amq, ub1amc =ubisignal_ap.ubisignal(ip_ub1,"22",5,2, True)
	
	# #Signal Ubi2
	# ub2signal, ub2amq, ub2amc =ubisignal_ap.ubisignal(ip_ub2,"22",5,2, False)
	
	
	# #pings
	# #white adrr
	# # average,dvr,ub1,ub2,sbor,cam1,cam2,cam3,cam4 = megamultiping.ping(pools)
	# average=verbose_ping(ip_well)
	# #average = megamultiping.ping(ip_well)
	# #ip_well,ip_dvr,ip_ub1,ip_ub2,ip_sbor,ip_cam1,ip_cam2,ip_cam3,ip_cam4)
	# #dvr
	# dvr=verbose_ping(ip_dvr)
	# #dvr = megamultiping.ping(ip_dvr)
	# #Ubi1_Ap
	# ub1=verbose_ping(ip_ub1)
	# #ub1 = megamultiping.ping (ip_ub1)
	# #Ubi2_Client
	# ub2=verbose_ping(ip_ub2)
	# #ub2 = megamultiping.ping (ip_ub2)
	# #Sbor
	# sbor=verbose_ping(ip_sbor)
	# #sbor = megamultiping.ping (ip_sbor)

	
	# #cams
	# if (analogdvr!=True):
		# cam1=verbose_ping(ip_cam1)
		# cam2=verbose_ping(ip_cam2)
		# cam3=verbose_ping(ip_cam3)
		# cam4=verbose_ping(ip_cam4)
		# # cam1 = megamultiping.ping (ip_cam1)
		# # cam2 = megamultiping.ping (ip_cam2)
		# # cam3 = megamultiping.ping (ip_cam3)
		# # cam4 = megamultiping.ping (ip_cam4)
	# else:
		# if (dvr>0):
			# #DO TEST ANALOG CAMS!
			# cam1=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_1.jpg")
			# cam2=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_2.jpg")
			# cam3=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_3.jpg")
			# cam4=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_4.jpg")
		
			# # cam1=1
			# # cam2=1
			# # cam3=1
			# # cam4=1
	
	
	# threadLock.acquire()

	# threadLock.release()
	
	
	# # #Текущее время
	# timestamp = int(time.time())+60*60*4

	# db_name=name_base
	# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	# cursor = db.cursor()
	# sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml, mrx, mtx, sigpoz, dvr, cam1, cam2, cam3, cam4, ub1, ub2, sbor, ub1amc, ub1amq, ub1sig, ub2amc, ub2amq, ub2sig) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+","+str(mrx)+","+str(mtx)+","+str(signal)+","+str(dvr)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(ub1)+","+str(ub2)+","+str(sbor)+","+str(ub1amc)+","+str(ub1amq)+","+str(ub1signal)+","+str(ub2amc)+","+str(ub2amq)+","+str(ub2signal)+")"
	# cursor.execute(sql)
	# db.commit()
	# db.close()
	

# #Текущее время
# timestamp = int(time.time())+60*60*4

# db_name='pconnect'
# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
# cursor = db.cursor()
# sql = "INSERT INTO "+db_name+"(date, p8888, p6222055149, p8084114180, p192168773, p31173187210) VALUE ("+str(timestamp)+","+str(average8888)+","+str(average62220)+","+str(average8084)+","+str(average773)+","+str(average3117)+")"
# cursor.execute(sql)
# db.commit()
# db.close()

# threadLock = threading.Lock()

												#zux/poz,?
                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Luch

#789 533
# check_trouble(False,"789","31.173.139.241","192.168.147.129","192.168.147.131","p3729899","192.168.19.49","192.168.19.49","192.168.147.135","192.168.147.136","192.168.147.137","192.168.147.138","192.168.147.139","192.168.147.141","192.168.147.140","192.168.147.130", False, False)
#

# 2103 542
check_trouble(False,"2103","31.173.139.91","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False, "192.168.146.238")
# threading.Thread(target=check_troble, args=[False,"915","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False]).start()
# pp915 = Process(target=check_trouble, args=(False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False))
# pp915.start()
# pp915.join()

# 935 534
check_trouble(False,"935","31.173.139.221","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False, "192.168.146.206")
# threading.Thread(target=check_troble, args=[False,"628","83.149.18.62","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False]).start()
# pp628 = Process(target=check_trouble, args=(False,"224","83.149.18.62","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False))
# pp628.start()
# pp628.join()

# 707 211Д 1РФ 71 37.29.103.111
check_trouble(False,"707","31.173.187.217","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False, "192.168.146.46")
# threading.Thread(target=check_troble, args=[False,"6611","31.173.177.246","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False]).start()
# pp6611 = Process(target=check_trouble, args=(False,"411","31.173.177.246","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False))
# pp6611.start()
# pp6611.join()

#240 228 Саратов 604
# check_trouble(False,"240","178.176.50.33","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False, "192.168.146.110")
# threading.Thread(target=check_troble, args=[True,"84","31.173.139.250","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False]).start()
# pp84 = Process(target=check_trouble, args=(True,"916","31.173.139.250","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False))
# pp84.start()
# pp84.join()

#721
# check_trouble(False,"721","37.29.98.26","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False, "192.168.146.78")

#51 721 450 828
check_trouble(False,"51","37.29.8.131","192.168.146.97","192.168.146.99",     "p372978226", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False, "192.168.146.78")
# threading.Thread(target=check_troble, args=[True,"605","78.25.78.110","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False]).start()
# pp715 = Process(target=check_trouble, args=(True,"110","78.25.78.110","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False))
# pp715.start()
# pp715.join()

#118 201 938 73
check_trouble(False,"118","37.29.78.251","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False, "192.168.146.177" )
# threading.Thread(target=check_troble, args=[True,"73","31.173.139.222","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False]).start()
# pp73 = Process(target=check_trouble, args=(True,"73","31.173.139.222","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False))
# pp73.start()
# pp73.join()

#535 629 632
check_trouble(False,"535","37.29.8.137","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.20","192.168.146.26",  "192.168.146.27", "192.168.146.28","192.168.146.29","192.168.146.24", "192.168.146.25", "192.168.146.19", False, "192.168.146.30")
# threading.Thread(target=check_troble, args=[False,"629","37.29.8.14","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.24","192.168.146.24",  "192.168.146.24", "192.168.146.24","192.168.146.24","192.168.146.24", "192.168.146.24", "192.168.146.19", True]).start()
# pp629 = Process(target=check_trouble, args=(False,"631","37.29.8.14","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.24","192.168.146.24",  "192.168.146.24", "192.168.146.24","192.168.146.24","192.168.146.24", "192.168.146.24", "192.168.146.19", True))
# pp629.start()
# pp629.join()

#4УПД 701 107
#99[False,"540","192.168.146.65","192.168.147.65","192.168.147.67",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.147.71","192.168.147.72",  "192.168.147.73", "192.168.147.74","192.168.147.75","192.168.147.76", "192.168.147.77", "192.168.147.66", False, "2"]
check_trouble(True,"4UPD","31.173.139.225","192.168.147.65","192.168.147.67",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.147.71","192.168.147.72",  "192.168.147.73", "192.168.147.74","192.168.147.75","192.168.147.76", "192.168.147.77", "192.168.147.66", False, "192.168.147.78")
# threading.Thread(target=check_troble, args=[False,"96","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True]).start()
# pp96 = Process(target=check_trouble, args=(False,"110","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# pp96.start()
# pp96.join()

#101 222 106 83
# check_trouble(False,"101","31.173.187.207","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.136",  "192.168.146.137", "192.168.146.138","192.168.146.139","192.168.146.140", "192.168.146.141", "192.168.146.130", False, "192.168.146.142")
# threading.Thread(target=check_troble, args=[True,"83","31.173.139.134","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True]).start()
# pp83 = Process(target=check_trouble, args=(False,"110","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# pp83.start()
# pp83.join()


												#zux/poz,?
                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR


#449 406
# check_trouble(False,"449","37.29.98.103","192.168.146.1","192.168.146.3",  "p1921681461", "192.168.19.225","192.168.19.225","192.168.146.7","192.168.146.8",    "192.168.146.9", "192.168.146.10", "192.168.146.11", "192.168.146.12", "192.168.146.13", "192.168.146.2", False, "192.168.146.14")
#threading.Thread(target=check_troble, args=[True,"401","31.173.139.129","192.168.146.1","192.168.146.3",  "p1921681461", "192.168.19.225","192.168.19.225","192.168.146.7","192.168.146.7",          "192.168.146.7", "192.168.146.7", "192.168.146.7", "192.168.146.7", "192.168.146.7", "192.168.146.2", True]).start()
# pp83 = Process(target=check_trouble, args=(False,"401","37.29.103.214","192.168.146.49","192.168.146.51",  "p1921681461", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# pp83.start()
# pp83.join()

#325 260
# check_trouble(False,"325","31.173.187.233","192.168.147.1","192.168.147.3",  "p1921681471", "192.168.19.225","192.168.19.225","192.168.147.7","192.168.147.8",    "192.168.147.9", "192.168.147.10", "192.168.147.11", "192.168.147.12", "192.168.147.13", "192.168.147.2", False, "192.168.147.30")
#threading.Thread(target=check_troble, args=[True,"610","31.173.139.129","192.168.147.1","192.168.147.3",  "p1921681471", "192.168.19.225","192.168.19.225","192.168.147.7","192.168.147.7",          "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.2", True]).start()
# pp83 = Process(target=check_trouble, args=(False,"610","37.29.103.214","192.168.147.49","192.168.147.51",  "p1921681471", "192.168.19.161","192.168.19.161","192.168.147.53","192.168.147.53",  "192.168.147.53", "192.168.147.53","192.168.147.53","192.168.147.53", "192.168.147.53", "192.168.147.50", True))
# pp83.start()
# pp83.join()

#627
# check_trouble(False,"627","37.29.14.185","192.168.147.33","192.168.147.33",  "p19216814733", "192.168.19.225","192.168.19.225","192.168.147.39","192.168.147.40",          "192.168.147.41", "192.168.147.42", "192.168.147.43", "192.168.147.44", "192.168.147.45", "192.168.147.34", False, False)
#threading.Thread(target=check_troble, args=[True,"610","31.173.139.129","192.168.147.1","192.168.147.3",  "p1921681471", "192.168.19.225","192.168.19.225","192.168.147.7","192.168.147.7",          "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.7", "192.168.147.2", True]).start()
# pp83 = Process(target=check_trouble, args=(False,"610","37.29.103.214","192.168.147.49","192.168.147.51",  "p1921681471", "192.168.19.161","192.168.19.161","192.168.147.53","192.168.147.53",  "192.168.147.53", "192.168.147.53","192.168.147.53","192.168.147.53", "192.168.147.53", "192.168.147.50", True))
# pp83.start()
# pp83.join()


#602 Ставрополь-153 Гривенская-16 Краснодар	  False,"16","192.168.0.250","192.168.0.250","192.168.0.2",        "p19216801", "192.168.19.161","192.168.19.161","192.168.0.64","192.168.0.69",    "192.168.0.66", "192.168.0.67", "192.168.0.68", "192.168.0.21", "192.168.0.22", "192.168.0.1", False, "3", "192.168.0.55"
check_trouble(False,"602","37.29.8.139","192.168.152.250","192.168.152.2",        "p19216801", "192.168.19.161","192.168.19.161","192.168.152.64","192.168.152.69",    "192.168.152.66", "192.168.152.67", "192.168.152.68", "192.168.152.21", "192.168.152.22", "192.168.152.3", False, "192.168.152.55")

#Степновская-438 Саратов	  False,"16","192.168.0.250","192.168.0.250","192.168.0.2",        "p19216801", "192.168.19.161","192.168.19.161","192.168.0.64","192.168.0.69",    "192.168.0.66", "192.168.0.67", "192.168.0.68", "192.168.0.21", "192.168.0.22", "192.168.0.1", False, "3", "192.168.0.55"
check_trouble(False,"438","192.168.148.250","192.168.148.250","192.168.148.2",        "p1921681481", "192.168.19.97","192.168.19.97","192.168.148.64","192.168.148.69",    "192.168.148.66", "192.168.148.67", "192.168.148.68", "192.168.148.21", "192.168.148.22", "192.168.148.1", False, "192.168.148.55")

#1 Восточно-Ивановское Краснодар
# check_trouble(False,"1","192.168.150.250","192.168.150.250","192.168.150.2",        "p1921681501", "192.168.19.145","192.168.19.145","192.168.150.64","192.168.150.69",    "192.168.150.66", "192.168.150.67", "192.168.150.68", "192.168.150.21", "192.168.150.22", "192.168.150.1", False, "192.168.150.55")


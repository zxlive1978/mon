#!/usr/bin/env python
# -*- coding: utf-8
import MySQLdb
import string
import time
import subprocess
#import pyping
import sys
import threading
from multiprocessing import Process
from ping3 import do_one, verbose_ping
# import ping3 

import telnetlib
#Speed test
import tellnet
#import tellnetipsec
#Test Mlcahe
import mlcache
#Speed zyxel
import zyxel
import pozmodem
import pozmodemsignal



def read_zyxel_ping_rxtx (poz_type, name_well,ip_well,ip_poz,ip_obrab,name_base,ippoz_modem,ip_signal,ip_dvr, ip_cam1, ip_cam2, ip_cam3, ip_cam4, ip_ub1, ip_ub2, ip_sbor, analogdvr):
	#Speed Время измерения
	c=10
	rx,tx,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor=-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0

	#Mlcache
	out1=mlcache.mlcacheOn(ip_obrab)
	if (len(out1)==1):
		ml=2
	else:
		ml=-1
	if (len(out1)==5):
		ml=1.8
	average=-100
	
	if (poz_type):
		#Speed poz_br0
		rx,tx= tellnet.speed(ip_poz,"5188",int(c))
	else:
		#Speed zyxel
		tx,rx=zyxel.speed_zyxel(ip_poz,"5188",int(c))
	
	#Speed poz_modem
	mrx, mtx = pozmodem.speed(ippoz_modem,"5188",int(c))
	
	#Signal level
	signal = pozmodemsignal.signal(ip_signal,"5188",int(c))
	
	#white adrr
	average = verbose_ping(ip_well)
	#dvr
	dvr = verbose_ping(ip_dvr)
	
	
	#cams
	if (analogdvr!=True):
		cam1 = verbose_ping (ip_cam1)
		cam2 = verbose_ping (ip_cam2)
		cam3 = verbose_ping (ip_cam3)
		cam4 = verbose_ping (ip_cam4)
	else:
		if (dvr>0):
		#DO TEST ANALOG CAMS!
			cam1=1
			cam2=1
			cam3=1
			cam4=1
	
	#Ubi1_Ap
	ub1 = verbose_ping (ip_ub1)
		
	#Ubi2_Client
	ub2 = verbose_ping (ip_ub2)
		
	#Sbor
	sbor = verbose_ping (ip_sbor)
	
	# #Текущее время
	timestamp = int(time.time())+60*60*4

	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	cursor = db.cursor()
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml, mrx, mtx, sigpoz, dvr, cam1, cam2, cam3, cam4, ub1, ub2, sbor) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+","+str(mrx)+","+str(mtx)+","+str(signal)+","+str(dvr)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(ub1)+","+str(ub2)+","+str(sbor)+")"
	cursor.execute(sql)
	db.commit()
	



#8888
average8888 = verbose_ping ('8.8.8.8')

#62.220.55.149
average62220 = verbose_ping ('62.220.55.149')

#80.247.113.226
average8084 = verbose_ping ('80.247.113.226')

#192.168.77.3
average773 = verbose_ping ('192.168.77.3')
	
#31.173.187.210
average3117 = verbose_ping ('31.173.187.210')

#Текущее время
timestamp = int(time.time())+60*60*4

db_name='pconnect'
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql = "INSERT INTO "+db_name+"(date, p8888, p6222055149, p8084114180, p192168773, p31173187210) VALUE ("+str(timestamp)+","+str(average8888)+","+str(average62220)+","+str(average8084)+","+str(average773)+","+str(average3117)+")"
cursor.execute(sql)
db.commit()




												#zux/poz,?
                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR



#915
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False]).start()

#628
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"224","83.149.18.62","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False]).start()

#6611
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"411","31.173.177.246","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False]).start()

#84
threading.Thread(target=read_zyxel_ping_rxtx, args=[True,"916","31.173.139.250","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False]).start()

#715
threading.Thread(target=read_zyxel_ping_rxtx, args=[True,"110","78.25.78.110","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False]).start()

#73
threading.Thread(target=read_zyxel_ping_rxtx, args=[True,"73","31.173.139.222","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False]).start()

#629
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"4450","37.29.8.14","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.24","192.168.146.24",  "192.168.146.24", "192.168.146.24","192.168.146.24","192.168.146.24", "192.168.146.24", "192.168.146.19", True]).start()

#96
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"89","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True]).start()

db.close()
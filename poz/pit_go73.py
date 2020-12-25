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
import os
from ping3 import do_one, verbose_ping
# import ping3 
import pyping
import telnetlib
#Speed test
import tellnet
#import tellnetipsec
#Test Mlcahe
import mlcache
#Speed zyxel
import zyxel
import zyxel_sngs_port2206
import zyxel_wan_all

import pozmodem
import pozmodemsignal
import badanalogcam
import ubisignal_ap
#import megamultiping



def read_zyxel_ping_rxtx (poz_type, name_well,ip_well,ip_poz,ip_obrab,name_base,ippoz_modem,ip_signal,ip_dvr, ip_cam1, ip_cam2, ip_cam3, ip_cam4, ip_ub1, ip_ub2, ip_sbor, analogdvr, ubi_ver):
	#Speed Время измерения
	c=5
	average,ml,rx,tx,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor, ub1amc, ub1amq, ub1signal, ub2amc, ub2amq, ub2signal,mlrx,mltx=-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-100.0,-1.0,-1.0,-100.0,-1.0,-1.0,-1.0,-1.0
	#pools={ip_well,ip_dvr,ip_ub1,ip_ub2,ip_sbor,ip_cam1,ip_cam2,ip_cam3,ip_cam4}
	#Mlcache
	out1=mlcache.mlcacheOn(ip_obrab)
	if (len(out1)==1 or len(out1)==2):
		ml=2
	else:
		ml=-1
	if (len(out1)==5):
		ml=1.8
	average=-1
	print "mlcache\n"
	
	if (poz_type):
		#Speed poz_br0
		rx,tx= tellnet.speed(ip_poz,"5188",int(c))
	else:
		#Speed zyxel
		# if (name_well == "604"):
			# tx,rx = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "213.80.235.178")
		# else:
			# tx,rx=zyxel.speed_zyxel(ip_poz,"5188",int(c))
		tx,rx = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "213.80.235.178")
		mlrx,mltx=zyxel_sngs_port2206.speed_zyxel(ip_poz,"5188",int(c), "213.80.235.178")
		#tx,rx=-1,-1
	print "speed zyxel/poz\n"
	
	#Speed poz_modem
	mrx, mtx = pozmodem.speed(ippoz_modem,"5188",int(c))
	print "speed poz\n"
	
	#Signal level
	signal = pozmodemsignal.signal(ip_signal,"5188",int(c))
	print "signal poz\n"
	
	
	#Signal Ubi1 ubisignal how connect!
	ub1signal, ub1amq, ub1amc =ubisignal_ap.ubisignal(ip_ub1,"22",5,2, True, ubi_ver)
	print "ubi1\n"
	
	#Signal Ubi2
	ub2signal, ub2amq, ub2amc =ubisignal_ap.ubisignal(ip_ub2,"22",5,2, False, ubi_ver)
	print "ubi2\n"
	
	threadLock.acquire()
	#pings
	#white adrr
	# average,dvr,ub1,ub2,sbor,cam1,cam2,cam3,cam4 = megamultiping.ping(pools)
	average=verbose_ping(ip_well)
	print "ping well\n"
	#average = megamultiping.ping(ip_well)
	#ip_well,ip_dvr,ip_ub1,ip_ub2,ip_sbor,ip_cam1,ip_cam2,ip_cam3,ip_cam4)
	#dvr
	dvr=verbose_ping(ip_dvr)
	print "ping dvr\n"
	#dvr = megamultiping.ping(ip_dvr)
	#Ubi1_Ap
	ub1=verbose_ping(ip_ub1)
	print "ping ubi1\n"
	#ub1 = megamultiping.ping (ip_ub1)
	#Ubi2_Client
	ub2=verbose_ping(ip_ub2)
	print "ping ubi2\n"
	#ub2 = megamultiping.ping (ip_ub2)
	#Sbor
	sbor=verbose_ping(ip_sbor)
	print "ping sbor\n"
	#sbor = megamultiping.ping (ip_sbor)

	
	#cams
	if (analogdvr!=True):
		cam1=verbose_ping(ip_cam1)
		cam2=verbose_ping(ip_cam2)
		cam3=verbose_ping(ip_cam3)
		cam4=verbose_ping(ip_cam4)
		print "ping cams\n"
		# cam1 = megamultiping.ping (ip_cam1)
		# cam2 = megamultiping.ping (ip_cam2)
		# cam3 = megamultiping.ping (ip_cam3)
		# cam4 = megamultiping.ping (ip_cam4)
	else:
		if (dvr>0):
			#DO TEST ANALOG CAMS!
			cam1=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_1.jpg")
			cam2=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_2.jpg")
			cam3=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_3.jpg")
			cam4=badanalogcam.check_crash_cam("/var/www/html/mon/poz/"+name_well+"_4.jpg")
		
			# cam1=1
			# cam2=1
			# cam3=1
			# cam4=1
	
	
	

	threadLock.release()
	
	
	# #Текущее время
	timestamp = int(time.time())+60*60*4

	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	cursor = db.cursor()
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml, mrx, mtx, sigpoz, dvr, cam1, cam2, cam3, cam4, ub1, ub2, sbor, ub1amc, ub1amq, ub1sig, ub2amc, ub2amq, ub2sig, mlrx, mltx) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+","+str(mrx)+","+str(mtx)+","+str(signal)+","+str(dvr)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(ub1)+","+str(ub2)+","+str(sbor)+","+str(ub1amc)+","+str(ub1amq)+","+str(ub1signal)+","+str(ub2amc)+","+str(ub2amq)+","+str(ub2signal)+","+str(mlrx)+","+str(mltx)+")"
	print sql
	cursor.execute(sql)
	db.commit()
	db.close()
	


average8888,average62220,average8084,average773,average3117=-1,-1,-1,-1,-1
#8888
r = pyping.ping('8.8.8.8')
if (r.ret_code==0):
		average8888=r.avg_rtt
#average8888 = megamultiping.ping ('8.8.8.8')

#62.220.55.149
r = pyping.ping('62.220.55.149')
if (r.ret_code==0):
		average62220=r.avg_rtt
#average62220 = megamultiping.ping ('62.220.55.149')

#80.247.113.226
r = pyping.ping('80.247.113.226')
if (r.ret_code==0):
		average8084=r.avg_rtt
#average8084 = megamultiping.ping ('80.247.113.226')

#213.80.235.178
r = pyping.ping('213.80.235.178')
if (r.ret_code==0):
		average773=r.avg_rtt
#average773 = megamultiping.ping ('192.168.77.3')

	
#31.173.187.210
r = pyping.ping('31.173.187.210')
if (r.ret_code==0):
		average3117=r.avg_rtt
#average3117 = megamultiping.ping ('31.173.187.210')

#Текущее время
timestamp = int(time.time())+60*60*4

db_name='pconnect'
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql = "INSERT INTO "+db_name+"(date, p8888, p6222055149, p8084114180, p192168773, p31173187210) VALUE ("+str(timestamp)+","+str(average8888)+","+str(average62220)+","+str(average8084)+","+str(average773)+","+str(average3117)+")"
cursor.execute(sql)
db.commit()
db.close()

threadLock = threading.Lock()

												#zux/poz,?
                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Версия_прошики_Ubi




#71 31.173.177.246 6611
# read_zyxel_ping_rxtx(False,"411","37.29.78.223","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False)
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"411","37.29.103.111","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False, "2"]).start()
# pp6611 = Process(target=read_zyxel_ping_rxtx, args=(False,"411","31.173.177.246","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False))
# pp6611.start()
# pp6611.join()

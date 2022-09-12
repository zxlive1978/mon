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
import zyxel_wan_all_luch

import pozmodem
import pozmodemsignal
import badanalogcam
import ubisignal_ap
#import megamultiping



def read_zyxel_ping_rxtx (poz_type, name_well,ip_well,ip_poz,ip_obrab,name_base,ippoz_modem,ip_signal,ip_dvr, ip_cam1, ip_cam2, ip_cam3, ip_cam4, ip_ub1, ip_ub2, ip_sbor, analogdvr, ubi_ver, ip_gbox):
	#Speed Время измерения
	c=5
	average,ml,rx,tx,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor, ub1amc, ub1amq, ub1signal, ub2amc, ub2amq, ub2signal,mlrx,mltx,obrab,gbox=-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-100.0,-1.0,-1.0,-100.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0
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
			# tx,rx=zyxel.speed_zyxel(ip_poz,"5188",int(c))95.182.120.47 95.182.120.47
		
		# if (name_well=='110'):
		# 	tx,rx = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "95.182.120.47")
		# else:
		# 	tx,rx = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "213.80.235.178")

		#GBOX 2 IP TUMEN
		rx,tx = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "178.72.74.118")
		rx2,tx2 = zyxel_wan_all.speed_zyxel(ip_poz,"5188",int(c), "217.151.129.61")
		tx = tx + tx2
		rx = rx + rx2

		mlrx,mltx=zyxel_sngs_port2206.speed_zyxel(ip_poz,"5188",int(c), "213.80.235.178")
        # if (luch):
        #     luchtx,luchrx = zyxel_wan_all_luch.speed_zyxel(ip_poz,"5188",int(c))
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
	#Obrab
	obrab=verbose_ping(ip_obrab)
	print "ping Obrab\n"
	#Gbox
	gbox=verbose_ping(ip_gbox)
	print "ping gbox\n"

	
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
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml, mrx, mtx, sigpoz, dvr, cam1, cam2, cam3, cam4, ub1, ub2, sbor, ub1amc, ub1amq, ub1sig, ub2amc, ub2amq, ub2sig, mlrx, mltx, luchrx, luchtx) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+","+str(mrx)+","+str(mtx)+","+str(signal)+","+str(dvr)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(ub1)+","+str(ub2)+","+str(sbor)+","+str(ub1amc)+","+str(ub1amq)+","+str(ub1signal)+","+str(ub2amc)+","+str(ub2amq)+","+str(ub2signal)+","+str(mlrx)+","+str(mltx)+","+str(obrab)+","+str(gbox)+")"
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

#31.173.139.34
r = pyping.ping('31.173.139.34')
if (r.ret_code==0):
		average62220=r.avg_rtt
#average62220 = megamultiping.ping ('62.220.55.149')

#80.247.113.226 Техноком 31.173.139.34
r = pyping.ping('31.173.139.33')
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
                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Версия_прошики_Ubi   Luch


# #789 533
# # read_zyxel_ping_rxtx(False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"789","31.173.139.241","192.168.147.129","192.168.147.131","p3729899","192.168.19.49","192.168.19.49","192.168.147.135","192.168.147.136","192.168.147.137","192.168.147.138","192.168.147.139","192.168.147.141","192.168.147.140","192.168.147.130", False, "2", "192.168.147.142"]).start()
# # 

# #542 934
# # read_zyxel_ping_rxtx(False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"631","37.29.8.91","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False, "1", "192.168.146.238"]).start()
# # pp915 = Process(target=read_zyxel_ping_rxtx, args=(False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226", False))
# # pp915.start()
# # pp915.join()

# # 534 37.29.103.85 9917 628 83.149.18.62 
# # read_zyxel_ping_rxtx(False,"224","83.149.18.62","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"224","37.29.8.13","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False, "2", "192.168.146.206"]).start()
# # pp628 = Process(target=read_zyxel_ping_rxtx, args=(False,"224","83.149.18.62","192.168.146.193","192.168.146.195","p31173187210","192.168.19.193","192.168.19.193","192.168.146.199","192.168.146.200","192.168.146.201","192.168.146.202","192.168.146.203","192.168.146.204","192.168.146.205","192.168.146.194", False))
# # pp628.start()
# # pp628.join()

# #211Д 1РФ 71 31.173.177.246 6611
# # read_zyxel_ping_rxtx(False,"211","192.168.146.33","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"211","37.29.8.21","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False, "2", "192.168.146.46"]).start()
# # pp6611 = Process(target=read_zyxel_ping_rxtx, args=(False,"411","31.173.177.246","192.168.146.33","192.168.146.35",     "p3729814", "192.168.19.209","192.168.19.209","192.168.146.39","192.168.146.40",  "192.168.146.41",    "192.168.146.42","192.168.146.43","192.168.146.44", "192.168.146.45", "192.168.146.34", False))
# # pp6611.start()
# # pp6611.join()

# #721 540 828
# # read_zyxel_ping_rxtx(True,"916","31.173.139.250","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"604","37.29.98.26","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False, "1", "192.168.146.78"]).start()
# # pp84 = Process(target=read_zyxel_ping_rxtx, args=(True,"916","31.173.139.250","192.168.146.65","192.168.146.67",     "p372978226", "192.168.19.113","192.168.19.113","192.168.146.71","192.168.146.72",  "192.168.146.73",    "192.168.146.74","192.168.146.75","192.168.146.76", "192.168.146.77", "192.168.146.66", False))
# # pp84.start()
# # pp84.join()

# # 235 609 31.173.139.214
# # read_zyxel_ping_rxtx(True,"110","78.25.78.110","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"235","178.176.50.33","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False, "2", "192.168.146.110"]).start()
# # pp715 = Process(target=read_zyxel_ping_rxtx, args=(True,"110","78.25.78.110","192.168.146.97","192.168.146.99",     "p19216814697", "192.168.19.241","192.168.19.241","192.168.146.103","192.168.146.104",  "192.168.146.105",    "192.168.146.106","192.168.146.107","192.168.146.108", "192.168.146.109", "192.168.146.98", False))
# # pp715.start()
# # pp715.join()
#                                                  #                            т             poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Версия_прошики_Ubi   Luch

# #201 938 73
# # read_zyxel_ping_rxtx(True,"73","192.168.146.161","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"73","37.29.78.251","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False, "1", "192.168.146.177"]).start()
# # pp73 = Process(target=read_zyxel_ping_rxtx, args=(True,"73","31.173.139.222","192.168.146.161","192.168.146.163",  "p31173139222", "192.168.19.129","192.168.19.129","192.168.146.167","192.168.146.168",  "192.168.146.169", "192.168.146.170","192.168.146.171","192.168.146.172", "192.168.146.173", "192.168.146.162", False))
# # pp73.start()
# # pp73.join()

# #629 632
# # read_zyxel_ping_rxtx(False,"631","37.29.8.14","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.24","192.168.146.24",  "192.168.146.24", "192.168.146.24","192.168.146.24","192.168.146.24", "192.168.146.24", "192.168.146.19", True)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"631","31.173.139.245","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.20","192.168.146.26",  "192.168.146.27", "192.168.146.28","192.168.146.29","192.168.146.24", "192.168.146.25", "192.168.146.19", False, "2", "192.168.146.30"]).start()
# # pp629 = Process(target=read_zyxel_ping_rxtx, args=(False,"631","37.29.8.14","192.168.146.17","192.168.146.18",  "p31173139214", "192.168.19.177","192.168.19.177","192.168.146.24","192.168.146.24",  "192.168.146.24", "192.168.146.24","192.168.146.24","192.168.146.24", "192.168.146.24", "192.168.146.19", True))
# # pp629.start()
# # pp629.join()

# #701 107 99
# # read_zyxel_ping_rxtx(False,"110","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"110","31.173.139.243","192.168.147.65","192.168.147.67",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.147.71","192.168.147.72",  "192.168.147.73", "192.168.147.74","192.168.147.75","192.168.147.76", "192.168.147.77", "192.168.147.66", False, "2", "192.168.147.78"]).start()
# # pp96 = Process(target=read_zyxel_ping_rxtx, args=(False,"110","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# # pp96.start()
# # pp96.join()

# #101 222 106 31.173.187.207
# # read_zyxel_ping_rxtx(False,"83","192.168.19.145","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"83","31.173.187.207","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.136",  "192.168.146.137", "192.168.146.138","192.168.146.139","192.168.146.140", "192.168.146.141", "192.168.146.130", False, "2", "192.168.146.142"]).start()
# # pp83 = Process(target=read_zyxel_ping_rxtx, args=(False,"110","37.29.103.214","192.168.146.49","192.168.146.51",  "p192168146161", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# # pp83.start()
# # pp83.join()


# 												#zux/poz,?
#                                                  #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Версия_прошики_Ubi  Luch


# #449 406
# # read_zyxel_ping_rxtx(False,"83","192.168.19.145","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"401","37.29.98.103","192.168.146.1","192.168.146.3",  "p1921681461", "192.168.19.225","192.168.19.225","192.168.146.7","192.168.146.8",    "192.168.146.9", "192.168.146.10", "192.168.146.11", "192.168.146.12", "192.168.146.13", "192.168.146.2", False, "2", "192.168.146.14"]).start()
# # pp83 = Process(target=read_zyxel_ping_rxtx, args=(False,"401","37.29.103.214","192.168.146.49","192.168.146.51",  "p1921681461", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# # pp83.start()
# # pp83.join()

# #325 260
# # read_zyxel_ping_rxtx(False,"83","192.168.19.145","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True)
# threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"610","31.173.187.233","192.168.147.1","192.168.147.3",  "p1921681471", "192.168.19.225","192.168.19.225","192.168.147.7","192.168.147.8",    "192.168.147.9", "192.168.147.10", "192.168.147.11", "192.168.147.12", "192.168.147.13", "192.168.147.2", False, "2", "192.168.147.30"]).start()
# # pp83 = Process(target=read_zyxel_ping_rxtx, args=(False,"401","37.29.103.214","192.168.146.49","192.168.146.51",  "p1921681461", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# # pp83.start()
# # pp83.join()

# #627
# # read_zyxel_ping_rxtx(False,"83","192.168.19.145","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True)
# # threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"627","37.29.14.185","192.168.147.33","192.168.147.35",  "p19216814733", "192.168.19.225","192.168.19.225","192.168.147.39","192.168.147.40",    "192.168.147.41", "192.168.147.42", "192.168.147.43", "192.168.147.44", "192.168.147.45", "192.168.147.34", False, "2", False]).start()
# # pp83 = Process(target=read_zyxel_ping_rxtx, args=(False,"401","37.29.103.214","192.168.146.49","192.168.146.51",  "p1921681461", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# # pp83.start()
# # pp83.join()


# 												#zux/poz,?
#                                                  #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor     AnalogDVR    Версия_прошики_Ubi   Luch

#16 Гривенская
# read_zyxel_ping_rxtx(False,"83","192.168.19.145","192.168.146.129","192.168.146.131",  "p192168146129", "192.168.19.145","192.168.19.145","192.168.146.135","192.168.146.135",  "192.168.146.135", "192.168.146.135","192.168.146.135","192.168.146.135", "192.168.146.135", "192.168.146.130", True)
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"16","192.168.0.250","192.168.0.250","192.168.0.2",        "p19216801", "192.168.19.161","192.168.19.161","192.168.0.64","192.168.0.69",    "192.168.0.66", "192.168.0.67", "192.168.0.68", "192.168.0.21", "192.168.0.22", "192.168.0.1", False, "3", "192.168.0.50"]).start()
# pp83 = Process(target=read_zyxel_ping_rxtx, args=(False,"401","37.29.103.214","192.168.146.49","192.168.146.51",  "p1921681461", "192.168.19.161","192.168.19.161","192.168.146.53","192.168.146.53",  "192.168.146.53", "192.168.146.53","192.168.146.53","192.168.146.53", "192.168.146.53", "192.168.146.50", True))
# pp83.start()
# pp83.join()

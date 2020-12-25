#!/usr/bin/env python 3
# -*- coding: utf-8
import MySQLdb
import string
import time
import subprocess
import pyping
import sys
import threading
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



def read_zyxel_ping_rxtx (poz_type, name_well,ip_well,ip_poz,ip_obrab,name_base,ippoz_modem,ip_signal,ip_dvr, ip_cam1, ip_cam2, ip_cam3, ip_cam4, ip_ub1, ip_ub2, ip_sbor):
	r = pyping.ping(ip_well, count=1)
	if (r.ret_code!=0):
		r = pyping.ping(ip_well, count=1)
	if (r.ret_code!=0):
		r = pyping.ping(ip_well, count=1)


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

	#Текущее время
	if (r.ret_code==0):
		average=r.avg_rtt
	#dvr
	r1 = pyping.ping(ip_dvr, count=1)
	if (r1.ret_code!=0):
		r1 = pyping.ping(ip_dvr, count=1)
	if (r1.ret_code!=0):
		r1 = pyping.ping(ip_dvr, count=1)		
	if (r1.ret_code==0):
		dvr=r1.avg_rtt
	#cams
	r2 = pyping.ping(ip_cam1, count=1)
	if (r2.ret_code!=0):
		r2 = pyping.ping(ip_cam1, count=1)
	if (r2.ret_code!=0):
		r2 = pyping.ping(ip_cam1, count=1)		
	if (r2.ret_code==0):
		cam1=r2.avg_rtt
	r3 = pyping.ping(ip_cam2, count=1)
	if (r3.ret_code!=0):
		r3 = pyping.ping(ip_cam2, count=1)
	if (r3.ret_code!=0):
		r3 = pyping.ping(ip_cam2, count=1)		
	if (r3.ret_code==0):
		cam2=r3.avg_rtt
	r4 = pyping.ping(ip_cam3, count=1)
	if (r4.ret_code!=0):
		r4 = pyping.ping(ip_cam3, count=1)
	if (r4.ret_code!=0):
		r4 = pyping.ping(ip_cam3, count=1)		
	if (r4.ret_code==0):
		cam3=r4.avg_rtt
	r5 = pyping.ping(ip_cam4, count=1)
	if (r5.ret_code!=0):
		r5 = pyping.ping(ip_cam4, count=1)
	if (r5.ret_code!=0):
		r5 = pyping.ping(ip_cam4, count=1)		
	if (r5.ret_code==0):
		cam4=r5.avg_rtt
	
	#Ubi1_Ap
	r6 = pyping.ping(ip_ub1, count=1)
	if (r6.ret_code!=0):
		r6 = pyping.ping(ip_ub1, count=1)
	if (r6.ret_code!=0):
		r6 = pyping.ping(ip_ub1, count=1)		
	if (r6.ret_code==0):
		ub1=r6.avg_rtt
		
	#Ubi2_Client
	r7 = pyping.ping(ip_ub2, count=1)
	if (r7.ret_code!=0):
		r7 = pyping.ping(ip_ub2, count=1)
	if (r7.ret_code!=0):
		r7 = pyping.ping(ip_ub2, count=1)		
	if (r7.ret_code==0):
		ub2=r7.avg_rtt
		
	#Sbor
	r8 = pyping.ping(ip_sbor, count=1)
	if (r8.ret_code!=0):
		r8 = pyping.ping(ip_sbor, count=1)
	if (r8.ret_code!=0):
		r8 = pyping.ping(ip_sbor, count=1)		
	if (r8.ret_code==0):
		sbor=r8.avg_rtt
	
	timestamp = int(time.time())+60*60*4

	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	cursor = db.cursor()
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml, mrx, mtx, sigpoz, dvr, cam1, cam2, cam3, cam4, ub1, ub2, sbor) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+","+str(mrx)+","+str(mtx)+","+str(signal)+","+str(dvr)+","+str(cam1)+","+str(cam2)+","+str(cam3)+","+str(cam4)+","+str(ub1)+","+str(ub2)+","+str(sbor)+")"
	cursor.execute(sql)
	db.commit()
	db.close()


#Speed Время измерения
c=10
rx,tx,mrx,mtx,signal,dvr,cam1,cam2,cam3,cam4,ub1,ub2, sbor=-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0


                                                 #poz_type,name_well,ip_well,        ip_poz,         ip_obrab,         name_base,    ippoz_modem,     ip_signal,           ip_dvr,            ip_cam1,         ip_cam2,         ip_cam3,          ip_cam4,          ip_ub1,           ip_ub2,           ip_sbor

#915
threading.Thread(target=read_zyxel_ping_rxtx, args=[False,"631","31.173.139.218","192.168.146.225","192.168.146.227","p31173139218","192.168.19.97","192.168.19.97","192.168.146.231","192.168.146.232","192.168.146.233","192.168.146.234","192.168.146.235","192.168.146.236","192.168.146.237","192.168.146.226"]).start()

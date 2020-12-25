#!/usr/bin/env python 3
# -*- coding: utf-8
import MySQLdb
import string
import time
import subprocess
import pyping
import sys
import telnetlib
#Speed test
import tellnet
#import tellnetipsec
#Test Mlcahe
import mlcache
#Speed zyxel
import zyxel




def read_ml_ping_rxtx (name_well,ip_well,ip_poz,ip_obrab,name_base):
	# echooff=' > /dev/null 2>&1'
	# err = '/usr/local/bin/telegram-send "SUCK 916"'+echooff


	r = pyping.ping(ip_well, count=1)
	if (r.ret_code!=0):
		r = pyping.ping(ip_well, count=1)
	if (r.ret_code!=0):
		r = pyping.ping(ip_well, count=1)


	#Mlcache
	out1=mlcache.mlcacheOn(ip_obrab)
	if (len(out1)==1 || len(out1)==2):
		ml=2
	else:
		ml=-1


	if (len(out1)==5):
		ml=1.8


	if (r.ret_code==0):
		average=r.avg_rtt
		#Speed pozitron
		#if (name_well=='104'):
		#	rx,tx= tellnet104.speed(ip_poz,"5188",int(c))
		#else:
		#rx,tx= tellnet.speed(ip_poz,"5188",int(c))
		#rx,tx= tellnetipsec.speed(ip_poz,"5188",int(c))
		
	else:
		average=-100
		rx,tx=-1,-1
		#		ml=-1
		#subprocess.Popen(err, shell = True)
	rx,tx= tellnet.speed(ip_poz,"5188",int(c))
	#Текущее время
	timestamp = int(time.time())+60*60*4

	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	cursor = db.cursor()
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+")"
	cursor.execute(sql)
	db.commit()

def read_zyxel_ping_rxtx (name_well,ip_well,ip_poz,ip_obrab,name_base):
	# echooff=' > /dev/null 2>&1'
	# err = '/usr/local/bin/telegram-send "SUCK 916"'+echooff


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
	
		#average=r.avg_rtt
		#Speed zyxel
	tx,rx=zyxel.speed_zyxel(ip_poz,"5188",10)
		#rx,tx= tellnet.speed(ip_poz,"5188",int(c))
		
	
#		ml=-1
		#subprocess.Popen(err, shell = True)
	# #Speed zyxel
	# tx,rx=zyxel.speed_zyxel(ip_poz,"5188",int(c))
	# ml = -1
	#Текущее время
	if (r.ret_code==0):
		average=r.avg_rtt
	
	timestamp = int(time.time())+60*60*4

	db_name=name_base
	db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
	cursor = db.cursor()
	sql = "INSERT INTO "+db_name+"(date, value, rx, tx, ml) VALUE ("+str(timestamp)+","+str(average)+","+str(rx)+","+str(tx)+","+str(ml)+")"
	cursor.execute(sql)
	db.commit()
	

#Speed Время измерения
c=5
rx,tx=-1,-1

#8888
r8888 = pyping.ping('8.8.8.8')
if (r8888.ret_code==0):
	average8888=r8888.avg_rtt	
else:
	average8888=-100

#62.220.55.149
r62220 = pyping.ping('62.220.55.149')
if (r62220.ret_code==0):
	average62220=r62220.avg_rtt	
else:
	average62220=-100

#80.247.113.226
r8084 = pyping.ping('80.247.113.226')
if (r8084.ret_code==0):
	average8084=r8084.avg_rtt	
else:
	average8084=-100

#192.168.77.3
r773 = pyping.ping('192.168.77.3')
if (r773.ret_code==0):
	average773=r773.avg_rtt	
else:
	average773=-100
	
#31.173.187.210
r3117 = pyping.ping('31.173.187.210')
if (r3117.ret_code==0):
	average3117=r3117.avg_rtt	
else:
	average3117=-100

#Текущее время
timestamp = int(time.time())+60*60*4

db_name='pconnect'
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql = "INSERT INTO "+db_name+"(date, p8888, p6222055149, p8084114180, p192168773, p31173187210) VALUE ("+str(timestamp)+","+str(average8888)+","+str(average62220)+","+str(average8084)+","+str(average773)+","+str(average3117)+")"
cursor.execute(sql)
db.commit()

if (r8888.ret_code!=0):
	sys.exit()


#84
#read_ml_ping_rxtx("916",'31.173.139.250',"192.168.146.65","192.168.146.67",'p372978226')

#629
#read_zyxel_ping_rxtx("4450",'37.29.8.14',"192.168.146.17","192.168.146.18",'p31173139214')

#928
#read_zyxel_ping_rxtx("631",'31.173.139.214',"192.168.146.97","192.168.146.99",'p31173139218')

#915
#read_zyxel_ping_rxtx("631",'31.173.139.218',"192.168.146.225","192.168.146.227",'p31173139218')

#715
#read_ml_ping_rxtx("110",'78.25.78.110',"192.168.146.97","192.168.146.99",'p19216814697')

#73
#read_ml_ping_rxtx("73",'31.173.139.222',"192.168.146.161","192.168.146.163",'p31173139222')

#628 PIT_GO2
#read_ml_ping_rxtx("224",'37.29.103.66',"192.168.146.65","192.168.146.67",'p31173187210')
#read_zyxel_ping_rxtx("224",'83.149.18.62',"192.168.146.193","192.168.146.195",'p31173187210')

#104
read_ml_ping_rxtx("104",'37.29.98.110',"192.168.146.1","192.168.146.3",'p31173139194')

#630
#read_ml_ping_rxtx("411",'192.168.146.25',"192.168.146.193","192.168.146.195",'p3729814')

#89 zyxel 192.168.146.49
#read_ml_ping_rxtx("89",'31.173.139.190',"192.168.146.161","192.168.146.163",'p192168146161')
#read_zyxel_ping_rxtx("89",'37.29.103.214',"192.168.146.49","192.168.146.51",'p192168146161')

#6611 zyxel 192.168.146.33
#read_ml_ping_rxtx("89",'31.173.139.190',"192.168.146.161","192.168.146.163",'p192168146161')
#read_zyxel_ping_rxtx("411",'31.173.177.246',"192.168.146.33","192.168.146.35",'p3729814')

db.close()




#Видео 4450
#subprocess.check_call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=1&subtype=0" -y /home/www/poz/4450_1.jpg', shell=True, timeout=360)   # try to get a screenshot if RTSP stream is OK
'''
while True:
    try:
        subprocess.check_call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=1&subtype=0" -y /home/www/poz/4450_1.jpg', shell=True, timeout=360)   # try to get a screenshot if RTSP stream is OK
    except: 
        break
		
while True:
    try:
        check_call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel2=&subtype=0" -y /home/www/poz/4450_2.jpg', shell=True, timeout=360)   # try to get a screenshot if RTSP stream is OK
    except: 
        break
		
while True:
    try:
        check_call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=3&subtype=0" -y /home/www/poz/4450_3.jpg', shell=True, timeout=360)   # try to get a screenshot if RTSP stream is OK
    except:
        break
		
while True:
    try:
        check_call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=4&subtype=0" -y /home/www/poz/4450_4.jpg', shell=True, timeout=360)   # try to get a screenshot if RTSP stream is OK
    except:
        break
		
'''
'''
#Видео 4450
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=1&subtype=0" -y /home/www/poz/4450_1.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=2&subtype=0" -y /home/www/poz/4450_2.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=3&subtype=0" -y /home/www/poz/4450_3.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.39:554/cam/realmonitor?channel=4&subtype=0" -y /home/www/poz/4450_4.jpg', shell=True)
#Видео 631
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.24:554/cam/realmonitor?channel=1&subtype=0" -y /home/www/poz/631_1.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.24:554/cam/realmonitor?channel=2&subtype=0" -y /home/www/poz/631_2.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.24:554/cam/realmonitor?channel=3&subtype=0" -y /home/www/poz/631_3.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.24:554/cam/realmonitor?channel=4&subtype=0" -y /home/www/poz/631_4.jpg', shell=True)
#Видео 916
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.8:554/Streaming/Channels/101" -y /home/www/poz/916_1.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.9:554/Streaming/Channels/101" -y /home/www/poz/916_2.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.10:554/Streaming/Channels/101" -y /home/www/poz/916_3.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.11:554/Streaming/Channels/101" -y /home/www/poz/916_4.jpg', shell=True)
#Видео 110
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=1&subtype=0" -y /home/www/poz/110_1.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=2&subtype=0" -y /home/www/poz/110_2.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=3&subtype=0" -y /home/www/poz/110_3.jpg', shell=True)
subprocess.call('/usr/bin/ffmpeg -rtsp_transport tcp -i "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=4&subtype=0" -y /home/www/poz/110_4.jpg', shell=True)
'''

#p31173139214
#31.173.139.218
#31.173.139.222
'''
f=open('/home/www/'+db_name,'r')
text=f.readlines()
if (len(text)>=10):
	last=text[10]
	dig=last.split("/")
	if (len(dig)>=4):
		average=float(dig[4])
	else:	
		average=-100
		
		subprocess.Popen(err, shell = True)
else:
	average=-100
	
	subprocess.Popen(err, shell = True)
'''
	

#print len(dig)
#Если пинга нет 0



# распаковка строки, в которой поля записаны с разделителем ";"

'''def unpack_line(line):
    line = string.replace(line, "'", "")
    els = string.split(line, ";")
    # выделяем имя, емейл, адрес и телефон
    fname = els[0]
    fmail = els[1]
    fadres = els[2]
    ftel = els[3]
    return fname, fmail, fadres, ftel


#Работает
# подключаемся к базе данных (не забываем указать кодировку, а то в базу запишутся иероглифы)
db = MySQLdb.connect(host="localhost", user="root", passwd="goodgood", db="pozitron", charset='utf8')
# формируем курсор, с помощью которого можно исполнять SQL-запросы
cursor = db.cursor()

#state =true;
sql = "INSERT INTO "+db_name+"(date, name,value) VALUE ("+str(timestamp)+",'916(37.29.78.226)',"+str(average)+")"
cursor.execute(sql)
db.commit()
# закрываем соединение с базой данных
db.close()
'''
'''
# открываем исходный csv-файл
f = open("log", "r")
# представляем его в виде массива строк
lines = f.readlines()

for line in lines:
    # если в строе присутствует емейл (определяем по наличию "@")
    if string.find(line, "@") > -1:
        # извлекаем данные из строки
        fname, fmail, fadres, ftel = unpack_line(line)
        # подставляем эти данные в SQL-запрос
        sql = """INSERT INTO contacts(name, mail, adres, tel)
        VALUES ('%(name)s', '%(mail)s', '%(adres)s', '%(tel)s')
        """%{"name":fname, "mail":fmail, "adres":fadres, "tel":ftel}
        # исполняем SQL-запрос
        cursor.execute(sql)
        # применяем изменения к базе данных
        db.commit()
'''

# закрываем файл
#f.close()

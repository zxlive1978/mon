#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MySQLdb
import string
import time
import sys

import gmail_post


#Текущее время
timestamp = int(time.time())+60*60*4
#630
db_name="a3729814"
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql="SELECT data, cam FROM "+str(db_name)+" WHERE data > " + str(timestamp-2*60)
cursor.execute(sql)

results1 = cursor.fetchall()
db.commit()
# print results1

db_name="p3729814"
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql="SELECT date, value, rx, tx, ml FROM "+str(db_name)+" WHERE date > " + str(timestamp-6*60)+ " AND value > 75"+ " AND ml > 1.8"+ " AND tx < 0.25"
cursor.execute(sql)
results2 = cursor.fetchall()
db.commit()
cam=1
if len(results2) > 2:
	cam=0
	try:
		if results1[len(results1-1)][1] != 0:
			gmail_post.post("630 отвалились камеры")
	except:
		a=0

else:
	try:
		if results1[len(results1-1)][1] == 0:
				gmail_post.post("630 включились камеры")
	except:
		a=0		
		# else:
	# if result1[1][0] == 0:
		# gmail_post.post("630 включились камеры")

db_name="a3729814"
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="goodman1978", db="pozitron", charset='utf8')
cursor = db.cursor()
sql = "INSERT INTO "+db_name+"(data, cam) VALUE ("+str(timestamp)+","+str(cam)+")"
cursor.execute(sql)
db.commit()
	



db.close()

# print results2
# print results1[0][1]
# def post(message):
	# msg = MIMEMultipart()
	# msg['From'] = 'zxlive@yandex.ru'
	# msg['To'] = 'djarastafarabg@gmail.com'
	# msg['Subject'] = 'Monitoring'
	# #message = 'here is the email'
	# msg.attach(MIMEText(message))

	# mailserver = smtplib.SMTP('smtp.gmail.com',587)
	# mailserver.ehlo()
	# mailserver.starttls()
	# mailserver.ehlo()
	# mailserver.login('djarastafarabg@gmail.com', 'whitelight@1')
	# mailserver.sendmail('zxlive@yandex.ru','djarastafarabg@gmail.com',msg.as_string())
	# mailserver.quit()

#post("trouble")


	
#Read more: http://plutonit.ru/view_post.php?id=704#ixzz51tiYknsb

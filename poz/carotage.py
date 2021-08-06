#!/usr/bin/env python3
# coding: utf-8

import time
import os
import sys
from pathlib import Path
from multiprocessing import Process
import shutil
import subprocess
from time import mktime
from datetime import date
from datetime import datetime
import fnmatch
import carot_file_to_db

def start_ws(share,shablon1,shablon2,dirr,skv):
	'''
	dt_now =datetime.utcfromtimestamp(time.time()-86400) # date.today()
	#print(datetime.utcfromtimestamp(dt_now))
	month_now = str(dt_now)[5:7]
	day_now = str(dt_now)[8:10]
	dt_now =datetime.utcfromtimestamp(time.time()) # date.today()
	#print(datetime.utcfromtimestamp(dt_now))
	# month_now1 = str(dt_now)[5:7]
	# day_now1 = str(dt_now)[8:10]
	# print (month_now,' ',day_now)
	'''
	'''
	try:
	
		# output = subprocess.check_output(['программа', 'аргумент 1', '2'])
		#output = subprocess.check_output("ls -R "+share, stderr=subprocess.STDOUT, shell=True)#.check_output(['ls', "-R", "/mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/","/dev/null"])
		# -iname без регистра
		output = subprocess.check_output("/usr/bin/find " +share +" -print", stderr=subprocess.STDOUT, shell=True)
		for a in output.split("\n"):
			b=a.decode('utf-8').upper()
			

			# LAS
			# if (a.find(shablon2)>0 and (a.find(month_now)>0) and (a.find(day_now)>0)):
			if (a.find(shablon2)>0 ):
				print(b)
				# subprocess.call('cp "'+a+'" "'+dirr+'"', shell=True)
				statbuf = os.stat(a)
				if ((statbuf.st_mtime>(time.time()-259200))): # 3 суток
					carot=''
					if (b.find('PTS')>0):
						carot='PTS'
					if (b.find('BK')>0):
						carot='BK'
					if (b.find('LM')>0):
						carot='LM'
					if (b.find('PROF')>0):
						carot='PROF'
					if (b.find('RK')>0):
						carot='RK'
					
					if (carot!=''):
						names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' '+skv+''+'.'+carot
						#Копирование файла
						subprocess.call('/bin/cp '+'"'+a+'"'+' "'+names+'"', shell=True)
						

			# ИНКЛИНОМЕРИЯ
			if (b.find('.TXT')>0  and (b.find(u'ИНК')>0 or  (b.find('INC')>0))):
			
			# if (b.find('.TXT')>0):
				print(b)
				statbuf = os.stat(a)
				# if ((statbuf.st_mtime>(time.time()-259200))): # 3 суток
				# names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' '+skv+''+'.INC'	
				# subprocess.call('/bin/cp '+'"'+a+'"'+' "'+names+'"', shell=True)

				if ((statbuf.st_mtime>(time.time()-259200))): # 3 суток
					carot=''
					if (b.find(u'ИНК')>0):
						carot='INC'
					if (b.find('INC')>0):
						carot='INC'
					
					if (carot!=''):
						names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' '+skv+''+'.'+carot
						
						subprocess.call('/bin/cp '+'"'+a+'"'+' "'+names+'"', shell=True)

			# if ((b.find('.DOC')>0 or b.find('.XLS')>0) and (b.find(u'ИНК')>0 or  (b.find('INC')>0))):
			# 	print(b)
			# 	statbuf = os.stat(a)
			# 	if ((statbuf.st_mtime>(time.time()-259200))): # 3 суток
			# 		carot=''
			# 		if (b.find(u'ИНК')>0):
			# 			carot='INC'
			# 		if (b.find('INC')>0):
			# 			carot='INC'


					
			# 		if (carot!=''):
			# 			htmlname=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' '+skv+''+'.html'
			# 			names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' '+skv+''+'.'+carot
						
			# 			subprocess.call('/bin/cp '+'"'+a+'"'+' "'+names+'"', shell=True)
			# 			subprocess.call('/usr/bin/unoconv -f html  '+'"'+names+'"', shell=True)
			# 			subprocess.call('/bin/rm '+'"'+names+'"', shell=True)
			
	'''
	output = subprocess.check_output("/usr/bin/find " +dirr +" -print", stderr=subprocess.STDOUT, shell=True)
	for a in output.split("\n"):
		print (a)
	'''
		exit
	except:
		# print ("неудача")
		exit
	'''
		


# 828 /АРХИВ/Архив скв.828/ pts. lm.las
t202 = Process(target=start_ws, args=['"/mnt/3oc//АРХИВ/Архив скв.828/"',"СКВ 828 Пл АГКМ сводка за", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-828'])
t202.start()




#542 Обработчик c: /mnt/915oc/Users/user/Desktop/ГИС 542/Мониторинг/ bk.LAS Prof.LAS rk.LAS
t204 = Process(target=start_ws, args=['"/mnt/915oc/Users/user/Desktop/Мониторинг/"',"СКВ 542 Пл АГКМ Сводка", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-542'])
t204.start()

# ------------------------------------------------------------------------
# 938
t203 = Process(target=start_ws, args=['"/mnt/20oc/Users/user/Desktop/Сводки 938/2020-2021/"',"СКВ 938 Пл АГКМ Сводка за", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-938'])
t203.start()


# ------------------------------------------------------------------------
# 632
t205 = Process(target=start_ws, args=['"/mnt/629oc/Users/User/Desktop/Мониторинг/"',"СКВ 632 АГКМ сводка ", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-632'])
t205.start()

# 1------------------------------------------------------------------------
# 107
# t206 = Process(target=read_well, args=['"/mnt/96oc/Users/User/Desktop/Суточные сводки №107 скв/"',"СКВ 107 Пл АГКМ Сводка за ", ".xlsx","/var/www/html/mon/poz/svodka",'АГКМ-107'])
# t206.start()

# ------------------------------------------------------------------------
# 222 /mnt/83oc/Users/User/Desktop
t207 = Process(target=start_ws, args=['"/mnt/83oc/Users/User/Desktop/"',"Скв 222 Пл АГКМ Сводка за ", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-222'])
t207.start()

# ------------------------------------------------------------------------
# 1РФ /mnt/83oc/Users/User/Desktop
t208 = Process(target=start_ws, args=['"/mnt/4450oc/d/Скважина 1-РФ/Материал в контору/"',"Скв №1-РФ Пл АГКМ Сводка за ", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-1РФ'])
t208.start()



# \c$\Users\user\Desktop\Мониторинг
# \d$\СНГС №14\АРХИВЫ СКВАЖИН\Архив скв.№449\Материал в КИП
# 449
t201 = Process(target=start_ws, args=['"/mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/Материал в КИП/"',"СКВ 449 Пл АГКМ Сводка за", ".LAS","/var/www/html/mon/poz/carotage",'АГКМ-449'])
t201.start()


t201.join(1000)
t202.join(1000)
t204.join(1000)
t203.join(1000)
t205.join(1000)
# t206.join(1000)
t207.join(1000)
t208.join(1000)



if t201.is_alive(): t201.terminate()
if t202.is_alive(): t202.terminate()


if t204.is_alive(): t204.terminate()


if t203.is_alive(): t203.terminate()


if t205.is_alive(): t205.terminate()


# if t206.is_alive(): t206.terminate()


if t207.is_alive(): t207.terminate()

if t208.is_alive(): t208.terminate()

# if t201.is_alive(): t201.terminate()


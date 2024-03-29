#!/usr/bin/env python
# coding: utf-8

from os.path import join, getsize
import os
import fnmatch
from struct import *
import math
import MySQLdb
import threading
import subprocess
import time
from multiprocessing import Process


def read_well(sbor,table,share_path):
	#print os.listdir(sbor)
	try:
		path, dirs, files = os.walk(sbor).next()
		file_count = len(files)
				 
		if file_count>0:
			print ("Good ",sbor)
		else:
			print ("Bad ",sbor)
			unmnt_str = 'umount -l ' + sbor
			subprocess.call(unmnt_str, shell=True)
			time.sleep(5)
			#Попытаемся смонтировать
			mnt_str = '/bin/mount -t cifs -o username=root,password=root,vers=2.1 "'+share_path + '" ' + sbor 
			subprocess.call(mnt_str, shell=True)
			time.sleep(5)
	except:
		test=0
		#Отмонтируем
		print ("Bad ",sbor)
		
		unmnt_str = 'umount -l ' + sbor
		subprocess.call(unmnt_str, shell=True)
		time.sleep(5)
		#Попытаемся смонтировать
		mnt_str = '/bin/mount -t cifs -o username=root,password=root "'+share_path + '" ' + sbor 
		subprocess.call(mnt_str, shell=True)
		time.sleep(5)
		
	
	
#Потоки Времянка
#449 406
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t110 = Process(target=read_well, args=["/mnt/104","s401","//192.168.146.2/d/PetroServices/Database/Online/Store"])
t110.start()
t110.join(30)
if t110.is_alive(): t110.terminate()

#533 Сборщик
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t544 = Process(target=read_well, args=["/mnt/544","s544","//192.168.147.130/d/PetroServices/Database/Online/Store"])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()

#533 Обработчик
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t544 = Process(target=read_well, args=["/mnt/544o","s544o","/""/192.168.147.131/c$/Program Files/Common Files/PS Shared/Database/"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()

#533 Обработчик c:
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t544 = Process(target=read_well, args=["/mnt/544oc","s544o","/""/192.168.147.131/c$"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()



#707 1РФ Сборщик
#threading.Thread(target=read_well, args=["/mnt/4450","s4450","//192.168.146.34/d/PetroServices/Database/Online/Store"]).start()
t4450 = Process(target=read_well, args=["/mnt/4450","s4450","//192.168.146.34/d/PetroServices/Database/Online/Store"])
t4450.start()
t4450.join(30)
if t4450.is_alive(): t4450.terminate()
#read_well("/mnt/4450","s4450")


#1РФ Обработчик c
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t544 = Process(target=read_well, args=["/mnt/4450o","s4450o","/""/192.168.146.35/c/Program Files/Common Files/PS Shared/Database/"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()

#1РФ Обработчик d
#threading.Thread(target=read_well, args=["/mnt/104","s110","//192.168.146.2/d/PetroServices/Database/Online/Store"]).start()
t544 = Process(target=read_well, args=["/mnt/4450oc","s4450oc","/""/192.168.146.35/d"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()


#325 610 Сборщик
t610 = Process(target=read_well, args=["/mnt/610","s610","//192.168.147.2/d/PetroServices/Database/Online/Store"])
t610.start()
t610.join(30)
if t610.is_alive(): t610.terminate()

#325 610 Обработчик
t629 = Process(target=read_well, args=["/mnt/610o","610o","/""/192.168.147.3/c$/Program Files/Common Files/PS Shared/Database/"""])
t629.start()
t629.join(30)
if t629.is_alive(): t629.terminate()

#325 610 Обработчик c
t6291 = Process(target=read_well, args=["/mnt/610oc","610oc","/""/192.168.147.3/c$"""])
t6291.start()
t6291.join(30)
if t6291.is_alive(): t6291.terminate()




#9917
#threading.Thread(target=read_well, args=["/mnt/630","s630","//192.168.146.194/d/PetroServices/Database/Online/Store"]).start()
t630 = Process(target=read_well, args=["/mnt/630","s630","//192.168.146.194/d/PetroServices/Database/Online/Store"])
t630.start()
t630.join(30)
if t630.is_alive(): t630.terminate()


#9917 Обработчик
t544 = Process(target=read_well, args=["/mnt/630o","s630o","/""/192.168.146.195/c/Program Files/Common Files/PS Shared/Database/"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()

#9917 Обработчик с:
t544 = Process(target=read_well, args=["/mnt/630oc","s630oc","/""/192.168.146.195/c$"""])
t544.start()
t544.join(30)
if t544.is_alive(): t544.terminate()

#938 Обработчик
# (Logs Builder) t20 = Process(target=read_well, args=["/mnt/20o","k20","/""/192.168.146.163/c/Program Files/Common Files/PS Shared/Database/"""])
t20 = Process(target=read_well, args=["/mnt/20","k20","/""/192.168.146.163/d/-=DATA=-/STORE/"""])
t20.start()
t20.join(30)
if t20.is_alive(): t20.terminate()

#938 Обработчик "
# (Logs Builder) t20 = Process(target=read_well, args=["/mnt/20oc","k20","/""/192.168.146.163/c/Program Files/Common Files/PS Shared/Database/"""])
t20 = Process(target=read_well, args=["/mnt/20o","k20o","/""/192.168.146.163/c/Program Files/Common Files/PS Shared/Database/"""])
t20.start()
t20.join(30)
if t20.is_alive(): t20.terminate()

#938 Обработчик c: /Users/user/Desktop/Сводки 938/2020-2021/Май 2021/Сводки директору СКВ 938/ "Сводка директору за 01.05.2021.xlsx"
# (Logs Builder) t20 = Process(target=read_well, args=["/mnt/20oc","k20","/""/192.168.146.163/c/Program Files/Common Files/PS Shared/Database/"""])
t20 = Process(target=read_well, args=["/mnt/20oc","k20","/""/192.168.146.163/c$"""])
t20.start()
t20.join(30)
if t20.is_alive(): t20.terminate()


#632 Сборщик
#threading.Thread(target=read_well, argsщ=["/mnt/631","s629","//192.168.146.19/d/PetroServices/Database/Online/Store"]).start()
t631 = Process(target=read_well, args=["/mnt/631","s629","//192.168.146.19/d/PetroServices/Database/Online/Store"])
t631.start()
t631.join(30)
if t631.is_alive(): t631.terminate()

#632 Обработчик
t629 = Process(target=read_well, args=["/mnt/629o","629o","/""/192.168.146.18/c$/Program Files/Common Files/PS Shared/Database/"""])
t629.start()
t629.join(30)
if t629.is_alive(): t629.terminate()

#632 Обработчик c: c/Users/User/Desktop/Сводки в контору скв. 632/2021/Май/Генералу/ "СКВ №632 09.05.2021.xlsx"
t629 = Process(target=read_well, args=["/mnt/629oc","629oc","/""/192.168.146.18/c$"""])
t629.start()
t629.join(30)
if t629.is_alive(): t629.terminate()


# Комментарии Geoscape
#938 Обработчик
# t20 = Process(target=read_well, args=["/mnt/20o","k20","//192.168.146.163/C/Program Files/GeoSketch/Forms"])
# t20.start()
# t20.join(30)
# if t20.is_alive(): t20.terminate()

# # Саратов комментарии  и геология Обработчик 235
t928 = Process(target=read_well, args=["/mnt/908o","k908","//192.168.146.99/C/Program Files/Common Files/PS Shared/Database/"])
t928.start()
t928.join(30)
if t928.is_alive(): t928.terminate()

#Саратов сводки или глубинка Обработчик 908 Обработчик c: /mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/Сводки скв.№449/Май 21/ "СКВ №449 01.05.2021.xlsx"
t104 = Process(target=read_well, args=["/mnt/908oc","908oc","/""/192.168.146.99/c/"""])
t104.start()
t104.join(30)
if t104.is_alive(): t104.terminate()

#Саратов 235 Сборщик c: /mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/Сводки скв.№449/Май 21/ "СКВ №449 01.05.2021.xlsx"
t1041 = Process(target=read_well, args=["/mnt/908","908","/""/192.168.146.98/d/"""])
t1041.start()
t1041.join(30)
if t1041.is_alive(): t1041.terminate()


#222 83 Обработчик
t547 = Process(target=read_well, args=["/mnt/83","k83","//192.168.146.131/C/Program Files/GeoSketch/Forms"])
t547.start()
t547.join(30)
if t547.is_alive(): t547.terminate()

#222 83 Обработчик с: /Users/User/Desktop/Сводки в контору/2021 скв 222/Май/Сводка директору Скв 222 Пл АГКМ/ "Сводка ГД за 01.05.2021г.xlsx"
t547 = Process(target=read_well, args=["/mnt/83oc","k83","//192.168.146.131/C$"])
t547.start()
t547.join(30)
if t547.is_alive(): t547.terminate()

#828 84
t3 = Process(target=read_well, args=["/mnt/3","3","/""/192.168.146.67/C$/Program Files/GeoSketch/Forms/"""])
t3.start()
t3.join(30)
if t3.is_alive(): t3.terminate()

#828 84 /mnt/3oc/АРХИВ/Архив скв.604/суточные сводки скв.604/ "СКВ 828 Пл АГКМ сводка за 06.05.2021.xlsx"
t3 = Process(target=read_well, args=["/mnt/3oc","3","/""/192.168.146.67/D$"""])
t3.start()
t3.join(30)
if t3.is_alive(): t3.terminate()


#107 99 Обработчик
t96 = Process(target=read_well, args=["/mnt/96","96","/""/192.168.147.67/C$/Program Files/GeoSketch/Forms/"""])
t96.start()
t96.join(30)
if t96.is_alive(): t96.terminate()

#107 99 Обработчик c: /Users/User/Desktop/Суточные сводки №107 скв/май2021/ "Сводка ген.директору_скв107 20.05.21.xlsx"
t96 = Process(target=read_well, args=["/mnt/96oc","96","/""/192.168.147.67/C$"""])
t96.start()
t96.join(30)
if t96.is_alive(): t96.terminate()


#627 Обработчик
t627 = Process(target=read_well, args=["/mnt/627o","627","/""/192.168.147.35/C$/Program Files/GeoSketch/Forms/"""])
t627.start()
t627.join(30)
if t627.is_alive(): t627.terminate()


#449 406  Обработчик
t104 = Process(target=read_well, args=["/mnt/104o","104o","/""/192.168.146.3/c$/Program Files/Common Files/PS Shared/Database/"""])
t104.start()
t104.join(30)
if t104.is_alive(): t104.terminate()

#449 406 Обработчик c: /mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/Сводки скв.№449/Май 21/ "СКВ №449 01.05.2021.xlsx"
t104 = Process(target=read_well, args=["/mnt/104oc","104o","/""/192.168.146.3/d$"""])
t104.start()
t104.join(30)
if t104.is_alive(): t104.terminate()




#438 Саратов
# t731 = Process(target=read_well, args=["/mnt/438","s438","//192.168.148.1/c/MLDIP/Mlsystem2.0/Store"])
# t731.start()
# t731.join(30)
# if t731.is_alive(): t731.terminate()

# #153 Ставрополь
# t153 = Process(target=read_well, args=["/mnt/153","s153","//192.168.152.3/c/MLDIP/Mlsystem2.0/Store"])
# t153.start()
# t153.join(30)
# if t153.is_alive(): t153.terminate()



#2103 НЕ МАГА НУРЖАН 542
#threading.Thread(target=read_well, args=["/mnt/915","s915","//192.168.146.226/d/PetroServices/Database/Online/Store"]).start()
# t631 = Process(target=read_well, args=["/mnt/915","s915","//192.168.146.226/d/PetroServices/Database/Online/Store"])
# t631 = Process(target=read_well, args=["/mnt/915","s915","//192.168.146.226/c/MLDIP/Mlsystem2.0/Store"])
# t631.start()
# t631.join(30)
# if t631.is_alive(): t631.terminate()

#542 Обработчик
# t629 = Process(target=read_well, args=["/mnt/915o","915o","/""/192.168.146.227/c$/Program Files/Common Files/PS Shared/Database/"""])
# t629.start()
# t629.join(30)
# if t629.is_alive(): t629.terminate()

#542 Обработчик c: /Users/user/Desktop/Сводки 542/Май 2021/Сводки директору Скв № 542 09.05.2021.xlsx
# t629 = Process(target=read_well, args=["/mnt/915oc","915o","/""/192.168.146.227/c$"""])
# t629.start()
# t629.join(30)
# if t629.is_alive(): t629.terminate()




#threading.Thread(target=read_well, args=["/mnt/631","s631","//192.168.146.19/d/PetroServices/Database/Online/Store"]).start()
#read_well("/mnt/631","s631")

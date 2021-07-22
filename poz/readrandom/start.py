#!/usr/bin/env python
# coding: utf-8

from os.path import join, getsize
import os
import sys
# import fnmatch
# from struct import *
# import math
# import MySQLdb
# import threading

# import time
# from multiprocessing import Process
# import shutil
# import zipfile
import subprocess
import shlex

from datetime import datetime
# from datetime import timezone

def read_well(nametime, table, start, stop, whathdo):

		# import subprocess
		# program = "notepad.exe"
		#pid = subprocess.Popen([sys.executable, "/path/to/file/no/spaces/in/path/thecommand.py"], stdin=None, stdout=None, stderr=None, close_fds=True) # call subprocess
		# process = subprocess.Popen(/usr/bin/python, "/var/www/html/mon/poz/readrandom/dtcis_read_random.py", nametime, table, start, stop, whathdo], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
		# print ("sukA")
		cmd ='/usr/bin/python '+'/var/www/html/mon/poz/readrandom/dtcis_read_random.py '+nametime+' '+table+' '+start+' '+stop+' '+whathdo
		args = shlex.split(cmd)
		# print (args)
		p = subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
		# sys.exit(0)
		

#Саратов (Обработчик)
# read_well(sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4],  sys.argv[5])
# t4450 = Process(target=read_well, args=[sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4],  sys.argv[5]])
# t4450.start()
# t4450.join(300)
# if t4450.is_alive(): t4450.terminate()




# #542
# #read_well("/mnt/915","s915")
# t915 = Process(target=read_well, args=["/mnt/915","s915depth"])
# t915.start()
# t915.join(300)
# if t915.is_alive(): t915.terminate()

# # #threading.Thread(target=read_well, args=["/mnt/631","s631"]).join(5)
# # #read_well("/mnt/631","s631")

# # #610
# # #read_well("/mnt/104","s110")
# # t610 = Process(target=read_well, args=["/mnt/610","s610"])
# # t610.start()
# # t610.join(30)
# # if t610.is_alive(): t610.terminate()

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

# # 23; 'ДМК' Dmk
# # 22; 'Скорость бурения' Vbur
# # 135; 'Ходов насоса 3' Xn3
# # 48; 'Объем емкости 5' V5
# # 236; 'Объем емкости 6' V6
# # 17; 'С2' C2
# # 18; 'С3' C3
# # 20; 'С4' C4
# # 21; 'С5' C5
# # 176; 'Кальцит' Kalcid
# # 196; 'Доломит' Dolomit
# # 216; 'С1 по шламу' C1sh
# # 217; 'С2 по шламу' C2sh
# # 218; 'С3 по шламу' C3sh
# # 219; 'С4 по шламу' C4sh
# # 220; 'С5 по шламу' C5sh
# # 222; 'Сумма шламу С1...С6' C1C5sh
# # 155; 'Минерализация на вх' Minbx
# # 156; 'Минерализация на вых' Minbix

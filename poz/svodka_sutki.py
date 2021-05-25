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
from datetime import datetime
import fnmatch

def read_well(share,shablon,dirr,skv, lastdir):
	# try:
		
		# subprocess.call('cp -R "'+share+'" "'+dirr+'"', shell=True)
		for root, dirs, files in os.walk(share, topdown=False):
				for name in files:
					if fnmatch.fnmatch(name, shablon):
						statbuf = os.stat(share+name)
						if ((statbuf.st_mtime>(time.time()-86400))):
							names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' АГКМ-'+skv+''+'.xlsx'
							shutil.copy(share+name, names)
							subprocess.call('unoconv -f html -e PageRange=1 '+names, shell=True)

							# subprocess.call('cd "'+dirr+lastdir+'" && ls && mv "' +name+'" "'+name[-15:-5]+skv+'.xlsx"'+' && unoconv -f html -e PageRange=1 "'+name[-15:-5]+skv+'.xlsx"', shell=True)

			# path = sorted(Path(dirr).glob(shablon))
		# filles=list(map(str, path))
		# for fil in filles:
		# 	# statbuf = os.stat(fil)
		# 	# if ((statbuf.st_mtime>(time.time()-86400))):
		# 	print("Modification time: {}".format(statbuf.st_mtime))
		# 		# names=dirr+'/'+str(datetime.fromtimestamp(statbuf.st_mtime))[:16]+' АГКМ-'+skv+''+'.xlsx'
		# 		# shutil.copy(fil, names)
		# 	subprocess.call('unoconv -f html -e PageRange=1 '+fil, shell=True)
			
			
			
			
	# except:
		# print ("неудача")
		exit
		# unoconv -f html -e PageRange=1 542.xlsx
		# wget --quiet https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \
    	# tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && \
    	# cp wkhtmltox/bin/wk* /usr/local/bin/ && \
    	# rm -rf wkhtmltox
		# pdfkit.from_url('http://google.com', 'out.pdf')
		# pdfkit.from_file(host, '542pdf.pdf')
		# pdfkit.from_string('Hello!', 'out.pdf')
	
	# 	print(reset_vpn_host + ": Error!")
# c=5	
# r,t=speed("192.168.146.49","5188",int(c))
# print r,t
# pozreboot(sys.argv[1],"5188", 10,sys.argv[1])

# ------------------------------------------------------------------------
# 938
# t201 = Process(target=read_well, args=["""/mnt/20oc/Users/user/Desktop/Сводки 938/2020-2021/Май 2021/Сводки директору/""","СКВ 938 Сводка директору за *.xlsx","/var/www/html/mon/poz/svodka",'АГКМ-938', '/Сводки директору/'])
# t201.start()
# t201.join(1000)
# if t201.is_alive(): t201.terminate()

# 449
t201 = Process(target=read_well, args=["""/mnt/104oc/СНГС №14/АРХИВЫ СКВАЖИН/Архив скв.№449/Сводки скв.№449/Май 21/""","СКВ №449 *.xlsx","/var/www/html/mon/poz/svodka",'АГКМ-449', '/Май 21/'])
t201.start()
t201.join(1000)
if t201.is_alive(): t201.terminate()
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

def read_well(share,shablon,dirr,skv):
	# try:
		path = sorted(Path(share).glob(shablon))
		filles=list(map(str, path))
		
		for fil in filles:
			statbuf = os.stat(fil)
			if ((statbuf.st_mtime>(time.time()-86400*2))):
				print("Modification time: {}".format(statbuf.st_mtime))
				shutil.copy(fil, dirr+'/'+skv+'_'+str(datetime.fromtimestamp(statbuf.st_mtime))+'.xlsx')
			# print (datetime.utcnow())
			# print (time.time())
			
			# print (fil)
			# subprocess.call('cp "'+fil+ '" '+dirr, shell=True)
			# shutil.copy(fil, dirr)
	# except:
		print ("неудача")
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
t201 = Process(target=read_well, args=["/mnt/20oc/Users/user/Desktop/Сводки 938/2020-2021/Май 2021/Сводки директору/","СКВ 938 Сводка директору за *.xlsx","/var/www/html/mon/poz/svodka","938"])
t201.start()
t201.join(1000)
if t201.is_alive(): t201.terminate()
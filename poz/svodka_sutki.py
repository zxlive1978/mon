#!/usr/bin/env python3

import sys
def pozread_well(share,shablon,dirr):
	try:
		a=0
		#
	except:
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
t201 = Process(target=read_well, args=["/mnt/20oc/Users/user/Desktop/Сводки 938/2020-2021/Май 2021/Сводки директору СКВ 938/","Сводка директору за 01.05.2021.xlsx","svodka"])
t201.start()
t201.join(300)
if t201.is_alive(): t201.terminate()
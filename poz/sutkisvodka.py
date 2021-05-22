#!/usr/bin/env python3

import sys
import pdfkit
def pozreboot(host,port,delay,reset_vpn_host):
	try:
		# unoconv -f html -e PageRange=1 542.xlsx
		pdfkit.from_url('http://google.com', 'out.pdf')
		pdfkit.from_file('test.html', 'out.pdf')
		pdfkit.from_string('Hello!', 'out.pdf')
	except:
		print(reset_vpn_host + ": Error!")
# c=5	
# r,t=speed("192.168.146.49","5188",int(c))
# print r,t
pozreboot(sys.argv[1],"5188", 10,sys.argv[1])
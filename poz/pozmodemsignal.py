#!/usr/bin/env python3

import sys
import telnetlib
def signal(host,port,delay):
	try:
	
		telnet = telnetlib.Telnet()
		telnet.open(host, port, timeout=delay+4)
		telnet.read_until("Router",timeout=delay+4)
		telnet.write("root\n")
		telnet.read_until("Password:",timeout=delay+4)
		telnet.write("superzxmn\n")
		telnet.read_until("~ #",timeout=delay+4)
		telnet.write("cat /tmp/modem.info; sleep "+ str(delay)+";\n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		signal=float(data[6][4:])
		
		telnet.close()
	
	except:
		signal=-1.0

	return signal
# c=5

# s=signal("192.168.19.209","5188",int(c))
# print s

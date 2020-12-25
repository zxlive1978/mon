#!/usr/bin/env python3

import sys
import telnetlib
def speed(host,port,delay):
	try:
	
		telnet = telnetlib.Telnet()
		telnet.open(host, port, timeout=delay+4)
		telnet.read_until("Router",timeout=delay+4)
		telnet.write("root\n")
		telnet.read_until("Password:",timeout=delay+4)
		telnet.write("superzxmn\n")
		telnet.read_until("~ #",timeout=delay+4)
		telnet.write("cat /sys/class/net/modem/statistics/rx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/modem/statistics/rx_bytes\n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		oldrx=float(data[1])
		newrx=float(data[3])
		if (oldrx>newrx):
            #speedrx =(4294967295-(oldrx-newrx))/1024*8/delay
			speedrx =(4294967295-(oldrx-newrx))/8/delay
		else:
			speedrx=(newrx-oldrx)/8/delay
		telnet.close()

		telnet = telnetlib.Telnet()
		telnet.open(host, port, timeout=delay+4)
		telnet.read_until("Router",timeout=delay+4)
		telnet.write("root\n")
		telnet.read_until("Password:",timeout=delay+4)
		telnet.write("superzxmn\n")
		telnet.read_until("~ #",timeout=delay+4)
		telnet.write("cat /sys/class/net/modem/statistics/tx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/modem/statistics/tx_bytes\n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		oldtx=float(data[1])
		newtx=float(data[3])
		if (oldtx>newtx):
			speedtx =(4294967295-(oldtx-newtx))/8/delay
		else:
			speedtx=(newtx-oldtx)/8/delay
		telnet.close()
	#Mbps
	#speedall=(speedrx+speedtx)/1024
	except:
		speedtx=-1024.0
		speedrx=-1024.0

	return str(round(speedrx/1024,4)), str(round(speedtx/1024,4))
# c=5	
# r,t=speed("192.168.146.49","5188",int(c))
# print r,t

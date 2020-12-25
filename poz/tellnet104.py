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
		#telnet.write("cat /sys/class/net/vlan0/statistics/rx_bytes; cat /sys/class/net/eth0/statistics/rx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/vlan0/statistics/rx_bytes; cat /sys/class/net/eth0/statistics/rx_bytes \n ")
		telnet.write("cat /sys/class/net/vlan0/statistics/rx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/vlan0/statistics/rx_bytes; \n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		oldrx=float(data[1])
		newrx=float(data[3])
		#oldrx=float(data[2]) - float(data[1])
		#newrx=float(data[5]) - float(data[4])
		if (oldrx>newrx):
			speedrx =(4294967295-(oldrx-newrx))/1024*8/delay
		else:
			speedrx=(newrx-oldrx)/1024*8/delay
		telnet.close()

		telnet = telnetlib.Telnet()
		telnet.open(host, port, timeout=delay+4)
		telnet.read_until("Router",timeout=delay+4)
		telnet.write("root\n")
		telnet.read_until("Password:",timeout=delay+4)
		telnet.write("superzxmn\n")
		telnet.read_until("~ #",timeout=delay+4)
		#telnet.write("cat /sys/class/net/vlan0/statistics/tx_bytes; cat /sys/class/net/eth0/statistics/tx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/vlan0/statistics/tx_bytes; cat /sys/class/net/eth0/statistics/tx_bytes \n ")
		telnet.write("cat /sys/class/net/vlan0/statistics/tx_bytes; sleep "+ str(delay)+"; cat /sys/class/net/vlan0/statistics/tx_bytes; \n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		oldtx=float(data[1])
		newtx=float(data[3])
		#oldtx=float(data[2]) - float(data[1])
		#newtx=float(data[5]) - float(data[4])
		if (oldtx>newtx):
			speedtx =(4294967295-(oldtx-newtx))/1024*8/delay
		else:
			speedtx=(newtx-oldtx)/1024*8/delay
		telnet.close()
	#Mbps
	#speedall=(speedrx+speedtx)/1024
	except:
		speedtx=0.0
		speedrx=0.0
	
	#print data[1],data[2],data[3],data[4],data[5]

	return str(round(speedrx/1024,2)), str(round(speedtx/1024,2))
#c=5	
#r,t=speed("192.168.146.1","5188",int(c))
#print r,t


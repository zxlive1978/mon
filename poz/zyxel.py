#!/usr/bin/env python3

import sys
import telnetlib

def speed_zyxel(host,port,delay):
	
		
	try:
		i=1
		while i<3:
			telnet = telnetlib.Telnet()
			telnet.open(host, port, timeout=delay)
			telnet.read_until("*",timeout=delay)
			telnet.write("admin\n")
			telnet.read_until("Password:",timeout=delay)
			telnet.write("suck\n")
			telnet.read_until("B",timeout=delay)
			telnet.write("enable\n")
			telnet.read_until("Router#",timeout=delay)
			telnet.write("show interface summary all status\n")
			telnet.read_until("N",timeout=delay)
			telnet.write("exit\n")
			data =telnet.read_all()
			data = data.splitlines()
			wan_str = data[4].split()
			# print wan_str[6]
			# print wan_str[7]
			telnet.close()
			speedtx = float(wan_str[6])
			speedrx = float(wan_str[7])
			i=i+1
	#Mbps
	#speedall=(speedrx+speedtx)/1024
	except:
		speedtx=-1
		speedrx=-1
		return str(speedtx), str(speedrx)

	return str(round(speedtx*8/1024/1024,3)), str(round(speedrx*8/1024/1024,3))
# c = 5	
# r,t=speed("192.168.146.225","5188",int(c))
# print r,t

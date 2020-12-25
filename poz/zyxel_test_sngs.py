#!/usr/bin/env python3

import sys
import telnetlib

def speed_zyxel(host,port,delay, ip_sngs):
	
	rx, tx = 0.0, 0.0	
	try:	
			telnet = telnetlib.Telnet()
			telnet.open(host, port, timeout=delay)
			telnet.read_until("*",timeout=delay)
			telnet.write("admin\n")
			telnet.read_until("Password:",timeout=delay)
			telnet.write("suck\n")
			telnet.read_until("B",timeout=delay)
			telnet.write("enable\n")
			telnet.read_until("Router#",timeout=delay)
			telnet.write("show conn destination "+ip_sngs+" \n")
			telnet.read_until("N",timeout=delay)
			telnet.write("exit\n")
			data =telnet.read_all()
			# print data
			data = data.splitlines()
			 
			numbs=(len(data) -8)
			if numbs>0:
				j=2
				while j<=numbs:
					head = data[j+1].split()
					head = head#.split()
					#print head[1]
					str = data[j+2].split()
					
					if head[1] == "Any_TCP" and str[0].split(':')[1] == "2206":
								r= str[1].split('(')
								rx=rx+float(r[0])
								t= str[2].split('(')
								tx=tx+float(t[0])
								# print j 
						#print numbs
								# print str
					j=j+2
			wan_str = "103.04" 
			# print wan_str[6]
			# print wan_str[7]
			# print round(rx,2),round(tx,2)
			telnet.close()
			#speedtx = float(wan_str[6])
			#speedrx = float(wan_str[7])
			
			return round(rx,2),round(tx,2)
	#Mbps
	#speedall=(speedrx+speedtx)/1024
	except:
			return -1,-1
		# speedtx=-1
		# speedrx=-1
		# return str(speedtx), str(speedrx)

	# return str(round(speedtx*8/1024/1024,3)), str(round(speedrx*8/1024/1024,3))
c = 5	
r,t=speed_zyxel("192.168.146.97","5188",int(c), "213.80.235.178")
print r,t

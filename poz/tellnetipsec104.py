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
		telnet.write("ip -s xfrm state list | grep bytes |grep packets | cut -d'(' -f1; sleep "+ str(delay)+"; ip -s xfrm state list | grep bytes |grep packets | cut -d'(' -f1; \n ")
		telnet.write("exit\n")
		data =telnet.read_all()
		data= data.splitlines()
		data.remove('exit')
		data.remove('~ #  exit')
		data.remove(" ip -s xfrm state list | grep bytes |grep packets | cut -d'(' -f1; sleep 5; i \x08p -s xfrm state list | grep bytes |grep packets | cut -d'(' -f1; ")
		i = 0
		oldrx,oldtx,newrx,newtx=0.0,0.0,0.0,0.0
		while i<len(data)/2:
			if i%2!=0:
				oldrx +=float(data[i])
			else:
				oldtx +=float(data[i])
			i+=1
		i=round((len(data))/2)
		while i<len(data):
			if i%2!=0:
				newrx +=float(data[i])
			else:
				newtx +=float(data[i])
			i+=1
		
		if (oldrx>newrx):
			speedrx =(4294967295-(oldrx-newrx))/1024*8/delay
		else:
			speedrx=(newrx-oldrx)/1024*8/delay
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


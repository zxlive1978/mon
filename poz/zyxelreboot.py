#!/usr/bin/env python3

import sys
import telnetlib
def pozreboot(host,port,delay,reset_vpn_host):
	try:
	
		telnet = telnetlib.Telnet()
		telnet.open(host, port, timeout=delay+4)
		telnet.read_until("Username:",timeout=delay+4)
		telnet.write("admin\n")
		telnet.read_until("Password:",timeout=delay+4)
		telnet.write("suck\n")
		telnet.read_until("Router>",timeout=delay+4)
		telnet.write("reboot\n")
		telnet.read_until("~ #",timeout=delay+4)
		telnet.close()
		print (reset_vpn_host+ ": good reboot! ")

	except:
		print(reset_vpn_host + ": Error!")

# c=5	
# r,t=speed("192.168.146.49","5188",int(c))
# print r,t
pozreboot(sys.argv[1],"5188", 10,sys.argv[1])
#!/usr/bin/env python
## -*- coding: utf-8 -*-
import sys
import paramiko
import time


def ubisignal(host, port, timeout, retry_interval, ap, ubi_ver):
	client = paramiko.client.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.load_system_host_keys()
	retry_interval = float(retry_interval)
	timeout = int(timeout)
	timeout_start = time.time()
	while time.time() < timeout_start + timeout:
			time.sleep(retry_interval)  
			try:
				client.connect(host, int(port), username="admin",  password="suck", allow_agent=False, look_for_keys=False)
				remote_conn = client.invoke_shell()
				output = remote_conn.recv(65535)
				remote_conn.send("sh ip firewall sessions outside-destination-port 4341\n")
				time.sleep(retry_interval)
				remote_conn.send("r")
				time.sleep(retry_interval)
				output = remote_conn.recv(65535)
				data = output.splitlines()
				remote_conn.send("exit\n")
				data = output.splitlines()
				time.sleep(retry_interval)
				client.close()
				return data[]
				# return data[8:]
                
			except:
				return -100,-100,-100
            	#print data
                
		        
                # output = remote_conn.recv(65535)
                # print data[30].split()[1][:-1]
                # print data[32].split()[1][:-1]
                # print data[33].split()[1]
                #wlanConnections=2 'wlanPollingQuality=90', 'wlanPollingCapacity=80') signal -100..-65
                # if (ap):
                # return data[9][16:], data[65][19:],data[67][20:]
                # else: 
                # return data[25][7:], data[65][19:],data[67][20:]

            
		        
				
s=ubisignal(sys.argv[1],"22",10,2, True,"1")
print ('hello' ,s)
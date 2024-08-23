#!/usr/bin/env python
## -*- coding: utf-8 -*-
import sys
import paramiko
import time


def speed_eltex(host, port, timeout, retry_interval):
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
				trash = output.splitlines()
				remote_conn.send("exit\n")
				trash = output.splitlines()
				time.sleep(retry_interval)
				client.close()
				

				rx=0
				tx=0
				for str in trash:
					
					if len(str)>3 and (str[0] =="M" ):
						rx+=int(str.split()[22])
						tx+=int(str.split()[23])
						print (rx,tx)
					if len(str)>3 and (str[0] =="t" ):
						rx+=int(str.split()[6])
						tx+=int(str.split()[7])
						print (rx,tx)
					
				# data =[rx,tx]
				
				return rx, tx
				
				print (trash[8][1])
				return trash
				# return data[8:]
                
			except:
				return -100,-100
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

            
		        
				
# s=ubisignal(sys.argv[1],"22",10,2, True,"1")
# print ('hello' ,s)
# for str in s:
# 		if len(str)>0:
# 			print (str[0])
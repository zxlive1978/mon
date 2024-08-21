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
	if (ubi_ver=="2"):
		while time.time() < timeout_start + timeout:
			time.sleep(retry_interval)
			try:
				client.connect(host, int(port), username="ubnt",  password="ubnt123", allow_agent=False, look_for_keys=False)
				remote_conn = client.invoke_shell()
				output = remote_conn.recv(65535)
				# print output

				remote_conn.send("mca-status\n")
				time.sleep(retry_interval)
				output = remote_conn.recv(65535)
				data = output.splitlines()
				
				remote_conn.send("exit\n")
				
				#print data
				time.sleep(retry_interval)
				client.close()
				# output = remote_conn.recv(65535)
				# print data[30].split()[1][:-1]
				# print data[32].split()[1][:-1]
				# print data[33].split()[1]
				#wlanConnections=2 'wlanPollingQuality=90', 'wlanPollingCapacity=80') signal -100..-65
				if (ap):
					return data[9][16:], data[65][19:],data[67][20:]
				else: 
					return data[25][7:], data[65][19:],data[67][20:]

				
			except:
				
					return -100,-100,-100
	
	if (ubi_ver=="1"):
		while time.time() < timeout_start + timeout:
			time.sleep(retry_interval)
			try:
				client.connect(host, int(port), username="ubnt",  password="ubnt123", allow_agent=False, look_for_keys=False)
				remote_conn = client.invoke_shell()
				output = remote_conn.recv(65535)
				# print output

				remote_conn.send("mca-status\n")
				time.sleep(retry_interval)
				output = remote_conn.recv(65535)
				data = output.splitlines()
				
				remote_conn.send("exit\n")
				
				time.sleep(retry_interval)
				client.close()
				# time.sleep(retry_interval)
				# output = remote_conn.recv(65535)
				# print data[30].split()[1][:-1]
				# print data[32].split()[1][:-1]
				# print data[33].split()[1]
				#wlanConnections=2 'wlanPollingQuality=90', 'wlanPollingCapacity=80') signal -100..-65
				if (ap):
					return data[14][16:], data[70][19:],data[72][20:]
				else: 
					return data[30][7:], data[70][19:],data[72][20:]

				
			except:
				
					return -100,-100,-100

	if (ubi_ver=="3"):
		# return -100,-100,-100
		while time.time() < timeout_start + timeout:
			time.sleep(retry_interval)
			try:
				client.connect(host, int(port), username="ubnt",  password="admin", allow_agent=False, look_for_keys=False)
				remote_conn = client.invoke_shell()
				output = remote_conn.recv(65535)
				# print output

				remote_conn.send("mca-status\n")
				time.sleep(retry_interval)
				output = remote_conn.recv(65535)
				data = output.splitlines()
				
				remote_conn.send("exit\n")
				time.sleep(retry_interval)
				client.close()
				# print data
				# time.sleep(retry_interval)
				# output = remote_conn.recv(65535)
				# print data[30].split()[1][:-1]
				# print data[32].split()[1][:-1]
				# print data[33].split()[1]
				#wlanConnections=2 'wlanPollingQuality=90', 'wlanPollingCapacity=80') signal -100..-65
				if (ap):
					return data[9][16:], data[65][19:],data[67][20:]
				else: 
					return data[25][7:], data[65][19:],data[67][20:]

				
			except:
				
					return -100,-100,-100

				
# s=ubisignal(sys.argv[1],"22",10,2, True,"1")
# print s


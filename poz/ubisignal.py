#!/usr/bin/env python
## -*- coding: utf-8 -*-
import sys
import paramiko
import time


def ubisignal(host, port, timeout, retry_interval):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    retry_interval = float(retry_interval)
    timeout = int(timeout)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        time.sleep(retry_interval)
        try:
			client.connect(host, int(port), username="ubnt",  password="ubnt123", allow_agent=False, look_for_keys=False)
			remote_conn = client.invoke_shell()
			output = remote_conn.recv(65535)
			# print output

			remote_conn.send("wstalist\n")
			time.sleep(retry_interval)
			output = remote_conn.recv(65535)
			data = output.splitlines()
			
			remote_conn.send("exit\n")
			# time.sleep(retry_interval)
			# output = remote_conn.recv(65535)
			# print data[30].split()[1][:-1]
			# print data[32].split()[1][:-1]
			# print data[33].split()[1]
			#quality capacity signal -100..-65
			return data

			
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but not SSH service responded
            if e.message == 'Error reading SSH protocol banner':
                # print(e)
				return -1,-1,-100
				continue
            # print(reset_vpn_host + ": Error!")
            break
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            return -1,-1,-100
            continue

s=ubisignal(sys.argv[1],"22",10,2)
print s


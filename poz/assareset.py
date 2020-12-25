#!/usr/bin/env python
## -*- coding: utf-8 -*-
import sys
import paramiko
import time


def wait_for_ssh_to_be_ready(host, port, timeout, retry_interval, reset_vpn_host):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    retry_interval = float(retry_interval)
    timeout = int(timeout)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        time.sleep(retry_interval)
        try:
			client.connect(host, int(port), username="s.sedyshev",  password="goodman1978$", allow_agent=False, look_for_keys=False)
			remote_conn = client.invoke_shell()
			output = remote_conn.recv(65535)
			# print output

			remote_conn.send("enable\n")
			time.sleep(retry_interval)
			output = remote_conn.recv(65535)
			# print output

			remote_conn.send("MasterKeyCisco@1\n")
			time.sleep(retry_interval)
			output = remote_conn.recv(65535)
			#print output
			
			remote_conn.send("clear ipsec sa peer "+reset_vpn_host+"\n")
			time.sleep(retry_interval)
			output = remote_conn.recv(65535)
			# print output

			remote_conn.send("exit\n")
			time.sleep(retry_interval)
			output = remote_conn.recv(65535)
			print (reset_vpn_host+ ": good logout! ")
			
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but not SSH service responded
            if e.message == 'Error reading SSH protocol banner':
                print(e)
                continue
            print(reset_vpn_host + ": Error!")
            break
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print(reset_vpn_host + ": Error!")
            continue

wait_for_ssh_to_be_ready("192.168.5.2","60001",20,5, sys.argv[1])


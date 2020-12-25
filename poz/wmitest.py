#!/usr/bin/env python3

import sys
import wmi_client_wrapper as wmi

def mlcacheOn(hosts):
	try:
		wmic = wmi.WmiClientWrapper(username="root",password="root",host=hosts)
		output = wmic.query("cmd.exe dir.exe")
	except:

		output="error"

	return output
outt=mlcacheOn("192.168.147.3")
print outt
#!/usr/bin/env python3

import sys
import wmi_client_wrapper as wmi

def mlcacheOn(hosts):
	try:
		wmic = wmi.WmiClientWrapper(username="root",password="root",host=hosts)
		output = wmic.query("SELECT Caption FROM win32_process  WHERE Name='MLCache.EXE'")
	except:

		output="error"

	return output
outt=mlcacheOn("192.168.146.35")
print len(outt)

#!/usr/bin/python

import wmi
 
conn = wmi.WMI('192.168.1.106', user='AGG\adm.s.sedyshev', password='bombjack1978$')
conn.Win32_Process.Create(CommandLine='cmd.exe /c mkdir teeemp')
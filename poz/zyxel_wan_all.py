#!/usr/bin/env python3

import sys
import telnetlib

def speed_zyxel(host,port,delay, ip_sngs):
	
	rx, tx = 0.0, 0.0	
	try:	
			telnet = telnetlib.Telnet()
			telnet.open(host, port, timeout=delay)
			telnet.read_until("*",timeout=delay)
			telnet.write("admin\n")
			telnet.read_until("Password:",timeout=delay)
			telnet.write("suck\n")
			telnet.read_until("B",timeout=delay)
			telnet.write("enable\n")
			telnet.read_until("Router#",timeout=delay)
			#SNGS VIDEO
			telnet.write("show conn destination "+ip_sngs+" \n")
			#ALL TRAFFIC
			# telnet.write("show conn"+" \n")
			telnet.read_until("N",timeout=delay)
			telnet.write("exit\n")
			data =telnet.read_all()
			
			data = data.splitlines()
			print data
			wanrx = float(data[len(data)-5].split(':')[1].split('(')[0][1:])
			wanr= data[len(data)-5].split(':')[1].split('(')[1]
			#print wanr
			#if Mb
			if wanr[0] == "B":
				wanrx = float((wanrx*8.0)/1048576.0)
			if wanr[0] == "K":
				wanrx = float((wanrx*8.0)/1024.0)
			if wanr[0] == "M":
				wanrx = float(wanrx*8.0)
			if wanr[0] == "G":
				wanrx = float((wanrx*1024.0)*8.0)
			

			# #if Kbps
			# if wanr[0] == "B":
			# 	wanrx = float((wanrx*8.0)/1024.0)
			# if wanr[0] == "K":
			# 	wanrx = float((wanrx*8.0))
			# if wanr[0] == "M":
			# 	wanrx = float((wanrx*8.0))*1024
			# if wanr[0] == "G":
			# 	wanrx = float((wanrx*1048576.0)*8.0)
				
			#print wanrx 
			
			wantx = float(data[len(data)-4].split(':')[1].split('(')[0][1:])
			want= data[len(data)-4].split(':')[1].split('(')[1]
			#print wanr
			# #if Mb
			if want[0] == "B":
				wantx = float((wantx*8.0)/1048576.0)
			if want[0] == "K":
				wantx = float((wantx*8.0)/1024.0)
			if want[0] == "M":
				wantx = float(wantx*8.0)
			if want[0] == "G":
				wantx = float((wantx*1024.0)*8.0)

			#if Kbps
			# if want[0] == "B":
			# 	wantx = float((wantx*8.0)/1024.0)
			# if want[0] == "K":
			# 	wantx = float((wantx*8.0))
			# if want[0] == "M":
			# 	wantx = float((wantx*8.0))*1024
			# if want[0] == "G":
			# 	wantx = float((wantx*1048576.0)*8.0)
				
			#print wantx
			
			 
			# numbs=(len(data) -8)
			# if numbs>0:
				# j=2
				# while j<=numbs:
					# head = data[j+1].split()
					# head = head#.split()
					# print head#[1]
					# str = data[j+2].split()
					
					# if head[1] == "Total Receive" and str[0].split(':')[1] == "2206":
								# r= str[1].split('(')
								# rf=float(r[0])
								# if r[1][0] == "B":
									# rf=rf/1048576
								# if r[1][0] == "K":
									# rf=rf/1024
								# if r[1][0] == "G":
									# rf=rf*1024
								# rx=rx+rf
								# t= str[2].split('(')
								# tf=float(t[0])
								# if t[1][0] == "B":
									# tf=tf/1048576
								# if t[1][0] == "K":
									# tf=tf/1024
								# if t[1][0] == "G":
									# tf=tf*1024
								# tx=tx+tf
								# #print j 
						# #print numbs
								# # print str
					# j=j+2
			#wan_str = "103.04" 
			# print wan_str[6]
			# print wan_str[7]
			# print round(rx,2),round(tx,2)
			telnet.close()
			#speedtx = float(wan_str[6])
			#speedrx = float(wan_str[7])
						
			return round(wanrx,3),round(wantx,3)
	#Mbps
	#speedall=(speedrx+speedtx)/1024
	except:
			return -1,-1
		# speedtx=-1
		# speedrx=-1
		# return str(speedtx), str(speedrx)

	# return str(round(speedtx*8/1024/1024,3)), str(round(speedrx*8/1024/1024,3))
#c = 5	
#r,t=speed_zyxel("192.168.146.97","5188",int(c), "213.80.235.178")
#print r,t

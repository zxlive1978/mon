#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import subprocess
import time

def shoot(conf,netcam_url, netcam_userpass, width, height, framerate, target_dir, snapshot_filename,delay):
	print snapshot_filename
	#Изменение текущего конфига
	s1 = open(conf+"motion.conf","r+")
	newconf =""
	for line in s1.readlines():
		
		if line.find("netcam_url")!=-1:
			line=line.replace(line, "netcam_url "+netcam_url+"\n")
		if line.find("netcam_userpass")!=-1:
			line=line.replace(line, "netcam_userpass "+netcam_userpass+"\n")
		if line.find("width")==0:
			line=line.replace(line, "width "+width+"\n")
		if line.find("height")==0:
			line=line.replace(line, "height "+height+"\n")
		if line.find("framerate")==0:
			line=line.replace(line, "framerate "+framerate+"\n")
		if line.find("target_dir")==0:
			line=line.replace(line, "target_dir "+target_dir+"\n")
		if line.find("snapshot_filename")==0:
			line=line.replace(line, "snapshot_filename "+snapshot_filename+"\n")
			
		newconf+=line
	   
	s2 = open(conf+"motion.conf","w")
	s2.write(newconf)
	s1.close()
	s2.close()
	#Запуск motion не дожидаясь конца
	myproc1 = subprocess.Popen(['motion', conf+"motion.conf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
	
	# пауза
	time.sleep(delay)
	# kill motion
	myproc2 = subprocess.Popen(['killall','-SIGQUIT','motion'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
	

	

#934_1
shoot("/var/www/html/mon/poz/", #motion.conf
 "rtsp://admin:admin123@192.168.146.232:554/Streaming/Channels/101", #rtsp addr
 "admin:admin123", #netcam_userpass
 "720", #width
 "480", #height
 "1", #framerate
 "/var/www/html/mon/poz/", #target_dir для камер
 "915_1", #snapshot_filename для камер
 5.0 ) # delay
#915_2
shoot("/var/www/html/mon/poz/", #motion.conf
 "rtsp://admin:admin123@192.168.146.233:554/Streaming/Channels/101", #rtsp addr
 "admin:admin123", #netcam_userpass
"720", #width
 "480", #height
"1", #framerate
 "/var/www/html/mon/poz/", #target_dir для камер
 "915_2", #snapshot_filename для камер
 5.0 ) # delay
#915_3
shoot("/var/www/html/mon/poz/", #motion.conf
 "rtsp://admin:admin123@192.168.146.234:554/Streaming/Channels/101", #rtsp addr
 "admin:admin123", #netcam_userpass
 "720", #width
 "480", #height
 "1", #framerate
"/var/www/html/mon/poz/", #target_dir для камер
 "915_3", #snapshot_filename для камер
5.0 ) # delay
 #4
shoot("/var/www/html/mon/poz/", #motion.conf
"rtsp://admin:admin123@192.168.146.235:554/Streaming/Channels/101", #rtsp addr
"admin:admin123", #netcam_userpass
 "720", #width
"480", #height
 "1", #framerate
 "/var/www/html/mon/poz/", #target_dir для камер
"915_4", #snapshot_filename для камер
5.0 ) # delay

#604
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.72:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","224_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.73:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","224_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.74:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","224_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.75:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","224_4",5.0 ) 


#609
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.104:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","908_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.105:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","908_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.106:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","908_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.107:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","908_4",5.0 ) 

#73
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.168:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","89_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.169:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","89_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.170:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","89_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.171:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","89_4",5.0 ) 

#71
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.40:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","411_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.41:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","411_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.42:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","411_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.43:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","411_4",5.0 ) 

#9917
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.200:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","628_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.201:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","628_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.202:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","628_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:admin123@192.168.146.203:554/Streaming/Channels/101","admin:admin123", "1280","720","1","/var/www/html/mon/poz/","628_4",5.0 ) 

#629
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.26:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","631_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.27:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","631_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.28:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","631_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.29:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","631_4",5.0 ) 

#99
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.72:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","110_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.73:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","110_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.74:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","110_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.75:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","110_4",5.0 ) 


#shoot("/var/www/html/mon/poz/", "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=1&subtype=0","admin:admin", "704","576","1","/var/www/html/mon/poz/","110_1",5.0 ) 
#shoot("/var/www/html/mon/poz/", "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=2&subtype=0","admin:admin", "704","576","1","/var/www/html/mon/poz/","110_2",5.0 ) 
#shoot("/var/www/html/mon/poz/", "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=3&subtype=0","admin:admin", "704","576","1","/var/www/html/mon/poz/","110_3",5.0 ) 
#shoot("/var/www/html/mon/poz/", "rtsp://admin:admin@192.168.146.53:554/cam/realmonitor?channel=4&subtype=0","admin:admin", "704","576","1","/var/www/html/mon/poz/","110_4",5.0 ) 

#83
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.136:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","83_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.137:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","83_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.138:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","83_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.139:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","83_4",5.0 ) 

#406
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.8:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","401_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.9:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","401_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.10:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","401_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.146.11:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","401_4",5.0 ) 

#260
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.8:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","610_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.9:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","610_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.10:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","610_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.11:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","610_4",5.0 ) 

#627
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.40:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","627_1",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.41:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","627_2",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.42:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","627_3",5.0 ) 
shoot("/var/www/html/mon/poz/", "rtsp://admin:Admin123@192.168.147.43:554/Streaming/Channels/101","admin:Admin123", "1280","720","1","/var/www/html/mon/poz/","627_4",5.0 )


 
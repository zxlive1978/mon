#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import sys

def camcam(message, bigsmall):
	#subprocess.call(["curl", "-s", "-X", "POST", "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage", "-d", "chat_id="+chat_id, "-d", "text="+message])
	#subprocess.call(["/usr/local/bin/yowsup-cli", "demos", "-c", "/root/.config/yowsup/79378222711/config.json", "-s", " "+chat_id, " "+message])
	if (bigsmall=='big'):
		os.system('/usr/bin/ffmpeg -rtsp_transport tcp -stimeout 5000000 -i  "rtsp://admin:Admin123@'+message+':554/Streaming/Channels/101"  -vframes 1 -y   /var/www/html/mon/poz/montag.jpg')
	else:
		os.system('/usr/bin/ffmpeg -rtsp_transport tcp -stimeout 5000000 -i  "rtsp://admin:admin123@'+message+':554/Streaming/Channels/101"  -vframes 1 -y   /var/www/html/mon/poz/montag.jpg')
        
#/usr/local/bin/yowsup-cli demos -c /root/.config/yowsup/79378222711/config.json -s 79272857676-1490802779 "Я РОБОТ"
#curl -s -X POST https://api.telegram.org/bot<ТОКЕН>/sendMessage -d chat_id=<ID_ЧАТА> -d text="Hello World"
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"-267211915","text":"test message here"}' "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"


camcam(sys.argv[1], sys.argv[2])


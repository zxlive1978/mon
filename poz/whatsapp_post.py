#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os

def post(message,chat_id):
	#subprocess.call(["curl", "-s", "-X", "POST", "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage", "-d", "chat_id="+chat_id, "-d", "text="+message])
	#subprocess.call(["/usr/local/bin/yowsup-cli", "demos", "-c", "/root/.config/yowsup/79378222711/config.json", "-s", " "+chat_id, " "+message])
	
	os.system('/usr/local/bin/yowsup-cli demos -c /root/.config/yowsup/79378222711/config.json -s 79272857676-1490802779 '+message)
post("123","79272857676-1490802779")
#/usr/local/bin/yowsup-cli demos -c /root/.config/yowsup/79378222711/config.json -s 79272857676-1490802779 "Я РОБОТ"
#curl -s -X POST https://api.telegram.org/bot<ТОКЕН>/sendMessage -d chat_id=<ID_ЧАТА> -d text="Hello World"
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"-267211915","text":"test message here"}' "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"
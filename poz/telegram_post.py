#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def post(message,chat_id):
	#subprocess.call("curl --header 'Content-Type: application/json' --request 'POST' --data '{\x22chat_id\x22:\x22-267211915\x22,\x22text\x22:"Одын одын"}' \x22https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage\x22")
	#subprocess.call(["curl", "--header" ,"'Content-Type: application/json'" ,"--request" ,"'POST'" ,"--data" ,"'{'chat_id':'-267211915','text':"Одын одын'}'","https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"])
	subprocess.call(["curl", "-s", "-X", "POST", "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage", "-d", "chat_id="+chat_id, "-d", "text="+message])
#post("О, да","-267211915")

#curl -s -X POST https://api.telegram.org/bot<ТОКЕН>/sendMessage -d chat_id=<ID_ЧАТА> -d text="Hello World"
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"-267211915","text":"test message here"}' "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"
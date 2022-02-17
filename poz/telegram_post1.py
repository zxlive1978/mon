#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import subprocess
import struct

def fullchr(n):
    return struct.pack('<I', n).decode('utf-32le')

def post(message,chat_id):
	#subprocess.call("curl --header 'Content-Type: application/json' --request 'POST' --data '{\x22chat_id\x22:\x22-267211915\x22,\x22text\x22:"Одын одын"}' \x22https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage\x22")
	#subprocess.call(["curl", "--header" ,"'Content-Type: application/json'" ,"--request" ,"'POST'" ,"--data" ,"'{'chat_id':'-267211915','text':"Одын одын'}'","https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"])
	subprocess.call(["curl", "-s", "-X", "POST", "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage", "-d", "chat_id="+chat_id, "-d", "text="+message])

#a = (""\"x"+str(hex(0xF0)[2:])+""\"x"+str(hex(0x9F)[2:])+""\"x"+str(hex(0x9A)[2:])+""\"x"+str(hex(random.randrange(0x80,0xA4))[2:]))

#print fullchr(random.randrange(0x1F680,0x1F6A4))
post(fullchr(random.randrange(0x1F680,0x1F6A4)) , "-576447110")

#\xF0\x9F\x9A\xA4
#post ("\xF0\x9F\x9A\x80","-267211915")



#curl -s -X POST https://api.telegram.org/bot<ТОКЕН>/sendMessage -d chat_id=<ID_ЧАТА> -d text="Hello World"
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"-267211915","text":"test message here"}' "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"
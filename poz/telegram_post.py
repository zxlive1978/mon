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

#App api_id:24694269
#App api_hash:3cf29c5fed7191044c41ccadb4cf703a
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigvO/vBfqACJLZtS7QMgCGXJ6XIR
# yy7mx66W0/sOFa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgQfaUHd8wJpDWHcR2OFwv
# plUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfmH0JP503wr5INS1poWg/
# j25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzXq5YOpk4bYEQ6mvRq7D1
# aHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpdKcSwHnd6FudwGO4pcCO
# j4WcDuXc2CTHgH8gFTNhp/Y8/SpDOhvn9QIDAQAB
# -----END RSA PUBLIC KEY-----
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
# 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
# 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
# +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
# t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
# 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB
# -----END RSA PUBLIC KEY-----
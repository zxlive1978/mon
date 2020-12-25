#!/usr/bin/env python
# -*- coding: utf-8 -*-

# >>> requests.post('https://httpbin.org/post', data={'key':'value'})
# >>> requests.put('https://httpbin.org/put', data={'key':'value'})
# >>> requests.delete('https://httpbin.org/delete')
# >>> requests.head('https://httpbin.org/get')
# >>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
# >>> requests.options('https://httpbin.org/get')
import subprocess
import requests

def check():
	#GET запрос с параметрами в URL
	response = requests.get("https://hydrofalll.ddns.net:5443/LiveApp/rest/broadcast/getList/0/50")
	# Вывод ответа, полученного от сервера API
	
	for captain in response.json():
		if (captain['hlsViewerCount']==0):
			print(captain)
			print(captain['streamId'])
			okdel=requests.post('https://hydrofalll.ddns.net:5443/LiveApp/rest/broadcast/delete/'+captain['streamId'])
			print(okdel)
			
check()

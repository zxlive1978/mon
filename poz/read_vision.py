#!/usr/bin/env python3

import sys
from PIL import Image, ImageFile
def check_crash_cam(shot):
	# try:
		im = Image.open(shot)
		width, height = im.size
		rgb_im = im.convert('RGB')
		for i in range(70, width-70, 10):
		  for j in range(70, height-70):
			r, g, b = rgb_im.getpixel((i, j))
			# print i,j, r, g, b
			#RGB
			if r!=0:
				signal=1.0
				print i,j ,r,g,b
				# return signal
			if g!=0:
				signal=1.0
				print i,j ,r,g,b
				# return signal
			if b!=0:
				signal=1.0
				print i,j ,r,g,b
				# return signal
		
		signal = -1.0
		# return signal
		#rgb_im.save("/var/www/html/mon/poz/631_1_black_.jpg","JPEG")
	
	# except:
		# signal= -1.0
		# return signal


ImageFile.MAXBLOCK = 2**20
s = check_crash_cam("/var/www/html/mon/poz/631_3_black.jpg")

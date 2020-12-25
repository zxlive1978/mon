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
			rgb_im.putpixel((i, j), (255,255,255))
			# print i,j, r, g, b
			#RGB
			# if r!=0:
				
				# if g!=0:
					
					# if b!=0:
						# signal=1.0
						# return signal
		
		signal = -1.0
		# return signal
		rgb_im.save("/var/www/html/mon/poz/547_3_fill.jpg","JPEG")
	
	# except:
		# signal= -1.0
		# return signal


ImageFile.MAXBLOCK = 2**20
s = check_crash_cam("/var/www/html/mon/poz/547_3.jpg")

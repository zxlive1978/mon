#!/usr/bin/env python3

import sys
from PIL import Image
def check_crash_cam(shot):
	try:
		im = Image.open(shot)
		width, height = im.size
		rgb_im = im.convert('RGB')
		rt, bt, gt =rgb_im.getpixel((int(width/2), int(height/2)))
		for i in range(70, width-70, 10):
		  for j in range(70, height-70):
			r, g, b = rgb_im.getpixel((i, j))
			# print i,j, r, g, b
			#RGB
			if r!=rt:
				signal=1.0
				return signal
			if g!=gt:
				signal=1.0
				return signal
			if b!=bt:
				signal=1.0
				return signal
		
		signal = -1.0
		return signal
	
	except:
		signal= -1.0
		return signal





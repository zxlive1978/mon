#!/usr/bin/env python
# coding: utf-8

from os.path import join, getsize
import os
import fnmatch
from struct import *
import math
import MySQLdb
import threading
import string
import struct
import time
from datetime import datetime, timedelta


#data = '\x00\xBC\xCE\x6F\xEC\xE7\xCC\x42'  # Time: 2015-04-16 09:25:47
#05 00 90 E3 38 8E A3 CB
#00 90 E3 38 8E A3 CB A8
#\x05\x00\x90\xE3\x38\x8E\xA3\xCB\xA8\x0E\x40\x07
#data = '\x05\x00\x90\xE3' 
#data = '\x00\x90\xE3\x38' 
#data = '\x90\xE3\x38\x8E' 
#data = '\xE3\x38\x8E\xA3' 
#data = '\x38\x8E\xA3\xCB' 
#data = '\x8E\xA3\xCB\xA8' 
#data = '\xA3\xCB\xA8\x0E' 
#data = '\xCB\xA8\x0E\x40' 
#data = '\xA8\x0E\x40\x07' 
#data = '\x05\x00\x90\xE3\x38\x8E\xA3\xCB' 
#data = '\x00\x90\xE3\x38\x8E\xA3\xCB\xA8' 
#data = '\x90\xE3\x38\x8E\xA3\xCB\xA8\x0E' 
#data = '\xE3\x38\x8E\xA3\xCB\xA8\x0E\x40' 
#data = '\x38\x8E\xA3\xCB\xA8\x0E\x40\x07' 
data = '\x05\x00\x90\xE3\x38\x8E\xA3\xCB\xA8\x0E\x40\x07'
#data_double = struct.unpack('<d', data)[0] 
data_double = struct.unpack('<cccccccccccc', data)[0]
#data_double = struct.unpack('<I', data)[0]
print data_double
#time_from_starting_date = timedelta(days=-2, milliseconds=long(data_double))
#starting_date = datetime(0001, 01, 02)
#result_date = starting_date + time_from_starting_date

#print "Time:", result_date
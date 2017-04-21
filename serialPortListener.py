# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:53:48 2017

@author: Rupert.Thomas

Python 2.7 tested
"""

# Serial port listener

import serial

port='COM9'
baudrate=4800
timeout=0.5

with serial.Serial(port=port, baudrate=baudrate, timeout=timeout) as ser:
	while True:
		try:
			line = ser.readline()   # read a '\n' terminated line
			if line is not '':
				print line
		except:
			ser.close()
			break
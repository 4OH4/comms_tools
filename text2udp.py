# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:52:09 2017
@author: not really Rupert.Thomas

text2udp.py

Read a text file and relay each line as a UDP packet to localhost:3001

Modified from:
https://gist.github.com/gerkey/bf749775e6bc600368b97ce3d9f113e5
"""

import dpkt
import sys
import socket
import time

UDP_IP = "localhost"
UDP_PORT = 3001

delay_time = 2
loop = True

def parse(fname):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	i = 0
	while True:
		with open(fname,'rb') as f:	# open text file
			
			for line in f:	   	# relay each line as a single packet	 
				ts = time.time()
				packet_data = line

				print('[%d] [%s] sending %d-byte message'%(i,ts,len(packet_data)))
				sock.sendto(packet_data, (UDP_IP, UDP_PORT))
				i += 1
				time.sleep(delay_time)
		if not loop:
			break

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('ERROR: must supply text filename')
		sys.exit(1)
		
		# Alternative: use default file
		# fname = 'single_UDP.txt'
		# parse(fname)
	else:
		parse(sys.argv[1])
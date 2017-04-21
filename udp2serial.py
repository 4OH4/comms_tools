# https://github.com/cylinderlight/udp2serial
# Written by Marco Brianza. Copyright (c) 2014

'''
Permission to use, copy, modify, distribute, and distribute modified versions of this software and its documentation without fee and without a signed licensing agreement, is hereby granted, provided that the above copyright notice, this paragraph and the following two paragraphs appear in all copies, modifications, and distributions.
'''

# Generate test packets with:
# echo "foo" | nc -w1 -u 127.0.0.1 10000

import socket,select
import time
# import tty  # Unix only

UDP_PORT_IN = 10000 # UDP server port
UDP_PORT_OUT = 11000
MAX_UDP_PACKET=512 # max size of incoming packet to avoid sending too much data to the micro
SERIAL_PORT='/dev/ttyATH0'
BROADCAST_MODE=False #set to True if you want a broadcast replay instead of unicast


udp_client_address=('127.0.0.1',UDP_PORT_OUT) #where to forward packets coming from serial port
udp_server_address = ('',UDP_PORT_IN) #udp server
udp_broadcast=('<broadcast>',UDP_PORT_OUT) #broadcast address

#serial=open(SERIAL_PORT,'r+b') #open the file corrisponding to YUN serial port
#tty.setraw(serial) #this avoids the terminal to change bytes with value 10 in 13 10

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(udp_server_address)
if BROADCAST_MODE: 
	udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while True:
	(rlist, wlist, xlist) = select.select([udp_socket], [], [])    
                                
	if udp_socket in rlist:
		udp_data,udp_client = udp_socket.recvfrom(MAX_UDP_PACKET)	
		print udp_data
		# serial.write(udp_data)
		# serial.flush()
		udp_client_address=(udp_client[0],UDP_PORT_OUT)
		time.sleep(0.001)
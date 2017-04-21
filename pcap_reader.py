#!/usr/bin/env python
"""
Created on Mon Apr 10 14:52:09 2017
@author: not really Rupert.Thomas

pcap_reader.py

Read a .pcap file full of UDP packets from a velodyne and play them back to localhost:3001

Heavily derived from:
https://gist.github.com/gerkey/bf749775e6bc600368b97ce3d9f113e5
"""

import dpkt
import sys
import socket
import time

UDP_IP = "localhost"
UDP_PORT = 3001

delay_time = 0.1
loop = False

def parse(fname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    n = 0
    while True:

        with open(fname,'rb') as f:	# open pcap file
            id = 1  # wireshark packet index (appears to start at 1)
            pcap = dpkt.pcap.Reader(f)
            for ts, buf in pcap:	# extract layers of data
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                if isinstance(ip.data, dpkt.udp.UDP):	# check packet is actually UDP

                    udp = ip.data
                    if udp.dport == UDP_PORT:   # only forward packets that match the target port num.

                        packet_data = udp.data #.encode("hex")

                        print('[%d] [%d] [%s] sending %d-byte message'%(n,id,ts,len(packet_data.encode('hex'))/2))
                        print packet_data.encode('hex')
                        sock.sendto(packet_data, (UDP_IP, UDP_PORT))
                        n += 1
                        time.sleep(delay_time)

                id += 1

        if not loop:
            break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR: must supply pcap filename')
        sys.exit(1)
		
		# Alternative: use default files
        # fname = 'Nav_UDP_packet_capture.pcap'
        # fname = 'single_UDP3.pcap'
        # parse(fname)
    else:
        parse(sys.argv[1])
#!/usr/bin/env python

"""
Python UDP Tutorial: Client side
Client sends to server and expects to receive sent data pack from server
"""

import socket
import sys

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = "This is the message it will be repeated"

try:

    # send data
    print sys.stderr, 'sending %s' %message
    sent = sock.sendto(message, server_address)

    # receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received %s' %data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

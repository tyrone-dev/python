#!/usr/bin/env python

"""
Python UDP Tutorial: Server side
Server waits for messages from clients and returns the recieved data
"""

import socket
import sys

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' %server_address

sock.bind(server_address) # allows incoming connections on this address

# continuously check for messages from clients
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096) # recvfrom returns data as well as address from whence it came

    print >>sys.stderr, 'received %s bytes from %s' %(len(data), address)
    print >>sys.stderr, data

    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' %(sent, address)

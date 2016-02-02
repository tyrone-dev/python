#!/usr/bin/env python

"""
Tutorial on endianness

Endianness refers to the order of BYTES making up a digital WORD (usually > 1 BYTE)
    - it also refers to the order in which BYTES are transferred over a DIGIAL LINK
    
Big Endian - big-end of the data/word, the MOST SIGNIFICANT BYTE, is stored in the lowest memory address (or sent first)
           - also network byte order

Little Endian - little-end of the data/word, the LEAST SIGNIFICANT BYTE, is stored in the lowest memory address (or sent first)
              - this storage method is popular for microprocessors

"""

import struct
import binascii

"""
The functions below SWAP the endianess of a given 16 bit (2 byte) or 32 bit (4 byte) data stream.
When sending packets over a network, the preferred method of endianness is BIG ENDIAN. Most systems are natively
little endian.

The struct package has an option for specifying the byte order: '!' is used for NETWORK BYTE ORDER

"""

def endianSwap_16bit(data_in):
    
    data_out = ((data_in >> 8) & 0xFF) | ((data_in << 8) & 0xFF00)
    
    return data_out

def endianSwap_32bit(data_in):
    data_out = ((data_in >> 24) & 0xFF) | ((data_in >> 8) & 0xFF00) | ((data_in << 8) & 0xFF0000) | ((data_in << 24) & 0xFF000000);
    return data_out

data_in = [0x90AB12CD, 0xAB90CD12]
print "Original Data: ", hex(data_in[0]), ', ', hex(data_in[1])

print "\nNote: each multi-byte piece of data is stored with the specified endianness individually (i.e. only that piece of data is considered\n\
When printing the packed data below, memory locations (addresses) INCREASE from LEFT TO RIGHT\n"
       

# for little endian packing
little_packer = struct.Struct("2I")
little_packed = little_packer.pack(*data_in)
print "\nLittle Endian Packing     : ", repr(little_packed)


# for big endian packing (! or > is used for big-endian, ! is for networks)
big_packer = struct.Struct("!2I")
big_packed = big_packer.pack(*data_in)
print "\nBig Endian Packing        : ", repr(big_packed)

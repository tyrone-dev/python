#!/usr/bin/env python

"""
Learning python struct module
    : module allows for converting between strings of bytes and native Python data types (ints, strings)
    Structs support packing data into strings, and unpacking data from strings using format specifiers made up of characters representing the type of the data and optional count and endian-ness indicators
"""

import struct
import binascii

values = (1, 'ab', 2.7) # data to be packed

s = struct.Struct('I 2s f') # create struct object with specified format : 1 int or Long, 2 chars, 1 float
packed_data = s.pack(*values) # packs data

print 'Original values: ', values
print 'Format string  : ', s.format
print 'Uses           : ', s.size, 'bytes'
print 'Packed Value   : ', binascii.hexlify(packed_data)


# unpacking data

print "Unpacking . . . \n"
unpacked_data = s.unpack(packed_data)
print 'Unpacked Values: ', unpacked_data

# endianness

# Big Endianness: big-end of the data is read/stored/sent first
# Little Endianness: little-end of the data is read/stored/sent first

# note: network byte order == big endianness

# demonstrate various options for explicitly enforcing endianness

endianness = [('@', 'native, native'), ('=', 'native, standard'), ('<', 'little-endian'), ('>', 'big-endian'), ('!', 'network')]

print '\nDemonstrate enforcing endianness: '
print 'Original values: ', values

for code, name in endianness:
    
    s = struct.Struct(code + ' I 2s f') # create struct object with specified format : 1 int or Long, 2 chars, 1 float
    packed_data = s.pack(*values)
    print
    print 'Format string    : ', s.format, 'for', name
    print 'Uses             : ', s.size, 'bytes'
    print 'Packed Value(hex): ', binascii.hexlify(packed_data)
    print 'Packed Value     : ', repr(packed_data) # use repr to print our packed data
    print 'Unpacked Values  : ', s.unpack(packed_data)

# buffers

# optimize packing/unpacking by avoiding additional overhead of allocating new buffer for each packed structure
# pack_into() and unfrom_from() methods support writing to pre-allocated buffers directly

print '\nDemonstrating buffers . . .'
print 'Original values: ', values

s = struct.Struct("I 2s f")

print '\nctypes string buffer'

import ctypes
b = ctypes.create_string_buffer(s.size) # s.size indicated the size of the buffer required
print 'Before     : ', binascii.hexlify(b.raw)
s.pack_into(b, 0, *values)
print 'After      : ', binascii.hexlify(b.raw)
print 'Unpacked   : ', s.unpack_from(b, 0)

print '\narray'

import array
a = array.array('c', '\0' * s.size)
print 'Before     : ', binascii.hexlify(a)
s.pack_into(a, 0, *values)
print 'After      : ', binascii.hexlify(a)
print 'Unpacked   : ', s.unpack_from(a, 0)








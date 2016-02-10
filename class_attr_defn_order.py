#!/usr/bin/env python

"""
Implementing functionality to list Python Object attributes in 
definition order
"""

from collections import OrderedDict
from odict import odict
import struct

## what does object do here??
#class first(object):
#    #def __init__(self, *args, **kwargs):
#    #    self._attrs = OrderedDict(*args, **kwargs)
#
#    def __getattr__(self,name):
#        try:
#            return self._attrs[name]
#        except KeyError:
#            raise AttributeError(name)
#
#    def __setattr__(self, name, value):
#        if name == '_attrs':
#            return super(first, self).__setattr__(name, value)
#        self._attrs[name] = value
#
#class second(first):
#    def __init__(self, *args, **kwargs):
#        self.a = 1
#        self._attrs = OrderedDict(*args, **kwargs)
#        self.b = 2
#        self.c = 3
#        self.d = 4
#
#
##s = second()
##s.do_something()
##print s._attrs
#
## below works but wtf??
#class Test(object):
#    def __init__(self):
#        self.__dict__=OrderedDict()
#        self.__dict__['a'] = 1
#        self.__dict__['b'] = 2
#        self.__dict__['c'] = 3


#t = Test()
#print t.__dict__
#
#print t.a
#print t.b
#print t.c

#class OrderedClassMeta(type):
#    @classmethod
#    def __prepare__(cls, name, bases, **kwds):
#        return OrderedDict()
#    #def __new__(self,name, bases, classdic):
#        
#class OrderedClass(object):
#    __metaclass__ = OrderedClassMeta
#    pass
#
#class test2 (OrderedClass):
#    def __init__(self):
#        self.Header = "Hi"
#        self.BoardReg = "Hey"
#        self.RegAddress = "What"
#        self.RegDataHigh = "Who"
#        self.RegDataLow = "When"
#
##t2 = test2()
##print (t2.__dict__
# Command Packet Structures

def dataSplitAndPack(data):
    packer = struct.Struct("!I")
    packedData = packer.pack(data)
    
    dataHigh = packedData[:2]
    dataLow = packedData[-2:]
    
    return (dataHigh, dataLow)

#class command(object):
#    	
#        def __init__(self):
#            self.__dict__['_odict'] = odict()
#
#	def createPayload(self):
#            self.payload = ''
#            
#            orderedAttributes = [attr for attr in self._odict.items() if attr[0] != 'payload']
#
#            for attribute in orderedAttributes:
#                attr, value = attribute
#                    
#                if (isinstance(value, sCommandHeader)):
#                    for sub_attribute in value._odict.items():
#                        sub_attr, sub_value = sub_attribute
#                        print sub_attr, repr(sub_value)
#                        self.payload += sub_value
#                else:
#
#                    print attr, repr(value)
#                    self.payload += value
#
#            return self.payload
#
#	def packet2BytePacker(self, data):
#		packer = struct.Struct("!H")
#
#		return packer.pack(data)
#
#        def __getattr__(self, value):
#            return self.__dict__['_odict'][value]
#        def __setattr__(self, key, value):
#            self.__dict__['_odict'][key] = value
#
##Command Header
#class sCommandHeader(command):
#	def __init__(self, commandID, seqNum):
#		self.__dict__['_odict'] = odict()
#                self.CommandType = self.packet2BytePacker(commandID)
#		self.SequenceNumber = self.packet2BytePacker(seqNum)
#
## WRITE_REG
#class sWriteRegReq(command):
#	def __init__(self, commandID, seqNum, BoardReg, RegAddr, RegDataHigh, RegDataLow):
#		self.__dict__['_odict'] = odict()
#		self.Header       = sCommandHeader(commandID, seqNum)
#		self.BoardReg    = self.packet2BytePacker(BoardReg)
#		self.RegAddress  = self.packet2BytePacker(RegAddr)
#		self.RegDataHigh = RegDataHigh
#		self.RegDataLow  = RegDataLow
#
## template for using odict module
#class AnotherOne(command):
#    def __init__(self, commandID, seqNum, BoardReg, RegAddr, RegDataHigh, RegDataLow):
#        self.__dict__['_odict'] = odict()
#        self.commID = commandID
#        self.seqNum = seqNum
#        self.BoardReg = BoardReg
#        self.RegAddress = RegAddr
#        self.RegDataHigh = RegDataHigh
#        self.RegDataLow = RegDataLow
#
#    def __getattr__(self, value):
#        return self.__dict__['_odict'][value]
#    def __setattr__(self, key, value):
#        self.__dict__['_odict'][key] = value

# command packet structure
class command(object):
    	
        def __init__(self):
            self.__dict__['_odict'] = odict()
	
	def createPayload(self):
	    '''
	    Create payload for sending via UDP Packet to SKARAB
	    '''

            self.payload = ''
            
            orderedAttributes = [attr for attr in self._odict.items() if attr[0] != 'payload']

            for attribute in orderedAttributes:
                attr, value = attribute
                    
                if (isinstance(value, sCommandHeader)):
                    for sub_attribute in value._odict.items():
                        sub_attr, sub_value = sub_attribute
                        print sub_attr, repr(sub_value)
                        self.payload += sub_value
                else:

                    print attr, repr(value)
                    self.payload += value

            return self.payload

	def packet2BytePacker(self, data):
		packer = struct.Struct("!H")

		return packer.pack(data)

	def packet2ByteUnpacker(self, data):
		unpacker = struct.Struct("!H")

		return unpacker.unpack(data)

        def __getattr__(self, value):
            return self.__dict__['_odict'][value]
        def __setattr__(self, key, value):
            self.__dict__['_odict'][key] = value

   

#Command Header
class sCommandHeader(command):
	def __init__(self, commandID, seqNum):
		self.__dict__['_odict'] = odict()
                self.CommandType = self.packet2BytePacker(commandID)
                self.SequenceNumber = self.packet2BytePacker(seqNum)

# WRITE_REG
class sWriteRegReq(command):
	def __init__(self, commandID, seqNum, BoardReg, RegAddr, RegDataHigh, RegDataLow):
		self.__dict__['_odict'] = odict()
		self.Header       = sCommandHeader(commandID, seqNum)
		self.BoardReg    = self.packet2BytePacker(BoardReg)
		self.RegAddress  = self.packet2BytePacker(RegAddr)
		self.RegDataHigh = RegDataHigh
		self.RegDataLow  = RegDataLow

class sWriteRegResp(command):
	def __init__(self, commandID, seqNum, BoardReg, RegAddr, RegDataHigh, RegDataLow, Padding):
		self.__dict__['_odict'] = odict()
		self.Header       = sCommandHeader(commandID, seqNum)
		self.BoardReg    = BoardReg
		self.RegAddress  = RegAddr
		self.RegDataHigh = RegDataHigh
		self.RegDataLow  = RegDataLow
		self.Padding = Padding

writeObj = sWriteRegReq(1,2,3, 0xab, *(dataSplitAndPack(0xABCDEEFF)))

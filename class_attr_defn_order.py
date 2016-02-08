#!/usr/bin/env python

"""
Implementing functionality to list Python Object attributes in 
definition order
"""

from collections import OrderedDict



# what does object do here??
class first(object):
    #def __init__(self, *args, **kwargs):
    #    self._attrs = OrderedDict(*args, **kwargs)

    def __getattr__(self,name):
        try:
            return self._attrs[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == '_attrs':
            return super(first, self).__setattr__(name, value)
        self._attrs[name] = value

class second(first):
    def __init__(self, *args, **kwargs):
        self.a = 1
        self._attrs = OrderedDict(*args, **kwargs)
        self.b = 2
        self.c = 3
        self.d = 4


#s = second()
#s.do_something()
#print s._attrs

# below works but wtf??
class Test(object):
    def __init__(self):
        self.__dict__=OrderedDict()
        self.__dict__['a'] = 1
        self.__dict__['b'] = 2
        self.__dict__['c'] = 3


#t = Test()
#print t.__dict__
#
#print t.a
#print t.b
#print t.c

class OrderedClassMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        return OrderedDict()
    def __new__(self,name, bases, classdic):
        
class OrderedClass(object):
    __metaclass__ = OrderedClassMeta
    pass

class test2 (OrderedClass):
    def __init__(self):
        self.Header = "Hi"
        self.BoardReg = "Hey"
        self.RegAddress = "What"
        self.RegDataHigh = "Who"
        self.RegDataLow = "When"

t2 = test2()
print (t2.__dict__)

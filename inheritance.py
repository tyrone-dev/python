#!/usr/bin/env python

"""
Trying to figure out Python inheritance when
parent methods are name mangled/mangled
"""

# parent class
class Parent(object):
    def __init__(self, dev_name, ip_addr, mem_addr):
        # dict for holding info
        self.system_info = {}
        self.system_info['device_name'] = dev_name
        self.system_info['ip_addr'] = ip_addr
        self.system_info['mem_addr'] = mem_addr

    def display_info(self):
        for key in self.system_info.keys():
            if key == 'mem_addr':
                print '{} : 0x{:08X}'.format(key, self.system_info[key])
            else:
                print '{} : {}'.format(key, self.system_info[key])
    
    def reset(self):
        self.__clear_info()

    def __clear_info(self):
        self.system_info = {}

# child class
class Child(Parent):
    def __init__(self, dev_name, ip_addr, mem_addr, child_device="DaughterBoard"):
        self.child_device = child_device
        super(Child, self).__init__(dev_name, ip_addr, mem_addr)

    def display_child(self):
        print "Child device is {}".format(self.child_device)

    def reset_child(self):
        # this is how we can call obscured Parent Methods:
        self._Parent__clear_info()

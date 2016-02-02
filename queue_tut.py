#!/usr/bin/env python

# above - shebang line #! ensures that the correct interpreter is used to execute the script

# queuing and threading tut

import threading, Queue, logging, argparse, time

parser = argparse.ArgumentParser(description="Tutorial script demonstating Threading & Queues")

# basic thread class to count a number, sleep and output the number

class count_stuff(threading.Thread):

	def __init__ (self, start_num, end_num):
		self.num = start_num
		self.end = end_num
		threading.Thread.__init__(self)


	def run(self):
		while True:
			if self.num != self.end:
				self.num += 1
				print "Outputting: %i" %self.num
				time.sleep(2)

			else:
				break

myThread = count_stuff(1, 10)
myThread.start()
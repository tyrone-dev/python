#!/usr/bin/env python

# python socket programming walkthrough

import socket, time, threading, logging, Queue

def main():	
	import argparse

	global NumThreads

	# argument parser
	parser = argparse.ArgumentParser(description="Threading Tutorial, with some logging")
	# postional arguments
	parser.add_argument("Threads", help="Set the number of threads to create", type=int)
	
	#optional arguments
	parser.add_argument("-d", "--debug", dest="Debug", help="set log level to debug", action="store_true")

	args = parser.parse_args()
	NumThreads = args.Threads
	if args.Debug:

		log_level = logging.DEBUG

	else:
		log_level = logging.WARNING

	global logger

	logging.basicConfig(level=log_level, 
					format='%(asctime)s %(name)s %(levelname)s: (%(threadName)-10s) %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p'
					)

if __name__ == '__main__':
	main()	
	threader(NumThreads)

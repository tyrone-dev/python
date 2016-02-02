#!/usr/bin/env python

# threading tut

# if python interpreter is running script/module as the main program
# it sets the __name__ variable to '__main__'
# else it sets it to the module/script name

import threading, time, logging
NumThreads = 0
threads = []
NumDaemonThreads = 0
daemon_threads = []
do_event_test = False

# threading allows for parallel processing
# multiple threads can run in parallel

# define logger name for this specific module or script
# will use script name or __main__ if main script
# still use logging.basicConfig()

logger = logging.getLogger(__name__)


def main():	
	import argparse

	global NumThreads
	global NumDaemonThreads
	global do_event_test

	# argument parser
	parser = argparse.ArgumentParser(description="Threading Tutorial, with some logging")
	# postional arguments
	parser.add_argument("Threads", help="Set the number of threads to create", type=int)
	
	#optional arguments
	parser.add_argument("-d", "--debug", dest="Debug", help="set log level to debug", action="store_true")

	parser.add_argument("-a", "--addDaemon", dest="daemon", help="set the number of daemon threads to create", type=int)

	parser.add_argument("-e", "--eventTest", dest="event", help="test events to signal between threads", action="store_true")

	args = parser.parse_args()
	NumThreads = args.Threads
	if args.event: do_event_test = args.event
	if args.daemon: NumDaemonThreads = args.daemon
	if args.Debug:

		# logging allows certain messages to be displayed or written to a log file based on the LOG LEVEL
		# all messages logged with LOG LEVEL and HIGHER are processed
		# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

		# default = WARNING

		log_level = logging.DEBUG

	else:
		log_level = logging.WARNING

	global logger

	# basic config for logger
	# level - set log level
	# filename - file to write to (otherwise console)
	# format - how log messages are to be formatted

	logging.basicConfig(level=log_level, 
					format='%(asctime)s %(name)s %(levelname)s: (%(threadName)-10s) %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p'
					)

def threader(numThreads):
	global threads

	print "Number of threads is: {}".format(numThreads)
	for i in range (1, numThreads+1):
		name = "thread %s" %i
		t = threading.Thread(name=name, target=worker, args=(i,))
		threads.append(t)
		t.start() # thread starts running the moment this is executed

		#t.join()
	

def daemonThreader(numThreads):
	global daemon_threads

	# normal (non-daemon threads) are blocking to the main program: the main prog cannot exit until all threads have completed their work
	# daemon threads are non blocking - the main program does not wait for it to complete it's work before an exit

	# to mark a thread as a daemon thread use the setDaemon() method - by default this is False, so set to True
	if numThreads == 0: 
		logger.debug("No daemon threads")
		return
	else:
		print "Number of daemon threads is: {}".format(numThreads)
		for i in range(1, numThreads+1):
			name = "deamon_thread %s" %i
			dt = threading.Thread(name=name, target = daemonWorker, args=(i,))
			dt.setDaemon(True)
			daemon_threads.append(dt)
			dt.start()

			# can use join() to force block a daemon thread, join waits for a thread to complete before moving to next thread

			#dt.join()

def worker(number):
	logger.debug('Starting')
	print 'Worked: %i' %number
	time.sleep(2)
	logger.debug('Exiting')	
	return

# main program will not wait for daemonWorker to finish before exiting
def daemonWorker(number):
	logger.debug('Starting')
	print 'Worked: %i' %number
	time.sleep(5)
	logger.debug('Exiting')
	return

def waitForSignal(event):
	# this function demonstrates signalling between threads
	logger.debug("WaitForSignal starting....")
	event_is_set = event.wait()
	logger.debug("Event set?: %s" %event_is_set)


def waitForSignal2(event, timeout):
	# this function demonstrates signalling between threads

	# although a while loop, this is non blocking as it is a thread and a timeout on wait()
	while not event.isSet():
		logger.debug("WaitForSignal2 starting...")
		event_is_set = event.wait(timeout) # timeout - how long to wait before timing out and moving on
		logger.debug("Event set?: %s" %event_is_set)
		if event_is_set:
			logger.debug("Processing event now!")
		else:
			logger.debug("Event not caught, continue processing other work now")
	
	
if __name__ == '__main__':
	main()	
	threader(NumThreads)
	daemonThreader(NumDaemonThreads)
	logger.debug("Default tests done")
	
	if do_event_test:

		# create the event
		event_for_test = threading.Event()

		# create seperate threads for handling this test case
		et1 = threading.Thread(name="Block till event", target=waitForSignal, args=(event_for_test,))
		et1.start()

		et2 = threading.Thread(name="Non-Block till event", target=waitForSignal2, args=(event_for_test,2))
		et2.start()
		logger.debug("Waiting before calling event....")
		time.sleep(6)
		event_for_test.set() # call the event
		logger.debug("Event is Set!")

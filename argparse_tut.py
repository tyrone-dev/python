#!/usr/bin/env python

# above - shebang line #! ensures that the correct interpreter is used to execute the script

#argparse test

#import argparse module
import argparse

# create argument parser object
# add description when creating arg parser object
# this object holds all the information necessary to parse command line
parser = argparse.ArgumentParser(description="Test script to demonstrate argparse module")

# POSITIONAL ARGUMENTS

# positional arguments (these are required for the script to run)
# position of arguments is critical to function
# by default all arguments are parsed as strings: can set default type using type keyword
# add_argument: tells the ArgPars object how to take strings on command line and turn them into objects
# stored and used when parse_args() is called
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display the square of a given number", type=int)

# optional arguments (not required for script to run)
# position of arguments is not critical
parser.add_argument("-v", "--verbosity", help="increase output verbosity", type=int, choices=[0, 1]) # requires explicit value
# --verbosity requires an argument: either True(1) or False(0)
# when using choices specify type, and correctly represent type. i.e. don't use '1' if its an int
# to alleviate the need for this use action="store_true" - turns it into a flag (no value required)
parser.add_argument("-v2", "--verbosity2", help="increase output verbosity, no arg", action="store_true") # option is a flag, no value required

# use action count to count levels of verbosity (example)
# if optional argument is not specified, the value given is None. Can alter the default value using the default keyword
# using count only works with single char short options
parser.add_argument("-z", "--verbosity3", help="increase output verbosity", action="count", default=0)

# quiet option to perform opposite of verbose option
parser.add_argument("-q", "--quiet", help="decrease output verbosity", action="store_true")


# use add_mutually_exclusive_group() to specify options that cannot be run together
info_group = parser.add_mutually_exclusive_group()
info_group.add_argument("-a", help="test case 1", action="store_true")
info_group.add_argument("-b", help="test case 2", action="store_true")

# parse_args() returns some data about the arguments
# converts argument strings to objects and assigns them as atrributes of the namespace
args = parser.parse_args()

if args.verbosity: print "verbosity turned on"
if args.verbosity2: print "verbosity turn on, via flag"

# use verbosity to increase the amount of information displayed
# instead of changing the information displayed
if not args.quiet:
	if args.verbosity3 >= 2: print "Two levels: Extra Information: Running '{}'".format(__file__)
	if args.verbosity3 >= 1: print "One level: Usual Information"

if args.a:
	print "A"

elif args.b:
	print "B"

print args.echo
print args.square**2
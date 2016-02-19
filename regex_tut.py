#!/usr/bin/env python

# Regular Expressions (RegEx) Tutorial
""" 
Regex is a special sequence of chars that helps you match or find other strings or sets of strings, 
using specialized syntax held in a pattern 

the module to be used is re 
""" 

import re 

line = "Cats are smarter than dogs" 

# match - attempts to match RE pattern to string

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print "matchObj.group() :", matchObj.group()
    print "matchObj.group(1) :", matchObj.group(1)
    print "matchObj.group(2) :", matchObj.group(2)
else:
    print "No Match"


# search - searches for the first occurance of RE pattern within string

#TODO: finish this

#!/usr/bin/env python

# urllib tutorial

"""
urllib - module for fetching URLs (Uniform Resource Locators).

can be simple - using urlopen()

can be complex to handling additional situations: authentication, cookies, proxies etc.

supports various URL schemes i.e. ftp ftp:// - looks for tag before ://

"""

import urllib.request

with urllib.request.urlopen('http://www.pythonchallenge.com/pcc/def/linkedlist.php') as response:
    html = response.read()

print html

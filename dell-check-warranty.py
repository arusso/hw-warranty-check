#!/usr/bin/python
###############################################################################
###  @author:	Aaron Russo (arusso@library.ucr.edu)
###  @purpose: 	Given a valid dell service tag, returns the expiration date 
###############################################################################
import os
import re
import sys
from urllib import urlopen

def main(argv):
  for arg in argv:
    if validate(arg): get_warranty_info(arg)
    else: print "error: '" + arg + "' is not a valid dell service tag"
    exit

def validate(arg):
  valid = re.compile(r"[0-9a-zA-Z]{7}$")
  if valid.match(arg): return 1
  return 0

def get_warranty_info(arg):
  url="http://support.dell.com/support/topics/global.aspx/support/my_systems_info/details?ServiceTag="+arg
  text = urlopen(url).read()

  match = re.search(r'<td class="contract_oddrow">\d+/\d+/\d+</td><td class="contract_oddrow">(\d+/\d+/\d+)</td>', text)
  print match.group(1)

  return

if __name__ == "__main__":
  main(sys.argv[1:])

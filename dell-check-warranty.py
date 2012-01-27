#!/usr/bin/python
###############################################################################
###  @author:	Aaron Russo (aaron.n.russo@gmail.com)
###  @purpose: 	Given a valid dell service tag, returns the expiration date 
###############################################################################
import os
import re
import sys
from urllib import urlopen

## 
# Main Application Entrance
def main(argv):
  for arg in argv:
    if validate(arg): get_warranty_info(arg)
    else: print "error: '" + arg + "' is not a valid dell service tag"
    exit

##
# Service Tag Validation Function
#
# Currently supports the 7 digit svc tag that Dell uses
def validate(arg):
  valid = re.compile(r"[0-9a-zA-Z]{7}$")
  if valid.match(arg): return 1
  return 0

##
# Warranty retrieval function
#
# Opens the dell support url, and finds the first row in the contract table
# that containts a date.  If none is found, it returns N/A
def get_warranty_info(arg):
  # service page url to get our warranty info
  url="http://support.dell.com/support/topics/global.aspx/support/my_systems_info/details?ServiceTag="+arg
  
  # define our regexes
  re_date='\d+/\d+/\d+'
  re_class='contract_(?:odd|even)row'
  re_complete = '<td class="'+re_class+'">'+re_date+'</td><td class="'
  re_complete += re_class+'">(\d+/\d+/\d+)</td>'
  
  text = urlopen(url).read()

  # match our regex
  match = re.search(r""+re_complete,text)

  # check for match
  if match != None:
    print match.group(1) # match found, print first found
  else:
    print "N/A" # no match found
      
  return

if __name__ == "__main__":
  main(sys.argv[1:])

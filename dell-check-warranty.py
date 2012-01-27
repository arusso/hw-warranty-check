#!/usr/bin/python
###############################################################################
###  @author:	Aaron Russo (aaron.n.russo@gmail.com)
###  @purpose: 	Given a valid dell service tag, returns the expiration date 
###############################################################################
import os
import re
import sys
import argparse

from urllib import urlopen

## 
# Main Application Entrance
def main():
    parse_args()

    for tag in arg.tags:
        get_warranty_info(tag)

    exit

##
# Service Tag Validation Function
#
# Currently supports the 7 digit svc tag that Dell uses
# This function is used as a type for the argument parser, and simply calls our validate(tag) function
def valid_tag(tag):
    if validate(tag): return tag  # tag is ok
    raise argparse.ArgumentTypeError(msg) # tag is not ok
  
##
# Validates a service tag
def validate(tag):
    valid = re.compile(r"[0-9a-zA-Z]{7}$")
    if valid.match(tag): return True
    return False

##
# Parse CLI arguments
def parse_args():
    parser = argparse.ArgumentParser(description='provides warranty expiration dates, given a valid Dell service tag')
    parser.add_argument('tags',metavar='SVCTAG',type=valid_tag)

    # finish parser here

    return parser.parse_args()


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

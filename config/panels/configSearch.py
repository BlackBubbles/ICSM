#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 07/15/2017
Last Updated: 07/15/2017
Version: 0.0.1
Description:
    The following python module contains the configuration data for the
    "Search" panel
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
'''
The following variable contains the alternative browsing label for the
panel browse button
'''
SEARCH_BROWSE_LABEL = "Browse for Directory ..."

'''
The following variable contains the title for the "Search" Panel
'''
TITLE = "Search for Worksheet"

'''
The following function returns a confirmation that tells the calling code
which configuration file this function belongs to
'''
def confirm(value):
  
  # Check to make sure that the inputted value is a string that is equal
  # to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "search":
      return True
    else:
      return False
  else:
    return False

#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/08/2017
Last Updated: 08/08/2017
Version: 1.0.0
Description:
    The following python file contains the configuration data for the "Lab" panel
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
'''
The following variable contains the title for the "Lab" Panel
'''
TITLE = "Lab Anaylsis"

'''
The following function returns a confirmation that tells the calling code which configuration file this function
belongs to
'''
def confirm(value):

  # Check to make sure that the inputted value is a string that is equal to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "lab":
      return True
    else:
      return False
  else:
    return False
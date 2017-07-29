#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 07/15/2017
Last Updated: 07/15/2017
Version: 0.0.1
Description:
    The following python module contains the configuration data for the
    "Quick Access" panel
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
'''
The following variable contains the number of columns of buttons for the
"Quick Access" Panel
'''
NUM_OF_COLUMNS_OF_BUTTONS = 2

'''
The following variable contains the number of rows of buttons for the
"Quick Access" Panel
'''
NUM_OF_ROWS_OF_BUTTONS = 2

'''
The following variable contains the height of each button on the
"Quick Access" Panel
'''
QA_BUTTON_HEIGHT = 20

'''
The following variable contains the width of each button on the
"Quick Access" Panel
'''
QA_BUTTON_WIDTH = 20

'''
The following function returns a confirmation that tells the calling code
which configuration file this function belongs to
'''
def confirm(value):
  
  # Check to make sure that the inputted value is a string that is equal
  # to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "qa":
      return True
    else:
      return False
  else:
    return False

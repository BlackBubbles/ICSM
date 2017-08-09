#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/21/2017
Last Updated: 08/09/2017
Version: 1.0.0
Description:
    The following python file contains the testing functions used to test the ICSM program
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"
COLOR_RANGE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
               "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]

'''
The following function tests to make sure that the inputted dictionary contains all arrays of strings
'''
def testConfigDicString(dictionary, string):
  if not isinstance(dictionary, dict):
    message = "%s:\n%s is not an dictionary" % (ERROR, string)
    return False, message
  for key, array in dictionary.iteritems():
    secString = string + ":" + key
    doesWork, message = testConfigListString(array, secString)
    if not doesWork:
      return doesWork, message
  return True, ""
  
'''
The following function tests to make sure that the inputted array contains all strings
'''
def testConfigListString(array, string):
  if not isinstance(array, list):
    message = "%s:\n%s is not an array" % (ERROR, string)
    return False, message
  for value in array:
    if not isinstance(value, basestring):
      message = "%s:\n%s " % (ERROR, string) + "contains a value that is not a string"
      return False, message
  return True, ""
  
'''
The following function tests to make sure that the inputted array contains all positive integer numbers
'''
def testConfigListPosInt(array, length, string):
  if not isinstance(array, list):
    message = "%s:\n%s is not an array" % (ERROR, string)
    return False, message
  if not len(array) == length:
    message = "%s:\n%s is not the correct length" % (ERROR, string)
    return False, message
  for value in array:
    if not isinstance(value, int):
      message = "%s:\n%s " % (ERROR, string) + "contains a value that is not an integer value"
      return False, message
    if not value >= 0:
      message = "%s:\n%s " % (ERROR, string) + "contains a value that is not a positive integer value"
      return False, message
  return True, ""
  
'''
The following function tests to make sure that the inputted value is a string that can be used on a color scheme
'''
def testConfigColors(value, string):
  if not isinstance(value, basestring):
    message = "%s:\n%s is not a string value" % (ERROR, string)
    return False, message
  if not value[:1] is "#":
    message = "%s:\n%s first value is not \"#\"" % (ERROR, string)
    return False, message
  if not len(value) == 7:
    message = "%s:\n%s is not the correct length" % (ERROR, string)
    return False, message
  for part in value[1:]:
    if not any(part in s for s in COLOR_RANGE):
      message = "%s:\n%s values must be in hex range" % (ERROR, string)
      return False, message
  return True, ""
  
'''
The following function tests to make sure that the inputted value is a positive integer value above 0
'''
def testConfigPosInt(num, string):
  if not isinstance(num, int):
    message = "%s:\n%s is not a integer value" % (ERROR, string)
    return False, message
  if not num > 0:
    message = "%s:\n%s is not a positive integer value" % (ERROR, string)
    return False, message
  return True, ""
  
'''
The following function tests to make sure that the inputted value is a string
'''
def testConfigString(value, string):
  if not isinstance(value, basestring):
    message = "%s:\n%s is not a string value" % (ERROR, string)
    return False, message
  return True, ""
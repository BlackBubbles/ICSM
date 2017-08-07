#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/05/2017
Last Updated: 08/07/2017
Version: 1.0.0
Description:
    The following python file contains the code that tests the Model to make sure that nothing is initially wrong
'''

'''
Imported files/libraries
'''
from types import ModuleType

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
function that tests out to make sure that nothing is wrong with the "configData.py" file
'''
def __testConfig(testF, config):
  return True, ""

'''
Initial test function for the Model that calls all the private functions within this file
'''
def test(testF, config):
  
  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Data"):
        return False, "%s:\nconfig file for Data is not configData" % ERROR
    else:
      return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
  else:
    return False, "%s:\ninputted file is not a Module" % ERROR
    
  # Call the "__testConfig" function to test the config file
  doesWork = False
  message = ""
  doesWork, message = __testConfig(testF, config)
  
  # Return the value that determines wheather or not the test worked
  return doesWork, message
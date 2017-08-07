#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 07/15/2017
Last Updated: 08/07/2017
Version: 1.0.0
Description:
    The following python file contains the code that tests the GUI's panel "Search" to make sure that nothing is
    initially wrong
'''

'''
Imported config files
'''
from types import ModuleType

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
the following function that tests out to make sure that nothing is wrong with the "configSearch.py" file
'''
def __testConfig(testF, config):
  
  # Set up return variables
  doesWork = False
  message = ""
  
  # Test config.SEARCH_BROWSE_LABEL
  doesWork, message = testF.testConfigString(config.SEARCH_BROWSE_LABEL, "configQuickAccess.SEARCH_BROWSE_LABEL")
  if not doesWork:
    return doesWork, message
    
  # Test config.TITLE
  doesWork, message = testF.testConfigString(config.TITLE, "configQuickAccess.TITLE")
  if not doesWork:
    return doesWork, message
    
  # If there are no problems found with the config file for the GUI panel, then return the proper values
  return True, ""
  
'''
Initial test function for the GUI's panel "Search" that calls all the private functions within this file
'''
def test(testF, config):
  
  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Search"):
        return False, "%s:\nconfig file for GUI panel \"Search\" is not configSearch" % ERROR
    else:
      return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
  else:
    return False, "%s:\ninputted file is not a Module" % ERROR
    
  # Call the "__testConfig" function to test the config file
  doesWork = False
  message = ""
  doesWork, message = __testConfig(testF, config)
  
  # If there are no problems found with the config file for the GUI, then return the proper values
  return doesWork, message
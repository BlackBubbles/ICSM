#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 07/15/2017
Last Updated: 08/07/2017
Version: 1.0.0
Description:
    The following python file contains the code that tests the GUI's panel "Quick Access" to make sure that nothing is
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
the following function that tests out to make sure that nothing is wrong with the "configQuickAccess.py" file
'''
def __testConfig(testF, config):
  
  # Set up return variables
  doesWork = False
  message = ""
  
  # Test config.NUM_OF_COLUMNS_OF_BUTTONS
  doesWork, message = testF.testConfigPosInt(config.NUM_OF_COLUMNS_OF_BUTTONS,
                                             "configQuickAccess.NUM_OF_COLUMNS_OF_BUTTONS")
  if not doesWork:
    return doesWork, message
    
  # Test config.NUM_OF_ROWS_OF_BUTTONS
  doesWork, message = testF.testConfigPosInt(config.NUM_OF_ROWS_OF_BUTTONS, "configQuickAccess.NUM_OF_ROWS_OF_BUTTONS")
  if not doesWork:
    return doesWork, message
    
  # Test config.QA_BUTTON_HEIGHT
  doesWork, message = testF.testConfigPosInt(config.QA_BUTTON_HEIGHT, "configQuickAccess.QA_BUTTON_HEIGHT")
  if not doesWork:
    return doesWork, message
    
  # Test config.QA_BUTTON_WIDTH
  doesWork, message = testF.testConfigPosInt(config.QA_BUTTON_WIDTH, "configQuickAccess.QA_BUTTON_WIDTH")
  if not doesWork:
    return doesWork, message
    
  # If there are no problems found with the config file for the GUI panel, then return the proper values
  return True, ""
  
'''
Initial test function for the GUI's panel "Quick Access" that calls all the private functions within this file
'''
def test(testF, config):
  
  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, 'confirm'):
      if not config.confirm('QA'):
        return False, "%s:\nconfig file for GUI panel \"Quick Access\" is not configQuickAccess" % ERROR
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
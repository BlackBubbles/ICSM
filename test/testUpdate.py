#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/21/2017
Last Updated: 08/07/2017
Version: 1.0.0
Description:
    The following python file contains the code that tests the GUI's panel "Update" to make sure that nothing is
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
the following function that tests out to make sure that nothing is wrong with the "configUpdate.py" file
'''
def __testConfig(testF, config):
  
  # Set up return variables
  doesWork = False
  message = ""
  
  # Test config.EXTRUDERS
  doesWork, message = testF.testConfigListString(config.EXTRUDERS, "configQuickAccess.EXTRUDERS")
  if not doesWork:
    return doesWork, message
    
  # Test config.EXTRUDER_DIES
  doesWork, message = testF.testConfigDicString(config.EXTRUDER_DIES, "configQuickAccess.EXTRUDER_DIES")
  if not doesWork:
    return doesWork, message
    
  # Test config.FEEDERS
  doesWork, message = testF.testConfigListString(config.FEEDERS, "configQuickAccess.FEEDERS")
  if not doesWork:
    return doesWork, message
    
  # Test config.FEEDER_SCREWS
  doesWork, message = testF.testConfigDicString(config.FEEDER_SCREWS, "configQuickAccess.FEEDER_SCREWS")
  if not doesWork:
    return doesWork, message
    
  # Test config.FEEDER_TUBES
  doesWork, message = testF.testConfigDicString(config.FEEDER_TUBES, "configQuickAccess.FEEDER_TUBES")
  if not doesWork:
    return doesWork, message
    
  # Test config.NUM
  doesWork, message = testF.testConfigListPosInt(config.NUM, 5, "configQuickAccess.NUM")
  if not doesWork:
    return doesWork, message
    
  # Test config.PELLETIZING
  doesWork, message = testF.testConfigListString(config.PELLETIZING, "configQuickAccess.PELLETIZING")
  if not doesWork:
    return doesWork, message
    
  # Test config.PORT_OPTIONS
  doesWork, message = testF.testConfigListString(config.PORT_OPTIONS, "configQuickAccess.PORT_OPTIONS")
  if not doesWork:
    return doesWork, message

  # Test config.PORT_OPTIONS_11MM
  doesWork, message = testF.testConfigListString(config.PORT_OPTIONS_11MM, "configQuickAccess.PORT_OPTIONS_11MM")
  if not doesWork:
    return doesWork, message

  # Test config.PRE_DIE
  doesWork, message = testF.testConfigListString(config.PRE_DIE, "configQuickAccess.PRE_DIE")
  if not doesWork:
    return doesWork, message
    
  # Test config.SIDE_STUFFER
  doesWork, message = testF.testConfigListString(config.SIDE_STUFFER, "configQuickAccess.SIDE_STUFFER")
  if not doesWork:
    return doesWork, message

  # Test config.SIDE_STUFFER_WITHOUT_VACCUM
  doesWork, message = testF.testConfigListString(config.SIDE_STUFFER_WITHOUT_VACCUM,
                                                 "configQuickAccess.SIDE_STUFFER_WITHOUT_VACCUM")
  if not doesWork:
    return doesWork, message

  # Test config.TITLE
  doesWork, message = testF.testConfigString(config.TITLE, "configQuickAccess.TITLE")
  if not doesWork:
    return doesWork, message
    
  # If there are no problems found with the config file for the GUI panel, then return the proper values
  return True, ""
  
'''
Initial test function for the GUI's panel "Update" that calls all the private functions within this file
'''
def test(testF, config):
  
  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Update"):
        return False, "%s:\nconfig file for GUI panel \"Update\" is not configUpdate" % ERROR
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
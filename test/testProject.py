#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 07/15/2017
Last Updated: 08/08/2017
Version: 1.0.0
Description:
    The following python file tests the code for the "Project" panel
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
function that tests out to make sure that nothing is wrong with the "configProject.py" file
'''
def __testConfig(testF, config):
  return True, ""

'''
Initial test function that calls all the private functions within this function
'''
def test(testF, config):

  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Project"):
        return False, "%s:\nconfig file for Project is not configProject" % ERROR
    else:
      return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
  else:
    return False, "%s:\ninputted file is not a Module" % ERROR

  # Call the "__testConfig" function to test the config file
  doesWork, message = __testConfig(testF, config)

  # Return the value that determines wheather or not the test worked
  return doesWork, message
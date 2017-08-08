#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/07/2017
Last Updated: 08/08/2017
Version: 1.0.0
Description:
    The following python file contains the model code functions for the "Quick Access" panel for the ICSM program
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the model for the "Quick Access" panel
'''
class QAD:

  '''
  The following function is the initial instance creation function for the "QAD" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "QAD" class
    self.default = 0

  '''
  The following function returns the configuration file for this instance of the "QAD" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for this instance of the class. If the inputted config file does
  not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("QA"):
          self.config = config
        else:
          return False, "%s:\nconfig file for QAD is not configQuickAccess" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "qa":
        return True
      else:
        return False
    else:
      return False
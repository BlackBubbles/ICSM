#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 03/05/2017
Last Updated: 06/03/2017
Version: 0.0.1
Description:
    The following python file contains multiple interaction functions for
    the model of the program
'''

'''
imported files/libraries
'''
import sys
from types import ModuleType

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the Model for the MVC for the IISM program
'''
class Data:
  
  '''
  The following function is the initial instance creation function for
  the "Data" class
  '''
  def __init__(self, config):
    
    # Call set functions and is the return is False, then return the
    # message for the error
    doesWork = True
    message = ""
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()
      
    # Initial function does not require an instance of an Actions class
    self.actions = None
    
  '''
  The following function returns the configuration file for the "Data"
  class
  '''
  def getConfig(self):
    return self.config
  
  '''
  The following function sets the configuration file for the "Data"
  class. If the inputted config file does not meet the requirements
  then the function returns a False and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, 'confirm'):
        if config.confirm("Data"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Data is not configData"\
                         % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file"\
                       + " for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""
      
  '''
  The following function returns the instance of the "Action" class for
  the "Data" class
  '''
  def getActions(self):
    return self.actions
    
  '''
  The following function sets the instance of the "Action" class for the 
  "Data" class. If the inputted Actions class file does not meet the
  requirements then the function returns a False and an error message
  '''
  def setActions(self, first, actions):
    
    # Create the initial return variables and their values
    doesWork = True
    message = ""
    
    # Check to make sure that the inputted value is an instance of the
    # "Actions" class
    if hasattr(actions, 'confirm'):
      if actions.confirm("Actions"):
        self.actions = actions
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a Actions class"\
                  " file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class"\
                " file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message
      
  '''
  The following function returns a confirmation that tells the calling 
  code which class file this function belongs to
  '''
  def confirm(self, value):
    
    # Check to make sure that the inputted value is a string that is equal
    # to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "data":
        return True
      else:
        return False
    else:
      return False

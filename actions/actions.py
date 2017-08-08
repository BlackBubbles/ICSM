#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/16/2017
Last Updated: 08/08/2017
Version: 1.0.0
Description:
    The following python file contains multiple interaction functions for the Controller for the ICSM program
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import frameActions as frameA
from add import feederActions as feederA
from add import TDIActions as TDIA
from panels import quickAccessActions as qaA
from panels import extruderActions as extruderA
from panels import labActions as labA
from panels import projectActions as projectA

from panels import updateActions as updateA
from panels import searchActions as searchA

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the Controller for the MVC for the ICSM program
'''
class Actions:
  
  '''
  The following function is the initial instance creation function for
  the "Actions" class
  '''
  def __init__(self, config):
    
    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()
      
    # Set the rest of the initial "Actions" class variables
    self.data = None
    self.graphics = None
    
  '''
  The following function returns the configuration file for this instance of the "Actions" class
  '''
  def getConfig(self):
    return self.config
    
  '''
  The following function sets the configuration file for the "Actions" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Actions"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Actions is not configActions" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""
          
  '''
  The following function returns the instance of the "Data" class for the "Actions" class
  '''
  def getData(self):
    return self.data
    
  '''
  The following function sets the instance of the "Data" class for the "Actions" class. If the inputted Data class file
  does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, first, data):
    
    # Create the initial return variables and their values
    doesWork = True
    message = ""
    
    # Check to make sure that the inputted value is an instance of the
    # "Data" class
    if hasattr(data, "confirm"):
      if data.confirm("Data"):
        self.data = data
      else:
        doesWork = False
        message = "%s:\ninputted file for Actions is not a Data class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Data class file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message
      
  '''
  The following function returns the instance of the "Graphics" class for this instance of the "Actions" class
  '''
  def getGraphics(self):
    return self.graphics
    
  '''
  The following function sets the instance of the "Graphics" class for this instance of the "Actions" class. If the
  inputted Graphics class file does not meet the requirements then the function returns a "False" boolean value and an
  error message
  '''
  def setGraphics(self, first, graphics):
    
    # Create the initial return variables and their values
    doesWork = True
    message = ""
    
    # Check to make sure that the inputted parameter is an instance of a
    # "Graphics" class
    if hasattr(graphics, "confirm"):
      if graphics.confirm("Graphics"):
        self.graphics = graphics
      else:
        doesWork = False
        message = "%s:\ninputted file for Actions is not a Graphics class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Graphics class file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message
      
  '''
  The following function returns the "frameActions" module
  '''
  def getFrameActions(self):
    return frameA

  '''
  The following function returns the "feederActions" module
  '''
  def getFeederActions(self):
    return feederA

  '''
  The following function returns the "TDIActions" module
  '''
  def getTDIActions(self):
    return TDIA
    
  '''
  The following function returns the "quickAccessActions" module
  '''
  def getQuickAccessActions(self):
    return qaA

  '''
    The following function returns the "feederActions" module
    '''

  def getExtruderActions(self):
    return extruderA

  '''
  The following function returns the "TDIActions" module
  '''

  def getLabActions(self):
    return labA

  '''
  The following function returns the "quickAccessActions" module
  '''

  def getProjectActions(self):
    return projectA

  '''
  REMOVE SOON
  '''
  def getUpdateActions(self):
    return updateA
    
  '''
  REMOVE SOON
  '''
  def getSearchActions(self):
    return searchA
    
  '''
  The following function call the "exit" function which ends the mainloop of the main GUI
  '''
  def exit(self):
    self.getGraphics().getGUI().destroy()
    
  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    
    # Check to make sure that the inputted value is a string that is equal to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "actions":
        return True
      else:
        return False
    else:
      return False
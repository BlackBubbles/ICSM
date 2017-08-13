#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/07/2017
Last Updated: 08/11/2017
Version: 1.0.0
Description:
    The following python file contains the model code functions for the "Extruder" panel for the ICSM program
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
The following class is the model for the "Extruder" panel
'''
class ExtruderD:

  '''
  The following function is the initial instance creation function for the "ExtruderD" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "ExtruderD" class
    self.workflowFileName = None
    self.classifiedVariable = None

  '''
  The following function returns the configuration file for this instance of the "ExtruderD" class
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
        if config.confirm("Extruder"):
          self.config = config
        else:
          return False, "%s:\nconfig file for ExtruderD is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the file name of the workflow sheet that is currently being selected within the 
  "Extruder" panel
  '''
  def getWorkflowFileName(self):
    return self.workflowFileName

  '''
  The following function sets the file name of the workflow sheet that is currently being selected within the 
  "Extruder" panel.
  '''
  def setWorkflowFileName(self, workflowFileName):
    self.workflowFileName = workflowFileName

  '''
  The following function returns the variable for the classified radio buttons
  '''
  def getClassifiedVariable(self):
    return self.classifiedVariable

  '''
  The following function sets the variable for the classified radio buttons.
  '''
  def setClassifiedVariable(self, classifiedVariable):
    self.classifiedVariable = classifiedVariable
    return True, ""

  '''
  The following function checks the data to see if the data is ready to update the workflow .xlsx sheet
  '''
  def checkForUpdate(self):

    # Build the initial error variables and values
    ready = True
    errors = []
    errorTextLabels = []

    # Check the classified variable
    if self.getClassifiedVariable().get() is 0:
      ready = False
      errors.append("Choose a \"Classified\" option")
      errorTextLabels.append("Classified:")

    # Return the error variables
    return ready, errors, errorTextLabels

  '''
  The following function updates the workflow .xlsx sheets
  '''
  def updateWorkflow(self):
    print "updateWorkflow"

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "extruder":
        return True
      else:
        return False
    else:
      return False
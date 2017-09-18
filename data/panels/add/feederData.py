#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/16/2017
Last Updated: 08/16/2017
Version: 1.0.0
Description:
    The following python file contains the model function for the GUI that respond to events from the user
    interacting with the GUI for the Feeder configurations
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
The following class is the model code for the feeder GUI
'''
class FeederD:

  '''
  The following function is the initial function for the "FeederD" class
  '''
  def __init__(self, config, total):

    # Set and check the inputted config
    doesWork, message = self.setConfig(config)
    if not doesWork:
        print message
        sys.exit()

    # Create the initial variables for this instance of the class
    self.actions = None
    self.graphics = None
    self.feederVariable = None
    self.feederTubeVariable = None
    self.feederScrewVariable = None
    self.locationVariable = None
    self.setPointVariable = None
    self.RMList = {}
    self.completePercentage = total
    self.totalPercentage = 0.0

  '''
  The following function returns the configuration file for this instance of the "FeederD" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for the "FeederD" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Extruder"):
          self.config = config
        else:
          return False, "%s:\nconfig file for FeederD is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the instance of the "FeederA" class for this instance of the "FeederD" class
  '''
  def getActions(self):
    return self.actions

  '''
  The following function sets the instance of the "FeederA" class for the "FeederD" class. If the inputted Actions
  class file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setActions(self, actions):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "FeederA" class
    if hasattr(actions, "confirm"):
      if actions.confirm("Feeder"):
        self.actions = actions
      else:
        doesWork = False
        message = "%s:\ninputted file for FeederD is not a FeederA class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR

    # Return the initial variable
    return doesWork, message

  '''
  The following function returns the instance of the "FeederG" class for this instance of the "FeederD" class
  '''
  def getGraphics(self):
    return self.graphics

  '''
  The following function sets the instance of the "FeederG" class for the "FeederD" class. If the inputted Graphics
  class file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setGraphics(self, graphics):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "FeederG" class
    if hasattr(graphics, "confirm"):
      if graphics.confirm("Feeder"):
        self.graphics = graphics
      else:
        doesWork = False
        message = "%s:\ninputted file for FeederD is not a FeederG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR

    # Return the initial variable
    return doesWork, message

  '''
  The following function returns the feeder variable
  '''
  def getFeederVariable(self):
    return self.feederVariable

  '''
  The following function sets the feeder variable
  '''
  def setFeederVariable(self, feederVariable):
    self.feederVariable = feederVariable

  '''
  The following function returns the feeder tube variable
  '''
  def getFeederTubeVariable(self):
      return self.feederTubeVariable

  '''
  The following function sets the feeder tube variable
  '''
  def setFeederTubeVariable(self, feederTubeVariable):
      self.feederTubeVariable = feederTubeVariable

  '''
  The following function returns the feeder screw variable
  '''
  def getFeederScrewVariable(self):
      return self.feederScrewVariable

  '''
  The following function sets the feeder screw variable
  '''
  def setFeederScrewVariable(self, feederScrewVariable):
      self.feederScrewVariable = feederScrewVariable

  '''
  The following function returns the location variable
  '''
  def getLocationVariable(self):
      return self.locationVariable

  '''
  The following function sets the location variable
  '''
  def setLocationVariable(self, locationVariable):
      self.locationVariable = locationVariable

  '''
  The following function returns the set point variable
  '''
  def getSetPointVariable(self):
      return self.setPointVariable

  '''
  The following function sets the set point variable
  '''
  def setSetPointVariable(self, setPointVariable):
      self.setPointVariable = setPointVariable

  '''
  The following function returns the RM Code list
  '''
  def getRMList(self):
      return self.RMList

  '''
  The following function sets the RM Code list
  '''
  def setRMList(self, RMList):
      self.RMList = RMList

  '''
  The following function returns the percentage used so far by the other feeders
  '''
  def getCompletePercentage(self):
    return self.completePercentage

  def setCompletePercentage(self, completePercentage):
    self.completePercentage = completePercentage

  '''
  The following function returns the total percentage of all the RM codes in the list
  '''
  def getTotalPercentage(self):
      return self.totalPercentage

  '''
  The following function sets the total percentage of all the RM codes in the list
  '''
  def setTotalPercentage(self, totalPercentage):
      self.totalPercentage = totalPercentage

  '''
  The following function checks the content of the data to see if the content is ready to apply
  '''
  def checkForApply(self):

    # Build the initial error variables and values
    ready = True
    errors = []
    errorTextLabels = {}

    # Check the feeder section
    errorTextLabels[self.getConfig().FEEDER_OPTIONS_TITLE] = []
    labels = errorTextLabels[self.getConfig().FEEDER_OPTIONS_TITLE]

    # Check the feeder drop down menu
    if self.getFeederVariable().get() == self.getConfig().FEEDERS[0]:
      ready = False
      errors.append("Choose a \"Feeder\"\n")
      labels.append("Feeder")
    else:

      # Check the tube drop down menu
      if not self.getFeederVariable().get() == self.getConfig().FEEDERS[1] and \
          not self.getFeederVariable().get() == self.getConfig().FEEDERS[3]:
        if self.getFeederTubeVariable().get() == self.getConfig().FEEDER_TUBES[self.getFeederVariable().get()][0]:
          ready = False
          errors.append("Choose a \"Tube\" for the Feeder\n")
          labels.append("Tube")

      # Check the screw drop down menu
      if self.getFeederScrewVariable().get() == self.getConfig().FEEDER_SCREWS[self.getFeederVariable().get()][0]:
        ready = False
        errors.append("Choose a \"Screw\" for the Feeder\n")
        labels.append("Screw")

    # Check the location/measurement section
    errorTextLabels[self.getConfig().RADIO_BUTTON_TITLE] = []
    labels = errorTextLabels[self.getConfig().RADIO_BUTTON_TITLE]

    # Check the "Location" radio buttons
    if self.getLocationVariable().get() is 0:
      ready = False
      errors.append("Choose a \"Location\" for the Feeder\n")
      labels.append("Location:")

    # Check the RM Code section
    errorTextLabels[self.getConfig().RM_TITLE] = []
    labels = errorTextLabels[self.getConfig().RM_TITLE]

    # Check RM list length
    if len(self.getRMList()) is 0:
      ready = False
      errors.append("Feeder requires at least one \"RM Code\"\n")
      labels.append("")

    # Return the error variables
    return ready, errors, errorTextLabels

  '''
  The following function converts the entire class data into a dictionary
  '''
  def toDictionary(self):

    # Build the initial return variable
    dictionary = {}

    # Add the Feeder Data
    dictionary["Feeder"] = self.getFeederVariable().get()
    if not self.getFeederVariable().get() == self.getConfig().FEEDERS[1] and \
                    not self.getFeederVariable().get() == self.getConfig().FEEDERS[3]:
      dictionary["Tube"] = self.getFeederTubeVariable().get()
    dictionary["Screw"] = self.getFeederScrewVariable().get()

    # Add the Location/Measurment Data
    dictionary["Location"] = self.getLocationVariable().get()

    # Add the RM Code Data
    dictionary["RM"] = self.getRMList()
    dictionary["Total"] = self.getTotalPercentage()

    # Return the initial return variable
    return dictionary

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
      if isinstance(value, basestring):
          if value.lower() == "feeder":
              return True
          else:
              return False
      else:
          return False
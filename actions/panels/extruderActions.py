#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 08/11/2017
Version: 1.0.0
Description:
    The following python file contains the reaction functions for the "Extruder" panel for the GUI in the ICSM program
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import Tkinter as tk

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the controller for the "Extruder" panel
'''
class ExtruderA:

  '''
  The following function is the initial instance creation function for the "ExtruderA" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "ExtruderA" class
    self.data = None
    self.graphics = None

  '''
  The following function returns the configuration file for this instance of the "ExtruderA" class
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
          return False, "%s:\nconfig file for ExtruderA is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the model for this instance of the "Extruder" panel
  '''
  def getData(self):
    return self.data

  '''
  The following function sets the model for this instance of the "Extruder" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, data):
    if hasattr(data, "confirm"):
      if data.confirm("Extruder"):
        self.data = data
      else:
        return False, "%s:\ndata for ExtruderA is not extruderData" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function returns the view for this instance of the "Extruder" panel
  '''
  def getGraphics(self):
    return self.graphics

  '''
  The following function sets the view for this instance of the "Extruder" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setGraphics(self, graphics):
    if hasattr(graphics, "confirm"):
      if graphics.confirm("Extruder"):
        self.graphics = graphics
      else:
        return False, "%s:\ndata for ExtruderA is not extruderGraphics" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function calls the "" function in the Graphics to allow the user to add a feeder to the "Extruder"
  panel
  '''
  def addFeeder(self):
    print "addFeeder"

  '''
  The following function calls the "browseServer" function in the Graphics to allow the user to browse for a file
  '''
  def callBrowseServer(self, graphics, title, label):
    filename = graphics.getBrowseServerGraphics().browseServer(graphics, title, label)
    graphics.getData().getExtruderData().setWorkflowFileName(filename)

  '''
  The following function calls the "" function in the Graphics to allow the user to add a feeder to the Ex
  '''
  def changeCooling(self, graphics, value):
    print "changeCooling - ", value

  '''
  The following function calls the "" function in the Graphics to repsond to the user selecting an option from the
  "Pelletizier" drop down menu
  '''
  def changePellet(self, variable):
    print "changePellet - ", variable.get()

  '''
  The following function responds to the user selecting a radio button from the "Classified:" list and 
  '''
  def checkLabel(self, input):

    # Check to see if the label is red. If so change it back to the original color
    if not isinstance(input, tk.IntVar):
      section = input[0]
      label = input[1]
      if isinstance(label, tk.Label):
        if label["foreground"] == self.getConfig().ERROR_COLOR:
          print label
        else:
          print "hello"

  '''
  The following function responds to the user clicking on the large "Update Workflow" button on the bottom of the GUI
  '''
  def checkForUpdate(self):

    # Check the data to see if all the information is there
    ready, errors, errorTextLabels = self.getData().checkForUpdate()
    if ready:
      self.getData().updateWorkflow()
    else:
      self.getGraphics().displayUpdateError(errors, errorTextLabels)

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
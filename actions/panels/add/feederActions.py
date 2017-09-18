#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 08/16/2017
Version: 1.0.0
Description:
    The following python file contains the controller actions for the GUI that respond to events from the user
    interacting with the GUI for the Feeder configurations
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import Tkinter as tk
import tkMessageBox

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the controller code for the feeder GUI
'''
class FeederA:

  '''
  The following function is the initial function for the "FeederA" class
  '''
  def __init__(self, config, respond):

    # Set and check the inputted config
    doesWork, message = self.setConfig(config)
    if not doesWork:
        print message
        sys.exit()

    # Create the initial variables for this instance of the class
    self.data = None
    self.graphics = None
    self.respond = respond

  '''
  The following function returns the configuration file for this instance of the "FeederA" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for the "FeederA" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Extruder"):
          self.config = config
        else:
          return False, "%s:\nconfig file for FeederA is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the instance of the "FeederD" class for this instance of the "FeederA" class
  '''
  def getData(self):
      return self.data

  '''
  The following function sets the instance of the "FeederD" class for the "FeederA" class. If the inputted Data
  class file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, data):

      # Create the initial return variables and their values
      doesWork = True
      message = ""

      # Check to make sure that the inputted value is an instance of the "FeederD" class
      if hasattr(data, "confirm"):
          if data.confirm("Feeder"):
              self.data = data
          else:
              doesWork = False
              message = "%s:\ninputted file for FeederA is not a FeederD class file" % ERROR
      else:
          doesWork = False
          message = "%s:\ninputted file is not a designated Data class file for this program" % ERROR

      # Return the initial variable
      return doesWork, message

  '''
  The following function returns the instance of the "FeederG" class for this instance of the "FeederA" class
  '''
  def getGraphics(self):
      return self.graphics

  '''
  The following function sets the instance of the "FeederG" class for the "FeederA" class. If the inputted Graphics
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
              message = "%s:\ninputted file for FeederA is not a FeederG class file" % ERROR
      else:
          doesWork = False
          message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR

      # Return the initial variable
      return doesWork, message

  '''
  The following function responds to the user selecting a feeder option from the feeders drop down menu
  '''
  def respondToFeeder(self, section, label):

    # Check the label and section header
    self.checkLabel([section, label])

    # Change the values within the tube and screw menus
    self.getGraphics().changeFeeder()

  '''
  The following function responds to the user selecting something from the tube menu
  '''
  def respondToTube(self, section, label, value):
    self.getData().getFeederTubeVariable().set(value)
    self.respondToMenu(section, label)

  '''
  The following function responds to the user selecting something from the screw menu
  '''
  def respondToScrew(self, section, label, value):
    self.getData().getFeederScrewVariable().set(value)
    self.respondToMenu(section, label)

  def _is_rm(self, rm):
      if len(rm.split('-')) is 3:
          return False
      elif len(rm.split('-')) is 2:
          try:
              if int(rm.split('-')[0]) > 99999 or int(rm.split('-')[0]) < 1000:
                  return False
          except ValueError:
              return False
      else:
          if rm.lower()[-1] is 'x':
              rm = rm[:-1]
              if len(rm) is 5:
                  return False
          else:
              if len(rm) is 3:
                  return False
          try:
              if int(rm.split('-')[0]) > 99999 or int(rm.split('-')[0]) < 100:
                  return False
          except ValueError:
              return False
      return True

  '''
  The following function responds to the user clicking on the "Add" button to add an RM Code slot
  '''
  def respondToAdd(self, section):

    # Get both the values of the Entries
    RM = self.getGraphics().getRMCodeEntry().get()
    Percent = self.getGraphics().getRMPercentEntry().get()

    # Check the contents of the values
    if not RM or RM.isspace() or not Percent or Percent.isspace():
      return 0
    try:
      float(Percent)
    except ValueError:
      return 0
    if (self.getData().getTotalPercentage() + self.getData().getCompletePercentage() + float(Percent)) > 100.0:
      tkMessageBox.showerror("ERROR", "Total Percentage is Over 100.0")
    elif RM in self.getData().getRMList():
      tkMessageBox.showerror("ERROR", "RM is Already in Use")
    elif not self._is_rm(RM):
      tkMessageBox.showerror("ERROR", "Invalid RM Entry")
    else:

      # Remove original contents from Entries
      self.getGraphics().getRMCodeEntry().delete(0, "end")
      self.getGraphics().getRMPercentEntry().delete(0, "end")

      # Check the section header label
      self.getGraphics().checkSectionLabels(section)

      # Add the RM code slot to the list
      self.getData().setTotalPercentage(self.getData().getTotalPercentage() + float(Percent))
      self.getGraphics().getRMPercentEntry().insert(
          0, str(100.0 - (self.getData().getCompletePercentage() + self.getData().getTotalPercentage())))
      self.getData().getRMList()[RM] = float(Percent)
      self.getGraphics().addRM(RM, Percent)

  '''
  The following function repsonds to the user clicking on the "Delete" button alongside an RM Code slot
  '''
  def respondToDelete(self, frame, RM, Percent):

    # Subtract from total percentage
    self.getData().setTotalPercentage(self.getData().getTotalPercentage() - float(Percent))

    # Delete item in RMList
    del self.getData().getRMList()[RM]

    # Resize the RM Frame
    if len(self.getData().getRMList()) is 0:
      self.getGraphics().getRMFrame().configure(height=1)

    # Destroy the frame
    frame.destroy()

    # Reset the RM Percent entry
    self.getGraphics().getRMPercentEntry().delete(0, "end")
    self.getGraphics().getRMPercentEntry().insert(
        0, str(100.0 - (self.getData().getCompletePercentage() + self.getData().getTotalPercentage())))

  '''
  The following function responds to the user selection an option from the default drop down menu
  '''
  def respondToMenu(self, section, label):
    self.checkLabel([section, label])

  '''
  The following function responds to the user selection an option from the default radio buttons
  '''
  def respondToRadio(self, input):
    self.checkLabel(input)

  '''
  The following function checks the label of an item to make sure that the label isn't red
  '''
  def checkLabel(self, input):
    if not isinstance(input, tk.IntVar):
      section = input[0]
      label = input[1]
      if isinstance(label, tk.Label):
        if label["foreground"] == self.getConfig().ERROR_COLOR:
          label["foreground"] = self.getConfig().COMMENTS_COLOR
          self.getGraphics().checkSectionLabels(section)

  '''
  The following function responds to the user clicking on the "Cancel" button on the bottom
  '''
  def respondToCancel(self, frame):
    frame.destroy()

  '''
  The following function responds to the user clicking on the "Apply" button on the bottom
  '''
  def respondToApply(self, edit=False, back=None):
    ready, errors, errorTextLabels = self.getData().checkForApply()
    if ready:
      self.respond(self.getData().toDictionary(), self.getData(), edit=edit, back=back)
      self.getGraphics().getGUI().destroy()
    else:
      self.getGraphics().displayErrorMessage(errors, errorTextLabels)

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
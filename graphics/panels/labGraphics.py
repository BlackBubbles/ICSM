#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/08/2017
Last Updated: 08/10/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Lab" panel
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
The following class builds the GUI for the "Lab" panel
'''
class LabG:

  '''
  The following function is the initial instance creation function for the "LabG" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "LabG" class
    self.default = 0

  '''
  The following function returns the configuration file for this instance of the "LabG" class
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
        if config.confirm("Lab"):
          self.config = config
        else:
          return False, "%s:\nconfig file for LabG is not configLab" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function builds the components for the default section within the "Lab" panel
  '''
  def __buildDefault(self, graphics, frame):
    label = graphics.getBuilder().buildH2Label(frame, "Coming Soon...")
    label.grid(row=0, column=0, padx=(50, 50), pady=(25, 25), sticky=tk.W)

  '''
  The following function builds the initial state for the "Lab" panel
  '''
  def buildPanel(self, graphics):

    # Get the "Lab" frame from the instance of the "FrameG" class
    panel = graphics.getFrameGraphics().getFrame("Lab")

    # Build the whitebackground and scrollbars
    frame = graphics.getBuilder().buildScrollingCanvas(panel)

    # Build the Panel's title
    graphics.getBuilder().buildTitle(graphics, frame, graphics.getConfig().getConfigLab().TITLE, True)

    # Build the "Default Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=3, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    defaultFrame = graphics.getBuilder().buildSection(tempFrame, "Default")
    self.__buildDefault(graphics, defaultFrame)

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "lab":
        return True
      else:
        return False
    else:
      return False
#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/18/2017
Last Updated: 08/11/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Project" panel
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
The following class builds the GUI for the "Project" panel
'''
class ProjectG:

  '''
  The following function is the initial instance creation function for the "ProjectG" class
  '''
  def __init__(self, config, builder):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setBuilder(builder)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "ProjectG" class
    self.data = None

  '''
  The following function returns the configuration file for this instance of the "ProjectG" class
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
        if config.confirm("Project"):
          self.config = config
        else:
          return False, "%s:\nconfig file for ProjectG is not configProject" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the builder for this instance of the "Project" panel
  '''
  def getBuilder(self):
    return self.builder

  '''
  The following function sets the builder for this instance of the "Project" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setBuilder(self, builder):
    if hasattr(builder, "confirm"):
      if builder.confirm("Builder"):
        self.builder = builder
      else:
        return False, "%s:\nbuilder for ProjectG is not GUIBuilder" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function returns the model for this instance of the "Project" panel
  '''
  def getData(self):
    return self.data

  '''
  The following function sets the model for this instance of the "Project" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, data):
    if hasattr(data, "confirm"):
      if data.confirm("Project"):
        self.data = data
      else:
        return False, "%s:\ndata for ProjectG is not projectData" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function builds the components for the default section within the "Project" panel
  '''
  def __buildDefault(self, graphics, frame):
    label = graphics.getBuilder().buildH2Label(frame, "Coming Soon...")
    label.grid(row=0, column=0, padx=(50, 50), pady=(25, 25), sticky=tk.W)

  '''
  The following function builds the initial state for the "Project" panel
  '''
  def buildPanel(self, graphics, panel):

    # Build the whitebackground and scrollbars
    frame = graphics.getBuilder().buildScrollingCanvas(panel)

    # Build the Panel's title
    graphics.getBuilder().buildTitle(graphics, frame, graphics.getConfig().getConfigProject().TITLE, False)

    # Build the "Default Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=3, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    defaultFrame, defaultLabel = graphics.getBuilder().buildSection(tempFrame, "Default")
    self.__buildDefault(graphics, defaultFrame)
    defaultFrame.configure(width=700, height=100)

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "project":
        return True
      else:
        return False
    else:
      return False
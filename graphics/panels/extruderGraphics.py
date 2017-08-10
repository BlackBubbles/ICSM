#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 08/10/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Extruder" panel
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
The following class builds the GUI for the "Extruder" panel
'''
class ExtruderG:

  '''
  The following function is the initial instance creation function for the "ExtruderG" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "ExtruderG" class
    self.default = 0

  '''
  The following function returns the configuration file for this instance of the "ExtruderG" class
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
          return False, "%s:\nconfig file for ExtruderG is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function builds the components for the extruder options section within the "Extruder" panel
  '''
  def __buildExtruderOptions(self, graphics, frame):
    print "__buildExtruderOptions"

  '''
  The following function builds the components for the port set-up section within the "Extruder" panel
  '''
  def __buildPortOptions(self, graphics, frame):
    print "__buildPortOptions"

  '''
  The following function builds the components for the feeders section within the "Extruder" panel
  '''
  def __buildAddFeedersOptions(self, graphics, frame):
    print "__buildAddFeedersOptions"

  '''
  The following function builds the components for the strand cooling options section within the "Extruder" panel
  '''
  def __buildStrandCoolingOptions(self, graphics, frame):
    print "__buildStrandCoolingOptions"

  '''
  The following function builds the components for the pelletizing options section within the "Extruder" panel
  '''
  def __buildPelletizingOptions(self, graphics, frame):
    print "__buildPelletizingOptions"

  '''
  The following function builds the components for the classified options section within the "Extruder" panel
  '''
  def __buildClassifiedOptions(self, graphics, frame):
    print "__buildClassifiedOptions"

  '''
  The following function builds the components for the capture options section within the "Extruder" panel
  '''
  def __buildCaptureOptions(self, graphics, frame):
    print "__buildCaptureOptions"

  '''
  The following function builds the initial state for the "Extruder" panel
  '''
  def buildPanel(self, graphics):

    # Get the "Extruder" frame from the instance of the "FrameG" class
    panel = graphics.getFrameGraphics().getFrame("Extruder")

    # Build the whitebackground and scrollbars
    frame = graphics.getBuilder().buildScrollingCanvas(panel)

    # Build the Panel's title
    graphics.getBuilder().buildTitle(graphics, frame, graphics.getConfig().getConfigExtruder().TITLE, True)

    # Build the "Port Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=4, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    portOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                     PORT_OPTIONS_SECTION_TITLE)
    self.__buildPortOptions(graphics, portOptionsFrame)

    # Build the "Extruder Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=3, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    extruderOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                         EXTRUDER_OPTIONS_SECTION_TITLE)
    self.__buildExtruderOptions(graphics, extruderOptionsFrame)

    # Build the "Add Feeders Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=5, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    addFeedersFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                    FEEDERS_SECTION_TITLE)
    self.__buildAddFeedersOptions(graphics, addFeedersFrame)

    # Build the "Strand Cooling Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=6, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    strandCoolingOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                              STRAND_COOLING_OPTIONS_SECTION_TITLE)
    self.__buildStrandCoolingOptions(graphics, strandCoolingOptionsFrame)

    # Build the "Pelletizing Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=7, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    pelletizingOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                            PELLETIZING_OPTIONS_SECTION_TITLE)
    self.__buildPelletizingOptions(graphics, pelletizingOptionsFrame)

    # Build the "Classified Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=8, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    classifiedOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                           CLASSIFIED_OPTIONS_SECTION_TITLE)
    self.__buildClassifiedOptions(graphics, classifiedOptionsFrame)

    # Build the "Capture Options Section"
    tempFrame = graphics.getBuilder().buildFrame(frame)
    tempFrame.grid(row=9, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    captureOptionsFrame = graphics.getBuilder().buildSection(tempFrame, graphics.getConfig().getConfigExtruder().
                                                                        CAPTURING_SECTION_TITLE)
    self.__buildCaptureOptions(graphics, captureOptionsFrame)

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
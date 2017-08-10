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
    self.feedersFrame = None
    self.pelletMillFrame = None
    self.portSetUpFrame = None
    self.strandCoolingFrame = None

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
  The following function returns the Tkinter frame that was built to be manipulated for the feeders section in the
  "Extruder" panel
  '''
  def getFeedersFrame(self):
    return self.feedersFrame

  '''
  The following function sets the Tkinter frame that was built to be manipulated for the feeders section in the
  "Extruder" panel. If the inputted frame does not meet the requirements then the function will return a "False" 
  boolean value and an error message
  '''
  def setFeedersFrame(self, feedersFrame):

    # Build the initial return variables and values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of Tkinter.Frame
    if not isinstance(feedersFrame, tk.Frame):
      doesWork = False
      message = "%s:\ninputted frame for ExtruderG.feedersFrame is not an instance of Tkinter.Frame" % ERROR
    else:
      self.feedersFrame = feedersFrame

    # Return the initial variables
    return doesWork, message

  '''
  The following function returns the Tkinter frame that was built to be manipulated for the pelletizier section in the
  "Extruder" panel
  '''
  def getPelletMillFrame(self):
    return self.pelletMillFrame

  '''
  The following function sets the Tkinter frame that was built to be manipulated for the pelletizier section in the
  "Extruder" panel. If the inputted frame does not meet the requirements then the function will return a "False" 
  boolean value and an error message
  '''
  def setPelletMillFrame(self, pelletMillFrame):

    # Build the initial return variables and values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of Tkinter.Frame
    if not isinstance(pelletMillFrame, tk.Frame):
      doesWork = False
      message = "%s:\ninputted frame for ExtruderG.pelletMillFrame is not an instance of Tkinter.Frame" % ERROR
    else:
      self.pelletMillFrame = pelletMillFrame

    # Return the initial variables
    return doesWork, message

  '''
  The following function returns the Tkinter frame that was built to be manipulated for the port set-up section in the
  "Extruder" panel
  '''
  def getPortSetUpFrame(self):
    return self.portSetUpFrame

  '''
  The following function sets the Tkinter frame that was built to be manipulated for the port set-up section in the
  "Extruder" panel. If the inputted frame does not meet the requirements then the function will return a "False" 
  boolean value and an error message
  '''
  def setPortSetUpFrame(self, portSetUpFrame):

    # Build the initial return variables and values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of Tkinter.Frame
    if not isinstance(portSetUpFrame, tk.Frame):
      doesWork = False
      message = "%s:\ninputted frame for ExtruderG.portSetUpFrame is not an instance of Tkinter.Frame" % ERROR
    else:
      self.portSetUpFrame = portSetUpFrame

    # Return the initial variables
    return doesWork, message

  '''
  The following function returns the Tkinter frame that was built to be manipulated for the strand cooling section in
  the "Extruder" panel
  '''
  def getStrandCoolingFrame(self):
    return self.strandCoolingFrame

  '''
  The following function sets the Tkinter frame that was built to be manipulated for the strand cooling section in the
  "Extruder" panel. If the inputted frame does not meet the requirements then the function will return a "False" 
  boolean value and an error message
  '''
  def setStrandCoolingFrame(self, strandCoolingFrame):

    # Build the initial return variables and values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of Tkinter.Frame
    if not isinstance(strandCoolingFrame, tk.Frame):
      doesWork = False
      message = "%s:\ninputted frame for ExtruderG.strandCoolingFrame is not an instance of Tkinter.Frame" % ERROR
    else:
      self.strandCoolingFrame = strandCoolingFrame

    # Return the initial variables
    return doesWork, message

  '''
  The following function builds the components for the extruder options section within the "Extruder" panel
  '''
  def __buildExtruderOptions(self, graphics, frame):
    print "__buildExtruderOptions"

  '''
  The following function builds the components for the port set-up section within the "Extruder" panel
  '''
  def __buildPortOptions(self, graphics, frame):

    # Set the inputted frame to this instance of the class as the port set-up frame
    doesWork, message = self.setPortSetUpFrame(frame)
    if not doesWork:
      print message
      sys.exit()

    # Build and add the label asking the user to choose an extruder
    label = graphics.getBuilder().buildH2Label(frame, "Please Choose Extruder")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

  '''
  The following function builds the components for the feeders section within the "Extruder" panel
  '''
  def __buildAddFeedersOptions(self, graphics, frame):

    # Build and add the "Add Feeder" Button
    button = graphics.getBuilder().buildButton(frame, "Add Feeder")
    button.configure(command=lambda: graphics.getActions().getExtruderActions().addFeeder(graphics))
    button.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)

    # Build and add the frame that will hold all the labels with data on the feeders
    self.setFeedersFrame(graphics.getBuilder().buildFrame(frame))
    self.getFeedersFrame().grid(row=1, column=0, padx=(15, 15), pady=(5, 15), sticky=tk.W)

  '''
  The following function builds the components for the strand cooling options section within the "Extruder" panel
  '''
  def __buildStrandCoolingOptions(self, graphics, frame):

    # Build and add the Selection line of radio buttons
    radios, variable = graphics.getBuilder().buildCoolingRadio(frame, graphics.getConfig().getConfigExtruder().
                                                                      STRAND_COOLING_OPTIONS, graphics)
    index = 0
    for radio in radios:
      if index == 0:
        radio.grid(row=0, column=index, padx=(50, 0), pady=(15, 0), sticky=tk.W)
      else:
        radio.grid(row=0, column=index, padx=(0, 0), pady=(15, 0), sticky=tk.W)
      index = index + 1

    # Build and add the label asking the user to choose a cooling option
    doesWork, message = self.setStrandCoolingFrame(graphics.getBuilder().buildFrame(frame))
    if not doesWork:
      print message
      sys.exit()
    self.getStrandCoolingFrame().grid(row=1, column=0, columnspan=20, padx=(0, 0), pady=(5, 15), sticky=tk.W)
    label = graphics.getBuilder().buildH2Label(self.getStrandCoolingFrame(), "Please Select a Strand Cooling Option")
    label.grid(row=0, column=0, padx=(100, 100), pady=(25, 35), sticky=tk.W)

  '''
  The following function builds the components for the pelletizing options section within the "Extruder" panel
  '''
  def __buildPelletizingOptions(self, graphics, frame):

    # Build and add the "Pelletizier" drop down menu
    pellitizerLabel = graphics.getBuilder().buildH2Label(frame, "Pelletizier")
    pellitizerLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    menu, variable = graphics.getBuilder().buildStringDropDownWithCommand(graphics, frame, 15, pellitizerLabel["text"],
                                                                          graphics.getConfig().getConfigExtruder().
                                                                          PELLETIZIERS)
    menu.grid(row=1, column=0, padx=(40, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Feed Roll" scrollbar
    feedLabel = graphics.getBuilder().buildH2Label(frame, "Feed Roll:")
    feedLabel.grid(row=2, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    feedScale = graphics.getBuilder().buildScale(frame, 0, 1000)
    feedScale.grid(row=2, column=0, padx=(145, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Rotor" scrollbar
    rotorLabel = graphics.getBuilder().buildH2Label(frame, "Rotor:")
    rotorLabel.grid(row=2, column=0, padx=(375, 0), pady=(15, 0), sticky=tk.W)
    rotorScale = graphics.getBuilder().buildScale(frame, 0, 1000)
    rotorScale.grid(row=2, column=0, padx=(437, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the pellet mill additional frame
    doesWork, message = self.setPelletMillFrame(graphics.getBuilder().buildFrame(frame))
    if not doesWork:
      print message
      sys.exit()
    self.getPelletMillFrame().grid(row=3, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Comments" textbox
    commentsLabel = graphics.getBuilder().buildH2Label(frame, "Comments")
    commentsLabel.grid(row=4, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    textbox = tk.Text(frame, width=70, height=9, highlightbackground=graphics.getConfig().LINE_COLOR,
                      highlightcolor=graphics.getConfig().ACTIVE_BACKGROUND)
    textbox.grid(row=5, column=0, padx=(40, 0), pady=(0, 15), sticky=tk.W)

  '''
  The following function builds the components for the classified options section within the "Extruder" panel
  '''
  def __buildClassifiedOptions(self, graphics, frame):

    # Build and add the "Coming Soon" label
    label = graphics.getBuilder().buildH2Label(frame, "Coming Soon")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

  '''
  The following function builds the components for the capture options section within the "Extruder" panel
  '''
  def __buildCaptureOptions(self, graphics, frame):

    # Build and add the "Coming Soon" label
    label = graphics.getBuilder().buildH2Label(frame, "Coming Soon")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

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
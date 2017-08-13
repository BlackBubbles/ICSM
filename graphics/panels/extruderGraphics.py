#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 08/11/2017
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
import tkMessageBox

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

    # Set initial values for this instance of the "ExtruderG" class
    self.actions = None
    self.data = None
    self.feedersFrame = None
    self.pelletMillFrame = None
    self.portSetUpFrame = None
    self.strandCoolingFrame = None
    self.labels = {}

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
  The following function returns the builder for this instance of the "Extruder" panel
  '''
  def getBuilder(self):
    return self.builder

  '''
  The following function sets the builder for this instance of the "Extruder" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setBuilder(self, builder):
    if hasattr(builder, "confirm"):
      if builder.confirm("Builder"):
        self.builder = builder
      else:
        return False, "%s:\nbuilder for ExtruderG is not GUIBuilder" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function returns the controller for this instance of the "Extruder" panel
  '''
  def getActions(self):
    return self.actions

  '''
  The following function sets the controller for this instance of the "Extruder" panel. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setActions(self, actions):
    if hasattr(actions, "confirm"):
      if actions.confirm("Extruder"):
        self.actions = actions
      else:
        return False, "%s:\nactions for ExtruderG is not extruderActions" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
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
        return False, "%s:\ndata for ExtruderG is not extruderData" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
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
  The following function returns the entire list of labels
  '''
  def getLabels(self):
    return self.labels

  '''
  The following function builds the components for the extruder options section within the "Extruder" panel
  '''
  def __buildExtruderOptions(self, frame):
    print "__buildExtruderOptions"

  '''
  The following function builds the components for the port set-up section within the "Extruder" panel
  '''
  def __buildPortOptions(self, frame):

    # Set the inputted frame to this instance of the class as the port set-up frame
    doesWork, message = self.setPortSetUpFrame(frame)
    if not doesWork:
      print message
      sys.exit()

    # Build and add the label asking the user to choose an extruder
    label = self.getBuilder().buildH2Label(frame, "Please Choose Extruder")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

  '''
  The following function builds the components for the feeders section within the "Extruder" panel
  '''
  def __buildAddFeedersOptions(self, frame):

    # Build and add the "Add Feeder" Button
    button = self.getBuilder().buildButton(frame, "Add Feeder")
    button.configure(command=lambda: self.getActions().addFeeder())
    button.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)

    # Build and add the frame that will hold all the labels with data on the feeders
    self.setFeedersFrame(self.getBuilder().buildFrame(frame))
    self.getFeedersFrame().grid(row=1, column=0, padx=(15, 15), pady=(5, 15), sticky=tk.W)

  '''
  The following function builds the components for the strand cooling options section within the "Extruder" panel
  '''
  def __buildStrandCoolingOptions(self, graphics, frame):

    # Build and add the Selection line of radio buttons
    radios, variable = graphics.getBuilder().buildCoolingRadio(graphics, frame,
                                                               graphics.getConfig().getConfigExtruder().
                                                               STRAND_COOLING_OPTIONS)
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
  def __buildPelletizingOptions(self, frame):

    # Build and add the "Pelletizier" drop down menu
    pellitizerLabel = self.getBuilder().buildH2Label(frame, "Pelletizier")
    pellitizerLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    menu, variable = self.getBuilder().buildStringDropDown(self.getActions().changePellet, frame, 15,
                                                           self.getConfig().PELLETIZIERS)
    menu.grid(row=1, column=0, padx=(40, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Feed Roll" scrollbar
    feedLabel = self.getBuilder().buildH2Label(frame, "Feed Roll:")
    feedLabel.grid(row=2, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    feedScale = self.getBuilder().buildScale(frame, 0, 1000)
    feedScale.grid(row=2, column=0, padx=(145, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Rotor" scrollbar
    rotorLabel = self.getBuilder().buildH2Label(frame, "Rotor:")
    rotorLabel.grid(row=2, column=0, padx=(375, 0), pady=(15, 0), sticky=tk.W)
    rotorScale = self.getBuilder().buildScale(frame, 0, 1000)
    rotorScale.grid(row=2, column=0, padx=(437, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the pellet mill additional frame
    doesWork, message = self.setPelletMillFrame(self.getBuilder().buildFrame(frame))
    if not doesWork:
      print message
      sys.exit()
    self.getPelletMillFrame().grid(row=3, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Comments" textbox
    commentsLabel = self.getBuilder().buildH2Label(frame, "Comments")
    commentsLabel.grid(row=4, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    textbox = tk.Text(frame, width=70, height=9, highlightbackground=self.getConfig().COMMENTS_COLOR,
                      highlightcolor=self.getConfig().ACTIVE_BACKGROUND)
    textbox.grid(row=5, column=0, padx=(40, 0), pady=(0, 15), sticky=tk.W)

  '''
  The following function builds the components for the classified options section within the "Extruder" panel
  '''
  def __buildClassifiedOptions(self, frame):

    # Build and add the "Classified" list of radio buttons
    text = "Classified:"
    classifiedLabel = self.getBuilder().buildH3Label(frame, text)
    classifiedLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    self.labels[self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE][text] = classifiedLabel
    radios, variable = self.getBuilder().buildRadio(self.getActions().checkLabel,
                                                    self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE, classifiedLabel,
                                                    frame, self.getConfig().CLASSIFIED_RADIO_BUTTON_NAMES)
    self.getData().setClassifiedVariable(variable)
    for radio in radios:
      radio.grid(row=0, column=radios.index(radio) + 1, padx=(0, 0), pady=(25, 0), sticky=tk.W)

    # Build and add the "Coming Soon" label
    label = self.getBuilder().buildH2Label(frame, "Rest Coming Soon")
    label.grid(row=1, column=0, columnspan=20, padx=(100, 100), pady=(25, 35), sticky=tk.W)

  '''
  The following function builds the components for the capture options section within the "Extruder" panel
  '''
  def __buildCaptureOptions(self, frame):

    # Build and add the "Coming Soon" label
    label = self.getBuilder().buildH2Label(frame, "Coming Soon")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

  '''
  The following function builds the initial state for the "Extruder" panel
  '''
  def buildPanel(self, graphics, panel):

    # Build the whitebackground and scrollbars
    frame = self.getBuilder().buildScrollingCanvas(panel)

    # Build the Panel's title
    self.getBuilder().buildTitle(graphics, frame, self.getConfig().TITLE, True)

    # Build the "Extruder Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=3, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    extruderOptionsFrame, extruderOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                                self.getConfig().
                                                                                EXTRUDER_OPTIONS_SECTION_TITLE)
    self.__buildExtruderOptions(extruderOptionsFrame)

    # Build the "Port Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=4, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    portOptionsFrame, portOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                        self.getConfig().PORT_OPTIONS_SECTION_TITLE)
    self.__buildPortOptions(portOptionsFrame)

    # Build the "Add Feeders Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=5, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    feedersFrame, feedersLabel  = self.getBuilder().buildSection(tempFrame, self.getConfig().FEEDERS_SECTION_TITLE)
    self.__buildAddFeedersOptions(feedersFrame)

    # Build the "Strand Cooling Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=6, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    strandCoolingOptionsFrame, strandCoolingOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE)
    self.__buildStrandCoolingOptions(graphics, strandCoolingOptionsFrame)

    # Build the "Pelletizing Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=7, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    pelletizingOptionsFrame, pelletizingOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                    self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE)
    self.__buildPelletizingOptions(pelletizingOptionsFrame)

    # Build the "Classified Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=8, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    classifiedOptionsFrame, classifiedOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                                    self.getConfig().
                                                                                    CLASSIFIED_OPTIONS_SECTION_TITLE)
    self.labels[self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE] = {self.getConfig().
                                                                      CLASSIFIED_OPTIONS_SECTION_TITLE:
                                                                        classifiedOptionsLabel}
    self.__buildClassifiedOptions(classifiedOptionsFrame)

    # Build the "Capture Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=9, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    captureOptionsFrame, captureOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                              self.getConfig().CAPTURING_SECTION_TITLE)
    self.labels[self.getConfig().CAPTURING_SECTION_TITLE] = {self.getConfig().CAPTURING_SECTION_TITLE:
                                                               captureOptionsLabel}
    self.__buildCaptureOptions(captureOptionsFrame)

    # Build and add the "Update Workflow" button
    updateButton = self.getBuilder().buildBottomButton(frame, "Update Workflow")
    updateButton.grid(row=10, column=0, padx=(200, 0), pady=(50, 75), sticky=tk.W)
    updateButton.configure(command=lambda: self.getActions().checkForUpdate())

    # Build and add the "Capture Extruder" button
    captureButton = self.getBuilder().buildBottomButton(frame, "Capture Extruder")
    captureButton.grid(row=10, column=0, padx=(500, 0), pady=(50, 75), sticky=tk.W)

  '''
  The following function displays a list of errors to the user
  '''
  def displayUpdateError(self, errors, errorTextLabels):

    # Set the unused labels to red
    print errorTextLabels
    print self.getLabels()

    # Display the error message
    tkMessageBox.showerror("ERROR", "".join(errors))

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
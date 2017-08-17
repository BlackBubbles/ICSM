#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 08/16/2017
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
from add import feederGraphics

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
    self.feederGraphics = feederGraphics.FeederG(self.getConfig(), self.getBuilder())
    self.feedersFrame = None
    self.pelletMillFrame = None
    self.portSetUpFrame = None
    self.strandCoolingFrame = None
    self.labels = {}
    self.dieMenu = None
    self.meshEntry = None
    self.airKnivesFrame = None
    self.waterTempScale = None
    self.lengthEntry = None
    self.locationEntry = None
    self.conveyorScale = None
    self.blowerScale = None
    self.vacBlowerScale = None
    self.feedRollScale = None
    self.rotorScale = None
    self.feederSpeedScale = None
    self.pumpSpeedScale = None
    self.pelletizingComments = None

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
        self.getFeederGraphics().setActions(actions.getFeederActions())
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
  The following function returns the instance of the "FeederG" class for this instance
  '''
  def getFeederGraphics(self):
    return self.feederGraphics

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
  The following function returns the menu for the die options
  '''
  def getDieMenu(self):
    return self.dieMenu

  '''
  The following function sets the menu for the die options
  '''
  def setDieMenu(self, dieMenu):
    self.dieMenu = dieMenu

  '''
  The following function returns the Tkinter Entry that stores the users notes on the mesh
  '''
  def getMeshEntry(self):
    return self.meshEntry

  '''
  The following function sets the Tkinter Entry that stores the users notes on the mesh
  '''
  def setMeshEntry(self, meshEntry):
    self.meshEntry = meshEntry

  '''
  The following function returns the Tkinter frame that displays the air knives options
  '''
  def getAirKnivesFrame(self):
    return self.airKnivesFrame

  '''
  The following function sets the Tkinter frame that displays the air knives options
  '''
  def setAirKnivesFrame(self, airKnivesFrame):
    self.airKnivesFrame = airKnivesFrame

  '''
  The following function returns the Tkinter scale for the water temp
  '''
  def getWaterTempScale(self):
    return self.waterTempScale

  '''
  The following function sets the Tkinter scale for the water temp
  '''
  def setWaterTempScale(self, waterTempScale):
    self.waterTempScale = waterTempScale

  '''
  The following function returns the Tkinter entry for the length of the water bath dip
  '''
  def getLengthEntry(self):
    return self.lengthEntry

  '''
  The following function sets the Tkinter entry for the length of the water bath dip
  '''
  def setLengthEntry(self, lengthEntry):
    self.lengthEntry = lengthEntry

  '''
  The following function returns the Tkinter entry for the location of the air knives
  '''
  def getLocationEntry(self):
    return self.locationEntry

  '''
  The following function sets the Tkinter entry for the location of the air knives
  '''
  def setLocationEntry(self, locationEntry):
    self.locationEntry = locationEntry

  '''
  The following function returns the Tkinter scale for the conveyor speed
  '''
  def getConveyorScale(self):
    return self.conveyorScale

  '''
  The following function sets the Tkinter scale for the conveyor speed
  '''
  def setConveyorScale(self, conveyorScale):
    self.conveyorScale = conveyorScale

  '''
  The following function returns the Tkinter scale for the blower speed
  '''
  def getBlowerScale(self):
    return self.blowerScale

  '''
  The following function sets the Tkinter scale for the blower speed
  '''
  def setBlowerScale(self, blowerScale):
    self.blowerScale = blowerScale

  '''
  The following function returns the Tkinter scale for the blower vac speed
  '''
  def getVacBlowerScale(self):
    return self.vacBlowerScale

  '''
  The following function sets the Tkinter scale for the blower vac speed
  '''
  def setVacBlowerScale(self, vacBlowerScale):
    self.vacBlowerScale = vacBlowerScale

  '''
  The following function returns the Tkinter scale instance that represents the feed roll speed
  '''
  def getFeedRollScale(self):
    return self.feedRollScale

  '''
  The following function sets the Tkinter scale instance that represents the feed roll speed
  '''
  def setFeedRollScale(self, feedRollScale):
    self.feedRollScale = feedRollScale

  '''
  The following function returns the Tkinter scale instance that represents the rotor speed
  '''
  def getRotorScale(self):
    return self.rotorScale

  '''
  The following function sets the Tkinter scale instance that represents the rotor speed
  '''
  def setRotorScale(self, rotorScale):
    self.rotorScale = rotorScale

  '''
    The following function returns the Tkinter scale instance that represents the feeder speed
    '''
  def getFeederSpeedScale(self):
    return self.feederSpeedScale

  '''
  The following function sets the Tkinter scale instance that represents the feeder speed
  '''
  def setFeederSpeedScale(self, feederSpeedScale):
    self.feederSpeedScale = feederSpeedScale

  '''
  The following function returns the Tkinter scale instance that represents the pump speed
  '''
  def getPumpSpeedScale(self):
    return self.pumpSpeedScale

  '''
  The following function sets the Tkinter scale instance that represents the pump speed
  '''
  def setPumpSpeedScale(self, pumpSpeedScale):
    self.pumpSpeedScale = pumpSpeedScale

  '''
  The following function returns the Tkinter text box that the user types his/her comments into
  '''
  def getPelletizingComments(self):
    return self.pelletizingComments

  '''
  The following function sets the Tkinter text box that the user types his/her comments into
  '''
  def setPelletizingComments(self, pelletizingComments):
    self.pelletizingComments = pelletizingComments

  '''
  The following function builds the components for the extruder options section within the "Extruder" panel
  '''
  def __buildExtruderOptions(self, frame):

    # Build and add the "Extruder" drop down menu
    extruderText = "Extruder"
    extruderLabel = self.getBuilder().buildH3Label(frame, extruderText)
    self.getLabels()[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE][extruderText] = extruderLabel
    extruderLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    extruderMenu, extruderVariable = self.getBuilder().buildStringDropDown(self.getActions().changeExtruderOptions,
                                                                           self.getConfig().
                                                                             EXTRUDER_OPTIONS_SECTION_TITLE,
                                                                           extruderLabel, frame, 15,
                                                                           self.getConfig().EXTRUDERS)
    self.getData().setExtruderVariable(extruderVariable)
    extruderMenu.grid(row=1, column=0, padx=(40, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Die Options" drop down menu
    dieText = "Die Options"
    dieLabel = self.getBuilder().buildH3Label(frame, dieText)
    self.getLabels()[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE][dieText] = dieLabel
    dieLabel.grid(row=0, column=0, padx=(250, 0), pady=(25, 0), sticky=tk.W)
    dieMenu, dieVariable = self.getBuilder().buildStringDropDown(self.getActions().selectDropDown,
                                                                 self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE,
                                                                 dieLabel, frame, 15,
                                                                 self.getConfig().EXTRUDER_DIES[
                                                                   self.getData().getExtruderVariable().get()])
    self.getData().setDieVariable(dieVariable)
    self.setDieMenu(dieMenu)
    dieMenu.grid(row=1, column=0, padx=(240, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Pre-Die" drop down menu
    preDieText = "Pre-Die"
    preDieLabel = self.getBuilder().buildH3Label(frame, preDieText)
    self.getLabels()[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE][preDieText] = preDieLabel
    preDieLabel.grid(row=0, column=0, padx=(450, 0), pady=(25, 0), sticky=tk.W)
    preDieMenu, preDieVariable = self.getBuilder().buildStringDropDown(self.getActions().selectDropDown,
                                                                       self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE,
                                                                       preDieLabel, frame, 15,
                                                                       self.getConfig().PRE_DIE)
    self.getData().setPreDieVariable(preDieVariable)
    preDieMenu.grid(row=1, column=0, padx=(440, 50), pady=(0, 0), sticky=tk.W)

    # Build and add the "Screen Pack" checkbox
    screenLabel = self.getBuilder().buildH3Label(frame, "Screen Pack:")
    screenLabel.grid(row=2, column=0, padx=(50, 0), pady=(15, 35), sticky=tk.W)
    screenBox, screenVariable = self.getBuilder().buildCheckBox(frame, "")
    self.getData().setScreenPackVariable(screenVariable)
    screenBox.grid(row=2, column=0, padx=(150, 0), pady=(16, 34), sticky=tk.W)

    # Build and add the "Mesh" text input line
    meshText = "Mesh:"
    meshLabel = self.getBuilder().buildH3Label(frame, meshText)
    self.getLabels()[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE][meshText] = meshLabel
    meshLabel.grid(row=2, column=0, padx=(250, 0), pady=(15, 35), sticky=tk.W)
    self.setMeshEntry(tk.Entry(frame, width=26))
    self.getMeshEntry().bind("<Key>",
                             lambda event: self.getActions().checkLabel([self.getConfig().
                                                                           EXTRUDER_OPTIONS_SECTION_TITLE,
                                                                         meshLabel]))
    self.getMeshEntry().grid(row=2, column=0, padx=(305, 0), pady=(15, 35), sticky=tk.W)

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
    button.grid(row=0, column=0, padx=(50, 50), pady=(25, 0), sticky=tk.W)

    # Build and add the frame that will hold all the labels with data on the feeders
    self.setFeedersFrame(self.getBuilder().buildFrame(frame))
    self.getFeedersFrame().grid(row=1, column=0, padx=(15, 15), pady=(5, 15), sticky=tk.W)

  '''
  The following function builds the components for the strand cooling options section within the "Extruder" panel
  '''
  def __buildStrandCoolingOptions(self, graphics, frame):

    # Build and add the Selection line of radio buttons
    radios, variable = graphics.getBuilder().buildRadio(self.getActions().changeCooling,
                                                        self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                        None, frame, self.getConfig().STRAND_COOLING_OPTIONS)
    self.getData().setStrandCoolingFrameVariable(variable)
    index = 0
    for radio in radios:
      if index == 0:
        radio.grid(row=0, column=index, padx=(50, 0), pady=(15, 0), sticky=tk.W)
      elif index == len(radios) - 1:
        radio.grid(row=0, column=index, padx=(0, 50), pady=(15, 0), sticky=tk.W)
      else:
        radio.grid(row=0, column=index, padx=(0, 0), pady=(15, 0), sticky=tk.W)
      index = index + 1

    # Build and add the label asking the user to choose a cooling option
    doesWork, message = self.setStrandCoolingFrame(graphics.getBuilder().buildFrame(frame))
    if not doesWork:
      print message
      sys.exit()
    self.getStrandCoolingFrame().grid(row=1, column=0, columnspan=20, padx=(0, 35), pady=(0, 35), sticky=tk.W)
    label = graphics.getBuilder().buildH2Label(self.getStrandCoolingFrame(), "Please Select a Strand Cooling Option")
    label.grid(row=0, column=0, padx=(100, 65), pady=(15, 0), sticky=tk.W)

  '''
  The following function builds the components for the pelletizing options section within the "Extruder" panel
  '''
  def __buildPelletizingOptions(self, frame):

    # Build and add the "Pelletizier" drop down menu
    text = "Pelletizier"
    pellitizerLabel = self.getBuilder().buildH3Label(frame, text)
    pellitizerLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    self.labels[self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE][text] = pellitizerLabel
    menu, variable = self.getBuilder().buildStringDropDown(self.getActions().changePellet,
                                                           self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE,
                                                           pellitizerLabel, frame, 15, self.getConfig().PELLETIZIERS)
    self.getData().setPelletizierVariable(variable)
    menu.grid(row=1, column=0, columnspan=20, padx=(40, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Feed Roll" scrollbar
    feedLabel = self.getBuilder().buildH3Label(frame, "Feed Roll:")
    feedLabel.grid(row=2, column=0, padx=(50, 0), pady=(18, 0), sticky=tk.W)
    self.setFeedRollScale(self.getBuilder().buildScale(frame, 0, 1000))
    self.getFeedRollScale().grid(row=2, column=1, padx=(0, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Rotor" scrollbar
    rotorLabel = self.getBuilder().buildH3Label(frame, "Rotor:")
    rotorLabel.grid(row=2, column=2, padx=(25, 0), pady=(18, 0), sticky=tk.W)
    self.setRotorScale(self.getBuilder().buildScale(frame, 0, 1000))
    self.getRotorScale().grid(row=2, column=3, padx=(0, 25), pady=(0, 0), sticky=tk.W)

    # Build and add the pellet mill additional frame
    doesWork, message = self.setPelletMillFrame(self.getBuilder().buildFrame(frame))
    if not doesWork:
      print message
      sys.exit()
    self.getPelletMillFrame().grid(row=3, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Comments" textbox
    commentsLabel = self.getBuilder().buildH3Label(frame, "Comments")
    commentsLabel.grid(row=4, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    self.setPelletizingComments(tk.Text(frame, width=70, height=9, highlightbackground=self.getConfig().COMMENTS_COLOR,
                                        highlightcolor=self.getConfig().ACTIVE_BACKGROUND))
    self.getPelletizingComments().grid(row=5, column=0, columnspan=20, padx=(40, 0), pady=(0, 15), sticky=tk.W)

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
    self.labels[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE] = {self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE:
                                                                      extruderOptionsLabel}
    self.__buildExtruderOptions(extruderOptionsFrame)

    # Build the "Port Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=4, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    portOptionsFrame, portOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                        self.getConfig().PORT_OPTIONS_SECTION_TITLE)
    self.labels[self.getConfig().PORT_OPTIONS_SECTION_TITLE] = {self.getConfig().PORT_OPTIONS_SECTION_TITLE:
                                                                  portOptionsLabel}
    self.__buildPortOptions(portOptionsFrame)

    # Build the "Add Feeders Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=5, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    feedersFrame, feedersLabel  = self.getBuilder().buildSection(tempFrame, self.getConfig().FEEDERS_SECTION_TITLE)
    self.labels[self.getConfig().FEEDERS_SECTION_TITLE] = {self.getConfig().FEEDERS_SECTION_TITLE:feedersLabel}
    self.__buildAddFeedersOptions(feedersFrame)

    # Build the "Strand Cooling Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=6, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    strandCoolingOptionsFrame, strandCoolingOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE)
    self.labels[self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE] = {self.getConfig().
                                                                          STRAND_COOLING_OPTIONS_SECTION_TITLE:
                                                                            strandCoolingOptionsLabel}
    self.__buildStrandCoolingOptions(graphics, strandCoolingOptionsFrame)

    # Build the "Pelletizing Options Section"
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=7, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    pelletizingOptionsFrame, pelletizingOptionsLabel = self.getBuilder().buildSection(tempFrame,
                                                                                      self.getConfig().
                                                                                      PELLETIZING_OPTIONS_SECTION_TITLE)
    self.labels[self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE] = {self.getConfig().
                                                                       PELLETIZING_OPTIONS_SECTION_TITLE:
                                                                         pelletizingOptionsLabel}
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
  The following function changes the drop down menu contents of the "Die Options" and the "Pre-Die"
  '''
  def changeDieMenus(self):
    function = self.getActions().respondToDieMenu
    dictionary = self.getConfig().EXTRUDER_DIES
    extruder = self.getData().getExtruderVariable().get()
    section = self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE
    label = self.getLabels()[section]["Die Options"]
    self.getDieMenu()["menu"].delete(0, "end")
    for string in dictionary[extruder]:
      self.getDieMenu()["menu"].add_command(label=string, command=lambda value=string: function(section, label, value))
    self.getData().getDieVariable().set(dictionary[extruder][0])

  '''
  The following function builds the label asking the user to select an extruder from the options
  '''
  def buildInitialPortFrame(self):
    label = self.getBuilder().buildH2Label(self.getPortSetUpFrame(), "Please Choose Extruder")
    label.grid(row=0, column=0, padx=(100, 100), pady=(35, 35), sticky=tk.W)

  '''
  The following function builds the "Port Set-Up" frame based on the inputted parameters
  '''
  def buildPortFrame(self, length, ports, sides, portOptions, sideOptions):

    # Build the frame for the diagram
    frame = self.getBuilder().buildFrame(self.getPortSetUpFrame())
    frame.configure(highlightbackground=self.getConfig().COMMENTS_COLOR,
                    highlightcolor=self.getConfig().COMMENTS_COLOR, highlightthickness=1)
    frame.grid(row=1, column=0, columnspan=20, padx=(50, 50), pady=(0, 35), sticky=tk.W)

    # Loop through all the ports spots in the extruder
    for index in range(0, length):

      # Build the square frame
      portFrame = self.getBuilder().buildFrame(frame)
      portFrame.configure(width=100, height=100, highlightbackground=self.getConfig().COMMENTS_COLOR,
                          highlightcolor=self.getConfig().COMMENTS_COLOR, highlightthickness=1)
      portFrame.grid_propagate(False)
      portFrame.grid(row=0, column=0, padx=((100 * (length - 1)) - (100 * index), 0), pady=(0, 0), sticky=tk.W)

      # Build and add the port number label
      portNum = self.getBuilder().buildLabel(self.getPortSetUpFrame(), index + 1)
      portNum.configure(font=["Arial", 10, "bold"])
      portNum.grid(row=0, column=0, padx=(((100 * (length - 1)) - (100 * index) + 50), 0), pady=(45, 0), sticky=tk.W)

      # Build and add the port options drop down menus
      if index in ports:
        port, variable = self.getBuilder().buildStringDropDown(self.getActions().respondToPortMenu,
                                                     self.getConfig().PORT_OPTIONS_SECTION_TITLE, portFrame,
                                                     self.getPortSetUpFrame(), 6, portOptions)
        self.getData().getPortVariables().append([index + 1, variable])
        port.grid(row=0, column=0, padx=(((100 * (length - 1)) - (100 * index) + 65), 0), pady=(45, 0), sticky=tk.W)

      # Build and add the side stuffer drop down menus
      if index in sides:
        side, variable = self.getBuilder().buildStringDropDown(self.getActions().respondToPortMenu,
                                                     self.getConfig().PORT_OPTIONS_SECTION_TITLE, portFrame,
                                                     portFrame, 6, sideOptions)
        self.getData().getSideVariables().append([index + 1, variable])
        side.grid(row=0, column=0, padx=(14, 0), pady=(35, 0), sticky=tk.W)

  '''
  The following function converts the inputted feeder dictionary into a string for the label
  '''
  def buildFeederLabelString(self, feeder):

    # Build the initial string variable
    string = ""

    # Build the string value
    if "Tube" in feeder:
      string = string + "Feeder: " + feeder["Feeder"] + " - Tube: " + feeder["Tube"] + " - Screw: " + feeder["Screw"]
    else:
      string = string + "Feeder: " + feeder["Feeder"] + " - Screw: " + feeder["Screw"]
    if feeder["Location"] is 2:
      location = "Side Stuffer"
    else:
      location = "Throat"
    if feeder["Location"] is 1:
      set = "lbs/hr"
    else:
      set = "kg/hr"
    RM = "{"
    first = True
    for key, val in feeder["RM"].iteritems():
      if first:
        RM = RM + key + ":" + str(val)
        first = False
      else:
        RM = RM + ", " + key + ":" + str(val)
    RM = RM + "}"
    string = string + " - Location: " + location + " - Weight In: " + set + " - RM: " + RM
    string = string + " - Total %: " + str(feeder["Total"])

    # Return the initial string variable
    return string

  '''
  The following function adds the feeder labels to the GUI
  '''
  def addFeederLabel(self, feeder):

    # Build the initial frame
    frame = self.getBuilder().buildFrame(self.getFeedersFrame())
    frame.configure(highlightbackground=self.getConfig().COMMENTS_COLOR,
                    highlightcolor=self.getConfig().COMMENTS_COLOR, highlightthickness=2)
    frame.pack(fill=tk.X)

    # Build the label that will be used
    text = self.buildFeederLabelString(feeder)
    label = self.getBuilder().buildH3Label(frame, text)
    label.grid(row=0, column=0, padx=(50, 0), pady=(15, 15), sticky=tk.W)

    # Build the edit button
    delete = self.getBuilder().buildButton(frame, "Edit")
    delete.grid(row=0, column=1, padx=(25, 0), pady=(15, 15), sticky=tk.W)
    delete.configure(command=lambda: self.getActions().respondToEdit(frame))

    # Build the delete buton
    delete = self.getBuilder().buildButton(frame, "Delete")
    delete.grid(row=0, column=2, padx=(25, 50), pady=(15, 15), sticky=tk.W)
    delete.configure(command=lambda: self.getActions().respondToDelete(frame))

    # Return the frame that is used
    return frame

  '''
  The following hidden function builds the water temp found on mister, bath and spray
  '''
  def __buildWaterTemp(self, frame):
    label = self.getBuilder().buildH3Label(frame, "Water Temp " + u"\u00b0" + "C:")
    label.grid(row=0, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    self.setWaterTempScale(self.getBuilder().buildScale(frame, 55, 80))
    self.getWaterTempScale().grid(row=0, column=0, padx=(175, 0), pady=(0, 0), sticky=tk.W)

  '''
  The following hidden function builds the two components found on each of the belt, mister and bath
  '''
  def __buildStrandAndFans(self, frame):

    # Build and add the strand seperator check box
    strandLabel = self.getBuilder().buildH3Label(frame, "Strand Separator:")
    strandLabel.grid(row=0, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    strandCheck, strandVariable = self.getBuilder().buildCheckBox(frame, "")
    self.getData().setSeparatorVariable(strandVariable)
    strandCheck.grid(row=0, column=0, padx=(185, 0), pady=(16, 0), sticky=tk.W)

    # Build and add the "# of fans" drop down menu
    fansLabel = self.getBuilder().buildH3Label(frame, "# of Fans:")
    fansLabel.grid(row=0, column=0, padx=(250, 0), pady=(15, 0), sticky=tk.W)
    fansMenu, fansVariable = self.getBuilder().buildStringDropDown(self.getActions().selectDropDown,
                                                                   self.getConfig().
                                                                     STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                                   fansLabel, frame, 4, self.getConfig().NUM)
    self.getData().setFansVariable(fansVariable)
    fansMenu.grid(row=0, column=0, padx=(330, 0), pady=(16, 0), sticky=tk.W)

  '''
  The following hidden function builds the air knives section
  '''
  def __buildAirKnives(self, frame):

    # Build and add the "air knives" section checkbox
    label = self.getBuilder().buildH3Label(frame, "Air Knives:")
    label.grid(row=0, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    box, variable = self.getBuilder().buildCheckBox(frame, "")
    self.getData().setAirKnivesVariable(variable)
    box.configure(command=lambda: self.getActions().repsondToAirKnives())
    box.grid(row=0, column=0, padx=(135, 0), pady=(16, 0), sticky=tk.W)

    # Build and add the frame for the air knives
    self.setAirKnivesFrame(self.getBuilder().buildFrame(frame))
    self.getAirKnivesFrame().grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)

  '''
  The following function builds the rest of the air knives section
  '''
  def buildAirKnivesFrame(self):

    # Build and add the "location" entry
    text = "Location:"
    locationLabel = self.getBuilder().buildH3Label(self.getAirKnivesFrame(), text)
    self.getLabels()[self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE][text] = locationLabel
    locationLabel.grid(row=0, column=0, padx=(75, 0), pady=(15, 0), sticky=tk.W)
    self.setLocationEntry(tk.Entry(self.getAirKnivesFrame(), width=26))
    self.getLocationEntry().insert(tk.END, "At End of Belt")
    self.getLocationEntry().grid(row=0, column=0, padx=(150, 0), pady=(15, 0), sticky=tk.W)
    self.getLocationEntry().bind("<Key>",
                                 lambda event: self.getActions().checkLabel([self.getConfig().
                                                                               STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                                             locationLabel]))

    # Build and add the "# of air knives" drop down menu
    numLabel = self.getBuilder().buildH3Label(self.getAirKnivesFrame(), "# of Air Knives:")
    numLabel.grid(row=0, column=0, padx=(425, 0), pady=(15, 0), sticky=tk.W)
    menu, variable = self.getBuilder().buildStringDropDown(self.getActions().selectDropDown,
                                                           self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                           numLabel, self.getAirKnivesFrame(), 4,
                                                           self.getConfig().NUM_NO_ZERO)
    self.getData().setNumAirKnivesVariable(variable)
    menu.grid(row=0, column=0, padx=(540, 0), pady=(16, 0), sticky=tk.W)

  '''
  The following function builds the user options for the strand cooling "Belt" option
  '''
  def buildSCBelt(self):
    self.__buildStrandAndFans(self.getStrandCoolingFrame())

  '''
  The following function builds the user options for the strand cooling "Belt w/ Mister" option
  '''
  def buildSCMister(self):

    # Build and add the water temp scale
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildWaterTemp(frame)

    # Build and add the "strand seperator" checkbox and the "# of fans" drop down menu
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildStrandAndFans(frame)

    # Build and add the "air knives" section
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildAirKnives(frame)

  '''
  The following function builds the user options for the strand cooling "Water Bath" option
  '''
  def buildSCBath(self):

    # Build and add the "length of dip" entry
    text = "Length of Dip:"
    label = self.getBuilder().buildH3Label(self.getStrandCoolingFrame(), text)
    self.getLabels()[self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE][text] = label
    label.grid(row=0, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    self.setLengthEntry(tk.Entry(self.getStrandCoolingFrame(), width=26))
    self.getLengthEntry().grid(row=0, column=0, padx=(165, 0), pady=(15, 0), sticky=tk.W)
    self.getLengthEntry().bind("<Key>",
                               lambda event: self.getActions().checkLabel([self.getConfig().
                                                                            STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                                           label]))

    # Build and add the "strand seperator" checkbox and the "# of fans" drop down menu
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildStrandAndFans(frame)

    # Build and add the "air knives" section
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildAirKnives(frame)

  '''
  The following function builds the user options for the strand cooling "Spray Belt" option
  '''
  def buildSCSprayBelt(self):

    # Build and add misters frame
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=0, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Misters" radio buttons
    mistersLabel = self.getBuilder().buildH3Label(frame, "Belt Misters")
    mistersLabel.grid(row=0, column=0, columnspan=20, padx=(300, 0), pady=(15, 0), sticky=tk.W)
    misters = []
    for index in range(0, 12):
      label = self.getBuilder().buildLabel(frame, 12 - index)
      label.configure(font=["Arial", 10, "bold"])
      mistersRadio, mistersVariable = self.getBuilder().buildRadio(self.getActions().checkMisters,
                                                                   self.getConfig().
                                                                     STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                                   mistersLabel, frame, ["On", "Off"])
      misters.append([index + 1, mistersVariable])
      mistersVariable.set(2)
      if index is 0:
        label.grid(row=1, column=index, padx=(50, 0), pady=(0, 0), sticky=tk.W)
        mistersRadio[0].grid(row=2, column=index, padx=(50, 0), pady=(0, 0), sticky=tk.W)
        mistersRadio[1].grid(row=3, column=index, padx=(50, 0), pady=(0, 0), sticky=tk.W)
      else:
        label.grid(row=1, column=index, padx=(0, 0), pady=(0, 0), sticky=tk.W)
        mistersRadio[0].grid(row=2, column=index, padx=(0, 0), pady=(0, 0), sticky=tk.W)
        mistersRadio[1].grid(row=3, column=index, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.getData().setBeltMisters(misters)

    # Build and add the "Belt Misters" radio buttons
    sluicelabel = self.getBuilder().buildH3Label(frame, "Sluice Misters")
    sluicelabel.grid(row=0, column=0, columnspan=20, padx=(685, 0), pady=(15, 0), sticky=tk.W)
    sluices = []
    for index in range(0, 2):
      label = self.getBuilder().buildLabel(frame, 2 - index)
      label.configure(font=["Arial", 10, "bold"])
      sluiceRadio, sluiceVariable = self.getBuilder().buildRadio(self.getActions().checkMisters,
                                                                 self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                                                 sluicelabel, frame, ["On", "Off"])
      sluices.append([index + 1, sluiceVariable])
      sluiceVariable.set(2)
      if index is 0:
        label.grid(row=1, column=index + 12, padx=(50, 0), pady=(0, 0), sticky=tk.W)
        sluiceRadio[0].grid(row=2, column=index + 12, padx=(50, 0), pady=(0, 0), sticky=tk.W)
        sluiceRadio[1].grid(row=3, column=index + 12, padx=(50, 0), pady=(0, 0), sticky=tk.W)
      else:
        label.grid(row=1, column=index + 12, padx=(0, 0), pady=(0, 0), sticky=tk.W)
        sluiceRadio[0].grid(row=2, column=index + 12, padx=(0, 0), pady=(0, 0), sticky=tk.W)
        sluiceRadio[1].grid(row=3, column=index + 12, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.getData().setSluiceMisters(sluices)

    # Build and add the "Water Temp" scale
    frame = self.getBuilder().buildFrame(self.getStrandCoolingFrame())
    frame.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    self.__buildWaterTemp(frame)

    # Build and add the "Conveyor Speed" scale
    conveyorLabel = self.getBuilder().buildH3Label(self.getStrandCoolingFrame(), "Conveyor Speed:")
    conveyorLabel.grid(row=1, column=0, padx=(400, 0), pady=(15, 0), sticky=tk.W)
    self.setConveyorScale(self.getBuilder().buildScale(self.getStrandCoolingFrame(), 0, 100))
    self.getConveyorScale().grid(row=1, column=0, padx=(550, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Blower Speed" scale
    blowerLabel = self.getBuilder().buildH3Label(self.getStrandCoolingFrame(), "Blower Speed:")
    blowerLabel.grid(row=2, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    self.setBlowerScale(self.getBuilder().buildScale(self.getStrandCoolingFrame(), 0, 100))
    self.getBlowerScale().grid(row=2, column=0, padx=(175, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Blower Vac Speed" scale
    vacLabel = self.getBuilder().buildH3Label(self.getStrandCoolingFrame(), "Blower Vac Speed:")
    vacLabel.grid(row=2, column=0, padx=(400, 0), pady=(15, 0), sticky=tk.W)
    self.setVacBlowerScale(self.getBuilder().buildScale(self.getStrandCoolingFrame(), 0, 100))
    self.getVacBlowerScale().grid(row=2, column=0, padx=(550, 0), pady=(0, 0), sticky=tk.W)

  '''
  The following function builds the user options for the strand cooling "UWP" or "Other" options
  '''
  def buildSCOther(self):

    # Build and add the "Coming Soon" label
    label = self.getBuilder().buildH2Label(self.getStrandCoolingFrame(), "Coming Soon")
    label.grid(row=0, column=0, columnspan=20, padx=(100, 65), pady=(15, 0), sticky=tk.W)

  '''
  The following function builds the pellet mill frame if the "Pellet Mill" option was selected from the "Pelletizier"
  drop down menu
  '''
  def buildPelletMillFrame(self):

    # Build and add the "Feeder Speed" scrollbar
    label = self.getBuilder().buildH3Label(self.getPelletMillFrame(), "Feeder Speed(%):")
    label.grid(row=0, column=0, padx=(50, 0), pady=(18, 0), sticky=tk.W)
    self.setFeederSpeedScale(self.getBuilder().buildScale(self.getPelletMillFrame(), 0, 100))
    self.getFeederSpeedScale().grid(row=0, column=1, padx=(0, 25), pady=(0, 0), sticky=tk.W)

    # Build and add the "Pump Speed" scrollbar
    label = self.getBuilder().buildH3Label(self.getPelletMillFrame(), "Pump Speed(Hz):")
    label.grid(row=0, column=2, padx=(25, 0), pady=(18, 0), sticky=tk.W)
    self.setPumpSpeedScale(self.getBuilder().buildScale(self.getPelletMillFrame(), 0, 60))
    self.getPumpSpeedScale().grid(row=0, column=3, padx=(0, 25), pady=(0, 0), sticky=tk.W)

  '''
  The following function checks to see if all the labels in a section have been changed back from the error color, red.
  If so then the function also turns the section header label back to it's original color
  '''
  def checkSectionLabels(self, section):
    allNormal = True
    labels = self.getLabels()[section]
    for key, label in labels.iteritems():
      if key is section:
        continue
      if label["foreground"] == self.getConfig().ERROR_COLOR:
        allNormal = False
        break
    if allNormal:
      labels[section]["foreground"] = self.getConfig().ACTIVE_BACKGROUND

  '''
  The following function destroy's all the content on a frame
  '''
  def destroyAllWidgets(self, frame):
    for widget in frame.winfo_children():
      widget.destroy()
    frame.configure(height=1)

  '''
  The following function displays an error message with the inputted string
  '''
  def displayError(self, message):
    tkMessageBox.showerror("ERROR", message)

  '''
  The following function displays an message with the inputted string
  '''
  def displayMessage(self, message):
    tkMessageBox.showinfo("ICSM", message)

  '''
  The following function displays a list of errors to the user
  '''
  def displayUpdateError(self, errors, errorTextLabels):

    # Set the unused labels to red
    for section, list in errorTextLabels.iteritems():
      labels = self.getLabels()[section]
      if not len(list) is 0:
        labels[section]["foreground"] = self.getConfig().ERROR_COLOR
      for item in list:
        if item == "":
          continue
        labels[item]["foreground"] = self.getConfig().ERROR_COLOR

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
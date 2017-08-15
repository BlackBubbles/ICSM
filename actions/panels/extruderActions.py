#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 08/15/2017
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
        return False, "%s:\ngraphics for ExtruderA is not extruderGraphics" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function repsonds to the user selecting the "Browse" button
  '''
  def callBrowseServer(self, graphics, title, label):
    filename = graphics.getBrowseServerGraphics().browseServer(graphics, title, label)
    graphics.getData().getExtruderData().setWorkflowFileName(filename)

  '''
  The following function responds to the user selecting a option from the extruder drop down menu
  '''
  def changeExtruderOptions(self, section, label):

    # Check the label
    self.checkLabel([section, label])

    # Change the values within the "Die Options" and "Pre-Die" drop down menus
    self.getGraphics().changeDieMenus()

    # Destroy contents of the port frame
    self.getGraphics().destroyAllWidgets(self.getGraphics().getPortSetUpFrame())
    self.getData().setPortVariables([])
    self.getData().setSideVariables([])

    # Build the port options frame based on extruder contained
    extruder = self.getData().getExtruderVariable().get()
    if extruder == self.getConfig().EXTRUDERS[0]:
      self.getGraphics().buildInitialPortFrame()
      return 0
    elif extruder == self.getConfig().EXTRUDERS[1]:
      portOptions = self.getConfig().PORT_OPTIONS_11MM
      sideOptions = ["None"]
    elif extruder == self.getConfig().EXTRUDERS[2] or extruder == self.getConfig().EXTRUDERS[3]:
      portOptions = self.getConfig().PORT_OPTIONS
      sideOptions = self.getConfig().SIDE_STUFFER_WITHOUT_VACCUM
    else:
      portOptions = self.getConfig().PORT_OPTIONS
      sideOptions = self.getConfig().SIDE_STUFFER
    self.getGraphics().buildPortFrame(self.getConfig().EXTRUDER_PORT_SIZES[extruder][0],
                                      self.getConfig().EXTRUDER_PORT_SPOTS[extruder],
                                      self.getConfig().EXTRUDER_SIDE_SPOTS[extruder], portOptions, sideOptions)

  '''
  The following function responds to the event made by the ICSM program when the user selects an extruder
  '''
  def respondToDieMenu(self, section, label, value):
    self.getData().getDieVariable().set(value)
    self.selectDropDown(section, label)

  '''
  The following function responds to the user selecting an option from a drop down menu from the port set-up
  '''
  def respondToPortMenu(self, section, frame):
    return 0

  '''
  The following function repsonds to the user selecting the "Add" button in the "Feeders" section
  '''
  def addFeeder(self):
    print "addFeeder"

  '''
  The following function repsonds to the user selecting the type of cooling he/she would like to use
  '''
  def changeCooling(self, input):

    # If the input is the initial input created by the widget ignore it
    if isinstance(input, tk.IntVar):
      return 0

    # Destroy all elements on the strand cooling frame
    self.getGraphics().destroyAllWidgets(self.getGraphics().getStrandCoolingFrame())

    # Reset Labels
    sectionLabel = self.getGraphics().getLabels()[input[0]][input[0]]
    self.getGraphics().getLabels()[input[0]] = {input[0]: sectionLabel}

    # Check to see which option the user has selected an adjust accordingly
    cooling = self.getData().getStrandCoolingFrameVariable().get()
    if cooling is 1:
      self.getGraphics().buildSCBelt()
    elif cooling is 2:
      self.getGraphics().buildSCMister()
    elif cooling is 3:
      self.getGraphics().buildSCBath()
    elif cooling is 4:
      self.getGraphics().buildSCSprayBelt()
    elif cooling is 5 or cooling is 6:
      self.getGraphics().buildSCOther()

    # Check to see if the section title is red
    self.getGraphics().checkSectionLabels(input[0])

  '''
  The following function repsonds to the user clicking on the "air knives" checkbox
  '''
  def repsondToAirKnives(self):

    # Destroy all elements on the strand cooling frame
    self.getGraphics().destroyAllWidgets(self.getGraphics().getAirKnivesFrame())

    # check to see if the variable if 1 or 0
    if self.getData().getAirKnivesVariable().get():
      self.getGraphics().buildAirKnivesFrame()

  '''
  The following function responds to the user selecting options from the line of mister radio buttons
  '''
  def checkMisters(self, input):
    if not isinstance(input, tk.IntVar):
      return 0

  '''
  The following function responds to the user selecting an option from the "Pelletizier" drop down menu
  '''
  def changePellet(self, section, label):

    # Destroy all elements on the pellet mill frame
    self.getGraphics().destroyAllWidgets(self.getGraphics().getPelletMillFrame())
    self.getGraphics().setFeederSpeedScale(None)
    self.getGraphics().setPumpSpeedScale(None)

    # Check the variable to see if the pelletizier variable has changed to "Pellet Mill"
    if self.getData().getPelletizierVariable().get() == self.getConfig().PELLETIZIERS[2]:
      self.getGraphics().buildPelletMillFrame()

    # Check the label to see if it is red
    self.checkLabel([section, label])

  '''
  The following function responds to the user selecting an option from a dropdown menu and all that needs to happen is
  to check the label with the drop down menu
  '''
  def selectDropDown(self, section, label):
    self.checkLabel([section, label])

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
          label["foreground"] = self.getConfig().COMMENTS_COLOR
          self.getGraphics().checkSectionLabels(section)

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
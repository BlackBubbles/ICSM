#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/07/2017
Last Updated: 08/14/2017
Version: 1.0.0
Description:
    The following python file contains the model code functions for the "Extruder" panel for the ICSM program
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
The following class is the model for the "Extruder" panel
'''
class ExtruderD:

  '''
  The following function is the initial instance creation function for the "ExtruderD" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "ExtruderD" class
    self.graphics = None
    self.workflowFileName = None
    self.extruderVariable = None
    self.dieVariable = None
    self.preDieVariable = None
    self.screenVariable = None
    self.classifiedVariable = None
    self.pelletizierVariable = None
    self.strandCoolingFrameVariable = None

  '''
  The following function returns the configuration file for this instance of the "ExtruderD" class
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
          return False, "%s:\nconfig file for ExtruderD is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
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
        return False, "%s:\ngraphics for ExtruderD is not extruderGraphics" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function returns the file name of the workflow sheet that is currently being selected within the 
  "Extruder" panel
  '''
  def getWorkflowFileName(self):
    return self.workflowFileName

  '''
  The following function sets the file name of the workflow sheet that is currently being selected within the 
  "Extruder" panel.
  '''
  def setWorkflowFileName(self, workflowFileName):
    self.workflowFileName = workflowFileName

  '''
  The following function returns the variable for the extruder drop down menu
  '''
  def getExtruderVariable(self):
    return self.extruderVariable

  '''
  The following function sets the variable for the extruder drop down menu
  '''
  def setExtruderVariable(self, extruderVariable):
    self.extruderVariable = extruderVariable

  '''
  The following function returns the variable for the die options drop down menu
  '''
  def getDieVariable(self):
    return self.dieVariable

  '''
  The following function sets the variable for the die options drop down menu
  '''
  def setDieVariable(self, dieVariable):
    self.dieVariable = dieVariable

  '''
  The following function returns the variable for the pre-die drop down menu
  '''
  def getPreDieVariable(self):
    return self.preDieVariable

  '''
  The following function sets the variable for the pre-die drop down menu
  '''
  def setPreDieVariable(self, preDieVariable):
    self.preDieVariable = preDieVariable

  '''
  The following function returns the variable for the screen pack check box
  '''
  def getScreenPackVariable(self):
    return self.screenVariable

  '''
  The following function sets the variable for the screen pack check box
  '''
  def setScreenPackVariable(self, screenVariable):
    self.screenVariable = screenVariable

  '''
  The following function returns the variable for the classified radio buttons
  '''
  def getClassifiedVariable(self):
    return self.classifiedVariable

  '''
  The following function sets the variable for the classified radio buttons
  '''
  def setClassifiedVariable(self, classifiedVariable):
    self.classifiedVariable = classifiedVariable

  '''
  The following function returns the variable for the pelletizer drop down menu
  '''
  def getPelletizierVariable(self):
    return self.pelletizierVariable

  '''
  The following function sets the variable for the pelletizer drop down menu
  '''
  def setPelletizierVariable(self, pelletizierVariable):
    self.pelletizierVariable = pelletizierVariable

  '''
  The following function returns the variable for the strand cooling frame
  '''
  def getSrandCoolingFrameVariable(self):
    return self.strandCoolingFrameVariable

  '''
  The following function sets the variable for the strand cooling frame
  '''
  def setSrandCoolingFrameVariable(self, strandCoolingFrameVariable):
    self.strandCoolingFrameVariable = strandCoolingFrameVariable

  '''
  The following function checks the data to see if the data is ready to update the workflow .xlsx sheet
  '''
  def checkForUpdate(self):

    # Build the initial error variables and values
    ready = True
    errors = []
    errorTextLabels = {}

    # Check the Extruder Section
    errorTextLabels[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE] = []
    labels = errorTextLabels[self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE]

    # Check the Extruder drop down menu
    if self.getExtruderVariable().get() == self.getConfig().EXTRUDERS[0]:
      ready = False
      errors.append("Choose an \"Extruder\"\n")
      labels.append("Extruder")
    else:
      if self.getDieVariable().get() == self.getConfig().EXTRUDER_DIES[self.getExtruderVariable().get()][0]:
        ready = False
        errors.append("Choose a \"Die Option\"\n")
        labels.append("Die Options")
    if self.getPreDieVariable().get() == self.getConfig().PRE_DIE[0]:
      ready = False
      errors.append("Choose an \"Pre-Die Option\"\n")
      labels.append("Pre-Die")
    if not self.getGraphics().getMeshEntry().get():
      ready = False
      errors.append("Enter message into \"Mesh\"\n")
      labels.append("Mesh:")

    # Check the strand cooling section
    errorTextLabels[self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE] = []
    labels = errorTextLabels[self.getConfig().STRAND_COOLING_OPTIONS_SECTION_TITLE]

    # Check the strand cooling radio buttons on the top of the section frame
    if self.getSrandCoolingFrameVariable().get() is 0:
      ready = False
      errors.append("Choose a \"Strand Cooling\" method\n")
      labels.append("")
    else:

      # FINISH
      x = 0

    # Check the pelletizing section
    errorTextLabels[self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE] = []
    labels = errorTextLabels[self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE]

    # Check the pelletizier variable
    if self.getPelletizierVariable().get() == self.getConfig().PELLETIZIERS[0]:
      ready = False
      errors.append("Choose a \"Pelletizier\"\n")
      labels.append("Pelletizier")

    # Check the classified section
    errorTextLabels[self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE] = []
    labels = errorTextLabels[self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE]

    # Check the classified variable
    if self.getClassifiedVariable().get() is 0:
      ready = False
      errors.append("Choose a \"Classified\" option\n")
      labels.append("Classified:")

    # Return the error variables
    return ready, errors, errorTextLabels

  '''
  The following function updates the workflow .xlsx sheets
  '''
  def updateWorkflow(self):

    # Build the initial dictionary variable
    update = {}

    # Add the data on the Extruder Section
    section = self.getConfig().EXTRUDER_OPTIONS_SECTION_TITLE
    update[section] = {"Extruder": self.getExtruderVariable().get()}
    update[section]["Die"] = self.getDieVariable().get()
    update[section]["Pre-Die"] = self.getPreDieVariable().get()
    update[section]["Screen Pack"] = self.getScreenPackVariable().get()
    update[section]["Mesh"] = self.getGraphics().getMeshEntry().get()

    # Add the data on the Pelletizing Section
    section = self.getConfig().PELLETIZING_OPTIONS_SECTION_TITLE
    update[section] = {"Pelletizier": self.getPelletizierVariable().get()}
    update[section]["Feed Roll"] = self.getGraphics().getFeedRollScale().get()
    update[section]["Rotor"] = self.getGraphics().getRotorScale().get()
    if self.getPelletizierVariable().get() == self.getConfig().PELLETIZIERS[2]:
      update[section]["Feeder Speed"] = self.getGraphics().getFeederSpeedScale().get()
      update[section]["Pump Speed"] = self.getGraphics().getPumpSpeedScale().get()
    update[section]["Comments"] = self.getGraphics().getPelletizingComments().get(1.0, "end-1c")

    # Add the data on the Classified Section
    section = self.getConfig().CLASSIFIED_OPTIONS_SECTION_TITLE
    names = self.getConfig().CLASSIFIED_RADIO_BUTTON_NAMES
    update[section] = {"Classified": names[self.getClassifiedVariable().get() - 1]}

    # Send the Server the update dictionary
    print update

    # Wait for a response
    # FINISH CODE

    # Message the user on the results
    # FINISH CODE

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
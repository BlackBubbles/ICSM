#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/05/2017
Last Updated: 08/14/2017
Version: 1.0.0
Description:
    The following python file contains multiple interaction functions for the model of the program
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import frameData as frameD
from panels import quickAccessData as qaD
from panels import projectData as projectD
from panels import extruderData as extruderD
from panels import labData as labD

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the Model for the MVC for the ICSM program
'''
class Data:

  '''
  The following function is the initial instance creation function for the "Data" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "Data" class
    self.actions = None
    self.graphics = None
    doesWork, message = self.setFrameData(frameD.FrameD(self.getConfig().getConfigFrame()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setQAData(qaD.QAD(self.getConfig().getConfigQA()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setExtruderData(extruderD.ExtruderD(self.getConfig().getConfigExtruder()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setLabData(labD.LabD(self.getConfig().getConfigLab()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setProjectData(projectD.ProjectD(self.getConfig().getConfigProject()))
    if not doesWork:
      print message
      sys.exit()

  '''
  The following function returns the configuration file for this instance of the "Data" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for the "Data" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Data"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Data is not configData" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the instance of the "Action" class for this instance of the "Data" class
  '''
  def getActions(self):
    return self.actions

  '''
  The following function sets the instance of the "Action" class for the "Data" class. If the inputted Actions class
  file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setActions(self, first, actions):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "Actions" class
    if hasattr(actions, "confirm"):
      if actions.confirm("Actions"):
        self.actions = actions
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a Actions class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message

  '''
  The following function returns the instance of the "Graphics" class for this instance of the "Data" class
  '''
  def getGraphics(self):
    return self.graphics

  '''
  The following function sets the instance of the "Graphics" class for the "Data" class. If the inputted Graphics class
  file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setGraphics(self, first, graphics):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "Graphics" class
    if hasattr(graphics, "confirm"):
      if graphics.confirm("Graphics"):
        self.actions = graphics
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a Graphics class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
      self.getExtruderData().setGraphics(graphics.getExtruderGraphics())
    else:
      return doesWork, message

  '''
  The following function returns the model code for the GUI frame for this instance of the "Data" class
  '''
  def getFrameData(self):
    return self.frame

  '''
  The following function sets the model code for the GUI frame for this instance of the "Data" class. If the inputted
  argument does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setFrameData(self, frame):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "FrameD" class
    if hasattr(frame, "confirm"):
      if frame.confirm("Frame"):
        self.frame = frame
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a FrameD class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the model code for the "Quick Access" panel for this instance of the "Data" class
  '''
  def getQAData(self):
    return self.qa

  '''
  The following function sets the model code for the "Quick Access" panel for this instance of the "Data" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setQAData(self, qa):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "QAD" class
    if hasattr(qa, "confirm"):
      if qa.confirm("QA"):
        self.qa = qa
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a QAD class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the model code for the "Extruder" panel for this instance of the "Data" class
  '''
  def getExtruderData(self):
    return self.extruder

  '''
  The following function sets the model code for the "Extruder" panel for this instance of the "Data" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setExtruderData(self, extruder):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "ExtruderD" class
    if hasattr(extruder, "confirm"):
      if extruder.confirm("Extruder"):
        self.extruder = extruder
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a ExtruderD class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the model code for the "Lab" panel for this instance of the "Data" class
  '''
  def getLabData(self):
    return self.lab

  '''
  The following function sets the model code for the "Lab" panel for this instance of the "Data" class. If the inputted
  argument does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setLabData(self, lab):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "LabD" class
    if hasattr(lab, "confirm"):
      if lab.confirm("Lab"):
        self.lab = lab
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a LabD class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the model code for the "Project" panel for this instance of the "Data" class
  '''
  def getProjectData(self):
    return self.project

  '''
  The following function sets the model code for the "Project" panel for this instance of the "Data" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setProjectData(self, project):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "ProjectD" class
    if hasattr(project, "confirm"):
      if project.confirm("Project"):
        self.project = project
      else:
        doesWork = False
        message = "%s:\ninputted file for Data is not a ProjectD class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):

    # Check to make sure that the inputted value is a string that is equal to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "data":
        return True
      else:
        return False
    else:
      return False
#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/09/2017
Version: 1.0.0
Description:
    The following python file contains multiple interaction functions for the Graphical User Interface for the ICSM
    program
'''

'''
Imported files/libraries
'''
import sys
import Tkinter as tk
import ttk
from types import ModuleType
import frameGraphics as frameG
from add import browseServerGraphics as browseServerG
from add import feederGraphics as feederG
from add import TDIGraphics as TDIG
from components import GUIBuilder as build
from panels import quickAccessGraphics as qaG
from panels import extruderGraphics as extruderG
from panels import labGraphics as labG
from panels import projectGraphics as projectG

'''
Global Variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the View for the MVC for the ICSM program
'''
class Graphics:

  '''
  The following function is the initial instance creation function for the "Graphics" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set the rest of the initial "Graphics" class variables
    self.actions = None
    self.data = None
    doesWork, message = self.setFrameGraphics(frameG.FrameG(self.getConfig().getConfigFrame()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setBuilder(build.Builder(self.getConfig()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setQAGraphics(qaG.QAG(self.getConfig().getConfigQA()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setExtruderGraphics(extruderG.ExtruderG(self.getConfig().getConfigExtruder()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setLabGraphics(labG.LabG(self.getConfig().getConfigLab()))
    if not doesWork:
      print message
      sys.exit()
    doesWork, message = self.setProjectGraphics(projectG.ProjectG(self.getConfig().getConfigProject()))
    if not doesWork:
      print message
      sys.exit()
    self.gui = None

    # REMOVE SOON
    self.notebook = None
    self.frames = {}

  '''
  The following function returns the configuration file for the "Graphics" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for the "Graphics" class. If the inputted config file does not
  meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Graphics"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Graphics is not configGraphics" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the instance of the "Actions" class for the "Graphics" class
  '''
  def getActions(self):
    return self.actions

  '''
  The following function sets the instance of the "Actions" class for the "Graphics" class
  '''
  def setActions(self, first, actions):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted parameter is an instance of a "Actions" class
    if hasattr(actions, "confirm"):
      if actions.confirm("Actions"):
        self.actions = actions
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a Actions class file" % ERROR
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
  The following function returns the instance of the "Data" class for the "Graphics" class
  '''
  def getData(self):
    return self.data

  '''
  The following function sets the instance of the "Data" class for the "Graphics" class
  '''
  def setData(self, first, data):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted parameter is an instance of a "Data" class
    if hasattr(data, "confirm"):
      if data.confirm("Data"):
        self.data = data
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a Data class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Data class file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message

  '''
  The following function returns the view code for the GUI frame for this instance of the "Graphics" class
  '''
  def getFrameGraphics(self):
    return self.frame

  '''
  The following function sets the view code for the GUI frame for this instance of the "Graphics" class. If the 
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setFrameGraphics(self, frame):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "FrameG" class
    if hasattr(frame, "confirm"):
      if frame.confirm("Frame"):
        self.frame = frame
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a FrameG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the "browseServerGraphics" module
  '''
  def getBrowseServerGraphics(self):
    return browseServerG

  '''
  The following function returns the "feederGraphics" module
  '''
  def getFeederGraphics(self):
    return feederG

  '''
  The following function returns the instance of the "TDIGraphics" module
  '''
  def getTDIGraphics(self):
    return TDIG

  '''
  The following function returns the instance of the "Builder" class for this instance of the "Graphics" class
  '''
  def getBuilder(self):
    return self.builder

  '''
  The following function sets the builder for this instance of the "Graphics" class. If the inputted argument does not
  meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setBuilder(self, builder):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "Builder" class
    if hasattr(builder, "confirm"):
      if builder.confirm("Builder"):
        self.builder = builder
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a Builder class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the "Quick Access" panel for the GUI of the ICSM program
  '''
  def getQAGraphics(self):
    return self.qa

  '''
  The following function sets the view code for the "Quick Access" panel for this instance of the "Graphics" class. If 
  the inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setQAGraphics(self, qa):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "QAG" class
    if hasattr(qa, "confirm"):
      if qa.confirm("QA"):
        self.qa = qa
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a QAG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the "Extruder" panel for the GUI of the ICSM program
  '''
  def getExtruderGraphics(self):
    return self.extruder

  '''
  The following function sets the view code for the "Extruder" panel for this instance of the "Graphics" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''
  def setExtruderGraphics(self, extruder):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "ExtruderG" class
    if hasattr(extruder, "confirm"):
      if extruder.confirm("Extruder"):
        self.extruder = extruder
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a ExtruderG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the "Lab" panel for the GUI of the ICSM program
  '''
  def getLabGraphics(self):
    return self.lab

  '''
  The following function sets the view code for the "Lab" panel for this instance of the "Graphics" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''

  def setLabGraphics(self, lab):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "LabG" class
    if hasattr(lab, "confirm"):
      if lab.confirm("Lab"):
        self.lab = lab
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a LabG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
    The following function returns the "Project" panel for the GUI of the ICSM program
    '''

  def getProjectGraphics(self):
    return self.project

  '''
  The following function sets the view code for the "Project" panel for this instance of the "Graphics" class. If the
  inputted argument does not meet the requirements then the function returns a "False" boolean value and an error
  message
  '''

  def setProjectGraphics(self, project):

    # Create the initial return variables and their values
    doesWork = True
    message = ""

    # Check to make sure that the inputted value is an instance of the "ProjectG" class
    if hasattr(project, "confirm"):
      if project.confirm("Project"):
        self.project = project
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a ProjectG class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated ICSM class file for this program" % ERROR

    # Return boolean variable and error message
    return doesWork, message

  '''
  The following function returns the instance of the GUI for the "Graphics" class
  '''
  def getGUI(self):
    return self.gui

  '''
  The following function sets the instance of the GUI for the "Graphics" class
  '''
  def setGUI(self, gui):

    # Check to make sure that the inputted value is an instance of the Tkinter "Tk" class
    if isinstance(gui, tk.Tk):
      self.gui = gui
      return True, ""
    return False, "%s:\nGraphics could not create the GUI" % ERROR

  '''
  The following function is the initial GUI executable function for this python program.
  '''
  def buildGUI(self, error, value):

    # Initilize the GUI function
    doesWork, message = self.setGUI(tk.Tk())
    if not doesWork:
      print message
      sys.exit()

    # Build the GUI for the ICSM program, unless an error has occurred
    if error:

      # If there is an intial error, build a GUI showing the error
      self.getFrameGraphics().buildErrorGUI(self, value)

    else:

      # If everthing is working, then build the intial GUI for the ICSM program
      self.getFrameGraphics().buildGUIFrame(self)
      self.getQAGraphics().buildPanel(self)
      self.getExtruderGraphics().buildPanel(self)
      self.getLabGraphics().buildPanel(self)
      self.getProjectGraphics().buildPanel(self)

    # Activate the GUI
    self.getGUI().mainloop()

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):

    # Check to make sure that the inputted value is a string that is equal to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "graphics":
        return True
      else:
        return False
    else:
      return False

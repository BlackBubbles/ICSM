#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 07/06/2017
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
from components import GUIBuilder as build
from panels import quickAccessGraphics as qAG
from panels import updateGraphics as updateG
from panels import searchGraphics as searchG
from add import TDIGrpahics as TDIG
from add import browseServerGraphics as browseServerG
from add import feederGraphics as feederG

'''
Global Variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the View for the MVC for the IISM program
'''
class Graphics:
  
  '''
  The following function is the initial instance creation function for
  the "Graphics" class
  '''
  def __init__(self, config):
    
    # Call set functions and is the return is False, then return the
    # message for the error
    doesWork = True
    message = ""
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()
      
    # Set the rest of the initial "Graphics" class variables
    self.config = config
    self.actions = None
    self.data = None
    self.gui = None
    self.notebook = None
    self.frames = {}
    self.builder = build.Builder(config)
    self.qAG = None
    self.searchG = None
    self.updateG = None
    
  '''
  The following function returns the configuration file for the "Graphics"
  class
  '''
  def getConfig(self):
    return self.config
    
  '''
  The following function sets the configuration file for the "Graphics"
  class. If the inputted config file does not meet the requirements
  then the function returns a False and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, 'confirm'):
        if config.confirm("Graphics"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Graphics is not "\
                        "configGraphics" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file"\
                      " for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""
          
  '''
  The following function returns the instance of the "Actions" class for
  the "Graphics" class
  '''
  def getActions(self):
    return self.actions
    
  '''
  The following function sets the instance of the "Actions" class for
  the "Graphics" class
  '''
  def setActions(self, first, actions):
    
    # Create the initial return variables and their values
    doesWork = True
    message = ""
    
    # Check to make sure that the inputted parameter is an instance of a
    # class
    if hasattr(actions, 'confirm'):
      if actions.confirm("Actions"):
        self.actions = actions
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a Actions"\
                  " class file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Actions class"\
                " file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message
      
  '''
  The following function returns the instance of the "Data" class for
  the "Graphics" class
  '''
  def getData(self):
    return self.data
    
  '''
  The following function sets the instance of the "Data" class for
  the "Graphics" class
  '''
  def setData(self, first, data):
    
    # Create the initial return variables and their values
    doesWork = True
    message = ""
    
    # Check to make sure that the inputted parameter is an instance of a
    # class
    if hasattr(data, 'confirm'):
      if data.confirm("Data"):
        self.data = data
      else:
        doesWork = False
        message = "%s:\ninputted file for Graphics is not a Data class"\
                  " file" % ERROR
    else:
      doesWork = False
      message = "%s:\ninputted file is not a designated Data class"\
                " file for this program" % ERROR
    if first:
      if not doesWork:
        print message
        sys.exit()
    else:
      return doesWork, message
      
  '''
  The following function returns the instance of the "Actions" class for
  the "Graphics" class
  '''
  def getGUI(self):
    return self.gui
    
  '''
  The following function returns the instance of the GUI for the
  "Graphics" class
  '''
  def setGUI(self, gui):
    
    # Check to make sure that the inputted value is an instance of the
    # Tkinter "Tk" class
    if isinstance(gui, tk.Tk):
      self.gui = gui
      
  '''
  The following function returns the instance of the "tkk.notebook" for
  the IISM program
  '''
  def getNotebook(self):
    return self.notebook
    
  '''
  The following function sets the instance of the "tkk.Notebook" for the
  IISM program
  '''
  def setNotebook(self, notebook):
    if isinstance(notebook, ttk.Notebook):
      self.notebook = notebook
      
  '''
  The following function returns the instance of an array containing the
  frames for the GUI for the "Graphics" class
  '''
  def getFrames(self):
    return self.frames
    
  '''
  The following function sets the instance of an array containing the
  frames for the GUI for the "Graphics" class
  '''
  def setFrames(self, frames):
    
    # Check to make sure that the inputted list is within the acceptable
    # terms of criteria
    test = True
    if isinstance(frames, dict):
      for frame in frames.values():
        if not isinstance(frame, ttk.Frame):
          test = False
          break;
    else:
      test = False
      
    # If everything checks out then set the inputted parameter
    if test:
      self.frames = frames
      
  '''
  The following function returns the a specific value of an array
  containing the frames for the GUI for the "Graphics" class
  '''
  def getFrame(self, key):
    return self.frames.get(key)
    
  '''
  The following function sets the a specific value of an array containing
  the frames for the GUI for the "Graphics" class
  '''
  def setFrame(self, key, value):
    if isinstance(frames[key], ttk.Frame):
      self.frames[key] = value
      
  '''
  The following function returns the instance of the "Builder" class for
  this instance of the "Graphics" class
  '''
  def getBuilder(self):
    return self.builder
    
  '''
  The following function returns the quick acces panel for the GUI of the
  IISM program
  '''
  def getQuickAccessPanel(self):
    return self.qAG
    
  '''
  COMMENT
  '''
  def getSearchPanel(self):
    return self.searchG
    
  '''
  COMMENT
  '''
  def getUpdatePanel(self):
    return self.updateG
    
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
  The following function is the initial GUI executable function for this 
  python program.
  '''
  def buildGUI(self, error, value):
    
    # Initilize the GUI function
    self.setGUI(tk.Tk())
    
    # Build the GUI for the IISM program, unless an error has occurred
    if error:
      
      # If there is an intial error, build a GUI showing the error
      frameG.buildErrorFrame(self)
      frameG.buildErrorPanel(self, value)
      
    else:
      
      # If everthing is working, then build the intial GUI for the IISM
      # program
      frameG.buildGUIFrame(self)
      frames, nb = frameG.buildTDI(self, self.getConfig())
      self.setFrames(frames)
      self.setNotebook(nb)
      '''
      self.qAG = qAG.QAG(self, self.getBuilder())
      self.qAG.buildPanel()
      self.searchG = searchG.SearchG(self, self.getBuilder())
      self.searchG.buildPanel()
      self.updateG = updateG.UpdateG(self, self.getBuilder())
      self.updateG.buildPanel()
      '''
      
    # Activate the GUI
    self.getGUI().mainloop()
    
  '''
  The following function returns a confirmation that tells the calling 
  code which class file this function belongs to
  '''
  def confirm(self, value):
    
    # Check to make sure that the inputted value is a string that is equal
    # to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "graphics":
        return True
      else:
        return False
    else:
      return False

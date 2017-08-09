#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/24/2017
Last Updated: 08/09/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Quick Access" panel
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
The following python class contains the functions that contains the components for the "Quick Access" panel
'''
class QAG:
  
  '''
  The following function is the initial function for the "QAG" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "QAG" class
    self.buttons = {}

  '''
  The following function returns the configuration file for this instance of the "QAG" class
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
        if config.confirm("QA"):
          self.config = config
        else:
          return False, "%s:\nconfig file for QAG is not configQuickAccess" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  the following function returns the dictionary of buttons that are on the "Quick Access" panel
  '''
  def getButtons(self):
    return self.buttons

  '''
  the following function sets the dictionary of buttons that are on the "Quick Access" panel. If the inputted dict does
  not meet the requirements, the function will return a "False" boolean value and an error message
  '''
  def setButtons(self, buttons):

    # Create the initial return variables and values
    doesWork = True
    message = ""

    # Check each button in buttons to make sure that each is an instance of tk.Button
    for image, button in buttons.iteritems():
      if not isinstance(button, tk.Button):
        doesWork = False
        message = "%s:\nbutton for QAG.buttons is not an instance of tk.Button" % ERROR

    # If nothing is wrong set the inputted frames
    if doesWork:
      self.buttons = buttons

    # Return the variable
    return doesWork, message

  '''
  The following function builds the initial state for the "Quick Access" panel
  '''
  def buildPanel(self, graphics):

    # Get the "Quick Access" frame from the instance of the "Graphics" class
    frame = graphics.getFrameGraphics().getFrame(graphics.getConfig().getConfigFrame().QUICK_ACCESS)
    
    # Change the background color
    panel = graphics.getBuilder().buildFrame(frame)
    panel.pack(fill=tk.BOTH, expand=1)
    
    # Add the four default buttons
    buttons = {}
    for i in range(0, self.getConfig().NUM_OF_ROWS_OF_BUTTONS):
      for j in range(0, self.getConfig().NUM_OF_COLUMNS_OF_BUTTONS):
        text = str(i) + ", " + str(j)
        button = graphics.getBuilder().buildButton(panel, text)
        button.configure(width=10, height=5)
        button.grid(row=i, column=j, padx=(50, 0), pady=(50, 0), sticky=tk.W)
        buttons[text] = button
    self.setButtons(buttons)

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):

    # Check to make sure that the inputted value is a string that is equal to the representaion of the class file
    if isinstance(value, basestring):
      if value.lower() == "qa":
        return True
      else:
        return False
    else:
      return False
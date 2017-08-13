#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/11/2017
Version: 1.0.0
Description:
    The following python file contains the configuration data for the Graphical User Interface
'''

'''
Imported files/libraries
'''
import configFrame as configF
from panels import configQuickAccess as configQA
from panels import configExtruder as configE
from panels import configLab as configL
from panels import configProject as configP

'''
Global variables
'''
'''
The following variable contains the active background color for the GUI
'''
ACTIVE_BACKGROUND = "#0099ff"

'''
The following variable contains the background color for the GUI
'''
BACKGROUND = "#ffffff"

'''
The following variable contains the default text for the browse button label that displays information to the user
'''
BROWSE_BUTTON_TEXT = "Browse"

'''
The following variable contains the default label for the browse button label that displays information to the user
'''
BROWSE_LABEL_TEXT = "Browse for workflow ..."

'''
The following variable contains the default height for buttons for the ICSM program
'''
BUTTON_HEIGHT = 1

'''
The following variable contains the default width for buttons for the ICSM program
'''
BUTTON_WIDTH = 8

'''
The following variable contains the font size for titles of size h1
'''
H1_FONT_SIZE = 24

'''
The following variable contains the font size for titles of size h2
'''
H2_FONT_SIZE = 20

'''
The following variable contains the font size for titles of size h2
'''
H3_FONT_SIZE = 16

'''
The following variable contains the color of the separation line
'''
LINE_COLOR = "#000000"

'''
The following variable contains the line width of the separation line
'''
LINE_HIEGHT = 2

'''
The following variable contains the font size for the panel title
'''
PANEL_TITLE_FONT_SIZE = 24

'''
The following function returns the configuration module for the GUI frame
'''
def getConfigFrame():
  return configF

'''
The following function returns the configuration module for the "Quick Access" panel
'''
def getConfigQA():
  return configQA

'''
The following function returns the configuration module for the "Extruder" panel
'''
def getConfigExtruder():
  return configE

'''
The following function returns the configuration module for the "Lab" panel
'''
def getConfigLab():
  return configL

'''
The following function returns the configuration module for the "Project" panel
'''
def getConfigProject():
  return configP
  
'''
The following function returns a confirmation that tells the calling code which configuration file this function
belongs to
'''
def confirm(value):
  
  # Check to make sure that the inputted value is a string that is equal to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "graphics":
      return True
    else:
      return False
  else:
    return False
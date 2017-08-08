#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/08/2017
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

# REMOVE SOON
from panels import configUpdate as update
from panels import configSearch as search

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
BROWSE_LABEL = "Browse for workflow ..."

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
H1_FONT_SIZE = 14

'''
The following variable contains the font size for titles of size h2
'''
H2_FONT_SIZE = 11

'''
REMOVE SOON
'''
HEIGHT = 500

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
REMOVE SOON
'''
QUICK_ACCESS = "+"

'''
REMOVE SOON
'''
RIGHT_CLICK_QA_MENU = ["Update", "Search"]

'''
REMOVE SOON
'''
RIGHT_CLICK_TDI_MENU = ["Undo Close Tab"]

'''
REMOVE SOON
'''
STARTING_TDI = ["Update", "Search"]

'''
REMOVE SOON
'''
TDI_BACKGROUND_COLOR = "#eeeeee"

'''
REMOVE SOON
'''
TDI_EXPAND = [1, 1, 1, 0]

'''
REMOVE SOON
'''
TDI_PADDING = [20, 5]

'''
REMOVE SOON
'''
TDI_SELECTED_COLOR = "#0099ff"

'''
REMOVE SOON
'''
TDI_TAB_MARGINS = [0, 0, 0, 0]

'''
REMOVE SOON
'''
TITLE = "Interfacial Consultant's Systems and Management - ICSM"

'''
REMOVE SOON
'''
WIDTH = 800

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
REMOVE SOON
'''
def getConfigUpdate():
  return update
  
'''
REMOVE SOON
'''
def getConfigSearch():
  return search
  
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
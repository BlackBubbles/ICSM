#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/07/2017
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
BROWSE_LABEL = "Browse for file ..."

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
The following variable contains the starting height for the GUI.
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
The following variable contains the default string used on the Quick Access tab
'''
QUICK_ACCESS = "+"

'''
The following variable contains a list of the menu options when the user right clicks on the QA tab
'''
RIGHT_CLICK_QA_MENU = ["Update", "Search"]

'''
The following variable contains a list of the menu options when the user right clicks on the TDI
'''
RIGHT_CLICK_TDI_MENU = ["Undo Close Tab"]

'''
The following variable contains a list of the starting TDI panel titles
'''
STARTING_TDI = ["Update", "Search"]

'''
The following variable contains the TDI unselected tab color in HEX. This one is a very light grey
'''
TDI_BACKGROUND_COLOR = "#eeeeee"

'''
The following variable contains the data that determines how much the TDI tab will grow while being selected.
'''
TDI_EXPAND = [1, 1, 1, 0]

'''
The following variable contains the padding spacing around the string titles in the tabs
'''
TDI_PADDING = [20, 5]

'''
The following variable contains the TDI selected tab color in HEX. This color is a light blue
'''
TDI_SELECTED_COLOR = "#0099ff"

'''
The following variable contains the margin spaces around the panels for each tab.
'''
TDI_TAB_MARGINS = [0, 0, 0, 0]

'''
The following variable contains the title for the GUI
'''
TITLE = "Interfacial Consultant's Systems and Management - ICSM"

'''
The following variable contains the starting width for the GUI.
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
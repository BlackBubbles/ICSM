#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 08/08/2017
Last Updated: 08/08/2017
Version: 1.0.0
Description:
    The following python file contains the configuration data for the GUI frame
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
'''
The following variable contains the starting height for the GUI.
'''
HEIGHT = 500

'''
The following variable contains the default string used on the Quick Access tab
'''
QUICK_ACCESS = "+"

'''
The following variable contains a list of the menu options when the user right clicks on the QA tab
'''
RIGHT_CLICK_QA_MENU = ["Project", "Extruder", "Lab"]

'''
The following variable contains a list of the menu options when the user right clicks on the TDI
'''
RIGHT_CLICK_TDI_MENU = ["Undo Close Tab"]

'''
The following variable contains a list of the starting TDI panel titles
'''
STARTING_TDI = ["Project", "Extruder", "Lab"]

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
The following function returns a confirmation that tells the calling code which configuration file this function
belongs to
'''
def confirm(value):

  # Check to make sure that the inputted value is a string that is equal to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "frame":
      return True
    else:
      return False
  else:
    return False
#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 08/09/2017
Version: 1.0.0
Description:
    The following python file contains the reaction functions for the "Extruder" panel for the GUI in the ICSM program
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
# NONE

'''
The following function calls the "browseServer" function in the Graphics the all the user to browse for a file
'''
def callBrowseServer(graphics, title, label):
  graphics.getBrowseServerGraphics().browseServer(graphics, title, label)
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
The following function calls the "" function in the Graphics to allow the user to add a feeder to the "Extruder"
panel
'''
def addFeeder(graphics):
  print "addFeeder"

'''
The following function calls the "browseServer" function in the Graphics to allow the user to browse for a file
'''
def callBrowseServer(graphics, title, label):
  filename = graphics.getBrowseServerGraphics().browseServer(graphics, title, label)
  graphics.getData().getExtruderData().setWorkflowFileName(filename)

'''
The following function calls the "" function in the Graphics to allow the user to add a feeder to the Ex
'''
def changeCooling(graphics, value):
  print "changeCooling - ", value

'''
The following function calls the "" function in the Graphics to repsond to the user selecting an option from the
"Pelletizier" drop down menu
'''
def changePellet(graphics, value):
  print "changePellet - ", value
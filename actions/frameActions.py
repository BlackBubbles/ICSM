#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 06/24/2017
Version: 0.0.1
Description:
    The following python file contains the controller options for the
    programs GUI frame
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
The following function calls the "showMenuDropDown" function in the
graphics to show the quick access drop down menu to the user
'''
def showMenuDropDown(graphics, event, config, QAMenu, TDIMenu):
  graphics.getTDIGraphics().showMenuDropDown(
                              event, config, QAMenu, TDIMenu)

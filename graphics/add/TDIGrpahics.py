#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 03/29/2017
Version: 1.0.0
Description:
    The following python file contains the code that adds the quick access drop down menu for the TDI
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
The following function shows the TDI drop down menus to the user based on where the user clicked on the notebook
'''
def showMenuDropDown(event, config, QAMenu, TDIMenu):
  
  # Check to make sure that only the quick access tab is being clicked on
  if event.widget.identify(event.x, event.y) == 'label' or\
      event.widget.identify(event.x, event.y) == 'padding':
    index = event.widget.index('@%d,%d' % (event.x, event.y))
    if event.widget.tab(index, 'text') == config.QUICK_ACCESS:
      
      # Show the Quick Access drop down menu
      QAMenu.post(event.x_root, event.y_root)
      
    # If the quick access tab is not being clicked on then post the default menu for the TDI
    else:
      TDIMenu.post(event.x_root, event.y_root)
  else:
    TDIMenu.post(event.x_root, event.y_root)

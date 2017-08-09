#!/usr/bin/python

"""
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/09/2017
Version: 1.0.0
Description:
    The following python file contains the initial main function for the ICSM program
"""

'''
Imported config files
'''
from config import configActions as configA
from config import configData as configD
from config import configGraphics as configG

'''
Imported test files
'''
from test import testActions as testA
from test import testData as testD
from test import testGraphics as testG
from test import testFrame as testFr
from test import testQuickAccess as testQ
from test import testExtruder as testE
from test import testLab as testL
from test import testProject as testP
from test import testFunctions as testF

'''
Imported files/libraries
'''
from actions import actions
from data import data
from graphics import graphics

'''
Global variables
'''
# NONE

'''
The following function calls a designated test function with the config parameter file
'''
def __test(test, testF, config, graphic):
  
  # Initialize varaible values
  doesWork = False
  message = ""
  
  # Call the "test" function
  doesWork, message = test.test(testF, config)
  
  # If the test failed, then call the "buildGUI" function to build a GUI message for the error
  if not doesWork:
    graphic.buildGUI(True, message)
    
  # Return the value that states whether the test succeeded or not
  return doesWork
  
'''
The following function is the initial main executable function for this python file.
'''
if __name__ == "__main__":
  
  # Create all parts of the MVC protocol
  action = actions.Actions(configA)
  data = data.Data(configD)
  graphic = graphics.Graphics(configG)
  
  # Create all links
  action.setData(True, data)
  action.setGraphics(True, graphic)
  data.setActions(True, action)
  graphic.setActions(True, action)
  graphic.setData(True, data)
  
  # Call all test functions to make sure that nothing is wrong with the program
  doesWork = True
  if doesWork:
    doesWork = __test(testA, testF, configA, graphic)
  if doesWork:
    doesWork = __test(testD, testF, configD, graphic)
  if doesWork:
    doesWork = __test(testG, testF, configG, graphic)
  if doesWork:
    doesWork = __test(testFr, testF, configG.getConfigFrame(), graphic)
  if doesWork:
    doesWork = __test(testQ, testF, configG.getConfigQA(), graphic)
  if doesWork:
    doesWork = __test(testE, testF, configG.getConfigExtruder(), graphic)
  if doesWork:
    doesWork = __test(testL, testF, configG.getConfigLab(), graphic)
  if doesWork:
    doesWork = __test(testP, testF, configG.getConfigProject(), graphic)

  # Open Credentials GUI
  # FINISH CODE

  # Run the Program if everything works
  if doesWork:
    graphic.buildGUI(False, None)
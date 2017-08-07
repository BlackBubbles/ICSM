#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/05/2017
Last Updated: 08/07/2017
Version: 1.0.0
Description:
    The following python file contains the code that tests the Graphica User Interface to make sure that nothing is
    initially wrong
'''

'''
Imported files/libraries
'''
from types import ModuleType

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"
  
'''
the following function that tests out to make sure that nothing is wrong with the "configGraphics.py" file
'''
def __testConfig(testF, config):
  
  # Set up return variables
  doesWork = False
  message = ""
  
  # Test config.ACTIVE_BACKGROUND
  doesWork, message = testF.testConfigColors(config.ACTIVE_BACKGROUND, "configGraphics.ACTIVE_BACKGROUND")
  if not doesWork:
    return doesWork, message
    
  # Test config.BACKGROUND
  doesWork, message = testF.testConfigColors(config.BACKGROUND, "configGraphics.BACKGROUND")
  if not doesWork:
    return doesWork, message
    
  # Test config.BROWSE_BUTTON_TEXT
  doesWork, message = testF.testConfigString(config.BROWSE_BUTTON_TEXT, "configGraphics.BROWSE_BUTTON_TEXT")
  if not doesWork:
    return doesWork, message
    
  # Test config.BROWSE_LABEL
  doesWork, message = testF.testConfigString(config.BROWSE_LABEL, "configGraphics.BROWSE_LABEL")
  if not doesWork:
    return doesWork, message
    
  # Test config.BUTTON_HEIGHT
  doesWork, message = testF.testConfigPosInt(config.BUTTON_HEIGHT, "configGraphics.BUTTON_HEIGHT")
  if not doesWork:
    return doesWork, message
    
  # Test config.BUTTON_WIDTH
  doesWork, message = testF.testConfigPosInt(config.BUTTON_WIDTH, "configGraphics.BUTTON_WIDTH")
  if not doesWork:
    return doesWork, message
    
  # Test config.H1_FONT_SIZE
  doesWork, message = testF.testConfigPosInt(config.H1_FONT_SIZE, "configGraphics.H1_FONT_SIZE")
  if not doesWork:
    return doesWork, message
    
  # Test config.H2_FONT_SIZE
  doesWork, message = testF.testConfigPosInt(config.H2_FONT_SIZE, "configGraphics.H2_FONT_SIZE")
  if not doesWork:
    return doesWork, message
    
  # Test config.HEIGHT
  doesWork, message = testF.testConfigPosInt(config.HEIGHT, "configGraphics.HEIGHT")
  if not doesWork:
    return doesWork, message
    
  # Test config.LINE_COLOR
  doesWork, message = testF.testConfigColors(config.LINE_COLOR, "configGraphics.LINE_COLOR")
  if not doesWork:
    return doesWork, message
    
  # Test config.LINE_HIEGHT
  doesWork, message = testF.testConfigPosInt(config.LINE_HIEGHT, "configGraphics.LINE_HIEGHT")
  if not doesWork:
    return doesWork, message
    
  # Test config.PANEL_TITLE_FONT_SIZE
  doesWork, message = testF.testConfigPosInt(config.PANEL_TITLE_FONT_SIZE, "configGraphics.PANEL_TITLE_FONT_SIZE")
  if not doesWork:
    return doesWork, message
    
  # Test config.QUICK_ACCESS
  doesWork, message = testF.testConfigString(config.QUICK_ACCESS, "configGraphics.QUICK_ACCESS")
  if not doesWork:
    return doesWork, message
    
  # Test config.RIGHT_CLICK_QA_MENU
  doesWork, message = testF.testConfigListString(config.RIGHT_CLICK_QA_MENU, "configGraphics.RIGHT_CLICK_QA_MENU")
  if not doesWork:
    return doesWork, message
    
  # Test config.RIGHT_CLICK_TDI_MENU
  doesWork, message = testF.testConfigListString(config.RIGHT_CLICK_TDI_MENU, "configGraphics.RIGHT_CLICK_TDI_MENU")
  if not doesWork:
    return doesWork, message
    
  # Test config.STARTING_TDI
  doesWork, message = testF.testConfigListString(config.STARTING_TDI, "configGraphics.STARTING_TDI")
  if not doesWork:
    return doesWork, message
    
  # Test config.TDI_BACKGROUND_COLOR
  doesWork, message = testF.testConfigColors(config.TDI_BACKGROUND_COLOR, "configGraphics.TDI_BACKGROUND_COLOR")
  if not doesWork:
    return doesWork, message
    
  # Test config.TDI_EXPAND
  doesWork, message = testF.testConfigListPosInt(config.TDI_EXPAND, 4, "configGraphics.TDI_EXPAND")
  if not doesWork:
    return doesWork, message
    
  # Test config.TDI_PADDING
  doesWork, message = testF.testConfigListPosInt(config.TDI_PADDING, 2, "configGraphics.TDI_PADDING")
  if not doesWork:
    return doesWork, message
    
  # Test config.TDI_SELECTED_COLOR
  doesWork, message = testF.testConfigColors(config.TDI_SELECTED_COLOR, "configGraphics.TDI_SELECTED_COLOR")
  if not doesWork:
    return doesWork, message
    
  # Test config.TDI_TAB_MARGINS
  doesWork, message = testF.testConfigListPosInt(config.TDI_TAB_MARGINS, 4, "configGraphics.TDI_TAB_MARGINS")
  if not doesWork:
    return doesWork, message
    
  # Test config.TITLE
  doesWork, message = testF.testConfigString(config.TITLE, "configGraphics.TITLE")
  if not doesWork:
    return doesWork, message
    
  # Test config.WIDTH
  doesWork, message = testF.testConfigPosInt(config.WIDTH, "configGraphics.WIDTH")
  if not doesWork:
    return doesWork, message
    
  # If there are no problems found with the config file for the GUI, then return the proper values
  return True, ""
  
'''
Initial test function for the Graphical User Interface that calls all the private functions within this file
'''
def test(testF, config):
  
  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Graphics"):
        return False, "%s:\nconfig file for Graphics is not configGraphics" % ERROR
    else:
      return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
  else:
    return False, "%s:\ninputted file is not a Module" % ERROR
  
  # Call the "__testConfig" function to test the config file
  doesWork = False
  message = ""
  doesWork, message = __testConfig(testF, config)
  
  # If there are no problems found with the config file for the GUI, then return the proper values
  return doesWork, message

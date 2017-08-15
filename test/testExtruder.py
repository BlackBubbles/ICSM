#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/21/2017
Last Updated: 08/15/2017
Version: 1.0.0
Description:
    The following python file tests the code for the "Extruder" panel
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
function that tests out to make sure that nothing is wrong with the "configExtruder.py" file
'''
def __testConfig(testF, config):

  # Set up return variables
  doesWork = False
  message = ""

  # Test config.ACTIVE_BACKGROUND
  doesWork, message = testF.testConfigColors(config.ACTIVE_BACKGROUND, "configExtruder.ACTIVE_BACKGROUND")
  if not doesWork:
    return doesWork, message

  # Test config.CAPTURING_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.CAPTURING_SECTION_TITLE,
                                             "configExtruder.CAPTURING_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.CLASSIFIED_OPTIONS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.CLASSIFIED_OPTIONS_SECTION_TITLE,
                                             "configExtruder.CLASSIFIED_OPTIONS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.CLASSIFIED_RADIO_BUTTON_NAMES
  doesWork, message = testF.testConfigListString(config.CLASSIFIED_RADIO_BUTTON_NAMES,
                                                 "configExtruder.CLASSIFIED_RADIO_BUTTON_NAMES")
  if not doesWork:
    return doesWork, message

  # Test config.COMMENTS_COLOR
  doesWork, message = testF.testConfigColors(config.COMMENTS_COLOR, "configExtruder.COMMENTS_COLOR")
  if not doesWork:
    return doesWork, message

  # Test config.ERROR_COLOR
  doesWork, message = testF.testConfigColors(config.ERROR_COLOR, "configExtruder.ERROR_COLOR")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDERS
  doesWork, message = testF.testConfigListString(config.EXTRUDERS, "configExtruder.EXTRUDERS")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDER_DIES
  doesWork, message = testF.testConfigDicString(config.EXTRUDER_DIES, "configExtruder.EXTRUDER_DIES")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDER_OPTIONS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.EXTRUDER_OPTIONS_SECTION_TITLE,
                                             "configExtruder.EXTRUDER_OPTIONS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDER_PORT_SIZES
  doesWork, message = testF.testConfigDicInt(config.EXTRUDER_PORT_SIZES, "configExtruder.EXTRUDER_PORT_SIZES")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDER_PORT_SPOTS
  doesWork, message = testF.testConfigDicInt(config.EXTRUDER_PORT_SPOTS, "configExtruder.EXTRUDER_PORT_SPOTS")
  if not doesWork:
    return doesWork, message

  # Test config.EXTRUDER_SIDE_SPOTS
  doesWork, message = testF.testConfigDicInt(config.EXTRUDER_SIDE_SPOTS, "configExtruder.EXTRUDER_SIDE_SPOTS")
  if not doesWork:
    return doesWork, message

  # Test config.FEEDERS
  doesWork, message = testF.testConfigListString(config.FEEDERS, "configExtruder.FEEDERS")
  if not doesWork:
    return doesWork, message

  # Test config.FEEDER_SCREWS
  doesWork, message = testF.testConfigDicString(config.FEEDER_SCREWS, "configExtruder.FEEDER_SCREWS")
  if not doesWork:
    return doesWork, message

  # Test config.FEEDERS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.FEEDERS_SECTION_TITLE, "configExtruder.FEEDERS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.FEEDER_TUBES
  doesWork, message = testF.testConfigDicString(config.FEEDER_TUBES, "configExtruder.FEEDER_TUBES")
  if not doesWork:
    return doesWork, message

  # Test config.NUM
  doesWork, message = testF.testConfigListPosInt(config.NUM, 5, "configExtruder.NUM")
  if not doesWork:
    return doesWork, message

  # Test config.NUM_NO_ZERO
  doesWork, message = testF.testConfigListPosInt(config.NUM_NO_ZERO, 4, "configExtruder.NUM_NO_ZERO")
  if not doesWork:
    return doesWork, message

  # Test config.PELLETIZIERS
  doesWork, message = testF.testConfigListString(config.PELLETIZIERS, "configExtruder.PELLETIZIERS")
  if not doesWork:
    return doesWork, message

  # Test config.PELLETIZING_OPTIONS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.PELLETIZING_OPTIONS_SECTION_TITLE,
                                             "configExtruder.PELLETIZING_OPTIONS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.PORT_OPTIONS
  doesWork, message = testF.testConfigListString(config.PORT_OPTIONS, "configExtruder.PORT_OPTIONS")
  if not doesWork:
    return doesWork, message

  # Test config.PORT_OPTIONS_11MM
  doesWork, message = testF.testConfigListString(config.PORT_OPTIONS_11MM, "configExtruder.PORT_OPTIONS_11MM")
  if not doesWork:
    return doesWork, message

  # Test config.PORT_OPTIONS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.PORT_OPTIONS_SECTION_TITLE,
                                             "configExtruder.PORT_OPTIONS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.PRE_DIE
  doesWork, message = testF.testConfigListString(config.PRE_DIE, "configExtruder.PRE_DIE")
  if not doesWork:
    return doesWork, message

  # Test config.SIDE_STUFFER
  doesWork, message = testF.testConfigListString(config.SIDE_STUFFER, "configExtruder.SIDE_STUFFER")
  if not doesWork:
    return doesWork, message

  # Test config.SIDE_STUFFER_WITHOUT_VACCUM
  doesWork, message = testF.testConfigListString(config.SIDE_STUFFER_WITHOUT_VACCUM,
                                                 "configExtruder.SIDE_STUFFER_WITHOUT_VACCUM")
  if not doesWork:
    return doesWork, message

  # Test config.STRAND_COOLING_OPTIONS
  doesWork, message = testF.testConfigListString(config.STRAND_COOLING_OPTIONS,
                                                 "configExtruder.STRAND_COOLING_OPTIONS")
  if not doesWork:
    return doesWork, message

  # Test config.STRAND_COOLING_OPTIONS_SECTION_TITLE
  doesWork, message = testF.testConfigString(config.STRAND_COOLING_OPTIONS_SECTION_TITLE,
                                             "configExtruder.STRAND_COOLING_OPTIONS_SECTION_TITLE")
  if not doesWork:
    return doesWork, message

  # Test config.TITLE
  doesWork, message = testF.testConfigString(config.TITLE, "configExtruder.TITLE")
  if not doesWork:
    return doesWork, message

  # If there are no problems found with the config file for the GUI panel, then return the proper values
  return True, ""

'''
Initial test function that calls all the private functions within this function
'''
def test(testF, config):

  # Check to make sure that the imputted config file is indeed a config file and is the correct config file
  if isinstance(config, ModuleType):
    if hasattr(config, "confirm"):
      if not config.confirm("Extruder"):
        return False, "%s:\nconfig file for Extruder is not configExtruder" % ERROR
    else:
      return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
  else:
    return False, "%s:\ninputted file is not a Module" % ERROR

  # Call the "__testConfig" function to test the config file
  doesWork, message = __testConfig(testF, config)

  # Return the value that determines wheather or not the test worked
  return doesWork, message
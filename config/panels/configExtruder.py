#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/20/2017
Last Updated: 08/10/2017
Version: 1.0.0
Description:
    The following python file contains the configuration data for the "Extruder" panel
'''

'''
Imported files/libraries
'''
# NONE

'''
Global variables
'''
'''
The following string variable contains the title for the add feeders section within the "Extruder" panel
'''
CAPTURING_SECTION_TITLE = "Capturing Options"

'''
The following string variable contains the title for the extruder options section within the "Extruder" panel
'''
CLASSIFIED_OPTIONS_SECTION_TITLE = "Classified Options"

'''
The following list contains all the possible extruders that the user can choose
'''
EXTRUDERS = ["Select", "Process 11mm", "27mm Entek", "27mm Leistritz", "33mm Entek", "35mm Leistritz"]

'''
The following dictionary contains all the possible die options for each extruder that the user can choose
'''
EXTRUDER_DIES = {
  "Select": ["None"],
  "Process 11mm": ["Select", "1-0.5mm", "1-1mm", "1-2mm", "1-2.5mm", "1-3mm"],
  "27mm Entek": ["Select", "2-4.5mm", "3-3mm", "3-4.5mm", "3-5mm", "5-2mm", "7-1mm"],
  "27mm Leistritz": ["Select", "3-3mm", "5-3mm"],
  "33mm Entek": ["Select", "7-4.5mm", "10-3.5mm", "16-2mm"],
  "35mm Leistritz": ["Select", "7-4.5mm", "10-3.5mm", "16-2mm"]}

'''
The following string variable contains the title for the extruder options section within the "Extruder" panel
'''
EXTRUDER_OPTIONS_SECTION_TITLE = "Extruder Options"

'''
The following list contains all the possible feeder types that the user can choose
'''
FEEDERS = ["Select", "Process 11", "FW40", "DDSR", "K-tron S60-S120", "K-tron S60-S60"]

'''
The following dictionary contains all the possible screw options for each feeder that the user can choose
'''
FEEDER_SCREWS = {
  "Select": ["None"],
  "Process 11": ["Select", "Pigtail", "Std"],
  "FW40": ["Select", "18/13", "18/19", "20/15", "22/37", "43/43"],
  "DDSR": ["Select", "Pigtail", "Sm", "Lg"],
  "K-tron S60-S120": ["Select", "15", "25 fine", "25 course", "40 fine", "40 course"],
  "K-tron S60-S60": ["Select", "15", "25 fine", "25 course", "40 fine", "40 course"]}

'''
The following string variable contains the title for the add feeders section within the "Extruder" panel
'''
FEEDERS_SECTION_TITLE = "Feeders"

'''
The following dictionary contains all the possible tube options for each feeder that the user can choose
'''
FEEDER_TUBES = {
  "Select": ["None"],
  "Process 11": ["None"],
  "FW40": ["Select", "28", "32", "48"],
  "DDSR": ["None"],
  "K-tron S60-S120": ["Select", "15", "25", "40", "60"],
  "K-tron S60-S60": ["Select", "15", "25", "40", "60"]}

'''
The following list contains the numbers from 0 to 4
'''
NUM = [0, 1, 2, 3, 4]

'''
The following list contains all the possible pelletizing options that the user can choose
'''
PELLETIZIERS = ["Select", "Thermo", "Pellet Mill", "Red Eng Bullet 62", "Red Eng Bullet 64", "Red Eng Bullet 66"]

'''
The following string variable contains the title for the pelletizing options section within the "Extruder" panel
'''
PELLETIZING_OPTIONS_SECTION_TITLE = "Pelletizier Options"

'''
The following list contains all the possible options for each port on the extruder that the user can choose
'''
PORT_OPTIONS = ["Closed", "Vent", "Vaccum"]

'''
The following list contains all the possible options for each port on the "Process 11mm" extruder that the user can
choose
'''
PORT_OPTIONS_11MM = ["Closed", "Vent", "Feed Throat"]

'''
The following string variable contains the title for the port options section within the "Extruder" panel
'''
PORT_OPTIONS_SECTION_TITLE = "Port Set-Up"

'''
The following list contains all the possible pre-die options that the user can choose
'''
PRE_DIE = ["Select", "Melt Pump", "Breaker Plate", "Through"]

'''
The following list contains all the possible options for each side stuffer on the extruder that the user can choose
'''
SIDE_STUFFER = ["Closed", "Sides Stuffer", "Vaccum Stuffer"]

'''
The following list contains all the possible options for each side stuffer without the vaccum option on the extruder
that the user can choose
'''
SIDE_STUFFER_WITHOUT_VACCUM = ["Closed", "Sides Stuffer"]

'''
The following list contains all the possible options for the possible strand cooling options for the extruder that the
user can choose
'''
STRAND_COOLING_OPTIONS = ["Belt", "Belt w/ Mister", "Water Bath", "Spray Belt", "UWP", "Other"]

'''
The following string variable contains the title for the strand cooling options section within the "Extruder" panel
'''
STRAND_COOLING_OPTIONS_SECTION_TITLE = "Strand Cooling Options"

'''
The following directory contains the title for the "Update" panel
'''
TITLE = "Extruder Workshop"

'''
The following function returns a confirmation that tells the calling code which configuration file this function
belongs to
'''
def confirm(value):

  # Check to make sure that the inputted value is a string that is equal to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "extruder":
      return True
    else:
      return False
  else:
    return False
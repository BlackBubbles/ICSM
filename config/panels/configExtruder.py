#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/20/2017
Last Updated: 08/22/2017
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
The following variable contains the active background color for the GUI
'''
ACTIVE_BACKGROUND = "#0099ff"

'''
The following list contains all the possible text strings for the am/pm radio buttons
'''
AM_PM_RADIO_NAMES = ["AM", "PM"]

'''
The following string variable contains the title for the add feeders section within the "Extruder" panel
'''
CAPTURING_SECTION_TITLE = "Capturing Options"

'''
The following string variable contains the title for the extruder options section within the "Extruder" panel
'''
CLASSIFIED_OPTIONS_SECTION_TITLE = "Classified Options"

'''
The following list contains all the possible radio button names that the user can choose from the classified section
in the "Extruder" panel
'''
CLASSIFIED_RADIO_BUTTON_NAMES = ["None", "Witte", "Hand"]

'''
The following variable contains the color of the Comments text box border
'''
COMMENTS_COLOR = "#000000"

'''
The following variable contains all possible time spaces for getting data from the extruder
'''
DATA_POINT_EVERY = ["Select", "15 secs", "30 secs", "1 min", "2 min", "5 min", "10 min"]

'''
The following variable contains the string for the drop down menu for all the possible time spaces for getting data
from the extruder
'''
DATA_POINT_EVERY_LABEL = "Data Point Every:"

'''
The following variable contains the color that signals to the user that there is an error
'''
ERROR_COLOR = "#FF0000"

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
  "27mm Leistritz": ["Select", "3-4.5mm", "5-3mm"],
  "33mm Entek": ["Select", "7-4.5mm", "10-3.5mm", "16-2mm"],
  "35mm Leistritz": ["Select", "7-4.5mm", "10-3.5mm", "16-2mm"]}

'''
The following string variable contains the title for the extruder options section within the "Extruder" panel
'''
EXTRUDER_OPTIONS_SECTION_TITLE = "Extruder Options"

'''
The following dictionary contains all the port lengths for each extruder
'''
EXTRUDER_PORT_SIZES = {
  EXTRUDERS[0]: [0],
  EXTRUDERS[1]: [8],
  EXTRUDERS[2]: [13],
  EXTRUDERS[3]: [10],
  EXTRUDERS[4]: [13],
  EXTRUDERS[5]: [13]
}

'''
The following dictionary contains the array of spots along the extruder where a port exists
'''
EXTRUDER_PORT_SPOTS = {
  EXTRUDERS[0]: [0],
  EXTRUDERS[1]: [1, 2, 3, 4, 5, 6, 7],
  EXTRUDERS[2]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
  EXTRUDERS[3]: [1, 5, 6],
  EXTRUDERS[4]: [4, 6, 7, 10, 11],
  EXTRUDERS[5]: [1, 4, 5, 6, 7, 10, 11]
}

'''
The following dictionary contains the array of spots along the extruder where a side stuffer exists
'''
EXTRUDER_SIDE_SPOTS = {
  EXTRUDERS[0]: [0],
  EXTRUDERS[1]: [],
  EXTRUDERS[2]: [5, 6],
  EXTRUDERS[3]: [4],
  EXTRUDERS[4]: [4, 6, 10],
  EXTRUDERS[5]: [5, 7, 10]
}

'''
The following list contains all the possible feeder types that the user can choose
'''
FEEDERS = ["Select", "Process 11", "FW40", "DDSR", "K-tron S60-S120", "K-tron S60-S60"]

'''
The following list contains all possible locations for the feeder
'''
FEEDER_LOCATIONS = ["Throat", "Side Stuffer"]

'''
The following string variable is the feeder options section title for the feeder GUI
'''
FEEDER_OPTIONS_TITLE = "Feeder Options"

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
The following list contains all the possible weight set points for the feeder
'''
FEEDER_SET_POINTS = ["lbs/hr", "kg/hr"]

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
The following variable contains the label name for the From entry widget
'''
FROM_LABEL = "From:"

'''
The following list contains the numbers from 0 to 4
'''
NUM = [0, 1, 2, 3, 4]

'''
The following list contains the numbers from 1 to 4
'''
NUM_NO_ZERO = [1, 2, 3, 4]

'''
The following list contains all the possible number of data points for capturing the data from the extruder
'''
NUM_OF_DATA_POINTS = ["Select", "1", "2", "3", "4", "5", "All"]

'''
The following list contains the label text for that drop down menu that contains all the possible number of data points
for capturing the data from the extruder
'''
NUM_OF_DATA_POINTS_LABEL = "# of Total Data Points:"

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
The following string holds the title for the feeder gui with the two radio button selections
'''
RADIO_BUTTON_TITLE = "Location/Measurement"

'''
The following string holds the title for the RM Code section in the feeder GUI
'''
RM_TITLE = "RM CODE"

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
The following variable contains the label text for the To entry widget
'''
TO_LABEL = "To:"

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
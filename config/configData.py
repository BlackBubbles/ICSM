#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/05/2017
Last Updated: 08/24/2017
Version: 1.0.0
Description:
    The following python file contains the configuration data for the Model
'''

'''
Imported files/libraries
'''
import configFrame as configF
from panels import configQuickAccess as configQA
from panels import configExtruder as configE
from panels import configLab as configL
from panels import configProject as configP

'''
Global variables
'''
'''
The following variable contains the TCP IP address for the server
'''
TCP_IP = "192.168.0.150"

'''
The following variable contains the TCP IP port for the ICSM program on the server
'''
TCP_PORT = 1234

'''
The following variable contains the TCP Buffer Size for the socket
'''
BUFFER_SIZE = 1024

'''
The following function returns the configuration module for the GUI frame
'''
def getConfigFrame():
  return configF

'''
The following function returns the configuration module for the "Quick Access" panel
'''
def getConfigQA():
  return configQA

'''
The following function returns the configuration module for the "Extruder" panel
'''
def getConfigExtruder():
  return configE

'''
The following function returns the configuration module for the "Lab" panel
'''
def getConfigLab():
  return configL

'''
The following function returns the configuration module for the "Project" panel
'''
def getConfigProject():
  return configP

'''
The following function returns a confirmation that tells the calling code which configuration file this function
belongs to
'''
def confirm(value):
  
  # Check to make sure that the inputted value is a string that is equal to the representaion of the configuration file
  if isinstance(value, basestring):
    if value.lower() == "data":
      return True
    else:
      return False
  else:
    return False
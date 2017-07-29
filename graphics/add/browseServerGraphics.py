#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 04/20/2017
Version: 0.0.1
Description:
    The following python file builds the add-on GUI that the user will
    interact with in able to browse the server directory
'''

'''
Imported files/libraries
'''
import tkFileDialog

'''
Global Variables
'''
# NONE

'''
The following function creates the GUI that allows the user to browse
the server directory to select a file to update/change
'''
def browseServer(graphics, label):
  
  # Build the GUI and record the file name of the file selected
  text = tkFileDialog.\
           askopenfilename(parent=graphics.getGUI(),
                           filetypes=[('all files', '.*'), 
                                      ('text files', '.txt'),
                                      ('excel files', '.csv')],
                           title="Browse for a file...")
  
  # Change the browse label to inform the user what file was selected
  if not len(text) == 0:
    fileName = text.split("/")[-1]
    label['text'] = fileName

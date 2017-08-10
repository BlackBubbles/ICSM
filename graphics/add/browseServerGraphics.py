#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 08/10/2017
Version: 1.0.0
Description:
    The following python file builds the add-on GUI that the user will interact with in able to browse the server
    directory
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
The following function creates the GUI that allows the user to browse the server directory to select a file to
update/change
'''
def browseServer(graphics, title, label):
  
  # Build the GUI and record the file name of the file selected
  filename = tkFileDialog.askopenfilename(parent=graphics.getGUI(),
                                          filetypes=[('all files', '.*'),
                                                     ('text files', '.txt'),
                                                     ('excel files', '.xlsx')],
                                          title="Browse for a file...")
  
  # Change the browse label to inform the user what file was selected and return the filepath
  if not len(filename) == 0:
    label["text"] = filename.split("/")[-1]
    return filename
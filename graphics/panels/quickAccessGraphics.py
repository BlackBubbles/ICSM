#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/24/2017
Last Updated: 07/06/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Quick Access" panel
'''

'''
Imported files/libraries
'''
import Tkinter as tk

'''
Global variables
'''
# NONE

'''
The following python class contains the functions that contains the
components for the quick access panel
'''
class QAG:
  
  '''
  The following function is the initial function for the "qAG" class
  '''
  def __init__(self, graphics, builder):
    self.graphics = graphics
    self.builder = builder
    self.buttons = {}
    
  '''
  The following function returns the instance of the graphics
  '''
  def getGraphics(self):
    return self.graphics
    
  '''
  The following function returns the instance of the gui builder for this
  panel
  '''
  def getBuilder(self):
    return self.builder
    
  '''
  The following function returns the dictionary of buttons for this panel
  '''
  def getButtons(self):
    return self.buttons
    
  '''
  The following function returns the instance the requested Tkinter
  button with the inputted key
  '''
  def getButton(self, key):
    return self.buttons[key]
    
  '''
  The following function builds the initial state for the "Quick Access"
  panel
  '''
  def buildPanel(self):
    
    # Get the "Quick Access" frame from the instance of the "Graphics"
    # class
    frame = self.graphics.getFrame("+")
    
    # Change the background color
    panel = self.builder.buildFrame(frame)
    panel.pack(fill=tk.BOTH, expand=1)
    
    # Add the four default buttons
    buttons = self.getButtons()
    for i in range(0,2):
      for j in range(0,2):
        text = str(i) + ", " + str(j)
        button = self.builder.buildButton(panel, text)
        button.configure(width=35, height=10)
        button.grid(row=i, column=j, padx=(50, 0), pady=(50, 0), 
                    sticky=tk.W)
        buttons[text] = button

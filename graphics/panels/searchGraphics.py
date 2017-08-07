#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/18/2017
Last Updated: 07/06/2017
Version: 1.0.0
Description:
    The following python file contains the class and functions for the "Search" panel
'''

'''
Imported files/libraries
'''
import Tkinter as tk

'''
Global Variables
'''
# NONE

'''
COMMENT
'''
class SearchG:
  
  '''
  COMMENT
  '''
  def __init__(self, graphics, builder):
    self.graphics = graphics
    self.builder = builder
    
  '''
  COMMENT
  '''
  def getGraphics(self):
    return self.graphics
    
  '''
  COMMENT
  '''
  def getBuilder(self):
    return self.builder
    
  '''
  The following function ...
  '''
  def buildPanel(self):
    
    # Get the "update" panel
    frame = self.graphics.getFrame("Search")
    
    # COMMENT
    panel = self.builder.buildFrame(frame)
    panel.pack(fill=tk.BOTH, expand=1)
    
    # COMMENT
    self.builder.buildTitle(self.graphics, panel, 
                            self.graphics.getConfig().
                            getConfigSearch().TITLE)
    
    # COMMENT
    KeyPanel = self.builder.buildFrame(panel)
    KeyPanel.grid(row=3, column=0, columnspan=20, padx=(0, 0),
                  pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    keyLabel = self.builder.build11Label(KeyPanel, "Keyword:")
    keyLabel.grid(row=0, column=0, padx=(100, 0), pady=(50, 0), 
                  sticky=tk.W)
    
    # COMMENT
    keyBox = tk.Entry(KeyPanel, width=20)
    keyBox.grid(row=0, column=1, padx=(10, 0), pady=(50, 0), 
                sticky=tk.W)
    
    # COMMENT
    searchButton = self.builder.buildButton(panel, "Search")
    searchButton.grid(row=4, column=0, padx=(125, 0), pady=(25, 0), 
                      sticky=tk.W)

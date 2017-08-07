#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/24/2017
Last Updated: 07/06/2017
Version: 1.0.0
Description:
    The following python file contains multiple interaction functions for the ICSM program to build the specific
    components of the Graphical User Interface
'''

'''
Imported files/libraries
'''
import sys
import Tkinter as tk
from types import ModuleType

'''
Global Variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class contains multiple interaction functions for the ICSM program to build the specific components of
the Graphical User Interface
'''
class Builder:
  
  '''
  The following function is the initial instance creation function for the "Builder" class
  '''
  def __init__(self, config):
    
    # Call set functions and is the return is False, then return the message for the error
    doesWork = True
    message = ""
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()
      
    # Set the rest of the initial "Builder" class variables
    self.config = config
    
  '''
  The following function returns the configuration file for the "Builder" class
  '''
  def getConfig(self):
    return self.config
    
  '''
  The following function sets the configuration file for the "Builder" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Graphics"):
          self.config = config
        else:
          return False, "%s:\nconfig file for Builder is not configGraphics" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""
    
  '''
  COMMENT
  '''
  def configureScroll(self, event, canvas, parent):
    canvas.configure(scrollregion=canvas.bbox("all"),
                     width=parent.winfo_screenwidth(),
                     height=parent.winfo_screenheight())
    
  '''
  COMMENT
  '''
  def buildScrollingCanvas(self, parent):
    
    # COMMENT
    canvas = tk.Canvas(parent, background=self.getConfig().BACKGROUND)
    panel = tk.Frame(canvas, background=self.getConfig().BACKGROUND)
    
    # COMMENT
    scroll = tk.Scrollbar(parent, orient="vertical", command=canvas.yview,
                          activebackground=self.getConfig().
                                                ACTIVE_BACKGROUND)
    scrollX = tk.Scrollbar(parent, 
                          orient="horizontal", command=canvas.xview,
                          activebackground=self.getConfig().
                                                ACTIVE_BACKGROUND)
    canvas.configure(yscrollcommand=scroll.set)
    canvas.configure(xscrollcommand=scrollX.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    scrollX.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.pack(side=tk.LEFT)
    canvas.create_window((0,0), window=panel, anchor='nw')
    panel.bind("<Configure>", 
               lambda event: self.configureScroll(event, canvas, parent))
    
    # COMMENT
    return panel
    
  '''
  COMMENT
  '''
  def buildTitle(self, graphics, parent, title):
    
    # Add the Title for the panel
    title = self.buildTitleLabel(parent, title)
    title.grid(row=0, column=0, columnspan=20, padx=(75, 0), pady=(50, 0),
               sticky=tk.W)
    
    # COMMENT
    browsePanel = self.buildFrame(parent)
    browsePanel.grid(row=1, column=0, columnspan=20, padx=(0, 0),
                     pady=(0, 0), sticky=tk.W)
    
    # Build the browse button
    browseButton = self.buildButton(browsePanel,
                                    self.getConfig().BROWSE_BUTTON_TEXT)
    browseButton.configure(
                   command=lambda: 
                     graphics.getActions().getUpdateActions().
                              browseServer(graphics, fileString))
    browseButton.grid(row=0, column=0, padx=(125, 0), pady=(25, 0),
                      sticky=tk.W)
    
    # Add line of text for the file name browsed for
    fileString = self.buildLabel(browsePanel,
                                 self.getConfig().BROWSE_LABEL)
    fileString.grid(row=0, column=1, padx=(50, 0), pady=(25, 0),
                    sticky=tk.W)
    
    # Add Line for decoration
    line = tk.Frame(parent, 
                    background=self.getConfig().LINE_COLOR,
                    height=self.getConfig().LINE_HIEGHT, 
                    width=parent.winfo_screenwidth())
    line.grid(row=2, column=0, columnspan=20, padx=(0, 0), pady=(25, 0), 
              sticky=tk.W)
    
  '''
  The following function returns a built Tkinter frame component
  '''
  def buildFrame(self, parent):
    frame = tk.Frame(parent, background=self.config.BACKGROUND)
    return frame
    
  '''
  COMMENT
  '''
  def buildLabel(self, parent, text):
    label = tk.Label(parent, text=text, background=self.config.BACKGROUND)
    return label
    
  '''
  COMMENT
  '''
  def build11Label(self, parent, text):
    label = tk.Label(parent, text=text,
                     background=self.getConfig().BACKGROUND,
                     font=["Arial", 11, "bold"])
    return label
    
  '''
  COMMENT
  '''
  def build13Label(self, parent, text):
    label = tk.Label(parent, text=text,
                     background=self.getConfig().BACKGROUND,
                     font=["Arial", 13, "bold"])
    return label
    
  '''
  COMMENT
  '''
  def build14Label(self, parent, text):
    label = tk.Label(parent, text=text,
                     background=self.getConfig().BACKGROUND,
                     foreground=self.getConfig().ACTIVE_BACKGROUND,
                     font=["Arial", 14, "bold"])
    return label
    
  '''
  COMMENT
  '''
  def buildTitleLabel(self, parent, text):
    label = tk.Label(parent, text=text,
                     background=self.getConfig().BACKGROUND,
                     foreground=self.getConfig().ACTIVE_BACKGROUND,
                     font=["Arial", 24, "bold"])
    return label
    
  '''
  COMMENT
  '''
  def buildButton(self, parent, text):
    button = tk.Button(parent, text=text,
                  width=self.getConfig().BUTTON_WIDTH,
                  height=self.getConfig().BUTTON_HEIGHT,
                  activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return button
    
  '''
  COMMENT
  '''
  def buildUpdateButton(self, parent, text):
    button = tk.Button(parent, text=text,
                  width=15, font=["Arial", 18, "bold"],
                  height=2, activeforeground=self.getConfig().BACKGROUND,
                  activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return button
    
  '''
  COMMENT
  '''
  def buildCheckBox(self, parent, text):
    variable = tk.IntVar(parent)
    check = tk.Checkbutton(parent, text=text, variable=variable,
                      background=self.getConfig().BACKGROUND,
                      activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return check
    
  '''
  COMMENT
  '''
  def buildScale(self, parent, smin, smax, length):
    scale = tk.Scale(parent, from_=smin, to=smax, orient=tk.HORIZONTAL,
                     background=self.getConfig().BACKGROUND, length=200,
                     activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return scale
    
  '''
  COMMENT
  '''
  def buildRadio(self, parent, names):
    variable = tk.IntVar(parent)
    index = 1
    radios = []
    for value in names:
      radio = tk.Radiobutton(parent, text=value, variable=variable,
                      value=index,
                      background=self.getConfig().BACKGROUND,
                      activebackground=self.getConfig().ACTIVE_BACKGROUND)
      index = index + 1
      radios.append(radio)
    return radios
    
  '''
  COMMENT
  '''
  def buildCoolingRadio(self, parent, names, graphics, panel):
    variable = tk.IntVar(parent)
    index = 1
    radios = []
    for value in names:
      radio = tk.Radiobutton(parent, text=value, variable=variable,
                      value=index,
                      background=self.getConfig().BACKGROUND,
                      command=lambda: graphics.getActions().
                                      getUpdateActions().
                                      changeCooling(graphics, 
                                                    variable.get(),
                                                    panel),
                      activebackground=self.getConfig().ACTIVE_BACKGROUND)
      index = index + 1
      radios.append(radio)
    return radios
    
  '''
  COMMENT
  '''
  def buildStringDropDown(self, parent, width, dic):
    variable = tk.StringVar(parent)
    variable.set(dic[0])
    menu = tk.OptionMenu(parent, variable, *dic)
    menu.configure(width=width,
           activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return variable, menu

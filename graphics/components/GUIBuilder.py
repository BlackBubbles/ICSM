#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 06/24/2017
Last Updated: 08/14/2017
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
  The following function ... to be honest I have no idea why this is here except that this has to be here
  '''
  def __configureScroll(self, canvas, parent):
    canvas.configure(scrollregion=canvas.bbox("all"), width=parent.winfo_screenwidth(),
                     height=parent.winfo_screenheight())
    
  '''
  The following function builds and returns a Tkinter frame with both a vertical and horizontal scrollbar
  '''
  def buildScrollingCanvas(self, parent):
    
    # Build the initial Tkinter canvas and set the background to white
    canvas = tk.Canvas(parent, background=self.getConfig().BACKGROUND)
    panel = tk.Frame(canvas, background=self.getConfig().BACKGROUND)
    
    # Build both scrollbars
    scroll = tk.Scrollbar(parent, orient="vertical", command=canvas.yview,
                          activebackground=self.getConfig().ACTIVE_BACKGROUND)
    scrollX = tk.Scrollbar(parent, orient="horizontal", command=canvas.xview,
                           activebackground=self.getConfig().ACTIVE_BACKGROUND)
    canvas.configure(yscrollcommand=scroll.set)
    canvas.configure(xscrollcommand=scrollX.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    scrollX.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    canvas.create_window((0,0), window=panel, anchor="nw")

    # Bind the canvas to the events created by the scrollbars
    panel.bind("<Configure>", lambda event: self.__configureScroll(canvas, parent))
    
    # Return the completed panel
    return panel
    
  '''
  The following function builds the title for each panel in the ICSM GUI
  '''
  def buildTitle(self, graphics, parent, title, useBrowse):
    
    # Add the Title for the panel
    titleLabel = tk.Label(parent, text=title, background=self.getConfig().BACKGROUND,
                          foreground=self.getConfig().ACTIVE_BACKGROUND, font=["Arial", 36, "bold"])
    titleLabel.grid(row=0, column=0, columnspan=20, padx=(75, 0), pady=(50, 0), sticky=tk.W)
    
    # Check to see if the user wants to include a browse button and label
    if useBrowse:

      # Create the Frame for the browse button and label
      browseFrame = self.buildFrame(parent)
      browseFrame.grid(row=1, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    
      # Build the browse button
      browseButton = self.buildButton(browseFrame, self.getConfig().BROWSE_BUTTON_TEXT)
      if title is self.getConfig().getConfigExtruder().TITLE:
        browseButton.configure(command=lambda: graphics.getActions().getExtruderActions().callBrowseServer(graphics,
                                                                                                           title,
                                                                                                           fileString))
      elif title is self.getConfig().getConfigLab().TITLE:
        browseButton.configure(command=lambda: graphics.getActions().getLabActions().callBrowseServer(graphics, title,
                                                                                                      fileString))
      browseButton.grid(row=0, column=0, padx=(125, 0), pady=(25, 0), sticky=tk.W)
    
      # Add line of text for the file name browsed for
      fileString = self.buildLabel(browseFrame, self.getConfig().BROWSE_LABEL_TEXT)
      fileString.grid(row=0, column=1, padx=(50, 0), pady=(25, 0), sticky=tk.W)

      # Assign row value for the decoration line
      lineRow = 2
    else:
      lineRow = 1
    
    # Add Line for decoration
    line = tk.Frame(parent, background=self.getConfig().LINE_COLOR, height=self.getConfig().LINE_HIEGHT,
                    width=parent.winfo_screenwidth())
    line.grid(row=2, column=0, columnspan=20, padx=(0, 0), pady=(75 - (lineRow * 25), 0), sticky=tk.W)

  '''
  The following function builds and a section with a title and returns the frame within that section
  '''
  def buildSection(self, parent, title):

    # Create a Frame and a Label
    frame = self.buildFrame(parent)
    frame.configure(highlightbackground=self.getConfig().ACTIVE_BACKGROUND,
                    highlightcolor=self.getConfig().ACTIVE_BACKGROUND, highlightthickness=2, width=700, height=100)
    label = self.buildH1Label(parent, title)

    # Bind the Frame and Label
    frame.grid(row=0, column=0, padx=(25, 0), pady=(25, 0), sticky=tk.W)
    label.grid(row=0, column=0, padx=(100, 0), pady=(9, 0), sticky=tk.NW)

    # Return the the panel within the section
    return frame, label

  '''
  The following function returns a built Tkinter frame component
  '''
  def buildFrame(self, parent):
    frame = tk.Frame(parent, background=self.getConfig().BACKGROUND)
    return frame
    
  '''
  The following function builds and returns a Tkinter label
  '''
  def buildLabel(self, parent, text):
    label = tk.Label(parent, text=text, background=self.config.BACKGROUND)
    return label
    
  '''
  The following function builds and returns a Tkinter label with font size of H1
  '''
  def buildH1Label(self, parent, text):
    label = tk.Label(parent, text=text, background=self.getConfig().BACKGROUND,
                     foreground=self.getConfig().ACTIVE_BACKGROUND,
                     font=["Arial", self.getConfig().H1_FONT_SIZE, "bold"])
    return label

  '''
  The following function builds and returns a Tkinter label with font size of H2
  '''
  def buildH2Label(self, parent, text):
    label = tk.Label(parent, text=text, background=self.getConfig().BACKGROUND,
                     font=["Arial", self.getConfig().H2_FONT_SIZE, "bold"])
    return label

  '''
  The following function builds and returns a Tkinter label with font size of H3
  '''
  def buildH3Label(self, parent, text):
    label = tk.Label(parent, text=text, background=self.getConfig().BACKGROUND,
                     font=["Arial", self.getConfig().H3_FONT_SIZE, "bold"])
    return label
    
  '''
  The following function builds and returns a Tkinter button component
  '''
  def buildButton(self, parent, text):
    button = tk.Button(parent, text=text, width=self.getConfig().BUTTON_WIDTH, height=self.getConfig().BUTTON_HEIGHT,
                       activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return button
    
  '''
  The following function builds and returns a Tkinter button component that will be used on the bottom of the panels
  '''
  def buildBottomButton(self, parent, text):
    button = tk.Button(parent, text=text,
                       activeforeground=self.getConfig().BACKGROUND,
                       activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return button
    
  '''
  The following function builds and returns a Tkinter checkbox component
  '''
  def buildCheckBox(self, parent, text):
    variable = tk.IntVar(parent)
    check = tk.Checkbutton(parent, text=text, variable=variable, background=self.getConfig().BACKGROUND,
                           activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return check, variable
    
  '''
  The following function builds and returns a Tkinter scale component
  '''
  def buildScale(self, parent, smin, smax):
    scale = tk.Scale(parent, from_=smin, to=smax, orient=tk.HORIZONTAL, background=self.getConfig().BACKGROUND,
                     length=200, activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return scale
    
  '''
  The following function builds and returns a list of Tkinter radio components
  '''
  def buildRadio(self, function, section, label, parent, names):
    variable = tk.IntVar(parent)
    index = 1
    radios = []
    for value in names:
      radio = tk.Radiobutton(parent, text=value, variable=variable, value=index,
                             activebackground=self.getConfig().ACTIVE_BACKGROUND,
                             background=self.getConfig().BACKGROUND, command=lambda: function([section, label]))
      index = index + 1
      radios.append(radio)
    return radios, variable
    
  '''
  The following function builds a drop down menu from the input dictionary of components and returns the variable and
  the menu
  '''
  def buildStringDropDown(self, function, section, label, parent, width, dic):
    variable = tk.StringVar(parent)
    variable.set(dic[0])
    menu = tk.OptionMenu(parent, variable, *dic, command=lambda x: function(section, label))
    menu.configure(width=width, activebackground=self.getConfig().ACTIVE_BACKGROUND)
    return menu, variable

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "builder":
        return True
      else:
        return False
    else:
      return False
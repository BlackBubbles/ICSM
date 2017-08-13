#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 08/11/2017
Version: 1.0.0
Description:
    The following python file sets up the frame and adds the Tabbed Document Interface(TDI) to the program
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import Tkinter as tk
import ttk

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class sets up the GUI frame
'''
class FrameG:

  '''
  The following function is the initial instance creation function for the "FrameG" class
  '''
  def __init__(self, config):

    # Call set functions and if the return is False, then return the message for the error
    doesWork, message = self.setConfig(config)
    if not doesWork:
      print message
      sys.exit()

    # Set initial values for this instance of the "FrameG" class
    self.actions = None
    self.data = None
    self.notebook = None
    self.frames = {}

  '''
  The following function returns the configuration file for this instance of the "FrameG" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for this instance of the class. If the inputted config file does
  not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Frame"):
          self.config = config
        else:
          return False, "%s:\nconfig file for FrameG is not configFrame" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the controller for this instance of the class
  '''
  def getActions(self):
    return self.actions

  '''
  The following function sets the controller for this instance of the Frame. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setActions(self, actions):
    self.actions = actions
    return True, ""

  '''
  The following function returns the model for this instance of the class
  '''
  def getData(self):
    return self.data

  '''
  The following function sets the model for this instance of the Frame. If the input does not meet the
  requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, data):
    if hasattr(data, "confirm"):
      if data.confirm("Frame"):
        self.data = data
      else:
        return False, "%s:\ndata for FrameG is not frameData" % ERROR
    else:
      return False, "%s:\ninput is not a file for the ICSM program" % ERROR
    return True, ""

  '''
  The following function returns the TDI notebook for this instance of the "FrameG" class
  '''
  def getNotebook(self):
    return self.notebook

  '''
  The following function sets the TDI notebook for this instance of the "FrameG" class. If the inputted file does not
  meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setNotebook(self, notebook):
    if isinstance(notebook, ttk.Notebook):
      self.notebook = notebook
      return True, ""
    return False, "%s:\nframeGraphics could not create the Notebook TDI" % ERROR

  '''
  The following function returns the TDI frames for this instance of the "FrameG" class
  '''
  def getFrames(self):
    return self.frames

  '''
  The following function returns the TDI frames for this instance of the "FrameG" class. If the inputted file does not
  meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setFrames(self, frames):

    # Create the initial return variables and values
    doesWork = True
    message = ""

    # Check each frame in frames to make sure that each is an instance of ttk.Frame
    for title, frame in frames.iteritems():
      if not isinstance(frame, ttk.Frame):
        doesWork = False
        message = "%s:\nframe for FrameG.frames is not an instance of ttk.Frame" % ERROR

    # If nothing is wrong set the inputted frames
    if doesWork:
      self.frames = frames

    # Return the variable
    return doesWork, message

  '''
  The following function returns a specific frame based on the inputted key value
  '''
  def getFrame(self, key):
    return self.frames[key]

  '''
  The following function builds a GUI frame based on the input parameters
  '''
  def __buildFrame(self, gui, title, width, height):

    # Set the title of the GUI
    gui.title(title)

    # Find the middle of the screen
    ws = gui.winfo_screenwidth()
    hs = gui.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)

    # Set the initial size and position for the GUI
    gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

  '''
  The following function builds the initial error GUI before the ICSM starts to execute
  '''
  def buildErrorGUI(self, gui, message, exit):

      # Call the "__buildFrame" function to build the frame
      self.__buildFrame(gui, "ICSM - ERROR", 800, 200)
      gui.resizable(width=False, height=False)

      # Build the label with the error message on it for the GUI and place the message in the middle of the frame
      errorLabel = tk.Label(gui, font=("Arial", 16, 'bold'), text=message)
      errorLabel.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

      # Create and place a "OK" bottom towards the bottom of the frame
      okButton = tk.Button(gui, text="OK", width=10, height=2, command=exit)
      okButton.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

  '''
  The following function builds the ICSM program GUI frame and TDI system
  '''
  def buildGUIFrame(self, graphics, gui):

    # Call the "__buildFrame" function to build the frame
    self.__buildFrame(gui, self.getConfig().TITLE, self.getConfig().WIDTH, self.getConfig().HEIGHT)

    # Create the style for the TDI
    style = ttk.Style()
    style.theme_create("ICSMTDI", parent="alt",
                       settings={"TNotebook": {"configure": {"tabmargins": self.getConfig().TDI_TAB_MARGINS}},
                                 "TNotebook.Tab": {"configure": {"padding": self.getConfig().TDI_PADDING,
                                                                 "background": self.getConfig().TDI_BACKGROUND_COLOR},
                                                   "map": {"background":[("selected",
                                                                          self.getConfig().TDI_SELECTED_COLOR)],
                                                           "expand":[("selected", self.getConfig().TDI_EXPAND)]}}})
    style.theme_use("ICSMTDI")

    # Create the quick access popup menu
    QAMenu = tk.Menu(gui, tearoff=0)
    for value in self.getConfig().RIGHT_CLICK_QA_MENU:
      QAMenu.add_command(label=value, command=lambda value=value: graphics.getActions().getTDIActions().react(value))

    # Create the TDI popup menu
    TDIMenu = tk.Menu(gui, tearoff=0)
    for value in self.getConfig().RIGHT_CLICK_TDI_MENU:
      TDIMenu.add_command(label=value, command=lambda value=value: graphics.getActions().getTDIActions().react2(value))

    # Create the 'Notebook' python module instance
    doesWork, message = self.setNotebook(ttk.Notebook(gui))
    if not doesWork:
      print message
      sys.exit()

    # Build the tab panels
    frames = {}
    for title in self.getConfig().STARTING_TDI:
      frame = ttk.Frame(self.getNotebook())
      frames[title] = frame
      self.getNotebook().add(frame, text=title)
    doesWork, message = self.setFrames(frames)
    if not doesWork:
      print message
      sys.exit()

    # Add Quick Access to TDI
    self.getFrames()[self.getConfig().QUICK_ACCESS] = ttk.Frame(self.getNotebook())
    self.getNotebook().add(frames[self.getConfig().QUICK_ACCESS], text=self.getConfig().QUICK_ACCESS)

    # Finish TDI specs
    self.getNotebook().pack(fill='both', expand=1)
    self.getNotebook().bind('<Control-1>',
                            lambda event: self.getActions().showMenuDropDown(graphics, event, self.getConfig(),
                                                                             QAMenu, TDIMenu))

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "frame":
        return True
      else:
        return False
    else:
      return False
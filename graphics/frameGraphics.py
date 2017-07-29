#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 02/26/2017
Last Updated: 06/24/2017
Version: 0.0.1
Description:
    The following python file sets up the frame and adds the Tabbed 
    Document Interface(TDI) to the program
'''

'''
Imported files/libraries
'''
import Tkinter as tk
import ttk

'''
Global variables
'''
# NONE

'''
The following function builds a GUI frame based on the input parameters
'''
def __buildFrame(gui, title, width, height):
  
  # Set the title of the GUI
  gui.title(title)
  
  # Find the middle of the screen
  ws = gui.winfo_screenwidth()
  hs = gui.winfo_screenheight()
  x = (ws/2) - (width/2)
  y = (hs/2) - (height/2)
  
  # Set the initial size and position for the GUI
  gui.geometry("%dx%d+%d+%d" % (width, height, x, y))
  
'''
The following function builds the initial frame for the GUI
'''
def buildGUIFrame(graphics):
  
  # Call the "__buildFrame" function to build the frame
  __buildFrame(graphics.getGUI(), graphics.getConfig().TITLE,
               graphics.getConfig().WIDTH, graphics.getConfig().HEIGHT)
  
'''
The following function builds the frame for the GUI that displays an error
'''
def buildErrorFrame(graphics):
  
  # Call the "__buildFrame" function to build the frame
  __buildFrame(graphics.getGUI(), "IISM - ERROR", 800, 200)
  graphics.getGUI().resizable(width=False, height=False)
  
'''
The following function adds the error message to the GUI frame
'''
def buildErrorPanel(graphics, message):
  
  # Build the label with the error message on it for the GUI and
  # place the message in the middle of the frame
  errorMessage = tk.Label(graphics.getGUI(), font=("Arial", 13, 'bold'),
                          text=message)
  errorMessage.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
  
  # Create and place a "OK" bottom towards the bottom of the frame
  okButton = tk.Button(graphics.getGUI(), text="OK", width="10",
                       height="2", command=graphics.getActions().exit)
  okButton.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
  
'''
The following function builds the TDI system for the GUI
'''
def buildTDI(graphics, config):
  
  # Create the style for the TDI
  style = ttk.Style()
  style.theme_create( "IISMTDI", parent="alt", settings = {
      "TNotebook": {"configure": {"tabmargins": config.TDI_TAB_MARGINS}},
      "TNotebook.Tab": {"configure": {"padding": config.TDI_PADDING, 
      "background": config.TDI_BACKGROUND_COLOR}, "map":{ "background": 
      [("selected", config.TDI_SELECTED_COLOR)], "expand": 
      [("selected", config.TDI_EXPAND)]}}})
  style.theme_use("IISMTDI")
  
  # Create the quick access popup menu
  QAMenu = tk.Menu(graphics.getGUI(), tearoff=0)
  for value in config.RIGHT_CLICK_QA_MENU:
    QAMenu.add_command(label=value, command=lambda value=value:
                       graphics.getActions().getTDIActions().react(value))
    
  # Create the TDI popup menu
  TDIMenu = tk.Menu(graphics.getGUI(), tearoff=0)
  for value in config.RIGHT_CLICK_TDI_MENU:
    TDIMenu.add_command(label=value, command=lambda value=value:
                        graphics.getActions().getTDIActions()
                                .react2(value))
    
  # Create the 'Notebook' python module instance
  nb = ttk.Notebook(graphics.getGUI())
  
  # Build the tab panels
  frames = {}
  for title in config.STARTING_TDI:
    frame = ttk.Frame(nb)
    frames[title] = frame
    nb.add(frame, text=title)
    
  # Add Quick Access to TDI
  frames[config.QUICK_ACCESS] = ttk.Frame(nb)
  nb.add(frames[config.QUICK_ACCESS], text=config.QUICK_ACCESS)
  
  # Finish TDI specs
  nb.pack(fill='both', expand=1)
  nb.bind('<3>', lambda event: graphics.getActions().getFrameActions()
                                       .showMenuDropDown(graphics, event,
                                         config, QAMenu, TDIMenu))
  
  # Return Frames
  return frames, nb;

#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/19/2017
Last Updated: 06/19/2017
Version: 1.0.0
Description:
    The following python module contains the code that builds the panel that contains the options for the feeders that
    are used on the extruders
'''

'''
Imported files/libraries
'''
from Tkinter import *

'''
Global Variables
'''
PERCENT = 0

'''
COMMENT
'''
def configureScroll(event, canvas, frame):
  canvas.configure(scrollregion=canvas.bbox("all"),
           width=frame.winfo_screenwidth(),
           height=frame.winfo_screenheight())

'''
COMMENT
'''
def buildAddFeederGUI(graphics, feedPanel, edit, dictionary):
  
  # COMMENT
  feederGUI = Toplevel(graphics.getGUI())
  
  # COMMENT
  feederGUI.wm_title("Feeder Options")
  
  # COMMENT
  width = feederGUI.winfo_screenwidth()
  height = feederGUI.winfo_screenheight()
  x = width/2 - 100
  y = height/2 - 100
  feederGUI.geometry("%dx%d+%d+%d" % (200, 200, x, y))
  feederGUI.wm_geometry("400x450")
  
  # COMMENT
  canvas = Canvas(feederGUI, background=graphics.getConfig().BACKGROUND)
  frame = Frame(canvas, background=graphics.getConfig().BACKGROUND)
  
  # Add scroll bar to the add frame
  scroll = Scrollbar(feederGUI, orient="vertical", command=canvas.yview,
             activebackground=graphics.getConfig().TDI_SELECTED_COLOR)
  canvas.configure(yscrollcommand=scroll.set)
  scroll.pack(side=RIGHT, fill=Y)
  canvas.pack(side=LEFT)
  canvas.create_window((0,0), window=frame, anchor='nw')
  frame.bind("<Configure>", lambda event: 
                            configureScroll(event, canvas, feederGUI))
  
  # COMMENT
  fedLabel = Label(frame, 
                   background=graphics.getConfig().BACKGROUND,
                   font=("Arial", 11, 'bold'), text="Feeder")
  fedLabel.grid(row=0, column=0, padx=(50, 0), pady=(30, 0), 
                sticky=W)
  
  # COMMENT
  tubeLabel = Label(frame, 
                   background=graphics.getConfig().BACKGROUND,
                   font=("Arial", 11, 'bold'), text="Feeder Tube")
  tubeLabel.grid(row=2, column=0, padx=(50, 0), pady=(30, 0), 
                 sticky=W)
  
  # COMMENT
  variableFT = StringVar(frame)
  variableFT.set(graphics.getConfig().getConfigUpdate().
                 FEEDER_TUBES["Select"][0])
  menuFT = apply(OptionMenu, (frame, variableFT) + tuple(graphics.
                 getConfig().getConfigUpdate().FEEDER_TUBES["Select"]))
  menuFT.config(activebackground=graphics.getConfig().
                      TDI_SELECTED_COLOR)
  menuFT.grid(row=3, column=0, padx=(50, 0), pady=(5, 0), 
              sticky=W, columnspan=2)
  
  # COMMENT
  screwLabel = Label(frame, 
                   background=graphics.getConfig().BACKGROUND,
                   font=("Arial", 11, 'bold'), text="Feeder Screw")
  screwLabel.grid(row=4, column=0, padx=(50, 0), pady=(30, 0), 
                  sticky=W)
  
  # COMMENT
  variableS = StringVar(frame)
  variableS.set(graphics.getConfig().getConfigUpdate().
                FEEDER_SCREWS["Select"][0])
  menuS = apply(OptionMenu, (frame, variableS) + tuple(graphics.
                getConfig().getConfigUpdate().FEEDER_SCREWS["Select"]))
  menuS.config(activebackground=graphics.getConfig().
                      TDI_SELECTED_COLOR)
  menuS.grid(row=5, column=0, padx=(50, 0), pady=(5, 0), 
             sticky=W, columnspan=2)
  
  # COMMENT
  variableF = StringVar(frame)
  variableF.set(graphics.getConfig().getConfigUpdate().FEEDERS[0])
  menuF = OptionMenu(frame, variableF,
                     *graphics.getConfig().getConfigUpdate().FEEDERS,
                     command=lambda x: graphics.getActions().
                       getFeederActions().changeFeeder(graphics,
                                                       variableF.get(),
                                                       variableFT,
                                                       menuFT,
                                                       variableS, menuS))
  menuF.config(activebackground=graphics.getConfig().TDI_SELECTED_COLOR)
  menuF.grid(row=1, column=0, padx=(50, 0), pady=(5, 0), 
             sticky=W, columnspan=2)
  
  # COMMENT
  locLabel = Label(frame, 
                   background=graphics.getConfig().BACKGROUND,
                   font=("Arial", 11, 'bold'), text="Location")
  locLabel.grid(row=6, column=0, padx=(50, 0), pady=(30, 0), 
                sticky=W)
  
  # COMMENT
  variableLoc = IntVar(frame)
  radioThroat = Radiobutton(frame, text="Throat", variable=variableLoc,
                            value=1, 
                            background=graphics.getConfig().BACKGROUND,
                            activebackground=graphics.getConfig().
                            TDI_SELECTED_COLOR)
  radioSS = Radiobutton(frame, text="Side Stuffer", variable=variableLoc,
                        value=2, 
                        background=graphics.getConfig().BACKGROUND,
                        activebackground=graphics.getConfig().
                        TDI_SELECTED_COLOR)
  radioThroat.grid(row=7, column=0, padx=(50, 0), pady=(5, 0), 
                sticky=W)
  radioSS.grid(row=7, column=1, padx=(10, 0), pady=(5, 0), 
                sticky=W)
  
  # COMMENT
  RMLabel = Label(frame, 
                  background=graphics.getConfig().BACKGROUND,
                  font=("Arial", 11, 'bold'), text="RM Code")
  RMLabel.grid(row=8, column=0, padx=(50, 0), pady=(30, 0), 
                sticky=W)
  
  # COMMENT
  RMPanel = Frame(frame, background=graphics.getConfig().BACKGROUND)
  RMPanel.grid(row=9, column=0, columnspan=20, padx=(0, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  RMName = Entry(RMPanel, width=15)
  RMName.grid(row=0, column=0, padx=(50, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  RMPercent = Entry(RMPanel, width=5)
  RMPercent.grid(row=0, column=1, padx=(10, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  RMPer = Label(RMPanel, background=graphics.getConfig().BACKGROUND,
                text="%")
  RMPer.grid(row=0, column=2, padx=(0, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  RMAddPanel = Frame(frame, background=graphics.getConfig().BACKGROUND)
  RMAddPanel.grid(row=10, column=0, columnspan=20, padx=(0, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  RMAdd = Button(RMPanel,
      activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
      text="Add", 
      width=graphics.getConfig().BUTTON_WIDTH,
      height=1,
      command=lambda: graphics.getActions().getFeederActions()
                      .addRM(graphics, RMAddPanel, RMName,
                             RMPercent))
  RMAdd.grid(row=0, column=3, padx=(10, 0),
               pady=(0, 0), sticky=W)
  
  # COMMENT
  perssLabel = Label(frame, 
                   background=graphics.getConfig().BACKGROUND,
                   font=("Arial", 11, 'bold'), text="Set Point")
  perssLabel.grid(row=11, column=0, padx=(50, 0), pady=(30, 0), 
                sticky=W)
  
  # COMMENT
  variableSet = IntVar(frame)
  radioThroat = Radiobutton(frame, text="lbs/hr", variable=variableSet,
                            value=1, 
                            background=graphics.getConfig().BACKGROUND,
                            activebackground=graphics.getConfig().
                            TDI_SELECTED_COLOR)
  radioSS = Radiobutton(frame, text="kg/hr", variable=variableSet,
                        value=2, 
                        background=graphics.getConfig().BACKGROUND,
                        activebackground=graphics.getConfig().
                        TDI_SELECTED_COLOR)
  radioThroat.grid(row=12, column=0, padx=(50, 0), pady=(5, 0), 
                sticky=W)
  radioSS.grid(row=12, column=1, padx=(10, 0), pady=(5, 0), 
                sticky=W)
  
  # COMMENT
  addButton = Button(frame, 
      activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
      text="Apply", 
      width=graphics.getConfig().BUTTON_WIDTH,
      height=graphics.getConfig().BUTTON_HEIGHT,
      command=lambda: graphics.getActions().getFeederActions()
                              .apply(graphics, 
                                     feederGUI, 
                                     feedPanel,
                                     variableF,
                                     variableFT,
                                     variableS,
                                     variableLoc, variableSet))
  addButton.grid(row=13, column=0, padx=(50, 0), pady=(30, 30), 
                sticky=W)
  
  # COMMENT
  clearButton = Button(frame, 
      activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
      text="Cancel", 
      width=graphics.getConfig().BUTTON_WIDTH,
      height=graphics.getConfig().BUTTON_HEIGHT,
      command=lambda: graphics.getActions().getFeederActions()
                                    .cancel(feederGUI))
  clearButton.grid(row=13, column=1, padx=(25, 0), pady=(30, 30), 
                sticky=W)

#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/29/2017
Last Updated: 04/20/2017
Version: 1.0.0
Description:
    The following python file contains the controller actions for the "Update" panel
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
The following function calls the "buildAddFeederGUI" function in the
graphics which will show a GUI to add a feeder for a extruder
'''
def addFeeder(graphics, feedPanel):
  graphics.getFeederGraphics().buildAddFeederGUI(graphics, feedPanel, 
                                                 False, None)
  
'''
The following function calls the "browseServer" function in the graphics
which will show a GUI to browse the server directory
'''
def browseServer(graphics, label):
  graphics.getBrowseServerGraphics().browseServer(graphics, label)
  
'''
COMMENT
'''
def __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                low, high, emptyPort, emptySide):
  for i in range(low, high):
    if i in emptyPort:
      continue
    if extruder == "11mm":
      portOptions = graphics.getConfig().getConfigUpdate().\
                                         PORT_OPTIONS_11MM
    else:
      portOptions = graphics.getConfig().getConfigUpdate().PORT_OPTIONS
    var, menu = graphics.getBuilder().buildStringDropDown(portMenuPanel,
                                                          6, portOptions)
    menu.grid(row=0, column=0, padx=(75 + (i * 100), 0), pady=(5, 0), 
              sticky=tk.W)
  portBoxPanel.configure(highlightbackground="black",
                         highlightcolor="black",
                         highlightthickness=2)
  for i in range(low, high):
    num = graphics.getBuilder().buildLabel(portBoxPanel, high - i)
    num.configure(font=["Arial", 7, "bold"])
    num.grid(row=0, column=0, padx=((18 + (i * 100)), 0),
             pady=(15, 0), sticky=tk.W)
    if i is not 0:
      line = tk.Frame(portBoxPanel, width=2, height=75,
                      background="black")
      line.grid(row=0, column=0, padx=((13 + (i * 100)), 100),
                pady=(0, 0), sticky=tk.W, rowspan=2)
    if i in emptySide:
      continue
    if extruder == "11mm":
      sideOptions = ["No Side Stuffer"]
    elif extruder == "27mm Leistritz" or extruder == "27mm Entek":
      sideOptions = graphics.getConfig().getConfigUpdate().\
                                         SIDE_STUFFER_WITHOUT_VACCUM
    else:
      sideOptions = graphics.getConfig().getConfigUpdate().SIDE_STUFFER
    var, menu = graphics.getBuilder().buildStringDropDown(
                     portBoxPanel, 6, sideOptions)
    menu.grid(row=1, column=0, padx=((18 + (i * 100)), 15),
              pady=(0, 15), sticky=tk.W)
    
'''
COMMENT
'''
def __buildPortPanel(graphics, extruder, portMenuPanel, portBoxPanel):
  
  # COMMENT
  for widget in portMenuPanel.winfo_children():
    widget.destroy()
  for widget in portBoxPanel.winfo_children():
    widget.destroy()
  portBoxPanel.configure(highlightbackground="white",
                         highlightcolor="white")
  
  # COMMENT
  if extruder == "Select":
    message = graphics.getBuilder().build11Label(portBoxPanel,
                                               "Select Extruder")
    message.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                 sticky=tk.W)
  elif extruder == "11mm":
    __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                0, 8, [7],
                [0, 3, 4, 5, 6, 7])
  elif extruder == "27mm Leistritz":
    __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                0, 10, [0, 1, 2, 5, 6, 7, 9], 
                [0, 1, 2, 3, 4, 6, 7, 8, 9])
  elif extruder == "27mm Entek":
    __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                0, 13, [12], [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12])
  elif extruder == "33mm Entek":
    __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                0, 13, [0, 3, 4, 7, 9, 10, 11, 12],
                [0, 1, 3, 4, 5, 7, 9, 10, 11, 12])
  elif extruder == "35mm Leistritz":
    __buildPort(graphics, portMenuPanel, portBoxPanel, extruder,
                0, 13, [0, 3, 4, 9, 10, 12],
                [0, 1, 3, 4, 6, 8, 9, 10, 11, 12])
    
'''
COMMENT
'''
def __buildSprayBeltBottomContentPanel(graphics, panel):
  
  # COMMENT
  blowerScale = graphics.getBuilder().buildScale(panel, 0, 100, 200)
  blowerScale.grid(row=0, column=0, padx=(50, 0), pady=(5, 0), 
                   sticky=tk.W)
  
  # COMMENT
  blowerVacScale = graphics.getBuilder().buildScale(panel, 0, 100, 200)
  blowerVacScale.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                      sticky=tk.W)
  
'''
COMMENT
'''
def __buildSprayBeltBottomTitlePanel(graphics, panel):
  
  # COMMENT
  blowerLabel = graphics.getBuilder().build11Label(panel, "Blower Speed")
  blowerLabel.grid(row=0, column=0, padx=(100, 0), pady=(5, 0),
                   sticky=tk.W)
  
  # COMMENT
  blowerVacLabel = graphics.getBuilder().build11Label(panel,
                                                      "Blower Vac Speed")
  blowerVacLabel.grid(row=0, column=0, padx=(300, 0), pady=(5, 0),
                      sticky=tk.W)
  
'''
COMMENT
'''
def __buildSprayBeltTopContentPanel(graphics, panel):
  
  # COMMENT
  waterTempScale = graphics.getBuilder().buildScale(panel, 0, 100, 200)
  waterTempScale.grid(row=0, column=0, padx=(50, 0), pady=(5, 0), 
                      sticky=tk.W)
  
  # COMMENT
  conveyorScale = graphics.getBuilder().buildScale(panel, 0, 100, 200)
  conveyorScale.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                     sticky=tk.W)
  
'''
COMMENT
'''
def __buildSprayBeltTopTitlePanel(graphics, panel):
  
  # COMMENT
  C = u"\u00b0" + "C"
  waterTempLabel = graphics.getBuilder().build11Label(panel,
                                                      "Water Temp " + C)
  waterTempLabel.grid(row=0, column=0, padx=(100, 0), pady=(5, 0),
                      sticky=tk.W)
  
  # COMMENT
  conveyorLabel = graphics.getBuilder().build11Label(panel, 
                                                     "Conveyor Speed")
  conveyorLabel.grid(row=0, column=0, padx=(300, 0), pady=(5, 0),
                     sticky=tk.W)
  
'''
COMMENT
'''
def __buildSprayBeltMistersContentPanel(graphics, panel):
  
  # COMMENT
  index = 0
  for i in range(0, 12):
    index = i
    radios = graphics.getBuilder().buildRadio(panel, ["On", "Off"])
    label = graphics.getBuilder().buildLabel(panel, str(12 - i))
    label.grid(row=0, column=0, padx=((i*45), 0), pady=(0, 0), 
               sticky=tk.W)
    label.configure(font=["Arial", 7])
    radios[0].grid(row=1, column=0, padx=((i*45), 0), pady=(0, 0), 
                   sticky=tk.W)
    radios[1].grid(row=2, column=0, padx=((i*45), 0), pady=(0, 0), 
                   sticky=tk.W)
  index = index + 1
  for i in range(0, 2):
    radios = graphics.getBuilder().buildRadio(panel, ["On", "Off"])
    radios[0].grid(row=1, column=0, padx=(600 + (i*45), 0),
                   pady=(0, 0), sticky=tk.W)
    radios[1].grid(row=2, column=0, padx=(600 + (i*45), 0),
                   pady=(0, 0), sticky=tk.W)
    
'''
COMMENT
'''
def __buildSprayBeltMistersTitlePanel(graphics, panel):
  
  # COMMENT
  mistersLabel = graphics.getBuilder().build11Label(panel, "Misters")
  mistersLabel.grid(row=0, column=0, padx=(200, 0), pady=(5, 0), 
                    sticky=tk.W)
  
  # COMMENT
  sluiceLabel = graphics.getBuilder().build11Label(panel, "Belt Misters")
  sluiceLabel.grid(row=0, column=0, padx=(650, 0), pady=(5, 0), 
                   sticky=tk.W)
  
'''
COMMENT
'''
def __buildSprayBeltPanel(graphics, panel):
  
  # COMMENT
  SprayBeltMistersTitlePanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltMistersTitlePanel.grid(row=0, column=0, padx=(0, 0),
                                  pady=(0, 0), sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildSprayBeltMistersTitlePanel(graphics, SprayBeltMistersTitlePanel)
  
  # COMMENT
  SprayBeltMistersContentPanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltMistersContentPanel.grid(row=1, column=0, padx=(50, 0),
                                    pady=(0, 0), sticky=tk.W,
                                    columnspan=20)
  
  # COMMENT
  __buildSprayBeltMistersContentPanel(graphics,
                                      SprayBeltMistersContentPanel)
  
  # COMMENT
  SprayBeltTopTitlePanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltTopTitlePanel.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), 
                              sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildSprayBeltTopTitlePanel(graphics, SprayBeltTopTitlePanel)
  
  # COMMENT
  SprayBeltTopContentPanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltTopContentPanel.grid(row=3, column=0, padx=(0, 0),
                                pady=(0, 0), sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildSprayBeltTopContentPanel(graphics, SprayBeltTopContentPanel)
  
  # COMMENT
  SprayBeltBottomTitlePanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltBottomTitlePanel.grid(row=4, column=0, padx=(0, 0),
                                 pady=(0, 0), sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildSprayBeltBottomTitlePanel(graphics, SprayBeltBottomTitlePanel)
  
  # COMMENT
  SprayBeltBottomContentPanel = graphics.getBuilder().buildFrame(panel)
  SprayBeltBottomContentPanel.grid(row=5, column=0, padx=(0, 0),
                                   pady=(0, 0), sticky=tk.W,
                                   columnspan=20)
  
  # COMMENT
  __buildSprayBeltBottomContentPanel(graphics,
                                     SprayBeltBottomContentPanel)
  
'''
COMMENT
'''
def __buildUWPBottomContentPanel(graphics, panel):
  
  # COMMENT
  airKnifeEntry = tk.Entry(panel, width=20)
  airKnifeEntry.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                     sticky=tk.W)
  
  # COMMENT
  x, airKnifeNumMenu = graphics.getBuilder().buildStringDropDown(panel, 
                       6, graphics.getConfig().getConfigUpdate().NUM)
  airKnifeNumMenu.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                       sticky=tk.W)
  
  # COMMENT
  y, fanMenu = graphics.getBuilder().buildStringDropDown(panel,
                    6, graphics.getConfig().getConfigUpdate().NUM)
  fanMenu.grid(row=0, column=0, padx=(425, 0), pady=(5, 0), 
               sticky=tk.W)
  
'''
COMMENT
'''
def __buildUWPBottomTitlePanel(graphics, panel):
  
  # COMMENT
  airKnifeLabel = graphics.getBuilder().build11Label(panel,
                                            "Air Knife/Location")
  airKnifeLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                     sticky=tk.W)
    
  # COMMENT
  airKnifeNumLabel = graphics.getBuilder().build11Label(panel, 
                                               "# of Air Knifves")
  airKnifeNumLabel.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                        sticky=tk.W)
  
  # COMMENT
  fanLabel = graphics.getBuilder().build11Label(panel, "# of Fans")
  fanLabel.grid(row=0, column=0, padx=(425, 0), pady=(5, 0), 
                sticky=tk.W)
  
'''
COMMENT
'''
def __buildUWPTopContentPanel(graphics, panel):
  
  # COMMENT
  waterTempScale = graphics.getBuilder().buildScale(panel, 60, 120, 200)
  waterTempScale.grid(row=0, column=0, padx=(50, 0), pady=(5, 0), 
                      sticky=tk.W)
    
  # COMMENT
  lengthEntry = tk.Entry(panel, width=15)
  lengthEntry.grid(row=0, column=0, padx=(300, 0), pady=(5, 0), 
                   sticky=tk.W)
    
  # COMMENT
  strandRadios = graphics.getBuilder().buildRadio(panel, ["yes", "no"])
  strandRadios[0].grid(row=0, column=0, padx=(475, 0), pady=(5, 0), 
                       sticky=tk.W)
  strandRadios[1].grid(row=0, column=1, padx=(0, 0), pady=(5, 0), 
                       sticky=tk.W)
  
'''
COMMENT
'''
def __buildUWPTopTitlePanel(graphics, panel):
  
  # COMMENT
  C = u"\u00b0" + "C"
  waterTempLabel = graphics.getBuilder().build11Label(panel, 
                                                      "Water Temp " + C)
  waterTempLabel.grid(row=0, column=0, padx=(100, 0), pady=(5, 0), 
                      sticky=tk.W)
  
  # COMMENT
  lengthLabel = graphics.getBuilder().build11Label(panel, "Length of DIp")
  lengthLabel.grid(row=0, column=0, padx=(300, 0), pady=(5, 0), 
                   sticky=tk.W)
  
  # COMMENT
  strandLabel = graphics.getBuilder().build11Label(panel,
                                                   "Strand Separator")
  strandLabel.grid(row=0, column=0, padx=(475, 0), pady=(5, 0), 
                   sticky=tk.W)
  
'''
COMMENT
'''
def __buildUWPPanel(graphics, panel):
  
  # COMMENT
  UWPTopTitlePanel = graphics.getBuilder().buildFrame(panel)
  UWPTopTitlePanel.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), 
                        sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildUWPTopTitlePanel(graphics, UWPTopTitlePanel)
  
  # COMMENT
  UWPTopContentPanel = graphics.getBuilder().buildFrame(panel)
  UWPTopContentPanel.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), 
                          sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildUWPTopContentPanel(graphics, UWPTopContentPanel)
  
  # COMMENT
  UWPBottomTitlePanel = graphics.getBuilder().buildFrame(panel)
  UWPBottomTitlePanel.grid(row=2, column=0, padx=(0, 0), pady=(0, 0), 
                           sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildUWPBottomTitlePanel(graphics, UWPBottomTitlePanel)
  
  # COMMENT
  UWPBottomContentPanel = graphics.getBuilder().buildFrame(panel)
  UWPBottomContentPanel.grid(row=3, column=0, padx=(0, 0), pady=(0, 0), 
                             sticky=tk.W, columnspan=20)
  
  # COMMENT
  __buildUWPBottomContentPanel(graphics, UWPBottomContentPanel)
  
'''
COMMENT
'''
def changeCooling(graphics, cool, panel):
  
  # COMMENT
  for widget in panel.winfo_children():
    widget.destroy()
    
  # COMMENT
  if cool == 1:
    __buildUWPPanel(graphics, panel)
  elif cool == 2:
    __buildSprayBeltPanel(graphics, panel)
  else:
    message = graphics.getBuilder().build11Label(panel, "Coming Soon")
    message.grid(row=0, column=0, padx=(75, 0), pady=(5, 0),
                 sticky=tk.W)
    
'''
COMMENT
'''
def changeExtruder(graphics, variable, extruder, menu,
                   portMenuPanel, portBoxPanel):
  menu["menu"].delete(0, "end")
  dic = graphics.getConfig().getConfigUpdate().EXTRUDER_DIES
  for value in dic[extruder]:
    menu["menu"].add_command(label=value, 
                        command=tk._setit(variable, value))
  variable.set(dic[extruder][0])
  
  # COMMENT
  __buildPortPanel(graphics, extruder, portMenuPanel, portBoxPanel)
  
'''
COMMENT
'''
def changePellet(graphics, variable, PMPanel):
  
  # COMMENT
  for widget in PMPanel.winfo_children():
    widget.destroy()
    
  # COMMENT
  if variable == "Pellet Mill":
    feederLabel = graphics.getBuilder().build11Label(PMPanel,
                                                     "Feeder Speed(%)")
    feederLabel.grid(row=0, column=0, padx=(100, 0), pady=(5, 0),
                     sticky=tk.W)
    pumpLabel = graphics.getBuilder().build11Label(PMPanel,
                                                   "Pump Speed(Hz)")
    pumpLabel.grid(row=0, column=0, padx=(350, 0), pady=(5, 0),
                   sticky=tk.W)
    feederScale = graphics.getBuilder().buildScale(PMPanel, 0, 100, 200)
    feederScale.grid(row=1, column=0, padx=(50, 0), pady=(0, 0), 
                     sticky=tk.W)
    pumpScale = graphics.getBuilder().buildScale(PMPanel, 0, 60, 200)
    pumpScale.grid(row=1, column=0, padx=(300, 0), pady=(0, 0), 
                   sticky=tk.W)

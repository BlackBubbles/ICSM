#!/usr/bin/python

'''
Program: Intergrated Interactive Systems and Management - IISM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 06/21/2017
Version: 0.0.1
Description:
    The following python file ...
'''

'''
Imported files/libraries
'''
import Tkinter as tk
import tkMessageBox

'''
Global variables
'''
# NONE

'''
COMMENT
'''
def __getDictionary(string):
  
  # COMMENT
  dictionary = {}
  
  # COMMENT
  values = string.split("   ")
  for value in values:
    parts = value.split(":")
    dictionary[parts[0].replace(" ", "")] = parts[1]
    
  # COMMENT
  return dictionary
  
'''
COMMENT
'''
def __getLabel(F, FT, S, Loc, Set, Per, RMS):
  if Loc.get() is 0:
    L = "None"
  elif Loc.get() is 1:
    L = "Throat"
  else:
    L = "Side Stuffer"
  if Set.get() is 0:
    Se = "None"
  elif Set.get() is 1:
    Se = "lbs/hr"
  else:
    Se = "kg/hr"
  RMString = "{" + "".join(RMS) + "}"
  string = "Feeder:" + F.get() +\
           "   Tubes:" + FT.get() +\
           "   Screw:" + S.get() +\
           "   Loc:" + L +\
           "   Set:" + Se +\
           "   Ingr:" + RMString +\
           "   Total:" + str(Per) + "%"
  return string
  
'''
COMMENT
'''
def cancel(feederGUI):
  feederGUI.destroy()
  
'''
COMMENT
'''
def deleteFeeder(graphics, panel):
  
  # COMMENT
  feeder = graphics.getUpdatePanel().getFeeders()[panel]
  total = float(feeder["Total"].replace("%", ""))
  per = graphics.getUpdatePanel().getTotalPercentage()
  graphics.getUpdatePanel().setTotalPercentage(per - total)
  graphics.getUpdatePanel().getFeeders().pop(panel, None)
  
  # COMMENT
  panel.destroy()

'''
COMMENT
'''
def deleteRM(graphics, panel, string, num):
  
  # COMMENT
  per = graphics.getUpdatePanel().getPercentage()
  graphics.getUpdatePanel().setPercentage(per - num)
  
  # COMMENT
  graphics.getUpdatePanel().getRMS().remove(string)
  
  # COMMENT
  panel.destroy()
  
'''
COMMENT
'''
def edit(graphics, feedPanel, feeder):
  graphics.getFeederGraphics().buildAddFeederGUI(graphics, feedPanel,
                                                 True, feeder)
  
'''
COMMENT
'''
def addRM(graphics, panel, name, percent):
  
  # COMMENT
  RMPanel = tk.Frame(panel, background=graphics.getConfig().BACKGROUND)
  RMPanel.pack()
  
  # COMMENT
  RM = name.get()
  per = percent.get()
  total = graphics.getUpdatePanel().getTotalPercentage()
  fper = graphics.getUpdatePanel().getPercentage()
  
  # COMMENT
  try:
    float(per)
  except ValueError:
    RMPanel.destroy()
    return 0
    
  # COMMENT
  if not RM or RM.isspace():
    RMPanel.destroy()
  elif (float(per) + total + fper) > 100.0:
    tkMessageBox.showwarning("ERROR", "Percentage is over 100%")
    RMPanel.destroy()
  else:
    
    # COMMENT
    percentage = graphics.getUpdatePanel().getPercentage()
    percentage = percentage + float(per)
    graphics.getUpdatePanel().setPercentage(percentage)
    
    # COMMENT
    name.delete(0, "end")
    percent.delete(0, "end")
    
    # COMMENT
    string = RM + "  " + per + "%"
    graphics.getUpdatePanel().getRMS().append(string)
    label = tk.Label(RMPanel,
                background=graphics.getConfig().BACKGROUND,
                text=string)
    label.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), sticky=tk.W)
    
    # COMMENT
    delete = tk.Button(RMPanel, text="delete",
           width=graphics.getConfig().BUTTON_WIDTH,
           height=graphics.getConfig().BUTTON_HEIGHT,
           activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
           command=lambda: graphics.getActions().getFeederActions()
                                   .deleteRM(graphics, RMPanel, string,
                                             float(per)))
    delete.grid(row=0, column=1, padx=(5, 0), pady=(5, 0), sticky=tk.W)
    
'''
COMMENT
'''
def apply(graphics, feederGUI, feedPanel, variableF, variableFT,
          variableS, variableLoc, variableSet):
  
  # COMMENT
  feederGUI.destroy()
  
  # COMMENT
  panel = tk.Frame(feedPanel, background=graphics.getConfig().BACKGROUND)
  panel.pack()
  
  # COMMENT
  string = __getLabel(variableF, variableFT, variableS, variableLoc,
                      variableSet, 
                      graphics.getUpdatePanel().getPercentage(),
                      graphics.getUpdatePanel().getRMS())
  label = tk.Label(panel, text=string,
                   background=graphics.getConfig().BACKGROUND)
  label.grid(row=0, column=0, padx=(100, 0), pady=(10, 0), sticky=tk.W)
  
  # COMMENT
  total = graphics.getUpdatePanel().getPercentage() +\
          graphics.getUpdatePanel().getTotalPercentage()
  graphics.getUpdatePanel().setTotalPercentage(total)
  graphics.getUpdatePanel().setPercentage(0)
  graphics.getUpdatePanel().resetRMS()
  graphics.getUpdatePanel().getFeeders()[panel] = __getDictionary(string)
  
  # COMMENT
  feeder = graphics.getUpdatePanel().getFeeders()[panel]
  edit = tk.Button(panel, text="Edit",
           width=graphics.getConfig().BUTTON_WIDTH,
           height=graphics.getConfig().BUTTON_HEIGHT,
           activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
           command=lambda: graphics.getActions().getFeederActions().
                                    edit(graphics, feedPanel, feeder))
  edit.grid(row=0, column=1, padx=(25, 0), pady=(10, 0), sticky=tk.W)
  
  # COMMENT
  delete = tk.Button(panel, text="Delete",
             width=graphics.getConfig().BUTTON_WIDTH,
             height=graphics.getConfig().BUTTON_HEIGHT,
             activebackground=graphics.getConfig().TDI_SELECTED_COLOR,
             command=lambda: graphics.getActions().getFeederActions()
                                     .deleteFeeder(graphics, panel))
  delete.grid(row=0, column=2, padx=(25, 0), pady=(10, 0), sticky=tk.W)
  
'''
COMMENT
'''
def changeFeeder(graphics, feeder, tubeVariable, tubeMenu, screwVariable,
                 screwMenu):
  tubeMenu["menu"].delete(0, "end")
  screwMenu["menu"].delete(0, "end")
  tubeDic = graphics.getConfig().getConfigUpdate().FEEDER_TUBES
  screwDic = graphics.getConfig().getConfigUpdate().FEEDER_SCREWS
  for value in tubeDic[feeder]:
    tubeMenu["menu"].add_command(label=value, 
                                 command=tk._setit(tubeVariable, value))
  for value in screwDic[feeder]:
    screwMenu["menu"].add_command(label=value, 
                                  command=tk._setit(screwVariable, value))
  tubeVariable.set(tubeDic[feeder][0])
  screwVariable.set(screwDic[feeder][0])

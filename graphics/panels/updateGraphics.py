#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 03/23/2017
Last Updated: 07/06/2017
Version: 1.0.0
Description:
    The following python file contains the code that builds the panel that updates the workflow .xlsx files
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
class UpdateG:
  
  '''
  COMMENT
  '''
  def __init__(self, graphics, builder):
    self.graphics = graphics
    self.builder = builder
    self.percentage = 0.0
    self.totalPercentage = 0.0
    self.RMS = []
    self.feeders = {}
      
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
  COMMENT
  '''
  def getPercentage(self):
    return self.percentage
    
  '''
  COMMENT
  '''
  def setPercentage(self, percentage):
    self.percentage = percentage
    
  '''
  COMMENT
  '''
  def getTotalPercentage(self):
    return self.totalPercentage
    
  '''
  COMMENT
  '''
  def setTotalPercentage(self, totalPercentage):
    self.totalPercentage = totalPercentage
    
  '''
  COMMENT
  '''
  def getRMS(self):
    return self.RMS
    
  '''
  COMMENT
  '''
  def resetRMS(self):
    self.RMS = []
    
  '''
  COMMENT
  '''
  def getFeeders(self):
    return self.feeders
    
  '''
  COMMENT
  '''
  def resetFeeders(self):
    self.feeders = {}
    
  '''
  COMMENT
  '''
  def __buildClassifiedContentPanel(self, panel):
    
    # COMMENT
    message = self.builder.buildLabel(panel, "COMING SOON")
    message.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                 sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildClassifiedTitlePanel(self, panel):
    
    # COMMENT
    classifiedLabel = self.builder.build11Label(panel, "Classified")
    classifiedLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                         sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildPelletizingCommentPanel(self, panel):
    
    # COMMENT
    commentLabel = self.builder.build11Label(panel, "Comments")
    commentLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                      sticky=tk.W)
    
    # COMMENT
    commentBox = tk.Text(panel, width=70, height=9)
    commentBox.grid(row=1, column=0, padx=(75, 0), pady=(0, 0), 
                    sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildPelletizingBottomContentPanel(self, panel):
    
    # COMMENT
    feedRollScale = self.builder.buildScale(panel, 0, 1000, 200)
    feedRollScale.grid(row=0, column=0, padx=(50, 0), pady=(0, 0), 
                       sticky=tk.W)
    
    # COMMENT
    rotorScale = self.builder.buildScale(panel, 0, 1000, 200)
    rotorScale.grid(row=0, column=0, padx=(300, 0), pady=(0, 0), 
                    sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildPelletizingBottomTitlePanel(self, panel):
    
    # COMMENT
    feedRollLabel = self.builder.build11Label(panel, "Feed Roll")
    feedRollLabel.grid(row=0, column=0, padx=(120, 0), pady=(5, 0), 
                       sticky=tk.W)
    
    # COMMENT
    rotorLabel = self.builder.build11Label(panel, "Rotor")
    rotorLabel.grid(row=0, column=0, padx=(380, 0), pady=(5, 0), 
                    sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildPelletizingTopContentPanel(self, panel, PMPanel):
    
    # COMMENT
    dic = self.graphics.getConfig().getConfigUpdate().PELLETIZING
    
    # COMMENT
    pellVariable = tk.StringVar(panel)
    pellVariable.set(dic[0])
    pellMenu = tk.OptionMenu(panel, pellVariable, *dic,
      command=lambda x: self.graphics.getActions().
                             getUpdateActions().
                             changePellet(self.graphics,
                                          pellVariable.get(), PMPanel))
    pellMenu.configure(width=15,
             activebackground=self.graphics.getConfig().ACTIVE_BACKGROUND)
    pellMenu.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                  sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildPelletizingTopTitlePanel(self, panel):
    
    # COMMENT
    pelletizingLabel = self.builder.build11Label(panel, "Pelletizing")
    pelletizingLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                          sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildOtherMessagePanel(self, panel):
    
    # COMMENT
    message = self.builder.buildLabel(panel, "COMING SOON")
    message.grid(row=0, column=0, padx=(125, 0), pady=(5, 0), 
                    sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildOtherPanel(self, panel):
    
    # COMMENT
    OtherLabel = self.builder.build13Label(panel, "Other")
    OtherLabel.grid(row=0, column=0, padx=(100, 0), pady=(15, 0), 
                    sticky=tk.W)
    
    # COMMENT
    OtherCheck = self.builder.buildCheckBox(panel, "")
    OtherCheck.grid(row=0, column=1, padx=(5, 0), pady=(15, 0), 
                    sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildStrandCoolingPanel(self, panel):
    
    # COMMENT
    label = self.builder.build11Label(panel, "Select Cooling")
    label.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
               sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildStrandCoolingRadio(self, panel, SCPanel):
    
    # COMMENT
    radios = self.builder.buildCoolingRadio(panel, 
                                     ["UWP", "Spray Belt", "Other"],
                                     self.graphics, SCPanel)
    index = 0
    for radio in radios:
      if index == 0:
        radio.grid(row=0, column=index, padx=(50, 0), pady=(5, 0),
                   sticky=tk.W)
      else:
        radio.grid(row=0, column=index, padx=(0, 0), pady=(5, 0),
                   sticky=tk.W)
      index = index + 1
      
  '''
  COMMENT
  '''
  def __buildPortSetUpPanel(self, panel):
    
    # COMMENT
    message = self.builder.build11Label(panel, "Select Extruder")
    message.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                 sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildFeederTitlePanel(self, panel):
    
    # COMMENT
    feederTitleLabel = self.builder.build14Label(panel, "Feeders")
    feederTitleLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), 
                          sticky=tk.W)
    
    # COMMENT
    feederPanel = self.builder.buildFrame(panel)
    feederPanel.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), 
                     sticky=tk.W, columnspan=20)
    
    # COMMENT
    feederButton = self.builder.buildButton(panel, "Add")
    feederButton.configure(command=lambda:
                           self.graphics.getActions().getUpdateActions().
                           addFeeder(self.graphics, feederPanel))
    feederButton.grid(row=0, column=1, padx=(15, 0), pady=(30, 0), 
                      sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildExtruderBottomContentPanel(self, panel):
    
    # COMMENT
    preDieVariable, preDieMenu = self.builder.buildStringDropDown(
           panel, 13, self.graphics.getConfig().getConfigUpdate().PRE_DIE)
    preDieMenu.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                    sticky=tk.W)
    
    # COMMENT
    screenPackCheckBox = self.builder.buildCheckBox(panel, "Yes")
    screenPackCheckBox.grid(row=0, column=0, padx=(275, 0), pady=(0, 0), 
                            sticky=tk.W)
    
    # COMMENT
    meshEntry = tk.Entry(panel)
    meshEntry.grid(row=0, column=0, padx=(400, 0), pady=(0, 0), 
                   sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildExtruderBottomTitlePanel(self, panel):
    
    # COMMENT
    preDieLabel = self.builder.build11Label(panel, "Pre-Die")
    preDieLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                     sticky=tk.W)
    
    # COMMENT
    screenPackLabel = self.builder.build11Label(panel, "Screen Pack")
    screenPackLabel.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                         sticky=tk.W)
    
    # COMMENT
    meshLabel = self.builder.build11Label(panel, "Mesh")
    meshLabel.grid(row=0, column=0, padx=(400, 0), pady=(5, 0), 
                   sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildExtruderTopContentPanel(self, panel, portMenuPanel,
                                     portBoxPanel):
    
    # COMMENT
    dic = self.graphics.getConfig().getConfigUpdate().EXTRUDERS
    
    # COMMENT
    dieVariable, dieMenu = self.builder.buildStringDropDown(panel, 11,
                             self.graphics.getConfig().
                                  getConfigUpdate().EXTRUDER_DIES[dic[0]])
    dieMenu.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                 sticky=tk.W)
    
    # COMMENT
    extruderVariable = tk.StringVar(panel)
    extruderVariable.set(dic[0])
    extruderMenu = tk.OptionMenu(panel, extruderVariable, *dic,
      command=lambda x: self.graphics.getActions().
                             getUpdateActions().
                             changeExtruder(self.graphics, dieVariable,
                                            extruderVariable.get(),
                                            dieMenu, portMenuPanel,
                                            portBoxPanel))
    extruderMenu.configure(width=15,
             activebackground=self.graphics.getConfig().ACTIVE_BACKGROUND)
    extruderMenu.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                      sticky=tk.W)
    
  '''
  COMMENT
  '''
  def __buildExtruderTopTitlePanel(self, panel):
    
    # COMMENT
    extruderLabel = self.builder.build11Label(panel, "Extruder")
    extruderLabel.grid(row=0, column=0, padx=(75, 0), pady=(5, 0), 
                       sticky=tk.W)
    
    # COMMENT
    dieLabel = self.builder.build11Label(panel, "Die Options")
    dieLabel.grid(row=0, column=0, padx=(275, 0), pady=(5, 0), 
                  sticky=tk.W)
    
  '''
  The following function builds the GUI for the update panel
  '''
  def buildPanel(self):
    
    # Get the "update" panel
    frame = self.graphics.getFrame("Update")
    
    # COMMENT
    panel = self.builder.buildScrollingCanvas(frame)
    
    # COMMENT
    self.builder.buildTitle(self.graphics, panel,
                            self.graphics.getConfig().
                            getConfigUpdate().TITLE)
    
    # COMMENT
    extruderTitleLabel = self.builder.build14Label(panel, 
                                                   "Extruder Options")
    extruderTitleLabel.grid(row=3, column=0, padx=(50, 0), pady=(25, 0), 
                            sticky=tk.W, columnspan=2)
    
    # COMMENT
    extruderTopTitlePanel = self.builder.buildFrame(panel)
    extruderTopTitlePanel.grid(row=4, column=0, padx=(0, 0), pady=(0, 0), 
                               sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildExtruderTopTitlePanel(extruderTopTitlePanel)
    
    # COMMENT
    extruderTopContentPanel = self.builder.buildFrame(panel)
    extruderTopContentPanel.grid(row=5, column=0, padx=(0, 0),
                                 pady=(0, 0), sticky=tk.W, columnspan=20)
    
    # COMMENT
    portSetUpDropDownPanel = self.builder.buildFrame(panel)
    portSetUpDropDownPanel.grid(row=9, column=0, padx=(0, 0),
                                pady=(0, 0), sticky=tk.W, columnspan=20)
    
    # COMMENT
    portSetUpBoxPanel = self.builder.buildFrame(panel)
    portSetUpBoxPanel.grid(row=10, column=0, padx=(55, 0), pady=(0, 0), 
                           sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildExtruderTopContentPanel(
      extruderTopContentPanel, portSetUpDropDownPanel, portSetUpBoxPanel)
    
    # COMMENT
    extruderBottomTitlePanel = self.builder.buildFrame(panel)
    extruderBottomTitlePanel.grid(row=6, column=0, padx=(0, 0),
                                  pady=(0, 0), sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildExtruderBottomTitlePanel(extruderBottomTitlePanel)
    
    # COMMENT
    extruderBottomContentPanel = self.builder.buildFrame(panel)
    extruderBottomContentPanel.grid(row=7, column=0, padx=(0, 0),
                                    pady=(0, 0), sticky=tk.W,
                                    columnspan=20)
    
    # COMMENT
    self.__buildExtruderBottomContentPanel(extruderBottomContentPanel)
    
    # COMMENT
    feederTitlePanel = self.builder.buildFrame(panel)
    feederTitlePanel.grid(row=11, column=0, padx=(0, 0), pady=(0, 0), 
                          sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildFeederTitlePanel(feederTitlePanel)
    
    # COMMENT
    portSetUpTitle = self.builder.build14Label(panel, "Port Set-Up")
    portSetUpTitle.grid(row=8, column=0, padx=(50, 0), pady=(25, 0), 
                        sticky=tk.W)
    
    # COMMENT
    self.__buildPortSetUpPanel(portSetUpBoxPanel)
    
    # COMMENT
    strandCoolingTitle = self.builder.build14Label(panel,
                                                 "Strand Cooling Options")
    strandCoolingTitle.grid(row=12, column=0, padx=(50, 0), pady=(25, 0), 
                            sticky=tk.W)
    
    # COMMENT
    strandCoolingPanel = self.builder.buildFrame(panel)
    strandCoolingPanel.grid(row=14, column=0, padx=(0, 0), pady=(0, 0),
                            sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildStrandCoolingPanel(strandCoolingPanel)
    
    # COMMENT
    strandCoolingRadioPanel = self.builder.buildFrame(panel)
    strandCoolingRadioPanel.grid(row=13, column=0, padx=(0, 0),
                                 pady=(0, 0), sticky=tk.W, columnspan=20)
    
    # COMMENT
    self.__buildStrandCoolingRadio(strandCoolingRadioPanel,
                                   strandCoolingPanel)
    
    # COMMENT
    pelletizingTitle = self.builder.build14Label(panel,
                                                 "Pelletizing Options")
    pelletizingTitle.grid(row=15, column=0, padx=(50, 0), pady=(25, 0), 
                          sticky=tk.W)
    
    # COMMENT
    pelletizingTopTitlePanel = self.builder.buildFrame(panel)
    pelletizingTopTitlePanel.grid(row=16, column=0, padx=(0, 0),
                                  pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildPelletizingTopTitlePanel(pelletizingTopTitlePanel)
    
    # COMMENT
    pelletizingPelletMillPanel = self.builder.buildFrame(panel)
    pelletizingPelletMillPanel.grid(row=20, column=0, padx=(0, 0),
                                    pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    pelletizingTopContentPanel = self.builder.buildFrame(panel)
    pelletizingTopContentPanel.grid(row=17, column=0, padx=(0, 0),
                                    pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildPelletizingTopContentPanel(pelletizingTopContentPanel,
                                           pelletizingPelletMillPanel)
    
    # COMMENT
    pelletizingBottomTitlePanel = self.builder.buildFrame(panel)
    pelletizingBottomTitlePanel.grid(row=18, column=0, padx=(0, 0),
                                     pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildPelletizingBottomTitlePanel(pelletizingBottomTitlePanel)
    
    # COMMENT
    pelletizingBottomContentPanel = self.builder.buildFrame(panel)
    pelletizingBottomContentPanel.grid(row=19, column=0, padx=(0, 0),
                                       pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildPelletizingBottomContentPanel(
             pelletizingBottomContentPanel)
    
    # COMMENT
    pelletizingCommentPanel = self.builder.buildFrame(panel)
    pelletizingCommentPanel.grid(row=21, column=0, padx=(0, 0),
                                 pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildPelletizingCommentPanel(pelletizingCommentPanel)
    
    # COMMENT
    classifiedTitle = self.builder.build14Label(panel,
                                                "Classified Options")
    classifiedTitle.grid(row=22, column=0, padx=(50, 0), pady=(25, 0), 
                         sticky=tk.W)
    
    # COMMENT
    classifiedTitlePanel = self.builder.buildFrame(panel)
    classifiedTitlePanel.grid(row=23, column=0, padx=(0, 0), pady=(0, 0), 
                              sticky=tk.W)
    
    # COMMENT
    self.__buildClassifiedTitlePanel(classifiedTitlePanel)
    
    # COMMENT
    classifiedContentPanel = self.builder.buildFrame(panel)
    classifiedContentPanel.grid(row=24, column=0, padx=(0, 0),
                                pady=(0, 0), sticky=tk.W)
    
    # COMMENT
    self.__buildClassifiedContentPanel(classifiedContentPanel)
    
    # COMMENT
    updateButton = self.builder.buildUpdateButton(panel, "Update")
    updateButton.configure(command=lambda:
                           tkMessageBox.showwarning(
                                   "ERROR", "Update Button is not Ready"))
    updateButton.grid(row=25, column=0, padx=(300, 0), pady=(50, 50),
                      sticky=tk.W)

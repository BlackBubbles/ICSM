#!/usr/bin/python

'''
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 04/19/2017
Last Updated: 08/16/2017
Version: 1.0.0
Description:
    The following python module contains the code that builds the panel that contains the options for the feeders that
    are used on the extruders
'''

'''
Imported files/libraries
'''
import sys
from types import ModuleType
import Tkinter as tk
import tkMessageBox

'''
Global variables
'''
ERROR = "AN ERROR HAS OCCURRED"

'''
The following class is the view code for the feeder GUI
'''
class FeederG:

  '''
  The following function is the initial function for the "FeederG" class
  '''
  def __init__(self, config, builder):

    # Set and check the inputted config
    doesWork, message = self.setConfig(config)
    if not doesWork:
        print message
        sys.exit()

    # Create the initial variables for this instance of the class
    self.actions = None
    self.data = None
    self.builder = builder
    self.gui = None
    self.feederTubeMenu = None
    self.feederScrewMenu = None
    self.RMFrame = None
    self.RMCodeEntry = None
    self.RMPercentEntry = None
    self.sections = {}
    self.labels = {}

  '''
  The following function returns the configuration file for this instance of the "FeederG" class
  '''
  def getConfig(self):
    return self.config

  '''
  The following function sets the configuration file for the "FeederG" class. If the inputted config file does not meet
  the requirements then the function returns a "False" boolean value and an error message
  '''
  def setConfig(self, config):
    if isinstance(config, ModuleType):
      if hasattr(config, "confirm"):
        if config.confirm("Extruder"):
          self.config = config
        else:
          return False, "%s:\nconfig file for FeederG is not configExtruder" % ERROR
      else:
        return False, "%s:\nconfig file is not a designated config file for this program" % ERROR
    else:
      return False, "%s:\ninputted file is not a Module" % ERROR
    return True, ""

  '''
  The following function returns the instance of the "FeederA" class for this instance of the "FeederG" class
  '''
  def getActions(self):
      return self.actions

  '''
  The following function sets the instance of the "FeederA" class for the "FeederG" class. If the inputted Data
  class file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setActions(self, actions):

      # Create the initial return variables and their values
      doesWork = True
      message = ""

      # Check to make sure that the inputted value is an instance of the "FeederA" class
      if hasattr(actions, "confirm"):
          if actions.confirm("Feeder"):
              self.actions = actions
          else:
              doesWork = False
              message = "%s:\ninputted file for FeederG is not a FeederA class file" % ERROR
      else:
          doesWork = False
          message = "%s:\ninputted file is not a designated Data class file for this program" % ERROR

      # Return the initial variable
      return doesWork, message

  '''
  The following function returns the instance of the "FeederD" class for this instance of the "FeederG" class
  '''
  def getData(self):
      return self.data

  '''
  The following function sets the instance of the "FeederD" class for the "FeederG" class. If the inputted Graphics
  class file does not meet the requirements then the function returns a "False" boolean value and an error message
  '''
  def setData(self, data):

      # Create the initial return variables and their values
      doesWork = True
      message = ""

      # Check to make sure that the inputted value is an instance of the "FeederD" class
      if hasattr(data, "confirm"):
          if data.confirm("Feeder"):
              self.data = data
          else:
              doesWork = False
              message = "%s:\ninputted file for FeederG is not a FeederD class file" % ERROR
      else:
          doesWork = False
          message = "%s:\ninputted file is not a designated Actions class file for this program" % ERROR

      # Return the initial variable
      return doesWork, message

  '''
  The following function returns the GUI builder
  '''
  def getBuilder(self):
    return self.builder

  '''
  The following function returns the whole GUi for the feeder
  '''
  def getGUI(self):
    return self.gui

  '''
  The following function returns the Tkinter Optionsmenu for the feeder tube options
  '''
  def getFeederTubeMenu(self):
    return self.feederTubeMenu

  '''
  The following function sets the Tkinter Optionsmenu for the feeder tube options
  '''
  def setFeederTubeMenu(self, feederTubeMenu):
    self.feederTubeMenu = feederTubeMenu

  '''
  The following function returns the Tkinter Optionsmenu for the feeder screw options
  '''
  def getFeederScrewMenu(self):
    return self.feederScrewMenu

  '''
  The following function sets the Tkinter Optionsmenu for the feeder screw options
  '''
  def setFeederScrewMenu(self, feederScrewMenu):
    self.feederScrewMenu = feederScrewMenu

  '''
  The following function returns the Tkinter Frame for the RM code section
  '''
  def getRMFrame(self):
    return self.RMFrame

  '''
  The following function sets the Tkinter Frame for the RM code section
  '''
  def setRMFrame(self, RMFrame):
    self.RMFrame = RMFrame

  '''
  The following function returns the Tkinter Entry for the RM Code
  '''
  def getRMCodeEntry(self):
    return self.RMCodeEntry

  '''
  The following function sets the Tkinter Entry for the RM Code
  '''
  def setRMCodeEntry(self, RMCodeEntry):
    self.RMCodeEntry = RMCodeEntry

  '''
  The following function returns the Tkinter Entry for the RM Percentage
  '''
  def getRMPercentEntry(self):
    return self.RMPercentEntry

  '''
  The following function sets the Tkinter Entry for the RM Percentage
  '''
  def setRMPercentEntry(self, RMPercentEntry):
    self.RMPercentEntry = RMPercentEntry

  def getSections(self):
    return self.sections

  '''
  The following function returns the dictionary of labels that contain the title of the selections their next to
  '''
  def getLabels(self):
    return self.labels

  '''
  The following function builds and adds the RM Code slot onto the GUI
  '''
  def addRM(self):
    print "addRM"

  '''
  The following function builds the "Feeder" section for the feeder GUI
  '''
  def __buildFeeder(self, frame, edit=False, data=None):

    # Build and add the "Feeder" drop down menu
    text = "Feeder"
    feederLabel = self.getBuilder().buildH3Label(frame, text)
    feederLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 0), sticky=tk.W)
    self.getLabels()[self.getConfig().FEEDER_OPTIONS_TITLE][text] = feederLabel
    feederMenu, feederVariable = self.getBuilder().buildStringDropDown(self.getActions().respondToFeeder,
                                                                       self.getConfig().FEEDER_OPTIONS_TITLE,
                                                                       feederLabel, frame, 15,
                                                                       self.getConfig().FEEDERS)
    self.getData().setFeederVariable(feederVariable)
    if edit:
      self.getData().getFeederVariable().set(data['Feeder'])
    feederMenu.grid(row=1, column=0, padx=(40, 0), pady=(0, 0), sticky=tk.W)

    # Build and add the "Tube" drop down menu
    text = "Tube"
    tubeLabel = self.getBuilder().buildH3Label(frame, text)
    tubeLabel.grid(row=0, column=0, padx=(250, 0), pady=(25, 0), sticky=tk.W)
    self.getLabels()[self.getConfig().FEEDER_OPTIONS_TITLE][text] = tubeLabel
    index = self.getConfig().FEEDERS.index(self.getData().getFeederVariable().get())
    tubeMenu, tubeVariable = self.getBuilder().buildStringDropDown(self.getActions().respondToMenu,
                                                                   self.getConfig().FEEDER_OPTIONS_TITLE,
                                                                   tubeLabel, frame, 15,
                                                                   self.getConfig().FEEDER_TUBES[
                                                                     self.getConfig().FEEDERS[index]])
    self.getData().setFeederTubeVariable(tubeVariable)
    if edit:
      if 'Tube' in data:
        self.getData().getFeederTubeVariable().set(data['Tube'])
    self.setFeederTubeMenu(tubeMenu)
    tubeMenu.grid(row=1, column=0, padx=(240, 50), pady=(0, 0), sticky=tk.W)

    # Build and add the "Screw" drop down menu
    text = "Screw"
    screwLabel = self.getBuilder().buildH3Label(frame, text)
    screwLabel.grid(row=2, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)
    self.getLabels()[self.getConfig().FEEDER_OPTIONS_TITLE][text] = screwLabel
    screwMenu, screwVariable = self.getBuilder().buildStringDropDown(self.getActions().respondToMenu,
                                                                     self.getConfig().FEEDER_OPTIONS_TITLE,
                                                                     screwLabel, frame, 15,
                                                                     self.getConfig().FEEDER_SCREWS[
                                                                       self.getConfig().FEEDERS[index]])
    self.getData().setFeederScrewVariable(screwVariable)
    if edit:
      self.getData().getFeederScrewVariable().set(data['Screw'])
    self.setFeederScrewMenu(screwMenu)
    screwMenu.grid(row=3, column=0, padx=(40, 0), pady=(0, 35), sticky=tk.W)

  '''
  The following function builds the "Location/Measurement" section for the feeder GUI
  '''
  def __buildLocationMeasure(self, frame, edit=False, data=None):

    # Build and add the radio buttons for "location"
    text = "Location:"
    locLabel = self.getBuilder().buildH3Label(frame, text)
    locLabel.grid(row=0, column=0, padx=(50, 0), pady=(25, 35), sticky=tk.W)
    self.getLabels()[self.getConfig().RADIO_BUTTON_TITLE][text] = locLabel
    locRadios, locVariable = self.getBuilder().buildRadio(self.getActions().respondToRadio,
                                                          self.getConfig().RADIO_BUTTON_TITLE, locLabel, frame,
                                                          self.getConfig().FEEDER_LOCATIONS)
    self.getData().setLocationVariable(locVariable)
    if edit:
      self.getData().getLocationVariable().set(data['Location'])
    locRadios[0].grid(row=0, column=1, padx=(0, 0), pady=(25, 35), sticky=tk.W)
    locRadios[1].grid(row=0, column=2, padx=(0, 50), pady=(25, 35), sticky=tk.W)

  '''
  The following function builds the "RM Code" section for the feeder GUI
  '''
  def __buildRMCode(self, frame, edit=False, data=None):

    # Build and add the two Entry slots
    self.setRMCodeEntry(tk.Entry(frame, width=21))
    self.getRMCodeEntry().grid(row=0, column=0, padx=(25, 0), pady=(25, 0), sticky=tk.W)
    self.setRMPercentEntry(tk.Entry(frame, width=6))
    self.getRMPercentEntry().grid(row=0, column=1, padx=(5, 0), pady=(25, 0), sticky=tk.W)
    per = 100.0 - (self.getData().getCompletePercentage() + self.getData().getTotalPercentage())
    self.getRMPercentEntry().insert(0, str(per))

    # Build and add the "Add" button
    button = self.getBuilder().buildButton(frame, "Add RM")
    button.grid(row=0, column=2, padx=(5, 25), pady=(25, 0), sticky=tk.W)
    button.configure(command=lambda: self.getActions().respondToAdd(self.getConfig().RM_TITLE))

    # Build and save the RM Code frame
    self.setRMFrame(self.getBuilder().buildFrame(frame))
    self.getRMFrame().grid(row=1, column=0, columnspan=20, padx=(0, 35), pady=(0, 35), sticky=tk.W)

    '''Check 'edit' and add any RM codes'''
    if edit:
      for rm, per in data['RM'].iteritems():
        self.addRM(rm, str(per))

  '''
  The following function builds the initial GUI for the feeder selection
  '''
  def buildGUI(self, edit=False, data=None, back=None):

    # Build the initial frame and give it a title
    gui = tk.Toplevel()
    gui.wm_title("Feeder Options")
    self.gui = gui
    #gui.attributes("-topmost", "true")

    # Resize and position the frame
    width = gui.winfo_screenwidth()
    height = gui.winfo_screenheight()
    x = width / 2 - 200
    y = height / 2 - 350
    gui.geometry("%dx%d+%d+%d" % (500, 600, x, y))
    gui.wm_geometry("500x600")

    # Build and add the scroll bar
    frame = self.getBuilder().buildScrollingCanvas(gui)

    # Build and add the feeder drop down menus options frame
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=0, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    feederFrame, feederLabel = self.getBuilder().buildSection(tempFrame, self.getConfig().FEEDER_OPTIONS_TITLE)
    self.sections[self.getConfig().FEEDER_OPTIONS_TITLE] = feederFrame
    self.labels[self.getConfig().FEEDER_OPTIONS_TITLE] = {self.getConfig().FEEDER_OPTIONS_TITLE: feederLabel}
    self.__buildFeeder(feederFrame, edit=edit, data=data)

    # Build and add the feeder radio buttons options frame
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=1, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    LMFrame, LMLabel = self.getBuilder().buildSection(tempFrame, self.getConfig().RADIO_BUTTON_TITLE)
    self.sections[self.getConfig().RADIO_BUTTON_TITLE] = LMFrame
    self.labels[self.getConfig().RADIO_BUTTON_TITLE] = {self.getConfig().RADIO_BUTTON_TITLE: LMLabel}
    self.__buildLocationMeasure(LMFrame, edit=edit, data=data)

    # Build and add the feeder RM Code section frame
    tempFrame = self.getBuilder().buildFrame(frame)
    tempFrame.grid(row=2, column=0, columnspan=20, padx=(0, 0), pady=(0, 0), sticky=tk.W)
    RMFrame, RMLabel = self.getBuilder().buildSection(tempFrame, self.getConfig().RM_TITLE)
    self.sections[self.getConfig().RM_TITLE] = RMFrame
    self.labels[self.getConfig().RM_TITLE] = {self.getConfig().RM_TITLE: RMLabel}
    self.__buildRMCode(RMFrame, edit=edit, data=data)

    # Build and add the "Apply" button on the bottom
    applyButton = self.getBuilder().buildBottomButton(frame, "Apply")
    applyButton.grid(row=3, column=0, padx=(100, 0), pady=(35, 50), sticky=tk.W)
    applyButton.configure(command=lambda: self.getActions().respondToApply(edit=edit, back=back))

    # Build and add the "Cancel" button on the bottom
    cancelButton = self.getBuilder().buildBottomButton(frame, "Cancel")
    cancelButton.grid(row=3, column=0, padx=(300, 0), pady=(35, 50), sticky=tk.W)
    cancelButton.configure(command=lambda: self.getActions().respondToCancel(gui))

  '''
  The following function changes the content of the tube and screw drop down menus
  '''
  def changeFeeder(self):

    # Set the initial variable's content
    tubeFunction = self.getActions().respondToTube
    screwFunction = self.getActions().respondToScrew
    tubeDictionary = self.getConfig().FEEDER_TUBES
    screwDictionary = self.getConfig().FEEDER_SCREWS
    extruder = self.getData().getFeederVariable().get()
    section = self.getConfig().FEEDER_OPTIONS_TITLE
    tubeLabel = self.getLabels()[section]["Tube"]
    screwLabel = self.getLabels()[section]["Screw"]

    # Delete the formor content
    self.getFeederTubeMenu()["menu"].delete(0, "end")
    self.getFeederScrewMenu()["menu"].delete(0, "end")

    # Fill both menus with content and bind the commands
    for string in tubeDictionary[extruder]:
      self.getFeederTubeMenu()["menu"].add_command(label=string, command=lambda value=string: tubeFunction(section, tubeLabel, value))
    for string in screwDictionary[extruder]:
      self.getFeederScrewMenu()["menu"].add_command(label=string, command=lambda value=string: screwFunction(section, screwLabel, value))

    # Set the initial values in both menus
    self.getData().getFeederTubeVariable().set(self.getConfig().FEEDER_TUBES[extruder][0])
    self.getData().getFeederScrewVariable().set(self.getConfig().FEEDER_SCREWS[extruder][0])

  '''
  The following function adds an RM slot to the feeder GUI
  '''
  def addRM(self, RM, Percent):

    # Create the RM Frame slot
    frame = self.getBuilder().buildFrame(self.getRMFrame())
    frame.pack()

    # Create the RM Label
    label = self.getBuilder().buildLabel(frame, RM + "   ==   " + Percent)
    label.grid(row=0, column=0, padx=(50, 0), pady=(15, 0), sticky=tk.W)

    # Create the RM delete button
    button = self.getBuilder().buildButton(frame, "Delete")
    button.grid(row=0, column=0, padx=(250, 0), pady=(15, 0), sticky=tk.W)
    button.configure(command=lambda: self.getActions().respondToDelete(frame, RM, Percent))

  '''
  The following function checks the labels of the section headers
  '''
  def checkSectionLabels(self, section):
    allNormal = True
    labels = self.getLabels()[section]
    for key, label in labels.iteritems():
      if key is section:
        continue
      if label["foreground"] == self.getConfig().ERROR_COLOR:
        allNormal = False
        break
    if allNormal:
      labels[section]["foreground"] = self.getConfig().ACTIVE_BACKGROUND
      self.sections[section].config(highlightbackground=self.getConfig().ACTIVE_BACKGROUND)

  '''
  The following function displays an error message to the user
  '''
  def displayErrorMessage(self, errors, errorTextLabels):

    # Set the unused labels to red
    for section, list in errorTextLabels.iteritems():
      labels = self.getLabels()[section]
      if not len(list) is 0:
        labels[section]["foreground"] = self.getConfig().ERROR_COLOR
        self.sections[section].config(highlightbackground=self.getConfig().ERROR_COLOR)
        for item in list:
          if item == "":
            continue
          labels[item]["foreground"] = self.getConfig().ERROR_COLOR

    # Display the error message
    tkMessageBox.showerror("ERROR", "".join(errors))

  '''
  The following function returns a confirmation that tells the calling code which class file this function belongs to
  '''
  def confirm(self, value):
    if isinstance(value, basestring):
      if value.lower() == "feeder":
        return True
      else:
        return False
    else:
      return False
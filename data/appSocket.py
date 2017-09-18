#!/usr/bin/python

"""
Program: Interfacial Consultant's Systems and Management - ICSM
Programmer: Talib M. Khan
Date Created: 09/05/2017
Last Updated: 09/05/2017
Version: 1.0.0
Description:
    The following python file contains the model code functions for the "Extruder" panel for the ICSM program
"""

'''
Imported files/libraries
'''
import json
import socket

'''
Global variables
'''
TCP_IP = "192.168.0.23"
# TCP_IP = '192.168.0.150'
TCP_PORT = 1234
BUFFER_SIZE = 1024

'''
The following class is the model for the "Extruder" panel
'''
class Socket:

    # Initial function
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    '''
    The following function returns the socket for this instance of the class
    '''
    def getSocket(self):
        return self.socket

    '''
    The following function attempts to connect to the socket
    '''
    def connect(self):
        try:
            self.getSocket().connect((TCP_IP, TCP_PORT))
            self.getSocket().send("App-0")
            if self.getSocket().recv(BUFFER_SIZE) == "1":
                return 2
            else:
                return 1
        except:
            return 0

    '''
    The following function converts an inputted dict, list, etc. into an array of strings
    '''
    def toStringArray(self, input, length):
        string = json.dumps(input)
        # print "String - ", string
        list = []
        for i in range(0, len(string), length):
            list.append(string[i:length + i])
            # print "   -   ", string[i:length + i]
        return list

    '''
    The following function attempts to send data to the server
    '''
    def send(self, command, project, panel, dict):
        self.getSocket().send(command)
        self.getSocket().recv(BUFFER_SIZE)
        self.getSocket().send(project)
        self.getSocket().recv(BUFFER_SIZE)
        self.getSocket().send(panel)
        self.getSocket().recv(BUFFER_SIZE)
        list = self.toStringArray(dict, 512)
        # print "list - ", list
        self.getSocket().send(str(len(list)))
        self.getSocket().recv(BUFFER_SIZE)
        for i in range(0, len(list)):
            self.getSocket().send(list[i])
            self.getSocket().recv(BUFFER_SIZE)
        return self.getSocket().recv(BUFFER_SIZE)
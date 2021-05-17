
This program takes input from the user to start the application, enter the commands, navigate throughout about, 
info, list and finally exit. The application displays a welcome message and a farewell message and quits. 
The user can edit by adding and removing contacts. the user can load a CSV file or save contacts in one by 
navigating to the Archove dialog boxes. Some contacts where added to the lsit for visualisation and for testing.
They can also save and visualize the list by navigating throughout the dialog boxes that are included.

The program opens a GUI using tkinter. The following included modules provide this functionality. 
	from tkinter import *
	from tkinter import filedialog
	import tkinter.messagebox



The dialog boxes have options to navigate and choose what the user wants to accomplish. 
The following example is the “About” dialog. 
	def dialog(opti):

The menu functions:
	def saving():
	def formating():
	def exiting():

The functions to archive and control content:
	def archive_in_usage(permissions):
    	def reading():
	def scribe():
	def delete_content()

Manage directories functions
	def new():
	def oppenig():
	def save_as(opti):
    
Clicking Functions:
	def adding(name, email, phone):
	def cleaning(opti):

Main and menu declaration:
	Using the Pack Manager
D	eclaring graphic elements and setting up GUI labels


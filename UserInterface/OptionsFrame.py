import customtkinter
from functools import partial
import math

BUTTON_FONT = ("Tekon Pro", 24)

'''
Options Button Frame Class:
    The class below defines the Frame and buttons for the options frame of the
    AutoBartender User Interface. Consiting of variable length columns
    and row count, the initialization of the class will populate itself
    (a customtkinter Frame inherited object) with a grid of buttons. The name 
    and callback functions are passed into the constructor as an array of 
    tuples (See input section below).

Constructor Input:
    master - The customtkinter application that the frame will attach to.
    options - An array of tuples in the form of (ItemName, CallbackFunction)
    callback - Function to be called when a button is selected
    colCount - The number of columns accross
    padding - The number of pixels in between buttons/ boarders

Public Functions:
    loadButtons - Populates the buttons array based on the options and callback of the class
    reloadButtons - reloadButtons based on passed in options, callback, colCount, and padding
    formatButtons - Reorganize the options based on the set column and padding values
    addOption - Adds an option to the button array
    deleteOption - Delete an option from the button array
    setCallback - Set the callback function of the class
    getCallback - Get the callback function
    setOptions - Set a new list of options
    getOptions - Retrieve a list of all of the options
    setPadding - Sets the padding value
    getPadding - Get the padding value
    setColCount - Sets the colCount value
    getColCount - Get the colCount value

Private Functions:
    N/A 
Destructor:
    N/A

'''

class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master, options, callback, colCount=3, padding=20):
        super().__init__(master)
        self.buttons = []
        self.colCount = colCount
        self.padding = padding
        self.options = list(options)
        self.callback = callback
        self.loadButtons()
        self.formatButtons()

    def reloadButtons(self, options, callback, colCount=3, padding=20):
        self.options = list(options)
        self.callback = callback
        self.colCount = colCount
        self.padding = padding
        self.loadButtons()
        self.formatButtons()

    def formatButtons(self):
        if 0 == len(self.buttons):
            return

        rowTuple = tuple([i for i in range(math.ceil(len(self.buttons)/self.colCount))])
        colTuple = tuple([i for i in range(min(len(self.buttons), self.colCount))])
        if rowTuple == ():
            rowTuple = 0

        self.grid_rowconfigure(rowTuple, weight=1)
        self.grid_columnconfigure(colTuple, weight=1)

        for i, button in enumerate(self.buttons):
            button.grid(row=i//self.colCount, column=i%self.colCount, 
                        padx=self.padding, pady=self.padding, sticky="nsew")

    def loadButtons(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []
        for option in self.options:
            assert type(option) == str
            button = customtkinter.CTkButton(self, text=option, font=BUTTON_FONT, command=partial(self.callback, option))
            self.buttons.append(button)
        self.formatButtons()

    def addOption(self, option):
        button = customtkinter.CTkButton(self, text=option, command=partial(self.callback, option))
        self.buttons.append(button)
        self.buttons = sorted(self.buttons, key=lambda x: x.cget('text'))
        self.options.append(option)
        self.options = sorted(self.options)

    def deleteOption(self, option):
        for button in self.buttons:
            if option == button.cget('text'):
                self.buttons.remove(button)
                self.options.remove(option)

    def setOptions(self, options):
        self.options = list(options)
        self.loadButtons()
    def getOptions(self):
        return list(self.options)
    def getCallback(self):
        return self.callback
    def setCallback(self, callback):
        self.callback = callback
    def setPadding(self, newPadding):
        self.padding = newPadding
    def getPadding(self):
        return self.padding
    def setColCount(self, newColCount):
        self.colCount = newColCount
    def getColCount(self):
        return self.colCount


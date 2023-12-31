import customtkinter
from functools import partial
import math

MAX_MOD_DISPLAY = 6
SPINBOX_PADX = 10
SPINBOX_PADY = 10

FONT_FAMILY = ("Tekon Pro", 20)

'''
    Modifications Frame Class:
        The following class defines the modifications frame, enabling a user to
        alter the content of their selection prior to submitting their request.
        Utilizing a custom spinbox class for each item, enabling a user to
        modify the quantity of each ingredient up to a total "cost" value.
        (Will eventually be using weight/ volume as a max to ensure a cup
        does not overflow). In the event not all ingredients fit in a single
        frame, there are previous and next buttons located at the top and bottom
        to "scroll" through the configurable elements. 
'''

class ModificationFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, elements=[], values=[], total=0, **kwargs):
        # Argument checking
        assert len(elements) == len(values)
        for i in range(len(elements)):
            assert str == type(elements[i])
            assert float == type(values[i])
        assert float == type(total)

        # Invoke init of super
        super().__init__(master, **kwargs)

        #Setup element data storage
        self.elements = {}
        for i in range(len(elements)):
            self.elements[elements[i]] = values[i]
        
        self.spinBoxes = []
        self.total = total

        # SpinBox Display Variables
        self.currIndex = 0
        
        # Ingredient Sum Variables
        self.sumVar = customtkinter.DoubleVar()
        self.sumVar.set(0)
        self.sumEntry = customtkinter.CTkEntry(self, font=FONT_FAMILY, width=100)
        self.sumEntry.grid(row=min(len(elements), MAX_MOD_DISPLAY)+3, column=0)

        # Next and Previous Button setup
        self.prevButton = customtkinter.CTkButton(self, text='^', font=FONT_FAMILY, command=self.showPrevious)
        self.nextButton = customtkinter.CTkButton(self, text='v', font=FONT_FAMILY, command=self.showNext)
        if (len(elements) > MAX_MOD_DISPLAY):
            self.nextButton.grid(row=min(len(elements), MAX_MOD_DISPLAY)+1, column=0, sticky='ns')
            self.prevButton.grid(row=0, column=0, sticky='ns')

        # Label for current items displayed
        self.rangeLabel = customtkinter.CTkLabel(self, font=FONT_FAMILY, text="", pady=10)
        self.rangeLabel.grid(row=min(len(elements), MAX_MOD_DISPLAY)+2, column=0)

        # Complete setup of spinboxes and labels/entries
        self.loadSpinBoxes()
        self.updateSpinBoxVisibility()
        self.updateRangeLabel()
        self.updateSum()
    
    def loadSpinBoxes(self):
        if 0 == len(self.elements):
            return
        
        rowTuple = tuple([i for i in range(8)])
        self.grid_rowconfigure(rowTuple, weight=1)

        self.grid_columnconfigure(0, weight=1)

        for ele in self.elements:
            spinBox = SpinBoxFrame(self, ele, self.elements[ele], self.sumVar, self.total)
            
            spinBox.value.trace_add('write', lambda *args, box=spinBox: self.updateSum())
            self.spinBoxes.append(spinBox)
        
        self.updateSpinBoxVisibility()

    def getElementValues(self):
        for spinBox in self.spinBoxes:
            self.elements[spinBox.getText()] = spinBox.getValue()
        return self.elements

    def resetDefaultValues(self):
        for spinBox in self.spinBoxes:
            item = spinBox.getText()
            spinBox.setValue(self.elements[item])
            spinBox.updateButtonStates()

    def updateSum(self):
        total = sum([spinBox.getValue() for spinBox in self.spinBoxes]) 
        self.sumVar.set(total)
        self.sumEntry.delete(0, customtkinter.END)
        self.sumEntry.insert(0, total)
        for spinBox in self.spinBoxes:
            spinBox.updateButtonStates()

    def showNext(self):
        if self.currIndex < len(self.spinBoxes) - 1 and len(self.elements) > MAX_MOD_DISPLAY:
            self.currIndex += min(MAX_MOD_DISPLAY, len(self.elements) - (self.currIndex+MAX_MOD_DISPLAY))
            self.updateSpinBoxVisibility()
            self.updateRangeLabel()

    def showPrevious(self):
        if self.currIndex > 0:
            self.currIndex -= min(MAX_MOD_DISPLAY, self.currIndex)
            self.updateSpinBoxVisibility()
            self.updateRangeLabel()

    def updateSpinBoxVisibility(self):
        for i, spinBox in enumerate(self.spinBoxes):
            if self.currIndex <= i and i < self.currIndex + MAX_MOD_DISPLAY:
                spinBox.grid(row=i - self.currIndex + 1, column=0, padx=10, pady=10, sticky='nswe')
            else:
                spinBox.grid_forget()
    
    def updateRangeLabel(self):
        self.rangeLabel.configure(text=f"Ingredients {self.currIndex+1} to {min(self.currIndex+MAX_MOD_DISPLAY, len(self.spinBoxes))} of {len(self.spinBoxes)}")

class SpinBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, text="", value=None, sum_var=None, sum_max=0, **kwargs):
        super().__init__(master, **kwargs)
        self.value = customtkinter.DoubleVar(self, value)
        self.sumVar = sum_var
        self.sumMax = sum_max
        self.text = text

        self.grid_columnconfigure(0, weight=3)

        self.label = customtkinter.CTkLabel(self, text=self.text, font=FONT_FAMILY,width=self.winfo_width()/2, anchor='w')
        self.label.grid(row=0, column=0, padx=SPINBOX_PADX, pady=SPINBOX_PADY, sticky='nsew')

        self.decButton = customtkinter.CTkButton(self, text='-', font=FONT_FAMILY, width=30, command=self.decrement)
        self.decButton.grid(row=0, column=1, padx=SPINBOX_PADX, pady=SPINBOX_PADY, sticky='nsew')
        self.decButton.configure(state="normal" if value > 0 else "disabled")
        
        self.valueEntry = customtkinter.CTkEntry(self, textvariable=self.value, font=FONT_FAMILY, width=80, state='readonly')
        self.valueEntry.grid(row=0, column=2, padx=SPINBOX_PADX, pady=SPINBOX_PADY, sticky='nsew')

        self.incButton = customtkinter.CTkButton(self, text='+', font=FONT_FAMILY, width=30, command=self.increment)
        self.incButton.grid(row=0, column=3, padx=SPINBOX_PADX, pady=SPINBOX_PADY, sticky='nsew')

    def getValue(self):
        return self.value.get()

    def setValue(self, value):
        self.value.set(value)
    
    def getText(self):
        return self.text

    def increment(self):
        current_val = self.value.get()
        self.value.set(current_val+0.5)
        self.sumVar.set(self.sumVar.get()+0.5)

    def decrement(self):
        currVal = self.value.get()
        self.value.set(currVal-0.5)
        self.sumVar.set(self.sumVar.get()-0.5)
        self.updateButtonStates()

    def updateButtonStates(self):
        currVal = self.value.get()    
        self.incButton.configure(state="normal" if self.sumVar.get() < self.sumMax else "disabled")
        self.decButton.configure(state="normal" if currVal > 0 else "disabled")


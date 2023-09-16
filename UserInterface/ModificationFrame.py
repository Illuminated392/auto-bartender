import customtkinter
from functools import partial
import math


MAX_MOD_DISPLAY = 5

'''
    Modifications Frame Class:
        The following class defines the modifications frame, enabling a user to
        alter the content of their selection prior to submitting their request.

'''

class ModificationFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, elements=[], values=[], total=0):
        assert len(elements) == len(values)
        for i in range(len(elements)):
            assert str == type(elements[i])
            assert int == type(values[i])
        assert int == type(total)
        super().__init__(master)
        self.elements = {}
        for i in range(len(elements)):
            self.elements[elements[i]] = values[i]
        self.total = total
        self.spinBoxes = []

        # SpinBox Display Variables
        self.currIndex = 0
        
        # Ingredient Sum Variables
        self.sumVar = customtkinter.IntVar()
        self.sumVar.set(0)
        self.sumEntry = customtkinter.CTkEntry(self, width=50)
        self.sumEntry.grid(row=9, column=0)

        # Next and Previous Button setup
        self.prevButton = customtkinter.CTkButton(self, text='^', command=self.showPrevious)
        self.prevButton.grid(row=0, column=0, sticky='ns')
        self.nextButton = customtkinter.CTkButton(self, text='v', command=self.showNext)
        self.nextButton.grid(row=min(len(elements), 5)+1, column=0, sticky='ns')

        # Label for current items displayed
        self.rangeLabel = customtkinter.CTkLabel(self, text="", pady=10)
        self.rangeLabel.grid(row=min(len(elements), 5)+2, column=0)

        self.__loadSpinBoxes()
        self.updateSpinBoxVisibility()
        self.updateRangeLabel()
        self.updateSum()
    
    def __loadSpinBoxes(self):
        if 0 == len(self.elements):
            return
        
        rowTuple = tuple([i for i in range(8)])
        self.grid_rowconfigure(rowTuple, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

        for ele in self.elements:
            spinBox = SpinBoxFrame(self, ele, self.elements[ele], self.sumVar, self.total)
            
            spinBox.value.trace_add('write', lambda *args, box=spinBox: self.updateSum())
            self.spinBoxes.append(spinBox)
        
        #for i, spinBox in enumerate(self.spinBoxes[:MAX_MOD_DISPLAY]):
        #    self.spinBoxes[i].grid(row=i+1,column=0,
        #                            padx=10, pady=10, sticky='nswe')
        self.updateSpinBoxVisibility()

    def getElementValues(self):
        return self.elements

    def updateSum(self):
        total = sum([spinBox.getValue() for spinBox in self.spinBoxes]) 
        self.sumVar.set(total)
        self.sumEntry.delete(0, customtkinter.END)
        self.sumEntry.insert(0, total)
        for spinBox in self.spinBoxes:
            spinBox.updateButtonStates()

    def showNext(self):
        if self.currIndex + MAX_MOD_DISPLAY < len(self.spinBoxes):
            self.currIndex += 5
            self.updateSpinBoxVisibility()
            self.updateRangeLabel()

    def showPrevious(self):
        if self.currIndex >= 5:
            self.currIndex -= 5
            self.updateSpinBoxVisibility()
            self.updateRangeLabel()

    def updateSpinBoxVisibility(self):
        for i, spinBox in enumerate(self.spinBoxes):
            if self.currIndex <= i < self.currIndex + 5:
                spinBox.grid(row=i - self.currIndex + 1, column=0, padx=10, pady=20)
            else:
                spinBox.grid_forget()
    
    def updateRangeLabel(self):
        self.rangeLabel.configure(text=f"Ingredients {self.currIndex} to {min(self.currIndex+5, len(self.spinBoxes))} of {len(self.spinBoxes)}")

class SpinBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, text="", value=None, sum_var=None, sum_max=0):
        super().__init__(master)
        self.value = customtkinter.IntVar(self, value)
        self.sumVar = sum_var
        self.sumMax = sum_max

        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0)

        self.decButton = customtkinter.CTkButton(self, text='-', width=30, command=self.decrement)
        self.decButton.grid(row=0, column=1)
        self.decButton.configure(state="normal" if value > 0 else "disabled")
        
        self.valueEntry = customtkinter.CTkEntry(self, textvariable=self.value, width=30, state='readonly')
        self.valueEntry.grid(row=0, column=2)

        self.incButton = customtkinter.CTkButton(self, text='+', width=30, command=self.increment)
        self.incButton.grid(row=0, column=3)

    def getValue(self):
        return self.value.get()

    def increment(self):
        current_val = self.value.get()
        self.value.set(current_val+1)
        self.sumVar.set(self.sumVar.get()+1)

    def decrement(self):
        currVal = self.value.get()
        self.value.set(currVal-1)
        self.sumVar.set(self.sumVar.get()-1)
        self.updateButtonStates()

    def updateButtonStates(self):
        currVal = self.value.get()    
        self.incButton.configure(state="normal" if self.sumVar.get() < self.sumMax else "disabled")
        self.decButton.configure(state="normal" if currVal > 0 else "disabled")


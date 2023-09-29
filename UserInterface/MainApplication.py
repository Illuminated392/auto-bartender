import customtkinter
from functools import partial
#Local Imports
from .OptionsFrame import OptionsFrame as optFrm
from .ModificationFrame import ModificationFrame as modFrm

# Setup theme of the application
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Configuration Globals
WINDOW_TITLE = "AutoBartender"
APP_TITLE = "Placeholder Title"
FONT_STYLE = "Tekon Pro"

# Home Page defualt index
HOME = 0

'''
    Input: Main Options - List of options that will have a designated option page
'''
class MainApp(customtkinter.CTk):

    # Value to hold whether modification menu is currently displayed
    isModify = False

    def __init__(self, orderCallback, randomCallback, mainOptions=[]):
        super().__init__()

        #Setup window attributes
        self.title(WINDOW_TITLE)
        self.wm_attributes('-fullscreen', True)
       
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=7)

        # Setup 
        self.optionFrames = {}
        self.frameNames = ["Home"]
        [self.frameNames.append(opt) for opt in mainOptions]
        self.activeFrame = -1
        self.modFrame = None
    
        #Setup Title
        self.titleFrame = customtkinter.CTkFrame(self)
        self.title = customtkinter.CTkLabel(self.titleFrame, text=APP_TITLE)
        self.title.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        self.title.configure(font=(FONT_STYLE, 28))
        self.homeButton = customtkinter.CTkButton(self.titleFrame, text="Home", command=self.showHome)
        self.fillerButton = customtkinter.CTkButton(self.titleFrame, text="Random", command=randomCallback)
        self.homeButton.grid(row=0, column=2, padx=10, pady=10, sticky='ns')
        self.fillerButton.grid(row=0, column=0, padx=10, pady=10, sticky='ns')
        self.titleFrame.grid(row=0, column=0, columnspan=6, sticky='ew')
        self.titleFrame.grid_rowconfigure(0, weight=1)

        self.titleFrame.grid_columnconfigure(0, weight=1)
        self.titleFrame.grid_columnconfigure(1, weight=8)
        self.titleFrame.grid_columnconfigure(2, weight=1)

        self.backButton = customtkinter.CTkButton(self, text="Back", font=(FONT_STYLE, 20), command=self.prevDrinkSelection)
        self.orderButton = customtkinter.CTkButton(self, text="Order", font=(FONT_STYLE, 20))
    
    # Display the options based selection frames (UPDATE: colCount, padding to be more dynamic)
    def DisplayOptionFrame(self, frameNum, options=[], callback=None, reset=False, padding=20, colCount=3):
        self.clearApp()

        # Clearing the saved frame to generate a new one
        if reset:
            self.optionFrames.pop(self.frameNames[frameNum])
    
        if self.activeFrame != frameNum or self.isModify:
            frameName = self.frameNames[frameNum]
            if frameNum != HOME:
                self.title.configure(text=frameName)
            else:
                self.title.configure(text=APP_TITLE)
            try:
                self.optionFrames[frameName].grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
            except KeyError:
                newFrame = optFrm(self, options, callback, colCount, padding=padding)
                newFrame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='nswe')
                self.optionFrames[frameName] = newFrame
            self.activeFrame = frameNum
                
    def DisplayHomePage(self, options=None, callback=None): 
        self.title.configure(text=APP_TITLE)
        self.DisplayOptionFrame(HOME, options=options, callback=callback)
        self.isModify = False

    def showHome(self):
        if self.activeFrame != HOME or self.isModify:
            self.DisplayOptionFrame(HOME)
            self.title.configure(text=APP_TITLE)
            self.isModify = False

    def DisplayModificationPage(self, drink, items, values, total, orderCallback):
        self.clearApp()
        self.isModify = True
        self.title.configure(text=drink)
        self.modFrame = modFrm(self, items, values, total)
        self.modFrame.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')
   
        self.orderButton.configure(command=partial(orderCallback, self.modFrame))

        self.backButton.grid(row=1, column=0, padx=10, pady=20, sticky='nsew')
        self.orderButton.grid(row=1, column=2, padx=10, pady=20, sticky='nsew')
        resetButton = None
        
    def DisplayMainOptionPage(self, frameName, options, callback, colCount=3):
        self.isModify = False
        frameNum = self.frameNames.index(frameName)
        if frameNum != None:
            self.DisplayOptionFrame(frameNum, options, callback, padding=10, colCount=colCount)
        
    def clearApp(self):
        try:
            if self.modFrame != None:
                self.modFrame.grid_remove()
            self.backButton.grid_remove()
            self.orderButton.grid_remove()
            frameName = self.frameNames[self.activeFrame]
            self.optionFrames[frameName].grid_remove()
        except Exception as e:
            print(f"Clean app exception: {e}")
    def prevDrinkSelection(self):
        self.clearApp()
        self.DisplayOptionFrame(self.activeFrame)


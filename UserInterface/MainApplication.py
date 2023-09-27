import customtkinter

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

    def __init__(self, mainOptions=[]):
        super().__init__()

        #Setup window attributes
        self.title(WINDOW_TITLE)
        self.wm_attributes('-fullscreen', True)
       
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=7)

        # Setup 
        self.optionFrames = {}
        self.frameNames = ["Home"]
        [self.frameNames.append(opt) for opt in mainOptions]
        self.activeFrame = -1

        #Setup Title
        self.titleFrame = customtkinter.CTkFrame(self)
        title = customtkinter.CTkLabel(self.titleFrame, text=APP_TITLE)
        title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        title.configure(font=(FONT_STYLE, 28))
        self.homeButton = customtkinter.CTkButton(self.titleFrame, text="Home", command=self.showHome)
        self.homeButton.grid(row=0, column=1, padx=10, pady=10, sticky='ns')
        self.titleFrame.grid(row=0, column=0, columnspan=5, sticky='ew')
        self.titleFrame.grid_rowconfigure(0, weight=1)
        self.titleFrame.grid_columnconfigure(0, weight=7)
        self.titleFrame.grid_columnconfigure(1, weight=1)
        #UPDATE: Add button to return home whenever
        self.homeButton = None

        self.modButtons = []

    # Display the options based selection frames (UPDATE: colCount, padding to be more dynamic)
    def DisplayOptionFrame(self, frameNum, options=[], callback=None, reset=False, padding=20, colCount=3):
        self.clearApp()

        # Clearing the saved frame to generate a new one
        if reset:
            self.optionFrames.pop(self.frameNames[frameNum])
        
    
        if self.activeFrame != frameNum or self.isModify:
            frameName = self.frameNames[frameNum]
            try:
                self.optionFrames[frameName].grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
            except KeyError:
                newFrame = optFrm(self, options, callback, colCount, padding=padding)
                newFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
                self.optionFrames[frameName] = newFrame

            self.activeFrame = frameNum
                
    def DisplayHomePage(self, options, callback):
        self.isModify = False
        self.DisplayOptionFrame(HOME, options=options, callback=callback)

    def showHome(self):
        if self.activeFrame != HOME or self.isModify:
            self.clearApp()
            self.DisplayOptionFrame(HOME)

    def DisplayModificationPage(self, items, values, total, orderCallback):
        self.clearApp()
        self.isModify = True
        self.modFrame = modFrm(self, items, values, total)
        self.modFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')

        # Buttons on the side of the modificaitons
        # Reset counters
        resetButton = None
        #Back to drink selection
        cancelButton = None
        #self.DisplayOptionFrame(self.activeFrame)
        orderButton = None
        '''
        The order callback will be used with the button to pass the \
        items and their values back to the AutoBartender.py and carry out
        the order process. 
        '''
        
    def DisplayMainOptionPage(self, frameName, options, callback, colCount=3):
        self.isModify = False
        frameNum = self.frameNames.index(frameName)
        if frameNum != None:
            self.DisplayOptionFrame(frameNum, options, callback, padding=10, colCount=colCount)
        
    def clearApp(self):
        try:
            frameName = self.frameNames[self.activeFrame]
            self.optionFrames[frameName].grid_remove()
            self.modFrame.grid_remove()
        except:
            pass


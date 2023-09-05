import customtkinter


# Local Imports
import OptionsFrame
import ModificationFrame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

HOME = 0
OPTION1 = 1
OPTION2 = 2
OPTION3 = 3

class FooterFrame(customtkinter.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.configure(font = ("Courier", 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

class AutoBarApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Auto Bartender")
        self.geometry("600x400")
        self.wm_attributes('-fullscreen', True)
        self.optionFrames = {}
        self.titleFame = None
        self.footerFrame = None
        self.frameNames = ("Home", "Option1", "Option2", "Option3")
        self.activeFrame = -1

        self.setupTitle()

    def setupTitle(self):
        self.titleFrame = customtkinter.CTkFrame(self)
        self.title = customtkinter.CTkLabel(self.titleFrame, text="Placeholder")
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.title.configure(font=("Tekton Pro", 20))
        self.titleFrame.grid(row=0, column=0, sticky="ew")
        self.titleFrame.grid_rowconfigure(0, weight=1)
        self.titleFrame.grid_columnconfigure(0, weight=1)

    def DisplayFrame(self, frameNum, reset, options, callback, padding=20, colCount=3):
        self.clearApp()

        if reset:
            self.optionFrames.pop(self.frameNames[frameNum])

        # Home page formating
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=7)

        # Home page button setup
        if self.activeFrame != frameNum:
            frameName = self.frameNames[frameNum]
            try:
                self.optionFrames[frameName]
            except KeyError:
                self.optionFrames[frameName] = OptionsFrame.OptionsFrame(self, options, callback, colCount=colCount, padding=padding)
            
            self.optionFrames[frameName].grid(row=1, column=0, padx=5, pady=5, sticky="nswe")
            self.activeFrame = frameNum
                                
    def DisplayHomePage(self, options, callback):
        self.DisplayFrame(HOME, False, options, callback)

    def DisplayOption3Page(self, options, callback):
        self.DisplayFrame(OPTION3, False, options, callback, colCount=4, padding=10)

    def DisplayOption2Page(self, options, callback):
        self.DisplayFrame(OPTION2, False, options, callback, padding=10, colCount=1)
    def clearApp(self):
        frameName = self.frameNames[self.activeFrame]
        try:
            self.optionFrames[frameName].grid_remove()
            self.activeFrame = -1
        except:
            print("Active Frame does not exist")

    def setFooterFrame(self, row):
        self.footerFrame.grid(row=row, column=0, padx=5, pady=5, sticky="nswe")

    def confirmSelection(self):
        selection = self.selection
        self.selection = ""
        return selection

def option1(option):
    print("Option 1")

def option2(option):
    print("Option 2")

def option3(option):
    global app
    print(option)
    print("----------")
    selections = [
            "apple", 
            "banana",
            "carrot",
            "date",
            "egg plant",
            "farro",
            "grape",
            "healthy",
            "intuative",
            "juicy"
            ]
    app.DisplayOption3Page(selections, optionCallback)

def optionCallback(option):
    global app
    print(option)
    app.DisplayOption2Page(["Test1", "Test2", "Test3"], option3)

options = [
"Option 1",
"Option 2",
"Option 3",
"Option 4",
"Option 5",
"Option 6"
]

app = AutoBarApp()

app.DisplayHomePage(options, option3)


app.mainloop()


